import pandas as pd
from tabula import read_pdf
import pdfplumber
from datetime import datetime
from azure_llm import create_azure_llm

from prompts.prompts_adefa import (
    adefa_production_automobiles_and_light_commercials_feb,
    adefa_production_automobiles_and_light_commercials,
    adefa_exports_automobiles_and_light_commercials_feb,
    adefa_exports_automobiles_and_light_commercials,
)

# Configurações iniciais
mes_atual = datetime.now().month

TITULOS_RELEVANTES = {
    "Producción Automóviles y Comerciales Livianos": (
        adefa_production_automobiles_and_light_commercials_feb,
        adefa_production_automobiles_and_light_commercials
    ),
    "Exportaciones Automóviles y Comerciales Livianos": (
        adefa_exports_automobiles_and_light_commercials_feb,
        adefa_exports_automobiles_and_light_commercials
    ),
}

# Para visualizar melhor as tabelas
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 1000)

def get_relevant_pages_and_titles_adefa(pdf_path):
    relevant_pages = {}

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            text = text.replace("\n", " ").replace("  ", " ").strip()  # <<< CORREÇÃO AQUI!

            for title in TITULOS_RELEVANTES:
                if title in text:
                    if page_number not in relevant_pages:
                        relevant_pages[page_number] = []
                    relevant_pages[page_number].append(title)

    return relevant_pages


def extract_tables_adefa(pdf_path, relevant_pages):
    extracted_data = {}

    for page_number, titulos in relevant_pages.items():
        tables = read_pdf(pdf_path, pages=str(page_number), lattice=True, stream=True)

        if not tables:
            continue

        for titulo in titulos:
            for table in tables:
                df = table.copy()
                df = df.dropna(how="all").fillna("")  # Remover linhas em branco e preencher valores vazios

                # Renomeando as colunas para A, B, C... para garantir que IA entenda
                num_colunas = len(df.columns)  # Número real de colunas na tabela
                colunas = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:num_colunas]  # Limita o número de letras conforme necessário
                df.columns = colunas  # Renomeia as colunas com A, B, C, etc.

                # Armazenando a tabela extraída para o título específico
                extracted_data[titulo] = df
                break

    return extracted_data


def process_pdf_and_generate_prompts_adefa(pdf_path):
    relevant_pages = get_relevant_pages_and_titles_adefa(pdf_path)
    extracted_tables = extract_tables_adefa(pdf_path, relevant_pages)
    llm = create_azure_llm()

    for titulo, table in extracted_tables.items():
        print(f"\n### Dados extraídos da tabela: {titulo} ###")
        tabela_texto = table.to_string(index=False, header=True)
        print(tabela_texto)

        prompt_feb_func, prompt_other_func = TITULOS_RELEVANTES[titulo]
        prompt_func = prompt_feb_func if mes_atual == 2 else prompt_other_func

        if prompt_func:
            prompt = prompt_func(tabela_texto)
            print("\n--- Análise com LLM ---")
            resposta = llm.invoke([prompt])
            print(resposta.content)




