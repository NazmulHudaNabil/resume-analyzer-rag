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
RUN mkdir -p uploads

# Render provides PORT env variable (default to 10000 — Render's default)
ENV PORT=10000

# Expose the port
EXPOSE ${PORT}

# Start FastAPI — Render sets $PORT automatically
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"]