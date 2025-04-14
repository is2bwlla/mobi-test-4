# # TESTANDO PEGAR A PRIMEIRA TABELA:

# import pandas as pd
# import pdfplumber
# from tabula import read_pdf
# from azure_llm import create_azure_llm
# from prompts.prompts_fenabrave import (
#     prompt_fenabrave_monthly_summary,
#     prompt_fenabrave_monthly_brand_ranking,
#     prompt_fenabrave_cumulative_brand_ranking
# )

# # Mapeamento de títulos e prompts
# titulos_relevantes = {
#     "Resumo mensal": prompt_fenabrave_monthly_summary,
#     "Ranking por marca": prompt_fenabrave_monthly_brand_ranking,
#     "Ranking por marca acumulado": prompt_fenabrave_cumulative_brand_ranking,
# }

# # Configuração do Pandas para visualizar melhor a tabela
# pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows", None)
# pd.set_option("display.width", 1000)

# def process_pdf_and_generate_prompts_fenabrave(pdf_path):
#     """
#     Função única para processar o PDF e gerar os prompts para a LLM com os dados de "AUTOMÓVEIS + COMERCIAIS LEVES" 
#     nas páginas 8 e 9 e o resumo mensal na página 1.
#     """
#     relevant_pages = {}
#     extracted_data = {}

#     # Função para extrair resumo mensal da página 1
#     def extract_resumo_mensal(pdf_path):
#         try:
#             tables = read_pdf(pdf_path, pages="1", lattice=True, stream=True, multiple_tables=True)
#             if tables and not tables[0].empty:
#                 tabela = tables[0]
#                 linha_a_b = tabela[tabela['Coluna1'] == 'A + B']  # Ajuste 'Coluna1' conforme necessário
#                 return linha_a_b[['Coluna A', 'Coluna C', 'Coluna D', 'Coluna E']].to_string(index=False)
#             else:
#                 raise ValueError("Tabela vazia ou não encontrada")
#         except Exception as e:
#             with pdfplumber.open(pdf_path) as pdf:
#                 texto = pdf.pages[0].extract_text()
#                 if texto:
#                     linhas = texto.split("\n")
#                     for linha in linhas:
#                         if "A + B" in linha:
#                             return linha
#                 return None

#     # Função para extrair dados de "AUTOMÓVEIS + COMERCIAIS LEVES"
#     def extract_ranking_por_marca(pdf_path, page_number):
#         with pdfplumber.open(pdf_path) as pdf:
#             page = pdf.pages[page_number - 1]  # Ajuste para índice 0-base
#             text = page.extract_text()
#             print(f"Texto extraído da página {page_number}:\n{text}")  # Depuração
#             if "Ranking por marca" in text or "Ranking por marca acumulado" in text:
#                 linhas = text.split("\n")
#                 relevant_lines = []
#                 for linha in linhas:
#                     if "AUTOMÓVEIS + COMERCIAIS LEVES" in linha:
#                         relevant_lines.append(linha)
#                 return "\n".join(relevant_lines) if relevant_lines else None
#         return None

#     # Processa o PDF e extrai os títulos relevantes
#     with pdfplumber.open(pdf_path) as pdf:
#         for page_number, page in enumerate(pdf.pages, start=1):
#             text = page.extract_text()
#             print(f"Texto extraído da página {page_number}:\n{text}\n")  # Depuração do texto completo da página

#             # Verifica e armazena os títulos relevantes
#             if "Resumo Mensal" in text and 1 not in relevant_pages:
#                 relevant_pages[1] = ['Resumo mensal']

#             if "Ranking por marca" in text or "Ranking por marca acumulado" in text:
#                 if page_number == 8 or page_number == 9:
#                     relevant_pages[page_number] = ["Ranking por marca", "Ranking por marca acumulado"]

