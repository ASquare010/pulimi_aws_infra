# Base image
FROM python:3.13-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy dependency files for this service
COPY apps/management_api/pyproject.toml ./pyproject.toml

# Install dependencies using uv
RUN uv pip install --system --no-deps .

# Copy only this service's source code
COPY apps/management_api/ ./

# Copy shared_lib from root
COPY shared_lib /shared_lib

# Set PYTHONPATH to include /app and /shared_lib
ENV PYTHONPATH="/app:/shared_lib"

# Allow port to be set at build/run time
ARG PORT=5000
ENV PORT=${PORT}
EXPOSE ${PORT}

# Start the service
CMD ["sh", "-c", "python main.py --port $PORT"]
