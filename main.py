# USANDO TABULA + PANDAS
import os
import pandas as pd
from tabula import read_pdf
import pdfplumber
from datetime import datetime
from azure_llm import create_azure_llm 

mes_atual = datetime.now().month    # Define qual o mês atual para fazer uma verificação no decorrer do código

titulos_relevantes = [
    "Produção de autoveículos montados",
    "Licenciamento total de autoveículos novos",
    "Licenciamento de autoveículos novos nacionais",
    "Licenciamento de autoveículos novos importados",
    "Exportações de autoveículos montados"
]

# Configuração do Pandas para visualizar melhor a tabela
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 1000)

def get_relevant_pages_and_titles(pdf_path):
    """
    Lê o PDF e retorna um dicionário com os números das páginas relevantes e seus títulos correspondentes.
    """
    relevant_pages = {}

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()  # Extrair título da página (a lógica de extração de títulos pode variar conforme o formato do PDF)
            for title in titulos_relevantes:
                if title in text:
                    relevant_pages[page_number] = title
                    break   # Não precisa continuar verificando outros títulos na mesma página

    return relevant_pages

def extract_and_process_tables_anfavea(pdf_path, relevant_pages):
    """
    Extrai tabelas do PDF com base nas páginas e títulos relevantes detectados.
    Retorna um dicionário contendo as tabelas extraídas.
    """
    extracted_data = {}

    for page_number, title in relevant_pages.items():
        print(f"Extraindo tabela da página {page_number} - {title}")
        tables = read_pdf(pdf_path, pages=str(page_number), lattice=False, stream=True)  # Ajuste páginas conforme necessário

        if tables:
            table = tables[0]   # Considerando que a tabela de interesse está na primeira posição

            # Ajuste o cabeçalho da tabela conforme o mês atual
            if mes_atual == 2:
                table.columns = table.iloc[1]   # Usar a segunda linha como cabeçalho
            else:
                table.columns = table.iloc[0]   # Usar a primeira linha como cabeçalho

            table = table[1:].reset_index(drop=True)


            # Limpar dados NaN e preencher valores vazios
            table = table.dropna(how="all")
            table = table.fillna('')

            extracted_data[title] = table
    
    return extracted_data


def process_pdf_and_generate_prompts(pdf_path):
    """
    Processa o PDF, extrai tabelas relevantes e gera prompts para análise com LLM.
    """
    relevant_pages_and_titles = get_relevant_pages_and_titles(pdf_path)
    extracted_tables = extract_and_process_tables_anfavea(pdf_path, relevant_pages_and_titles)
    
    llm = create_azure_llm()    # Essa função cria um cliente LLM conectado

    for title, table in extracted_tables.items();
        print(f"\n### Dados extraídos da tabela: {title} ###")

        tabela_texto = table.to_string(index=False, header=True)

        # Selecionar função de prompt baseada no título e no mês
        prompt_fev_func, prompt_outros_func = titulos_relevantes.get(title, (None, None))
        
        if mes_atual == 2:
            if titl


    # Processar a tabela extraída
    # for paginaTitulo, dadosTabela in extracted_tables.items():
    #     print(f"\n### Dados extraídos da página: {paginaTitulo}")
    #     print(dadosTabela)  # Aqui você vê a tabela como um DataFrame, direto

    #     # Converter a tabela para string (formato legível)
    #     tabela_texto = dadosTabela.to_string(index=False, header=True) # Transformando a tabela em texto

    #     prompt = f""" 
    #     Você é uma Inteligência Artificial especializada em dados automobilísticos da ANFAVEA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Licenciamento total de autoveículos novos":

    #     **ENTRADA**
    #     Aqui estão os dados extraídos da tabela de licenciamento total de autoveículos novos:

    #     {tabela_texto}

    #     Objetivo:
    #     1. Analisar e identificar os valores requisitados nas tabelas;
    #     2. Extrair os valores de acordo com o tipo de veículo solicitado;
    #     3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

    #     **Instruções para extração de dados:**
    #     1. Para "Veículos leves / Light vehicles / Vehiculos livianos", extraia o valor na coluna 'A' e na coluna 'C';
    #     2. Para  "Semileves / Semi-light / Semilivianos", extraia o valor na coluna 'A' e na coluna 'C';
    #     3. Para "Leves / Light / Livianos", extraia o valor na coluna 'A' e na coluna 'C';
    #     4. Para "Médios / Medium / Medianos", extraia o valor na coluna 'A' e na coluna 'C';
    #     5. Para "Semipesados / Semi-heavy / Semipesados", extraia o valor na coluna 'A' e na coluna 'C';
    #     6. Para "Pesados / Heavy / Pesados", extraia o valor na coluna 'A' e na coluna 'C';
    #     7. Para "Ônibus / Buses / Ómnibus y Colectivos", extraia o valor na coluna 'A' e na coluna 'C'; 

    #     **Nota**: 
    #     - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    #     - Retorne o valor como string, sem alterar o formato.

    #     ---
    #     """

    #     print("\n--- Análise com LLM ---")
    #     resposta = llm.invoke([prompt])
    #     print(resposta.content)


if __name__ == "__main__":
    pdf_filename = "carta453.pdf"
    pdf_path = os.path.join(os.path.dirname(__file__), pdf_filename)
    process_pdf_and_generate_prompts(pdf_path)
