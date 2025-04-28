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

    **Instruções para extração de dados:**
    1. Para "Autos + C.L.", extraia os valores da coluna F (valor) e da coluna G (valor).
    2. Para "Autos + C.L. + C.P.", extraia os valores da coluna F (valor) e da coluna G (valor).
    3. Para "Comercial Pesado", extraia os valores da coluna F (valor) e da coluna G (valor).

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Autos + C.L.": 
    Coluna F: value
    Coluna G: value

    ---

"""

def acara_40_lightweight_brands_ranking(tabela_texto): 
	return f""" 
	Você é uma Inteligência Artificial especializada em dados automobilísticos da ACARA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Ranking. TOP 40. Marcas Livianos (Automóviles + Comerciales Livianos)":

    **ENTRADA**
    Aqui estão os dados extraídos da tabela de Ranking. TOP 40. Marcas Livianos (Automóviles + Comerciales Livianos):

    {tabela_texto}

    Objetivo:
    1. Analisar e identificar os valores requisitados nas tabelas;
    2. Extrair os valores de acordo com o tipo de veículo solicitado;
    3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

    **Instruções para extração de dados:**
    1. Para cada linha da tabela, extraia:
    - Coluna A;
    - Coluna C;
    - Coluna E;
    - Coluna F.

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Marca": 
    Coluna A: value
    Coluna C: value	
    Coluna E: value
    Coluna F: value

    ---

"""

def acara_10_heavy_commercial_brands_ranking(tabela_texto):
	return f""" 
	Você é uma Inteligência Artificial especializada em dados automobilísticos da ACARA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Ranking. TOP 10. Marcas Comerciales Pesados":

    **ENTRADA**
    Aqui estão os dados extraídos da tabela de Ranking. TOP 10. Marcas Comerciales Pesados:

    {tabela_texto}

    Objetivo:
    1. Analisar e identificar os valores requisitados nas tabelas;
    2. Extrair os valores de acordo com o tipo de veículo solicitado;
    3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

    **Instruções para extração de dados:**
    1. Para cada linha da tabela, extraia:
    - Coluna A;
    - Coluna C;
    - Coluna E;
    - Coluna F.

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Marca": 
    Coluna A: value
    Coluna C: value	
    Coluna E: value
    Coluna F: value

    ---

"""
