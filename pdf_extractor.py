import pdfplumber
import re

class PDFExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def clean_header(self, header: list) -> list:
        """
        Limpa e padroniza os cabeçalhos das tabelas.
        """
        return [re.sub(r'\s+', ' ', cell.strip()) if cell else None for cell in header]

    def extract_relevant_tables(self) -> dict:
        """
        Extrai somente as tabelas das páginas relevantes e retorna um dicionário.
        """
        relevant_titles = [
            "Produção de autoveículos montados",
            "Licenciamento total de autoveículos novos",
            "Licenciamento de autoveículos novos nacionais",
            "Licenciamento de autoveículos novos importados",
            "Exportações de autoveículos montados"
        ]

        extracted_tables = {}

        with pdfplumber.open(self.pdf_path) as pdf:
            print(f"DEBUG: Título extraído -> {title}")

            for page_num, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()

                if not text:
                    continue
                title = text.split("\n")[0]  # Primeiro título da página

                if title in relevant_titles:
                    tables = page.extract_tables()
                    for i, table in enumerate(tables):

                        if table and len(table) > 1:
                            formatted_table = []
                            headers = self.clean_header(table[0])

                            for row in table[1:]:
                                row_dict = {headers[idx]: cell.replace("\n", " ").strip() if cell else None for idx, cell in enumerate(row)}
                                formatted_table.append(row_dict)
                            extracted_tables[f"{title} - Tabela_{i+1}"] = formatted_table

        
        return extracted_tables
        

