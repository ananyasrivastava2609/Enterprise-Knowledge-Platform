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


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100):
    """
    Splits text into overlapping chunks.
    """
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    text = load_pdfs_from_directory("data/raw_docs")
    chunks = chunk_text(text)

    print(f"Total chunks created: {len(chunks)}")
    print("\nFirst chunk preview:\n")
    print(chunks[0][:500])
