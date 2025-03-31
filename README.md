### bibliotecas:
- dotenv;
- langchain_openai;
- pandas;
- pdfplumber;

## ESTUDAR:
1. Biblioteca "tabula-py" :
     ```pip install tabula-py```

2. Biblioteca "pandas":
     ```pip install pandas```

3. Biblioteca "langchain_openai":
     ```pip install -qU "langchain[openai]"```

4. Biblioteca "jpype1":
     ```pip install jpype1```

## ADICIONAR NO PROMPT:
1. Adicionar a tratativa condicional sobre a diferença entre meses;
     - As cartas com as informações de janeiro possuem formatações diferentes de tabelas, essas cartas sempre saem em fevereiro;
     - As cartas dos outros meses possuem formatações diferentes da de janeiro;
     - Todas as cartas saem sempre no mês seguinte para fins de ter todos os dados do mês de consulta;
     - Retirar as informações que a IA retorna pra usar no código.


## FALTA FAZER:
1. Descobrir como extrair os dados das tabelas da fenabrave;
     a. Analisar quais as cartas da fenabrave que são usadas;
     b. Se tem diferença entre janeiro e os outros meses;
     c. Formatação das tabelas (cabeçalho);
     d. Prompts.

2. Descobrir como extrair os dados das tabelas da acara:
     a.

## PROMPTS:
- ANFAVEA:
     ### 1) Produção de autoveículos montados:
    - prompt_janeiro = f""" 
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

     ====================================================================================================================

    - prompt_others = f"""
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

    ### 2) Licenciamento total de autoveículos novos:
    - prompt_janeiro = f"""
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

    ---
    """

    ====================================================================================================================

    - prompt_others = f""" 
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

    ---
    """

    ### 3) Licenciamento de autoveículos novos importados:

    - prompt_janeiro = f""" 
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

    ---
    """

    ====================================================================================================================

    - prompt_others = f"""
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

    ---
    """

     ### 4) Licenciamento de autoveículos novos nacionais:

    - prompt_janeiro = f"""
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

    ---
    """

    ====================================================================================================================

    - prompt_others = """
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

    ---
    """

     ### 5) Exportações de autoveículos montados:

    - prompt_janeiro = f""" 
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

    ---
    """

    ====================================================================================================================

    - prompt_others = """
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

    ---
    """
