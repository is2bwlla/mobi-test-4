### bibliotecas:
- dotenv;
- langchain_openai;
- pandas;

## ESTUDAR:
1. Biblioteca "tabula-py" :
     ```pip install tabula-py```

2. Biblioteca "pandas":
     ```pip install pandas```

3. Biblioteca "langchain_openai":
     ```pip install -qU "langchain[openai]"```

## ADICIONAR NO PROMPT:
1. Adicionar a tratativa condicional sobre a diferença entre meses;
     - As cartas com as informações de janeiro possuem formatações diferentes de tabelas, essas cartas sempre saem em fevereiro;
     - As cartas dos outros meses possuem formatações diferentes da de janeiro;
     - Todas as cartas saem sempre no mês seguinte para fins de ter todos os dados do mês de consulta;
     - Retirar as informações que a IA retorna pra usar no código.


## FALTA FAZER:
1. Prompts das outras categorias da ANFAVEA: 
     - Produção de autoveículos montados: versão meses com acumulos (os que não são de janeiro);
          1) **JANEIRO** prompt = """ 
                Você é uma Inteligência Artificial especializada em dados automobilísticos da ANFAVEA. Sua tarefa é analisar e extrair os seguintes dados da categoria "Produção de autoveículos montados":

                Objetivo:
                1. Analisar e identificar os valores requisitados nas tabelas;
                2. Extrair os valores de acordo com o tipo de veículo solicitado;
                3. Retornar os valores sem arredondamentos e sem alterações, mantendo múltiplos números quando presentes.

                **TABELA DE EXEMPLO**:

                0                                                 NaN  NaN  JAN/ENE  DEZ/DIC  JAN/ENE    A/B    A/C  
                0                                                                 A        B        D      %      %  
                1                 Unidades - Total / Units / Unidades       175.541  190.131  152.564   -7,7   15,1  
                2   Veículos leves / Light vehicles / Vehículos li...       165.694  177.758  143.027   -6,8   15,8  
                3           Automóveis / Passenger cars / Automóviles       134.931  139.075  117.025   -3,0   15,3  
                4   Comerciais leves / Light commercials / Comerci...        30.763   38.683   26.002  -20,5   18,3  
                5                       Caminhões / Trucks / Camiones         8.041   10.679    7.941  -24,7    1,3  
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

          2) **OUTROS MESES** prompt = """

                """


     - Licenciamento total de autoveículos novos: ambas as versões, janeiro + outros meses;
     - Licenciamento de autoveículos novos nacionais: ambas as versões, janeiro + outros meses;
     - Licenciamento de autoveículos novos importados: ambas as versões, janeiro + outros meses;
     - Exportações de autoveículos montados: ambas as versões, janeiro + outros meses;
