import os
from extraction.pdf_extractor_anfavea import process_pdf_and_generate_prompts_anfavea
from extraction.pdf_extractor_fenabrave import process_pdf_and_generate_prompts_fenabrave
from extraction.pdf_extractor_adefa import process_pdf_and_generate_prompts_adefa
from extraction.pdf_extractor_acara import process_pdf_and_generate_prompts_acara
from excel_generator import create_excel_file

# Dicionário de arquivos PDF mapeados para suas funções de extração
pdf_files = {
    "carta452.pdf": process_pdf_and_generate_prompts_anfavea,
    "2025_02_02.pdf": process_pdf_and_generate_prompts_fenabrave,
    "resumen-2025-03-es.pdf": process_pdf_and_generate_prompts_adefa,
    "2025.02. SIOMAA. Informe de Mercado 4W.pdf": process_pdf_and_generate_prompts_acara
}

def main():
    # Caminho da pasta onde os PDFs estão localizados
    pdf_folder = os.path.join(os.path.dirname(__file__), "pdf")
    
    # Dicionários para armazenar os dados extraídos de cada função
    dados_anfavea = None
    dados_fenabrave = None
    dados_adefa = None
    dados_acara = None
    
    # Iterando sobre o dicionário de arquivos
    for pdf_filename, process_function in pdf_files.items():
        # Construindo o caminho completo do PDF
        pdf_path = os.path.join(pdf_folder, pdf_filename)
        
        # Verificando qual arquivo está sendo processado
        print(f"Processando o arquivo {pdf_filename}...")
        
        # Processa o arquivo PDF e gera os dados
        if process_function == process_pdf_and_generate_prompts_anfavea:
            dados_anfavea = process_function(pdf_path)
        elif process_function == process_pdf_and_generate_prompts_fenabrave:
            dados_fenabrave = process_function(pdf_path)
        elif process_function == process_pdf_and_generate_prompts_adefa:
            dados_adefa = process_function(pdf_path)
        elif process_function == process_pdf_and_generate_prompts_acara:
            dados_acara = process_function(pdf_path)

    # Depois de processar todos os PDFs, cria o Excel com os dados extraídos
    create_excel_file(dados_adefa, dados_acara, dados_anfavea, dados_fenabrave)
    print("Arquivo Excel gerado com sucesso!")

if __name__ == "__main__":
    main()
