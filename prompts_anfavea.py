def prompt_anfavea_production_assembled_vehicles_feb(tabela_texto):
    return f""" 
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

    ---
    """

def prompt_anfavea_production_assembled_vehicles(tabela_texto):
    return f"""
    Você é uma Inteligência Artificial especializada em dados automobilísticos da ANFAVEA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Produção de autoveículos montados":

    **ENTRADA**
    Aqui estão os dados extraídos da tabela de produção de autoveículos montados:

    {tabela_texto}

    Objetivo:
    1. Analisar e identificar os valores requisitados nas tabelas;
    2. Extrair os valores de acordo com o tipo de veículo solicitado;
    3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

    **Instruções para extração de dados:**
    1. Para "Unidades - Total / Units / Unidades", extraia o valor na coluna 'C' e na coluna 'E';
    2. Para "Veículos leves / Light vehicles / Vehículos livianos", extraia o valor na coluna 'C' e na coluna 'E';
    3. Para "Caminhões / Trucks / Camiones", extraia o valor na coluna 'C' e na coluna 'E';
    4. Para "Ônibus (Chassis)/Buses (Chassis)/Ómnibus y Colectivos (Chassis)", extraia o valor na coluna 'C' e na coluna 'E'.

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    ---
    """

