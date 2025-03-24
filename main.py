# Usando tabula-py + pandas
import os
import json
import pandas as pd
from tabula import read_pdf
from azure_llm import create_azure_llm 

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
        table.columns = table.iloc[0]  # Usar a primeira linha como cabeçalho
        table = table[1:].reset_index(drop=True)

        # Limpar NaN, removendo linhas com NaN ou substituindo por valores válidos
        table = table.dropna(how="all")  # Remove linhas que estão completamente vazias
        table = table.fillna('')  # Substitui os NaNs restantes por string vazia

        # Adicionar os dados extraídos como DataFrame
        extracted_data["Produção de autoveículos montados"] = table

        # Debug: Verificar as primeiras linhas para entender melhor a estrutura
        print("Primeiras linhas da tabela:")
        print(table.head())

    return extracted_data

def process_pdf_and_generate_prompts(pdf_path: str):
    """
    Processa o PDF, extrai tabelas relevantes e gera prompts para análise com LLM.
    """
    extracted_tables = extract_and_process_tables_anfavea(pdf_path)
    llm = create_azure_llm()

    # Processar a tabela extraída
    for paginaTitulo, dadosTabela in extracted_tables.items():
        print(f"\n### Dados extraídos da página: {paginaTitulo}")
        print(dadosTabela)  # Aqui você vê a tabela como um DataFrame, direto

        prompt = """ 
        Você é uma Inteligência Artificial especializada em dados automobilísticos da ANFAVEA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Produção de autoveículos montados":

        Objetivo:
        1. Analisar e identificar os valores requisitados nas tabelas;
        2. Extrair os valores de acordo com o tipo de veículo solicitado;
        3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

        **TABELA DE EXEMPLO**:

        0                                                 NaN  NaN  JAN/ENE  DEZ/DIC  JAN/ENE    A/B    A/C  
        0                                                 NaN  NaN        A        B        D      %      %  
        1                 Unidades - Total / Units / Unidades  NaN  175.541  190.131  152.564   -7,7   15,1  
        2   Veículos leves / Light vehicles / Vehículos li...  NaN  165.694  177.758  143.027   -6,8   15,8  
        3           Automóveis / Passenger cars / Automóviles  NaN  134.931  139.075  117.025   -3,0   15,3  
        4   Comerciais leves / Light commercials / Comerci...  NaN   30.763   38.683   26.002  -20,5   18,3  
        5                       Caminhões / Trucks / Camiones  NaN    8.041   10.679    7.941  -24,7    1,3  
        6               Semileves / Semi-light / Semilivianos           56       26       47  115,4   19,1  
        7                            Leves / Light / Livianos        1.152    1.413    1.637  -18,5  -29,6  
        8                          Médios / Medium / Medianos          320      328      162   -2,4   97,5  
        9              Semipesados / Semi-heavy / Semipesados        2.426    2.955    2.124  -17,9   14,2  
        10                          Pesados / Heavy / Pesados        4.087    5.957    3.971  -31,4    2,9  
        11  Ônibus (Chassis)/Buses (Chassis)/Ómnibus y Col...        1.806    1.694    1.596    6,6   13,2  
        12                       Rodoviário / Coach / Ómnibus          390      281      264   38,8   47,7  
        13                    Urbano / City bus / Colecti vos        1.416    1.413    1.332    0,2    6,3  

        ---

        **Instruções para extração de dados:**
        1. Para "Unidades - Total / Units / Unidades", extraia o valor na coluna correspondente ao mês 'A';
        2. Para "Veículos leves / Light vehicles / Vehículos livianos", extraia o valor na coluna 'A';
        3. Para "Caminhões / Trucks / Camiones", extraia o valor na coluna 'A';
        4. Para "Ônibus (Chassis)/Buses (Chassis)/Ómnibus y Colectivos (Chassis)", extraia o valor na coluna 'JAN/ENE'.

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

        print("\n--- Análise com LLM ---")
        resposta = llm.invoke([prompt])
        print(f"\n### Resposta da IA para {paginaTitulo}: {resposta.content}\n")


if __name__ == "__main__":
    pdf_filename = "carta465.pdf"
    pdf_path = os.path.join(os.path.dirname(__file__), pdf_filename)
    process_pdf_and_generate_prompts(pdf_path)
