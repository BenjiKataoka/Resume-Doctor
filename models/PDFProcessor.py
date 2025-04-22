import PyPDF2

class PdfProcessor:

    def __init__(self, resumepath: str):
        self.path = resumepath
        self.resumeOutput = self.parser()

    def parser(self) -> str:
        try:
            with open(self.path, 'rb') as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                text = ''
                for page in reader.pages:
                    text += page.extract_text() + '\n'
            return text.strip()
        except Exception as e:
            print(f"Error parsing PDF: {e}")
            return ""