#     # Extrai os dados conforme os títulos encontrados
#     for page_number, titles in relevant_pages.items():
#         with pdfplumber.open(pdf_path) as pdf:
#             page = pdf.pages[page_number - 1]  # Ajuste para índice 0-base
#             text = page.extract_text()
#             print(f"Texto extraído da página {page_number} para títulos {titles}:\n{text}\n")  # Depuração

#             for title in titles:
#                 if title == "Resumo mensal":
#                     resumo_mensal_str = extract_resumo_mensal(pdf_path)
#                     if resumo_mensal_str:
#                         extracted_data["Resumo mensal"] = resumo_mensal_str
#                 elif title == "Ranking por marca" or title == "Ranking por marca acumulado":
#                     ranking_data = extract_ranking_por_marca(pdf_path, page_number)
#                     if ranking_data:
#                         extracted_data[title] = ranking_data
#                 else:
#                     extracted_data[title] = text

#     # Verificação do conteúdo extraído
#     print("Dados extraídos para os prompts:")
#     for title, data in extracted_data.items():
#         print(f"{title}:\n{data}\n")

#     # Geração dos prompts para LLM
#     llm = create_azure_llm()
#     for title, data in extracted_data.items():
#         if isinstance(data, str):
#             tabela_texto = data
#         else:
#             tabela_texto = data.to_string(index=False, header=True)

#         prompt_func = titulos_relevantes.get(title)
#         if prompt_func:
#             prompt = prompt_func(tabela_texto)
#             resposta = llm.invoke([prompt])
#             print(f"Resultado da LLM para {title}: {resposta.content}")

import pandas as pd
import pdfplumber
from tabula import read_pdf
from azure_llm import create_azure_llm
from prompts.prompts_fenabrave import (
    prompt_fenabrave_monthly_summary,
    prompt_fenabrave_monthly_brand_ranking,
    prompt_fenabrave_cumulative_brand_ranking
)

# Mapeamento de títulos e prompts
titulos_relevantes = {
    "Resumo mensal": prompt_fenabrave_monthly_summary,
    "Ranking por marca": prompt_fenabrave_monthly_brand_ranking,
    "Ranking por marca acumulado": prompt_fenabrave_cumulative_brand_ranking,
}

# Configuração do Pandas para visualizar melhor a tabela
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 1000)

