from PyPDF2 import PdfReader


def extract_pdf_text(uploaded_file):
    """
    Extract text from a PDF file.

    Args:
        uploaded_file: Streamlit uploaded PDF file.

    Returns:
        str: Extracted text.
    """

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()