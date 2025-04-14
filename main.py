# USANDO TABULA + PANDAS
import os
from extraction.pdf_extractor_anfavea import process_pdf_and_generate_prompts_anfavea
from extraction.pdf_extractor_fenabrave import process_pdf_and_generate_prompts_fenabrave

# if __name__ == "__main__":
#     pdf_filename = "2025_01_02.pdf"
#     pdf_path = os.path.join(os.path.dirname(__file__), "pdf", pdf_filename)
#     processar_resumo_mensal(pdf_path)

if __name__ == "__main__":
    # pdf_filename = "carta452.pdf"
    pdf_filename = "2025_02_02.pdf"
    pdf_path = os.path.join(os.path.dirname(__file__), "pdf", pdf_filename)
    # process_pdf_and_generate_prompts_anfavea(pdf_path)         # RESPOSTA DA EXTRAÇÃO DA ANFAVEA
    process_pdf_and_generate_prompts_fenabrave(pdf_path)         # RESPOSTA DA EXTRAÇÃO DA FENABRAVE


