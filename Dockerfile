FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements.txt first (if exists) for caching dependencies installation
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .


# Command to run FastAPI with Uvicorn
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
