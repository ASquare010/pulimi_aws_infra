# Base image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Copy shared_lib from root
COPY shared_lib /shared_lib

# Set PYTHONPATH to include /app and /shared_lib
ENV PYTHONPATH="/app:/shared_lib"

# Expose port (default)
ARG PORT=5000
ENV PORT=${PORT}
EXPOSE ${PORT}

# Start FastAPI using env var
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
