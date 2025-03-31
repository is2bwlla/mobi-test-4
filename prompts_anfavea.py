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

    **OUTPUT**
    "Veículos leves / Light vehicles / Vehiculos livianos": 
    Coluna C: value
    Coluna E: value

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

    **OUTPUT**
    "Veículos leves / Light vehicles / Vehiculos livianos": 
    Coluna C: value
    Coluna E: value

    ---
    """

def prompt_total_licensing_new_vehicles_feb(tabela_texto):
    return f"""
    Você é uma Inteligência Artificial especializada em dados automobilísticos da ANFAVEA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Licenciamento total de autoveículos novos":

    **ENTRADA**
    Aqui estão os dados extraídos da tabela de licenciamento total de autoveículos novos:

    {tabela_texto}

    Objetivo:
    1. Analisar e identificar os valores requisitados nas tabelas;
    2. Extrair os valores de acordo com o tipo de veículo solicitado;
    3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

    **Instruções para extração de dados:**
    1. Para "Veículos leves / Light vehicles / Vehiculos livianos", extraia o valor na coluna 'A' e na coluna 'C';
    2. Para  "Semileves / Semi-light / Semilivianos", extraia o valor na coluna 'A' e na coluna 'C';
    3. Para "Leves / Light / Livianos", extraia o valor na coluna 'A' e na coluna 'C';
    4. Para "Médios / Medium / Medianos", extraia o valor na coluna 'A' e na coluna 'C';
    5. Para "Semipesados / Semi-heavy / Semipesados", extraia o valor na coluna 'A' e na coluna 'C';
    6. Para "Pesados / Heavy / Pesados", extraia o valor na coluna 'A' e na coluna 'C';
    7. Para "Ônibus / Buses / Ómnibus y Colectivos", extraia o valor na coluna 'A' e na coluna 'C'; 

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Veículos leves / Light vehicles / Vehiculos livianos": 
    Coluna C: value
    Coluna E: value

    ---
    """

def prompt_total_licensing_new_vehicles(tabela_texto):
    return f""" 
    Você é uma Inteligência Artificial especializada em dados automobilísticos da ANFAVEA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Licenciamento total de autoveículos novos":

    **ENTRADA**
    Aqui estão os dados extraídos da tabela de licenciamento total de autoveículos novos:

    {tabela_texto}

    Objetivo:
    1. Analisar e identificar os valores requisitados nas tabelas;
    2. Extrair os valores de acordo com o tipo de veículo solicitado;
    3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

    **Instruções para extração de dados:**
    1. Para "Veículos leves / Light vehicles / Vehiculos livianos", extraia o valor na coluna 'A', na coluna 'C', na coluna 'D' e na coluna 'E';
    2. Para  "Semileves / Semi-light / Semilivianos", extraia o valor na coluna 'C' e na coluna 'E';
    3. Para "Leves / Light / Livianos", extraia o valor na coluna 'C' e na coluna 'E';
    4. Para "Médios / Medium / Medianos", extraia o valor na coluna 'C' e na coluna 'E';
    5. Para "Semipesados / Semi-heavy / Semipesados", extraia o valor na coluna 'C' e na coluna 'E';
    6. Para "Pesados / Heavy / Pesados", extraia o valor na coluna 'C' e na coluna 'E';
    7. Para "Ônibus / Buses / Ómnibus y Colectivos", extraia o valor na coluna 'C' e na coluna 'E'; 

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Veículos leves / Light vehicles / Vehiculos livianos": 
    Coluna C: value
    Coluna E: value

    ---
    """

def prompt_licensing_new_imported_vehicles_feb(tabela_texto):
    return f""" 
    Você é uma Inteligência Artificial especializada em dados automobilísticos da ANFAVEA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Licenciamento de autoveículos novos importados":

    **ENTRADA**
    Aqui estão os dados extraídos da tabela de licenciamento total de autoveículos novos:

    {tabela_texto}

    Objetivo:
    1. Analisar e identificar os valores requisitados nas tabelas;
    2. Extrair os valores de acordo com o tipo de veículo solicitado;
    3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

    **Instruções para extração de dados:**
    1. Para "Unidades - Total / Units / Unidades", extraia o valor na coluna 'A' e na coluna 'C';

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Veículos leves / Light vehicles / Vehiculos livianos": 
    Coluna C: value
    Coluna E: value

    ---
    """

def prompt_licensing_new_imported_vehicles(tabela_texto):
    return f"""
    Você é uma Inteligência Artificial especializada em dados automobilísticos da ANFAVEA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Licenciamento de autoveículos novos importados":

    **ENTRADA**
    Aqui estão os dados extraídos da tabela de licenciamento total de autoveículos novos:

    {tabela_texto}

    Objetivo:
    1. Analisar e identificar os valores requisitados nas tabelas;
    2. Extrair os valores de acordo com o tipo de veículo solicitado;
    3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

    **Instruções para extração de dados:**
    1. Para "Unidades - Total / Units / Unidades", extraia o valor na coluna 'C' e na coluna 'E';

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Veículos leves / Light vehicles / Vehiculos livianos": 
    Coluna C: value
    Coluna E: value

    ---
    """

def vehicle_licensing_new_domestic_vehicles_feb(tabela_texto):
    return f"""
    Você é uma Inteligência Artificial especializada em dados automobilísticos da ANFAVEA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Exportações de autoveículos montados":

    **ENTRADA**
    Aqui estão os dados extraídos da tabela de licenciamento total de autoveículos novos:

    {tabela_texto}

    Objetivo:
    1. Analisar e identificar os valores requisitados nas tabelas;
    2. Extrair os valores de acordo com o tipo de veículo solicitado;
    3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

    **Instruções para extração de dados:**
    1. Para "Unidades - Total / Units / Unidades", extraia o valor na coluna 'A' e na coluna 'C';

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Veículos leves / Light vehicles / Vehiculos livianos": 
    Coluna C: value
    Coluna E: value

    ---
    """

def vehicle_licensing_new_domestic_vehicles(tabela_texto):
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

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Veículos leves / Light vehicles / Vehiculos livianos": 
    Coluna C: value
    Coluna E: value

    ---
    """

