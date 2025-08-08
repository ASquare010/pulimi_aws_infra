# Base image
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copy shared_lib from root
COPY shared_lib /shared_lib

# Set PYTHONPATH to include /app and /shared_lib
ENV PYTHONPATH="/app:/shared_lib"

# Allow port to be set at build/run time
ARG PORT=8501
ENV PORT=${PORT}
EXPOSE ${PORT}

# Start Gradio UI
CMD ["sh", "-c", "python main.py --port $PORT"]
