# Use the official Python 3.8 image as the base image
FROM python:3.8-slim

# Set environment variable to avoid caching issues
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the container
COPY . /app/

# Install system dependencies (including lib for MLflow)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libsm6 libxext6 libxrender-dev

# Install core dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install development dependencies
RUN pip install --no-cache-dir -r requirements_dev.txt

# Expose the MLflow UI port
EXPOSE 5000

# Set the default command to start MLflow UI
CMD ["mlflow", "ui", "--host", "0.0.0.0"]
