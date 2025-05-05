import pandas as pd
from tabula import read_pdf
import pdfplumber
import re
from azure_llm import create_azure_llm
from prompts.prompts_acara import (
    acara_market_summary,
    acara_40_lightweight_brands_ranking,
    acara_10_heavy_commercial_brands_ranking,
)

def guess_table_title(pagina: int, tabela_texto: str, pdf_path: str) -> str | None:
    if pagina == 8 and "TOP 40" in tabela_texto and "FIAT" in tabela_texto:
        return "TABLA 2. Ranking. TOP 40. Marcas Livianos (Automóviles + Comerciales Livianos)"
    if pagina == 9 and "TOP 10" in tabela_texto and "Mercedes-Benz" in tabela_texto:
        return "TABLA 4. Ranking. TOP 10. Marcas Comerciales Pesados"
    if pagina == 10 and "TOTAL MERCADO" in tabela_texto:
        return "TABLA 1. Resumen del mercado."
    return None

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 1000)

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
            text = re.sub(r"\s{2,}", " ", text.replace("\n", " ")).strip()
            for title in TITULOS_RELEVANTES_ACARA:
                if title in text:
                    relevant_pages.setdefault(page_number, []).append(title)
    return relevant_pages

def extract_tables_acara(pdf_path, relevant_pages):
    extracted_data = {}

    for page_number, titulos in relevant_pages.items():
        tables = read_pdf(
            pdf_path,
            pages=str(page_number),
            stream=True,
            guess=True,
            lattice=False,
            pandas_options={"header": None}
        )

        if not tables:
            continue

        for tabela in tables:
            if tabela.empty or tabela.shape[1] < 3:
                continue

            tabela = tabela.dropna(how="all").fillna("")
            tabela = tabela.loc[:, ~tabela.columns.duplicated()]
            tabela = tabela.map(lambda x: str(x).replace("\r", " ").replace("  ", " ").strip())

            tabela.rename(columns={0: "Categoria"}, inplace=True)
            categorias = tabela["Categoria"]
            tabela = tabela.drop(columns=["Categoria"])

            def preservar_valores(cell):
                if isinstance(cell, str):
                    return re.sub(r'(\d) (\d)', r'\1\2', cell)
                return cell
            tabela = tabela.map(preservar_valores)

            def split_cells(cell):
                if isinstance(cell, str) and re.search(r'\d{5,}', cell):
                    return [cell]
                return [cell]

            tabela_expandida = pd.DataFrame()
            for col in tabela.columns:
                expanded = tabela[col].apply(split_cells)
                max_len = expanded.apply(len).max()
                cols_exp = pd.DataFrame(expanded.tolist(), columns=[f"{col}_{i}" for i in range(max_len)])
                tabela_expandida = pd.concat([tabela_expandida, cols_exp], axis=1)

            tabela_final = pd.concat([categorias.reset_index(drop=True), tabela_expandida], axis=1)

            num_colunas = tabela_final.shape[1] - 1
            letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            if num_colunas <= len(letras):
                tabela_final.columns = ["Categoria"] + letras[:num_colunas]
            else:
                tabela_final.columns = ["Categoria"] + [f"Col_{i}" for i in range(1, num_colunas + 1)]

            titulo_detectado = titulos[0] if titulos else None

            if not titulo_detectado or titulo_detectado not in TITULOS_RELEVANTES_ACARA:
                tabela_texto = tabela_final.to_string(index=False, header=True)
                titulo_detectado = guess_table_title(page_number, tabela_texto, pdf_path)

            if titulo_detectado and titulo_detectado in TITULOS_RELEVANTES_ACARA:
                extracted_data[titulo_detectado] = tabela_final
                break  # Garante só uma tabela por página

    return extracted_data

def process_pdf_and_generate_prompts_acara(pdf_path):
    relevant_pages = get_relevant_pages_and_titles_acara(pdf_path)
    extracted_tables = extract_tables_acara(pdf_path, relevant_pages)
    llm = create_azure_llm()

    for titulo, table in extracted_tables.items():
        print(f"\n### Dados extraídos da tabela: {titulo} ###")
        tabela_texto = table.to_string(index=False, header=True)
        print(tabela_texto)

        prompt_func = TITULOS_RELEVANTES_ACARA.get(titulo)
        if prompt_func:
            prompt = prompt_func(tabela_texto)
            print("\n--- Análise com LLM ---")
            resposta = llm.invoke([prompt])
            print(resposta.content)
