# Base image
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose Gradio default port
EXPOSE 7860

# Start Gradio UI
CMD ["python", "main.py"]
