# USANDO TABULA + PANDAS
import os
import pandas as pd
from tabula import read_pdf
import pdfplumber
from datetime import datetime
from azure_llm import create_azure_llm 

from prompts_anfavea import (
    prompt_anfavea_production_assembled_vehicles_feb,
    prompt_anfavea_production_assembled_vehicles,
    prompt_total_licensing_new_vehicles_feb,
    prompt_total_licensing_new_vehicles,
    prompt_licensing_new_imported_vehicles_feb,
    prompt_licensing_new_imported_vehicles,
    vehicle_licensing_new_domestic_vehicles_feb,
    vehicle_licensing_new_domestic_vehicles,
    exports_assembled_vehicles_feb,
    exports_assembled_vehicles,
)

titulos_relevantes = {
    "Produção de autoveículos montados": (
        prompt_anfavea_production_assembled_vehicles_feb, 
        prompt_anfavea_production_assembled_vehicles
    ),
    "Licenciamento total de autoveículos novos": (
        prompt_total_licensing_new_vehicles_feb, 
        prompt_total_licensing_new_vehicles
    ),
    "Licenciamento de autoveículos novos nacionais": (
        vehicle_licensing_new_domestic_vehicles_feb, 
        vehicle_licensing_new_domestic_vehicles
    ),
    "Licenciamento de autoveículos novos importados": (
        prompt_licensing_new_imported_vehicles_feb, 
        prompt_licensing_new_imported_vehicles
    ),
    "Exportações de autoveículos montados": (
        exports_assembled_vehicles_feb, 
        exports_assembled_vehicles
    ),
}

mes_atual = datetime.now().month    # Define qual o mês atual para fazer uma verificação no decorrer do código

# Configuração do Pandas para visualizar melhor a tabela
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 1000)

def get_relevant_pages_and_titles_anfavea(pdf_path):
    """
    Lê o PDF e retorna um dicionário com os números das páginas relevantes e seus títulos correspondentes.
    """
    relevant_pages = {}

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()  # Extrair título da página (a lógica de extração de títulos pode variar conforme o formato do PDF)

            # Imprimir o texto extraído para verificar espaços extras ou quebras de linha
            # print(f"\nTexto extraído da página {page_number}:\n{text}")

            for title in titulos_relevantes:
                if title.strip() in text.strip():
                    # Adiciona o título se não estiver já na lista para essa página
                    if page_number not in relevant_pages:
                        relevant_pages[page_number] = []
                    relevant_pages[page_number].append(title)  # Armazenar múltiplos títulos encontrados

    return relevant_pages

def extract_and_process_tables_anfavea(pdf_path, relevant_pages):
    """
    Extrai tabelas do PDF com base nas páginas e títulos relevantes detectados.
    Retorna um dicionário contendo as tabelas extraídas.
    """
    extracted_data = {}

    for page_number, titles in relevant_pages.items():
        # print(f"Extraindo tabela da página {page_number} - {titles}")
        tables = read_pdf(pdf_path, pages=str(page_number), lattice=False, stream=True)  # Ajuste páginas conforme necessário

        if tables:
            for i, table in enumerate(tables):
                # print(f"Processando tabela {i+1} da página {page_number}")
                
                # Ajuste o cabeçalho da tabela conforme o mês atual
                if mes_atual == 2:
                    table.columns = table.iloc[1]   # Usar a segunda linha como cabeçalho
                else:
                    table.columns = table.iloc[0]   # Usar a primeira linha como cabeçalho

                table = table[1:].reset_index(drop=True)

                # Limpar dados NaN e preencher valores vazios
                table = table.dropna(how="all")
                table = table.fillna('')

                if "Licenciamento de autoveículos novos importados" in titles:
                    if page_number == 4 and i == 2:
                        extracted_data["Licenciamento de autoveículos novos importados"] = table
                        # print(f"📌 Tabela 'Licenciamento de autoveículos novos importados' extraída.")
                        break

                elif "Licenciamento de autoveículos novos nacionais" in titles:
                    if page_number == 4 and i == 0:  # Garantir pegar a primeira tabela da página 4
                        extracted_data["Licenciamento de autoveículos novos nacionais"] = table
                        # print(f"📌 Tabela 'Licenciamento de autoveículos novos nacionais' extraída.")
                        break  # Parar de procurar depois de encontrar a tabela

                # Verifica se os titulos correspondem aos que eu preciso
                for title in titles:
                    if title in titulos_relevantes and title not in extracted_data:
                        extracted_data[title] = table
                        break
                    
    return extracted_data


def process_pdf_and_generate_prompts(pdf_path):
    """
    Processa o PDF, extrai tabelas relevantes e gera prompts para análise com LLM.
    """
    relevant_pages_and_titles = get_relevant_pages_and_titles_anfavea(pdf_path)
    extracted_tables = extract_and_process_tables_anfavea(pdf_path, relevant_pages_and_titles)
    
    llm = create_azure_llm()    # Essa função cria um cliente LLM conectado

    for title, table in extracted_tables.items():
        print(f"\n### Dados extraídos da tabela: {title} ###")

        tabela_texto = table.to_string(index=False, header=True)
        # print(tabela_texto)

        # Selecionar função de prompt baseada no título e no mês
        prompt_feb_func, prompt_others_func = titulos_relevantes.get(title, (None, None))
        prompt_func = prompt_feb_func if mes_atual == 2 else prompt_others_func
        
        if prompt_func:
            prompt = prompt_func(tabela_texto)
            print("\n--- Análise com LLM ---")
            resposta = llm.invoke([prompt])
            print(resposta.content)


if __name__ == "__main__":
    pdf_filename = "carta452.pdf"
    pdf_path = os.path.join(os.path.dirname(__file__), "pdf", pdf_filename)
    process_pdf_and_generate_prompts(pdf_path)
