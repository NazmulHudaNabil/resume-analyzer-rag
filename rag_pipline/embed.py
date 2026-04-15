# rag_pipeline/embed.py
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma


def create_vector_store(chunks):
    embedding = MistralAIEmbeddings(model="mistral-embed")

    # Use in-memory Chroma (no persist_directory) — Render has ephemeral storage
    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=embedding,
    )

    return vectorstore