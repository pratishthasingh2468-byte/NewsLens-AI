"""
retrieve.py

Retrieves relevant news documents from the
local Chroma vector database.
"""

from langchain_chroma import Chroma

from rag.embeddings import get_embedding_model

DB_FOLDER = "data/embeddings"


def get_retriever():
    vectorstore = Chroma(
        persist_directory=DB_FOLDER,
        embedding_function=get_embedding_model()
    )

    return vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )
def retrieve_context(query: str) -> str:
    """
    Retrieve the top matching documents and combine them into one context string.
    """

    retriever = get_retriever()

    docs = retriever.invoke(query)

    if not docs:
        return ""

    return "\n\n".join(doc.page_content for doc in docs)


if __name__ == "__main__":
    retriever = get_retriever()

    query = "What is artificial intelligence?"

    docs = retriever.invoke(query)

    print(f"\nRetrieved {len(docs)} documents:\n")

    for i, doc in enumerate(docs, 1):
        print(f"----- Document {i} -----")
        print(doc.page_content)
        print()