from pathlib import Path
from pypdf import PdfReader


def load_pdfs_from_directory(directory_path: str) -> str:
    """
    Loads all PDFs from a directory and returns combined text.
    """
    all_text = ""

    pdf_dir = Path(directory_path)

    for pdf_file in pdf_dir.glob("*.pdf"):
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                all_text += text + "\n"

    return all_text


if __name__ == "__main__":
    text = load_pdfs_from_directory("data/raw_docs")
    print(text[:500])  # print first 500 characters