def exports_assembled_vehicles_feb(tabela_texto):
    return f""" 
    Você é uma Inteligência Artificial especializada em dados automobilísticos da ANFAVEA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Exportações de autoveículos montados":

    **ENTRADA**
    Aqui estão os dados extraídos da tabela de licenciamento total de autoveículos novos:

    {tabela_texto}

    Objetivo:
    1. Analisar e identificar os valores requisitados nas tabelas;
    2. Extrair os valores de acordo com o tipo de veículo solicitado;
    3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

    **Instruções para extração de dados:**
    1. Para "Unidades - Total / Units / Unidades", extraia o valor na coluna 'A' e na coluna 'C';
    2. Para "Caminhões / Trucks / Camiones", extraia o valor na coluna 'A' e na coluna 'C';
    3. Para "Ônibus / Buses / Ómnibus y Colectivos", extraia o valor na coluna 'A' e na coluna 'C';

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Veículos leves / Light vehicles / Vehiculos livianos": 
    Coluna C: value
    Coluna E: value

    ---
    """
def exports_assembled_vehicles(tabela_texto):
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
    2. Para "Caminhões / Trucks / Camiones", extraia o valor na coluna 'C' e na coluna 'E';
    3. Para "Ônibus / Buses / Ómnibus y Colectivos", extraia o valor na coluna 'C' e na coluna 'E';

    **Nota**: 
    - Caso um valor apareça na tabela em múltiplos números (como "20.395 6.976"), você deve considerar ambos os números separadamente e mantê-los no formato original.
    - Retorne o valor como string, sem alterar o formato.

    **OUTPUT**
    "Veículos leves / Light vehicles / Vehiculos livianos": 
    Coluna C: value
    Coluna E: value

    ---
    """

