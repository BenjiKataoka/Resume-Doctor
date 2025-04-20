import PyPDF2

@staticmethod
def parser(filepath: str) -> str:
    try:
        with open(filepath, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() + '\n'
        return text.strip()
    except Exception as e:
            print(f"Error parsing PDF: {e}")
            return ""

