# MOBI AI - Extração de PDF
O MOBI AI é um projeto de automatização de processo de criação de um report automobilístico, os arquivos de extração fazem o papel de extrair tabelas de determinados PDF de associações contendo informações sobre o mercado automotivo. 

A partir da extração feita através de um script python, as tabelas com dados relevantes para a criação do Market Report são passadas para um modelo de Inteligência Artificial Generativa da OpenAI, modelo 'gpt-4o-mini'. Juntamente com um prompt estruturado, a Inteligência Artificial é capaz de identificar quais os valores necessários para serem extraídos, dessa forma, excluindo o processo manual de leitura, compreensão e preenchimento de um arquivo Excel.

As associações utilizadas são divididas entre brasileiras e argentinas, sendo elas respectivamente ANFAVEA, FENABRAVE, ADEFA E ACARA. 

Cada uma das cartas recebe um arquivo de extração específico para seu tipo de arquivo, alguns deles sendo estruturados por meio de imagens, textos estruturados e tabelas.

