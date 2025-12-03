FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY server.py .

# Entrypoint must run the server
# When running via Stdio, the client will attach to stdin/stdout
ENTRYPOINT ["python", "server.py"]
