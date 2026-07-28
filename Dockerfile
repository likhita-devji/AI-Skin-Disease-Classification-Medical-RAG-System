# Use official PyTorch / Python slim image
FROM python:3.10-slim

# Prevent Python from writing bytecode and set unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (OpenCV / GL libraries)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create persistent storage directories
RUN mkdir -p uploads chroma_db models dataset

# Expose Flask Port
EXPOSE 5000

# Environment variables
ENV OLLAMA_BASE_URL="http://host.docker.internal:11434"
ENV PORT=5000

CMD ["python", "app.py"]
