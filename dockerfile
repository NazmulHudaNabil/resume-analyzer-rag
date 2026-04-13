# Use lightweight Python image
FROM python:3.11-slim

# Prevent Python from buffering logs
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (important for chromadb)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (cache optimization)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Create necessary directories
RUN mkdir -p uploads vector_db

# Render provides PORT env variable
ENV PORT=8000

# Start FastAPI (IMPORTANT: use $PORT)
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"]