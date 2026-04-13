# rag_pipeline/embed.py
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma

def create_vector_store(chunks):
    embedding = MistralAIEmbeddings(model="mistral-embed")

    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=embedding,
        persist_directory="vector_db"
    )

    return vectorstore