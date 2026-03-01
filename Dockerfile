# Use Python 3.10 slim for a smaller image size
FROM python:3.10-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Install system dependencies for PostgreSQL and PDF processing
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements from root and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project (including 'rag' and 'backend' folders)
COPY . .

# CRITICAL: Tell Python to look in /app for modules
ENV PYTHONPATH=/app

# Expose FastAPI port
EXPOSE 8000

# Start the application pointing to the main file inside the backend folder
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
