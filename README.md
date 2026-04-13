# 🚀 Resume Analyzer (RAG AI Project)

An AI-powered Resume Analyzer that uses **Retrieval-Augmented Generation (RAG)** to match resumes with job descriptions, extract skills, and provide improvement suggestions with a match score.

---

## 🔥 Features

- 📄 Upload Resume (PDF)
- 🧠 Extract skills using AI (Mistral LLM)
- 📊 Match with Job Description
- ❌ Identify missing skills
- ✅ Suggest improvements
- 🎯 Generate match score (%)

---


## ⚙️ Tech Stack

- **FastAPI** – Backend API
- **LangChain** – RAG pipeline
- **Mistral AI** – LLM & Embeddings
- **ChromaDB** – Vector database
- **Docker** – Containerization

---

## 🚀 Getting Started (Local Setup)

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/resume-analyzer-rag.git
cd resume-analyzer-rag

python -m venv .venv
source .venv/bin/activate   # Mac/Linux

pip install -r requirements.txt

MISTRAL_API_KEY=your_api_key_here

uvicorn app:app --reload

docker build -t resume-analyzer .

docker run -p 8000:8000 --env-file .env resume-analyzer
