# Base image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Expose port
EXPOSE 5000

# Start the Fast API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
