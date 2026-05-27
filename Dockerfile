# Use an official, hardened minimal Python footprint
FROM python:3.10-slim

# Enforce secure system environment flags
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_ENV=production

WORKDIR /secure_app

# Install dependencies securely under isolation
RUN pip install --no-cache-dir fastapi uvicorn uvloop pydantic

COPY . .

# Create a non-privileged system group and user to prevent root container breakouts
RUN groupadd -r auditor && useradd -r -g auditor system_auditor
USER system_auditor

EXPOSE 8000

# Run using a production-hardened ASGI worker configuration
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
