# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster
# Set the working directory to /app
WORKDIR /app
# Copy the requirements file into the container at /app
COPY requirements.txt .
# Install any dependencies
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt
# Copy the rest of the application code into the container at /app
COPY . .
