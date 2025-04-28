def adefa_production_automobiles_and_light_commercials_feb(tabela_texto):
	return f""" 
	Você é uma Inteligência Artificial especializada em dados automobilísticos da ADEFA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Producción
    Automóviles y Comerciales Livianos":

    **ENTRADA**
    Aqui estão os dados extraídos da tabela de Producción
    Automóviles y Comerciales Livianos:

    {tabela_texto}

    Objetivo:
    1. Analisar e identificar os valores requisitados nas tabelas;
    2. Extrair os valores de acordo com o tipo de veículo solicitado;
    3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

    **Instruções para extração de dados:**
    1. Para "Enero", extraia os valores da coluna A (valor) e da coluna B (valor). Certifique-se de que está pegando a linha "Enero" corretamente, e não o valor de "Total".

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Enero": 
    Coluna A: value
    Coluna B: value

    ---

"""

def adefa_exports_automobiles_and_light_commercials_feb(tabela_texto):
	return f"""
	Você é uma Inteligência Artificial especializada em dados automobilísticos da ADEFA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Exportaciones
    Automóviles y Comerciales Livianos":

    **ENTRADA**
    Aqui estão os dados extraídos da tabela de Exportaciones
    Automóviles y Comerciales Livianos:

    {tabela_texto}

    Objetivo:
    1. Analisar e identificar os valores requisitados nas tabelas;
    2. Extrair os valores de acordo com o tipo de veículo solicitado;
    3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

    **Instruções para extração de dados:**
    1. Para "Enero", extraia os valores da coluna A (valor) e da coluna B (valor). Certifique-se de que está pegando a linha "Enero" corretamente, e não o valor de "Total".

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Enero": 
    Coluna A: value
    Coluna B: value

    ---
"""

def adefa_production_automobiles_and_light_commercials(tabela_texto):
    return f""" 
    Você é uma Inteligência Artificial especializada em dados automobilísticos da ADEFA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Producción
    Automóviles y Comerciales Livianos":

    **ENTRADA**
    Aqui estão os dados extraídos da tabela de Producción
    Automóviles y Comerciales Livianos:

    {tabela_texto}

    **Instruções para extração de dados:**
    1. Para "Subtotal", extraia os valores da coluna A (valor) e da coluna B (valor). Certifique-se de que está pegando a linha "Subtotal" corretamente, e não o valor de "Total".

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Não extraia o valor da linha "Total", apenas a linha referente a "Subtotal".
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Subtotal": 
    Coluna A: value
    Coluna B: value

    ---
"""

def adefa_exports_automobiles_and_light_commercials(tabela_texto):
	return f"""
	Você é uma Inteligência Artificial especializada em dados automobilísticos da ADEFA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Exportaciones
    Automóviles y Comerciales Livianos":

    **ENTRADA**
    Aqui estão os dados extraídos da tabela de Exportaciones
    Automóviles y Comerciales Livianos:

    {tabela_texto}

    Objetivo:
    1. Analisar e identificar os valores requisitados nas tabelas;
    2. Extrair os valores de acordo com o tipo de veículo solicitado;
    3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

    **Instruções para extração de dados:**
    1. Para "Subtotal", extrair os dados da coluna A e da coluna B.

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Subtotal": 
    Coluna A: value
    Coluna B: value

    ---
"""
 