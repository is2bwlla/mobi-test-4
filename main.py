# USANDO TABULA + PANDAS
import os
import pandas as pd
from tabula import read_pdf
import pdfplumber
from datetime import datetime
from azure_llm import create_azure_llm 

def get_page_titles(pdf_path):
    titles = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            # Extrair título da página (a lógica de extração de títulos pode variar conforme o formato do PDF)
            lines = text.split('\n')
            for line in lines:
                if 'Produção de autoveículos montados' in line:
                    titles.append("Produção de autoveículos montados")
                elif 'Licenciamento total de autoveículos novos' in line:
                    titles.append("Licenciamento total de autoveículos novos")
    return titles

# Configuração do Pandas para visualizar melhor a tabela
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 1000)

def extract_and_process_tables_anfavea(pdf_path: str):
    """
    Extrai a tabela relevante do PDF e retorna como DataFrame.
    """
    print("Extraindo tabelas do PDF...")
    tables = read_pdf(pdf_path, pages="10", lattice=False, stream=True)  # Ajuste páginas conforme necessário
    
    extracted_data = {}
    
    # Processar a primeira tabela extraída
    if tables:
        table = tables[0]  # Pegando apenas a primeira tabela extraída
        table.columns = table.iloc[1]  # Usar a primeira linha como cabeçalho
        table = table[1:].reset_index(drop=True)

        # Limpar NaN, removendo linhas com NaN ou substituindo por valores válidos
        table = table.dropna(how="all")
        table = table.fillna('')

        #Adicionar os dados extraídos como DataFrame
        extracted_data["Produção de autoveículos montados"] = table
        print(table.columns)  # Verifica os rótulos das colunas


        #Verificar as primeiras linhas para entender melhor a estrutura
        # print("Primeiras linhas da tabela:")
        # print(table.head())

    return extracted_data

def process_pdf_and_generate_prompts(pdf_path: str):
    """
    Processa o PDF, extrai tabelas relevantes e gera prompts para análise com LLM.
    """
    extracted_tables = extract_and_process_tables_anfavea(pdf_path)
    page_titles = get_page_titles(pdf_path)
    llm = create_azure_llm()

    mes_atual = datetime.now().month
    print(mes_atual)

    # for page_title in page_titles:
    #     print(f"\n### Processando dados da página: {page_title}")

    #     if page_title == "Produção de autoveículos montados":
    #         if mes_atual == 2:

    #             return prompt
            
    #         else:
    #             prompt = 


    # Processar a tabela extraída
    for paginaTitulo, dadosTabela in extracted_tables.items():
        print(f"\n### Dados extraídos da página: {paginaTitulo}")
        print(dadosTabela)  # Aqui você vê a tabela como um DataFrame, direto

        # Converter a tabela para string (formato legível)
        tabela_texto = dadosTabela.to_string(index=False, header=True) # Transformando a tabela em texto

        prompt = f""" 
        Você é uma Inteligência Artificial especializada em dados automobilísticos da ANFAVEA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Produção de autoveículos montados":

        **ENTRADA**
        Aqui estão os dados extraídos da tabela de produção de autoveículos montados:

        {tabela_texto}

        Objetivo:
        1. Analisar e identificar os valores requisitados nas tabelas;
        2. Extrair os valores de acordo com o tipo de veículo solicitado;
        3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

        **Instruções para extração de dados:**
        1. Para "Unidades - Total / Units / Unidades", extraia o valor na coluna 'A' e na coluna 'D';
        2. Para "Veículos leves / Light vehicles / Vehículos livianos", extraia o valor na coluna 'A' e na coluna 'D';
        3. Para "Caminhões / Trucks / Camiones", extraia o valor na coluna 'A' e na coluna 'D';
        4. Para "Ônibus (Chassis)/Buses (Chassis)/Ómnibus y Colectivos (Chassis)", extraia o valor na coluna 'A' e na coluna 'D'.

        **Nota**: 
        - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
        - Retorne o valor como string, sem alterar o formato.

        **Exemplo de OUTPUT esperado:**

        Acumulados "Unidades - Total / Units / Unidades": "111.999"
        Acumulados "Veículos leves / Light vehicles / Vehículos livianos": "165.954"
        Acumulados "Caminhões / Trucks / Camiones": "8.461"
        Acumulados "Ônibus (Chassis)/Buses (Chassis)/Ómnibus y Colectivos (Chassis)": "1.840"

        ---
        """

        # print("\n--- Análise com LLM ---")
        # resposta = llm.invoke([prompt])
        # print(resposta.content)


if __name__ == "__main__":
    pdf_filename = "carta466.pdf"
    pdf_path = os.path.join(os.path.dirname(__file__), pdf_filename)
    process_pdf_and_generate_prompts(pdf_path)
