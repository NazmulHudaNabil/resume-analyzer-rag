import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def generate_response(context, job_description):
    api_key = os.getenv("MISTRAL_API_KEY")

    if not api_key:
        raise ValueError("MISTRAL_API_KEY not found")

    llm = ChatMistralAI(
        model="mistral-medium",
        mistral_api_key=api_key   # ✅ FIX
    )

    prompt = ChatPromptTemplate.from_template("""
    You are an expert HR system.

    Resume Context:
    {context}

    Job Description:
    {job_description}

    Tasks:
    1. Extract skills
    2. Missing skills
    3. Suggestions
    4. Match score (%)
    """)

    chain = prompt | llm

    return chain.invoke({
        "context": context,
        "job_description": job_description
    })