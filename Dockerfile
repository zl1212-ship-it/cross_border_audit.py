# 1. Base image built on a clean Python footprint
FROM python:3.10-slim

# 2. Enforce secure system environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_ENV=production

WORKDIR /secure_app

# 3. Explicitly bundle dependencies directly into the build layers
RUN pip install --no-cache-dir fastapi uvicorn pydantic

# 4. Copy current application context modules 
COPY . .

# 5. Open operational communication gate channels
EXPOSE 8000

# 6. Fire up premium high-volume server worker routines
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
