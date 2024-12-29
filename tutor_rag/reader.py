import PyPDF2
from docx import Document

class Reader:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_pdf(self):
        """Reads a PDF file and returns its text content."""
        try:
            with open(self.filepath, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                return text
        except Exception as e:
            return f"An error occurred while reading the PDF: {e}"

    def read_word(self):
        """Reads a Word (docx) file and returns its text content."""
        try:
            doc = Document(self.filepath)
            text = ""
            for para in doc.paragraphs:
                text += para.text + "\n"
            return text
        except Exception as e:
            return f"An error occurred while reading the Word file: {e}"