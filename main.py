# USANDO TABULA + PANDAS
import os
from extraction.pdf_extractor_anfavea import process_pdf_and_generate_prompts_anfavea
from extraction.pdf_extractor_fenabrave import process_pdf_and_generate_prompts_fenabrave
from extraction.pdf_extractor_adefa import process_pdf_and_generate_prompts_adefa
from extraction.pdf_extractor_acara import process_pdf_and_generate_prompts_acara
if __name__ == "__main__":
    pdf_filename = "2025.01. SIOMAA. Informe de Mercado 4W 1.pdf"
    pdf_path = os.path.join(os.path.dirname(__file__), "pdf", pdf_filename)
    # process_pdf_and_generate_prompts_anfavea(pdf_path)         # RESPOSTA DA EXTRAÇÃO DA ANFAVEA
    # process_pdf_and_generate_prompts_fenabrave(pdf_path)         # RESPOSTA DA EXTRAÇÃO DA FENABRAVE
    # process_pdf_and_generate_prompts_adefa(pdf_path)        # RESPOSTA DA EXTRAÇÃO DA ADEFA
    process_pdf_and_generate_prompts_acara(pdf_path)        # RESPOSTA DA EXTRAÇÃO DA ACARA


