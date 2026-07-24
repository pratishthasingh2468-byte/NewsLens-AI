"""
vectordb.py

Builds the local Chroma Vector Database
from the news documents stored in:

data/news_docs/
"""

from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_chroma import Chroma

from rag.embeddings import get_embedding_model

# -------------------------------------
# Paths
# -------------------------------------
NEWS_FOLDER = Path("data/news_docs")
DB_FOLDER = "data/embeddings"


def load_documents():
    """
    Load all .txt files from data/news_docs/

    Returns:
        list[Document]
    """

    documents = []

    if not NEWS_FOLDER.exists():
        print("News folder does not exist.")
        return documents

    txt_files = list(NEWS_FOLDER.glob("*.txt"))

    if not txt_files:
        print("No news files found.")
        return documents

    for file in txt_files:

        try:
            text = file.read_text(encoding="utf-8")

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": file.name
                    }
                )
            )

        except Exception as e:
            print(f"Skipping {file.name}: {e}")

    return documents


def split_documents(documents):
    """
    Split large documents into chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    return splitter.split_documents(documents)


def build_vector_database():
    """
    Create and save the Chroma vector database.
    """

    docs = load_documents()

    if not docs:
        print("No documents available.")
        return

    chunks = split_documents(docs)

    Chroma.from_documents(
        documents=chunks,
        embedding=get_embedding_model(),
        persist_directory=DB_FOLDER
    )

    print("\nVector database created successfully!")
    print(f"Location: {DB_FOLDER}")
    print(f"Indexed Chunks: {len(chunks)}")


if __name__ == "__main__":
    build_vector_database()

