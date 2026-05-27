# ==========================================
# STAGE 1: Build & Compiling Environment
# ==========================================
FROM python:3.10-slim AS builder

WORKDIR /build

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# ==========================================
# STAGE 2: Hardened Secure Final Runtime
# ==========================================
FROM python:3.10-slim AS runner

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy python packages compiled inside the builder phase safely
COPY --from=builder /root/.local /root/.local
COPY cross_border_audit.py main.py /app/

ENV PATH=/root/.local/bin:$PATH

# Production Security: Establish unprivileged isolated user context
RUN useradd -u 8888 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

CMD ["python", "main.py"]
