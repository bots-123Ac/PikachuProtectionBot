# Python 3.11 base image use kar rahe hain
FROM python:3.11-slim

# Working directory set kar
WORKDIR /app

# Environment variables set kar
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

# System dependencies install kar (psutil ke liye zaroori)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Requirements file copy kar aur install kar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Baaki saara code copy kar
COPY . .

# Port expose kar
EXPOSE 8080

# Gunicorn se Flask app run kar (Northflank ke liye recommended)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "2", "bot:flask_app"]
