# ACARA - Extração de tabelas com primeira coluna como CATEGORIA
import pandas as pd
from tabula import read_pdf
import pdfplumber
from azure_llm import create_azure_llm
from prompts.prompts_acara import (
    acara_market_summary,
    acara_40_lightweight_brands_ranking,
    acara_10_heavy_commercial_brands_ranking,
)

# Para visualizar melhor as tabelas
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 1000)

# Mapeamento dos títulos relevantes
TITULOS_RELEVANTES_ACARA = {
    "TABLA 1. Resumen del mercado.": acara_market_summary,
    "TABLA 2. Ranking. TOP 40. Marcas Livianos (Automóviles + Comerciales Livianos)": acara_40_lightweight_brands_ranking,
    "TABLA 4. Ranking. TOP 10. Marcas Comerciales Pesados": acara_10_heavy_commercial_brands_ranking,
}

def get_relevant_pages_and_titles_acara(pdf_path):
    relevant_pages = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            text = text.replace("\n", " ").replace("  ", " ").strip()
            for title in TITULOS_RELEVANTES_ACARA:
                if title in text:
                    if page_number not in relevant_pages:
                        relevant_pages[page_number] = []
                    relevant_pages[page_number].append(title)
    return relevant_pages

def extract_tables_acara(pdf_path, relevant_pages):
    extracted_data = {}

    for page_number, titulos in relevant_pages.items():
        tables = read_pdf(
            pdf_path,
            pages=str(page_number),
            lattice=True,
            guess=True,
            pandas_options={"header": None}
        )

        if not tables:
            continue

        for titulo in titulos:
            for table in tables:
                df = table.copy()
                df = df.dropna(how="all").fillna("")

                if df.empty:
                    continue

                # Primeira coluna é a "Categoria" (tipo "Autos", "Total Mercado", etc)
                categoria_col = df.iloc[:, 0].astype(str).str.strip()
                df = df.drop(columns=[0])  # Remove a coluna antiga da categoria

                # Resetar o índice para alinhar certinho
                df = df.reset_index(drop=True)

                # Nomear as colunas A, B, C, D... conforme o número de colunas restantes
                colunas = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:df.shape[1]]
                df.columns = colunas

                # Inserir novamente a coluna "Categoria" na frente
                df.insert(0, "Categoria", categoria_col)

                extracted_data[titulo] = df
                break

    return extracted_data

def process_pdf_and_generate_prompts_acara(pdf_path):
    relevant_pages = get_relevant_pages_and_titles_acara(pdf_path)
    extracted_tables = extract_tables_acara(pdf_path, relevant_pages)
    llm = create_azure_llm()

    for titulo, table in extracted_tables.items():
        print(f"\n### Dados extraídos da tabela: {titulo} ###")
        tabela_texto = table.to_string(index=False, header=True)
        print(tabela_texto)

        prompt_func = TITULOS_RELEVANTES_ACARA[titulo]

        # if prompt_func:
        #     prompt = prompt_func(tabela_texto)
        #     print("\n--- Análise com LLM ---")
        #     resposta = llm.invoke([prompt])
        #     print(resposta.content)
