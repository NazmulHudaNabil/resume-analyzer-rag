# rag_pipeline/generate.py
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

def generate_response(context, job_description):
    llm = ChatMistralAI(model="mistral-medium")

    prompt = ChatPromptTemplate.from_template("""
    You are an expert HR system.

    Resume Context:
    {context}

    Job Description:
    {job_description}

    Tasks:
    1. Extract skills from resume
    2. Compare with job description
    3. Provide missing skills
    4. Give improvement suggestions
    5. Provide a match score (0-100%)

    Output format:
    Skills:
    Missing Skills:
    Suggestions:
    Match Score:
    """)

    chain = prompt | llm
    return chain.invoke({
        "context": context,
        "job_description": job_description
    })