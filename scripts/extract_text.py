import os
from PyPDF2 import PdfReader
import re

def extract_text_from_pdfs(pdf_folder_path):
    chunks = []
    for filename in os.listdir(pdf_folder_path):
        if filename.endswith('.pdf'):
            path = os.path.join(pdf_folder_path, filename)
            with open(path, 'rb') as f:
                reader = PdfReader(f)
                for page in reader.pages:
                    text = page.extract_text() or ''
                    steps = re.split(r'(?=\d+\.\s)', text)
                    for step in steps:
                        step = step.strip()
                        if step:
                            chunks.append(step)
    return chunks