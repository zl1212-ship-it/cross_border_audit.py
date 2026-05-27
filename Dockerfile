# Use a secure, slim Python base image
FROM python:3.10-slim

# Set system running parameters
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establish isolated container workspace
WORKDIR /app

# Install operating system utility tools securely
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency mappings and install packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy remaining analytical engines
COPY cross_border_audit.py main.py /app/

# Set execution command target
CMD ["python", "main.py"]
