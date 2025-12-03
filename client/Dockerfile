FROM python:3.11-slim

WORKDIR /app

# Install Docker CLI so we can spawn sibling containers
RUN apt-get update && \
    apt-get install -y docker.io && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY client.py .

CMD ["python", "client.py"]
