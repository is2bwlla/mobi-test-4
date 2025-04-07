import os
import pandas as pd
from tabula import read_pdf
import pdfplumber
from datetime import datetime
import locale
from azure_llm import create_azure_llm

from prompts_fenabrave import (
    prompt_fenabrave_monthly_summary,
    prompt_fenabrave_monthly_brand_ranking,
    prompt_fenabrave_cumulative_brand_ranking
)

# Configurações
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
data_atual_pt = datetime.now().strftime("%B de %Y").capitalize()
data_atual_abreviado = datetime.now().strftime("%B/%Y").capitalize()

# 🔄 Titulações dinâmicas (altere para fixo se necessário)
# titulos_relevantes = {
#     f"Resumo mensal {data_atual_pt}": prompt_fenabrave_monthly_summary,
#     f"Ranking por marca {data_atual_abreviado}": prompt_fenabrave_monthly_brand_ranking,
#     f"Ranking por marca acumulado até {data_atual_abreviado}": prompt_fenabrave_cumulative_brand_ranking,
# }

# Titulações (estático neste caso, mas você pode voltar ao dinâmico se quiser)
titulos_relevantes = {
    "Resumo mensal Janeiro de 2025": prompt_fenabrave_monthly_summary,
    "Ranking por marca Janeiro/2025": prompt_fenabrave_monthly_brand_ranking,
    "Ranking por marca acumulado até Janeiro/2025": prompt_fenabrave_cumulative_brand_ranking,
}

# Config do Pandas
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 1000)


def get_relevant_pages_and_titles_fenabrave(pdf_path):
    relevant_pages = {}

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            print(f"\n📄 Página {page_number} - texto detectado:\n{text}")

            for title in titulos_relevantes:
                if title.strip() in text:
                    print(f"🔹 Título reconhecido: {title} na página {page_number}")
                    if page_number not in relevant_pages:
                        relevant_pages[page_number] = []
                    relevant_pages[page_number].append(title)

    return relevant_pages


def extract_and_process_tables_fenabrave(pdf_path, relevant_pages):
    extracted_data = {}

    for page_number, titles in relevant_pages.items():
        tables = read_pdf(pdf_path, pages=page_number, lattice=False, stream=True, multiple_tables=True)

        if not tables:
            print(f"[!] Nenhuma tabela detectada na página {page_number}")
            continue

        for i, table in enumerate(tables):
            table.columns = table.iloc[0]
            table = table[1:].reset_index(drop=True)
            table = table.dropna(how="all").fillna('')

            print(f"🟢 Tabela {i+1} extraída da página {page_number}:\n")
            print(table)

            for title in titles:
                if title not in extracted_data:
                    extracted_data[title] = table
                    break

    return extracted_data


def process_pdf_and_generate_prompts_fenabrave(pdf_path):
    relevant_pages_and_titles = get_relevant_pages_and_titles_fenabrave(pdf_path)
    extracted_tables = extract_and_process_tables_fenabrave(pdf_path, relevant_pages_and_titles)

    llm = create_azure_llm()

    for title, table in extracted_tables.items():
        print(f"\n### Tabela detectada para '{title}' ###")
        tabela_texto = table.to_string(index=False, header=True)
        print(tabela_texto)

        prompt_func = titulos_relevantes.get(title)
        if prompt_func:
            prompt = prompt_func(tabela_texto)
            print(f"\n--- LLM: {title} ---")
            resposta = llm.invoke([prompt])
            print(resposta.content)