def process_pdf_and_generate_prompts_fenabrave(pdf_path):
    """
    Função única para processar o PDF e gerar os prompts para a LLM com os dados de "AUTOMÓVEIS + COMERCIAIS LEVES" 
    nas páginas 8 e 9 e o resumo mensal na página 1.
    """
    relevant_pages = {}
    extracted_data = {}

    # Função para extrair resumo mensal da página 1
    def extract_resumo_mensal(pdf_path):
        try:
            tables = read_pdf(pdf_path, pages="1", lattice=True, stream=True, multiple_tables=True)
            if tables and not tables[0].empty:
                tabela = tables[0]
                linha_a_b = tabela[tabela['Coluna1'] == 'A + B']  # Ajuste 'Coluna1' conforme necessário
                return linha_a_b[['Coluna A', 'Coluna C', 'Coluna D', 'Coluna E']].to_string(index=False)
            else:
                raise ValueError("Tabela vazia ou não encontrada")
        except Exception as e:
            with pdfplumber.open(pdf_path) as pdf:
                texto = pdf.pages[0].extract_text()
                if texto:
                    linhas = texto.split("\n")
                    for linha in linhas:
                        if "A + B" in linha:
                            return linha
                return None

    # Função para extrair dados de "AUTOMÓVEIS + COMERCIAIS LEVES"
    def extract_ranking_por_marca(pdf_path, page_number):
        with pdfplumber.open(pdf_path) as pdf:
            page = pdf.pages[page_number - 1]  # Ajuste para índice 0-base
            text = page.extract_text()
            if "Ranking por marca" in text or "Ranking por marca acumulado" in text:
                linhas = text.split("\n")
                relevant_lines = []
                # Captura as linhas relacionadas a "AUTOMÓVEIS + COMERCIAIS LEVES"
                capture = False
                for linha in linhas:
                    if "AUTOMÓVEIS + COMERCIAIS LEVES" in linha:
                        capture = True
                    if capture:
                        relevant_lines.append(linha)
                        if len(relevant_lines) >= 21:  # Garante que pegue as 21 posições
                            break
                return "\n".join(relevant_lines) if relevant_lines else None
        return None

    # Função específica para "Ranking por marca"
    def extract_ranking_por_marca_normal(pdf_path):
        with pdfplumber.open(pdf_path) as pdf:
            page = pdf.pages[7]  # Página 8 (índice 7)
            text = page.extract_text()
            if "Ranking por marca" in text:
                linhas = text.split("\n")
                relevant_lines = []
                capture = False
                for linha in linhas:
                    if "AUTOMÓVEIS + COMERCIAIS LEVES" in linha:
                        capture = True
                    if capture:
                        relevant_lines.append(linha)
                        if len(relevant_lines) >= 21:  # Garante que pegue as 21 posições
                            break
                return "\n".join(relevant_lines) if relevant_lines else None
        return None

    # Função específica para "Ranking por marca acumulado"
    def extract_ranking_por_marca_acumulado(pdf_path):
        with pdfplumber.open(pdf_path) as pdf:
            page = pdf.pages[8]  # Página 9 (índice 8)
            text = page.extract_text()
            if "Ranking por marca acumulado" in text:
                linhas = text.split("\n")
                relevant_lines = []
                capture = False
                for linha in linhas:
                    if "AUTOMÓVEIS + COMERCIAIS LEVES" in linha:
                        capture = True
                    if capture:
                        relevant_lines.append(linha)
                        if len(relevant_lines) >= 21:  # Garante que pegue as 21 posições
                            break
                return "\n".join(relevant_lines) if relevant_lines else None
        return None

    # Processa o PDF e extrai os títulos relevantes
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()

            # Verifica e armazena os títulos relevantes
            if "Resumo Mensal" in text and 1 not in relevant_pages:
                relevant_pages[1] = ['Resumo mensal']

            if "Ranking por marca" in text:
                relevant_pages[8] = ["Ranking por marca"]
            if "Ranking por marca acumulado" in text:
                relevant_pages[9] = ["Ranking por marca acumulado"]

    # Extrai os dados conforme os títulos encontrados
    for page_number, titles in relevant_pages.items():
        with pdfplumber.open(pdf_path) as pdf:
            page = pdf.pages[page_number - 1]  # Ajuste para índice 0-base
            text = page.extract_text()

            for title in titles:
                if title == "Resumo mensal":
                    resumo_mensal_str = extract_resumo_mensal(pdf_path)
                    if resumo_mensal_str:
                        extracted_data["Resumo mensal"] = resumo_mensal_str
                elif title == "Ranking por marca":
                    ranking_data = extract_ranking_por_marca_normal(pdf_path)
                    if ranking_data:
                        extracted_data["Ranking por marca"] = ranking_data
                elif title == "Ranking por marca acumulado":
                    ranking_data_acumulado = extract_ranking_por_marca_acumulado(pdf_path)
                    if ranking_data_acumulado:
                        extracted_data["Ranking por marca acumulado"] = ranking_data_acumulado
                else:
                    extracted_data[title] = text

    # Verificação do conteúdo extraído
    for title, data in extracted_data.items():
        print(f"{title}:\n{data}\n")

    # Geração dos prompts para LLM
    llm = create_azure_llm()
    for title, data in extracted_data.items():
        if isinstance(data, str):
            tabela_texto = data
        else:
            tabela_texto = data.to_string(index=False, header=True)

        prompt_func = titulos_relevantes.get(title)
        if prompt_func:
            prompt = prompt_func(tabela_texto)
            resposta = llm.invoke([prompt])
            print(f"Resultado da LLM para {title}: {resposta.content}")



