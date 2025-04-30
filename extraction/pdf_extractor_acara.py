# ACARA - Extração de tabelas com primeira coluna como CATEGORIA
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
            stream=True,
            guess=True,
            lattice=False,
            pandas_options={"header": None}
        )

        if not tables:
            continue

        for titulo in titulos:
            for df in tables:
                if df.empty or df.shape[1] < 3:
                    continue

                df = df.dropna(how="all").fillna("")
                df = df.loc[:, ~df.columns.duplicated()]
                df = df.map(lambda x: str(x).replace("\r", " ").replace("  ", " ").strip())

                df.rename(columns={0: "Categoria"}, inplace=True)
                categorias = df["Categoria"]
                df = df.drop(columns=["Categoria"])

                def separar_valores_grudados(cell):
                    if isinstance(cell, str):
                        # separa valores como "11.53717,5%" em "11.537" e "17,5%"
                        return re.sub(r"(\d+\.\d{3})(\d)", r"\1 \2", cell)
                    return cell

                # Preserva valores com separador de milhar (não quebra 11.537)
                def preservar_valores(cell):
                    if isinstance(cell, str):
                        return re.sub(r'(\d) (\d)', r'\1\2', cell)
                    return cell
                df = df.map(preservar_valores).map(separar_valores_grudados)

                def split_cells(cell):
                    if isinstance(cell, str) and re.search(r'\d{5,}', cell):
                        return [cell]  # mantém como string única
                    return [cell]

                df_expanded = pd.DataFrame()
                for col in df.columns:
                    expanded = df[col].apply(split_cells)
                    max_len = expanded.apply(len).max()
                    cols_exp = pd.DataFrame(expanded.tolist(), columns=[f"{col}_{i}" for i in range(max_len)])
                    df_expanded = pd.concat([df_expanded, cols_exp], axis=1)

                df_final = pd.concat([categorias.reset_index(drop=True), df_expanded], axis=1)
                df_final.rename(columns={0: "Categoria"}, inplace=True)

                # Validação segura do número de colunas
                num_colunas = df_final.shape[1] - 1
                letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                if num_colunas <= len(letras):
                    df_final.columns = ["Categoria"] + letras[:num_colunas]
                else:
                    df_final.columns = ["Categoria"] + [f"Col_{i}" for i in range(1, num_colunas + 1)]

                # Log para debug: mostra estrutura da tabela
                print(f"\n✅ Tabela extraída: {titulo} | Página {page_number}")
                print(f"🔢 Total de colunas (sem Categoria): {num_colunas}")
                print(f"🔍 Primeira linha da tabela:\n{df_final.iloc[0]}")
                
                extracted_data[titulo] = df_final
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

        if prompt_func:
            prompt = prompt_func(tabela_texto)
            print("\n--- Análise com LLM ---")
            resposta = llm.invoke([prompt])
            print(resposta.content)
