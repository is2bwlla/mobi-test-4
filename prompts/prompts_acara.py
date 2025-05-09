def acara_market_summary(tabela_texto):
	return f""" 
	Você é uma Inteligência Artificial especializada em dados automobilísticos da ACARA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Resumen del mercado.":

    **ENTRADA**
    Aqui estão os dados extraídos da tabela de Resumen del mercado:

    {tabela_texto}

    Objetivo:
    1. Analisar e identificar os valores requisitados nas tabelas;
    2. Extrair os valores de acordo com o tipo de veículo solicitado;
    3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.
	4. Mantenha os valores exatamente como aparecem, inclusive com pontos separadores de milhar (ex: "11.537").

    **Instruções para extração de dados:**
    1. Para a linha "Autos + C.L.", extraia os valores da **coluna F** (Acumulado 2025) e **coluna G** (Acumulado 2024).
    2. Para a linha "Autos + C.L. + C.P.", extraia os valores da **coluna F** e **coluna G**.
    3. Para a linha "Comercial Pesado", extraia os valores da **coluna F** e **coluna G**.

    **Importante**: Use a **letra da coluna** para localizar o valor, e **não o cabeçalho** ou o conteúdo do cabeçalho.

    **OUTPUT**
    "Autos + C.L.":
    Coluna F: value
    Coluna G: value

    "Autos + C.L. + C.P.":
    Coluna F: value
    Coluna G: value

    "Comercial Pesado":
    Coluna F: value
    Coluna G: value

    ---
"""

def acara_40_lightweight_brands_ranking(tabela_texto):
    return f"""
    Você é uma Inteligência Artificial especializada em dados automobilísticos da ACARA. Sua tarefa é extrair dados de vendas por marca a partir da seguinte tabela, em que as colunas estão identificadas apenas por letras (Categoria, A, B, C...).

    ### Entrada:
    {tabela_texto}

    ### Objetivo:
    Para cada linha com uma marca válida, extraia os seguintes valores fixos:

    - Nome da marca → Coluna "Categoria"
    - Para a linha que contém "Marca", extraia o valor da coluna B;
    - Para a linha que contém "Marca", extraia o valor da coluna F;
    - Para a linha que contém "Marca", extraia o valor da coluna I;
    - Para a linha que contém "Marca", extraia o valor da coluna K;

    ### Instruções:
    - Use **apenas as letras das colunas** para localizar os valores. Ignore os títulos, nomes de meses ou quaisquer outras anotações nos cabeçalhos.
    - Mantenha os valores exatamente como aparecem, inclusive com pontos como separador de milhar (ex: "11.537").

    ### OUTPUT
    Marca:
    Coluna B: value
    Coluna F: value
    Coluna I: value
    Coluna K: value

    ---
"""


def acara_10_heavy_commercial_brands_ranking(tabela_texto):
    return f""" 
    Você é uma Inteligência Artificial especializada em dados automobilísticos da ACARA. Sua tarefa é extrair dados de vendas por marca a partir da seguinte tabela, em que as colunas estão identificadas apenas por letras (Categoria, A, B, C...).

    ### Entrada:
    {tabela_texto}

    ### Objetivo:
    Para cada linha com uma marca válida, extraia os seguintes valores fixos:

    - Nome da marca → Coluna "Categoria"
    - Para a linha que contém "Marca", extraia o valor da coluna B;
    - Para a linha que contém "Marca", extraia o valor da coluna F;
    - Para a linha que contém "Marca", extraia o valor da coluna J;
    - Para a linha que contém "Marca", extraia o valor da coluna L;

    ### Instruções:
    - Use **apenas a posição da coluna pela letra** para localizar os valores.
    - Mantenha os valores exatamente como aparecem, com pontos como separador de milhar (ex: "11.537").
    - Ignore linhas como “TOTAL”, “RESTO”, ou linhas incompletas.
    - Ignore colunas com porcentagens.

    ### OUTPUT
    Marca:
    Coluna B: value
    Coluna F: value
    Coluna J: value
    Coluna L: value

    ---
"""

