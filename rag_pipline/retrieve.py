# rag_pipeline/retrieve.py
def retrieve_chunks(vectorstore, query):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    return retriever.invoke(query)