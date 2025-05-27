import os
from PyPDF2 import PdfReader

def extract_text_from_pdfs(pdf_folder_path):
    texts = []
    for filename in os.listdir(pdf_folder_path):
        if filename.endswith('.pdf'):
            path = os.path.join(pdf_folder_path, filename)
            with open(path, 'rb') as f:
                reader = PdfReader(f)
                text = ''
                for page in reader.pages:
                    text += page.extract_text() or ''
                texts.append(text)
    return texts
