from pdf_extractor import PDFExtractor
from azure_llm import create_azure_llm
import json
import os
import pdfs
from prompts_anfavea import (
    prompt_anfavea_production_assembled_vehicles,
    # prompt_total_licensing_new_vehicles,
    # prompt_licensing_new_domestic_vehicles,
    # prompt_licensing_new_imported_vehicles,
    # prompt_exports_assembled_vehicles
)

def process_pdf_and_generate_prompts(pdf_path: str):
    """
    Processa o PDF, extrai tabelas relevantes e gera os prompts correspondentes.
    """
    pdf_extractor = PDFExtractor(pdf_path)
    extracted_tables = pdf_extractor.extract_relevant_tables()
    llm = create_azure_llm()

    for page_title, table_data in extracted_tables.items():
        print(f"\n### Dados extraídos da página: {page_title}")
        print(json.dumps(table_data, indent=4, ensure_ascii=False))
        
        if page_title == "Produção de autoveículos montados":
            prompt = prompt_anfavea_production_assembled_vehicles

        # elif page_title == "Licenciamento total de autoveículos novos":
        #     prompt = prompt_total_licensing_new_vehicles

        # elif page_title == "Licenciamento de autoveículos novos nacionais":
        #     prompt = prompt_licensing_new_domestic_vehicles

        # elif page_title == "Licenciamento de autoveículos novos importados":
        #     prompt = prompt_licensing_new_imported_vehicles

        # elif page_title == "Exportações de autoveículos montados":
        #     prompt = prompt_exports_assembled_vehicles
            
        else:
            print("Categoria não reconhecida, pulando...")
            continue
        
        print("\n--- Análise com LLM ---")
        resposta = llm.invoke([prompt])
        print(f"\n### Resposta da IA para {page_title}: {resposta.content}")

if __name__ == "__main__":
    pdf_filename = "carta465.pdf"
    pdf_path = os.path.join(os.path.dirname(__file__), "pdfs", pdf_filename)
    process_pdf_and_generate_prompts(pdf_path)