def prompt_fenabrave_monthly_summary(tabela_texto):
    return f"""
    Você é uma Inteligência Artificial especializada em dados automobilísticos da FENABRAVE.

    Sua tarefa é analisar **apenas os dados da tabela da página 1 do relatório**, que representa o **Resumo Mensal**. Essa tabela contém uma linha chamada "A + B", que reúne os dados totais de Automóveis e Comerciais Leves.

    ### ENTRADA:
    Texto extraído da tabela da página 1:

    {tabela_texto}

    ### OBJETIVO:
    1. Identificar a linha "A + B";
    2. Extrair os valores correspondentes às seguintes colunas:
    - **Coluna A** (Total de vendas no mês atual no ano atual);
    - **Coluna C** (Total acumulado até o mês atual no ano atual);
    - **Coluna D** (Total de vendas do mesmo mês no ano anterior);
    - **Coluna E** (Total acumulado até o mesmo mês no ano anterior).

    **Importante:**
    - Caso a célula contenha dois ou mais valores (ex: "20.395 6.976"), mantenha todos os valores **juntos, como string**.
    - Retorne exatamente o texto presente na célula, **sem arredondar ou modificar**.
    - Ignore qualquer valor de variação percentual ou colunas de comparação (ex: (A)/(B), (A)/(D), etc).

    ### OUTPUT ESPERADO:
    "Resumo Mensal":  
    Coluna A: value  
    Coluna C: value  
    Coluna D: value  
    Coluna E: value  

    ---
    """


def prompt_fenabrave_monthly_brand_ranking(tabela_texto):
    return f"""
    Você é uma Inteligência Artificial especializada em dados automobilísticos da FENABRAVE.

    A tabela a seguir representa **exclusivamente o 'Ranking por marca por mês'**, contendo dados combinados de **automóveis e comerciais leves**.

    ⚠️ **IMPORTANTE**:
    - Analise **somente a primeira tabela sequencial com os dados do mês**.
    - Ignore completamente outras tabelas ou seções que contenham:
        - Dados com porcentagem (%)
        - Dados com mais de um número por célula
        - Repetição de nomes de fabricantes
        - Títulos ou subtítulos de novas seções
    - **Interrompa a análise assim que perceber mudança de padrão, repetição ou nova tabela.**

    ### Entrada (tabela oficial do mês):
    {tabela_texto}

    ### Objetivo:
    1. Para cada linha da tabela, extraia:
    - **Fabricante** (nome da montadora);
    - **Quant.** (quantidade acumulada de unidades vendidas, sem % ou múltiplos valores).
    2. Retorne apenas os dados que seguem a sequência correta da tabela acumulada.
    3. Se houver qualquer descontinuidade, dados fora do padrão ou repetição de marcas, **interrompa a coleta imediatamente**.

    ### Saída esperada (formato):
    1°:
        fabricante: FIAT,
        quant.: 34.352
    2°:
        fabricante: VW,
        quant.: 21.126
    ...

    ---
    """

def prompt_fenabrave_cumulative_brand_ranking(tabela_texto):
    return f""" 
    Você é uma Inteligência Artificial especializada em dados automobilísticos da FENABRAVE.

    A tabela a seguir representa **exclusivamente o 'Ranking por marca acumulado'**, contendo dados combinados de **automóveis e comerciais leves**.

    **IMPORTANTE**:
    - Analise **somente a primeira tabela sequencial com os dados acumulados**.
    - Ignore completamente outras tabelas ou seções que contenham:
        - Dados com porcentagem (%)
        - Dados com mais de um número por célula
        - Repetição de nomes de fabricantes
        - Títulos ou subtítulos de novas seções
    - **Interrompa a análise assim que perceber mudança de padrão, repetição ou nova tabela.**

    ### Entrada (tabela oficial do acumulado):
    {tabela_texto}

    ### Objetivo:
    1. Para cada linha da tabela, extraia:
    - **Fabricante** (nome da montadora);
    - **Quant.** (quantidade acumulada de unidades vendidas, sem % ou múltiplos valores).
    2. Retorne apenas os dados que seguem a sequência correta da tabela acumulada.
    3. Se houver qualquer descontinuidade, dados fora do padrão ou repetição de marcas, **interrompa a coleta imediatamente**.

    ### Saída esperada (formato):
    1°:
        fabricante: FIAT,
        quant.: 34.352
    2°:
        fabricante: VW,
        quant.: 21.126
    ...

    ---
    """

