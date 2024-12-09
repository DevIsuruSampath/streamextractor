# Step 1: Use an official Python image as the base image with Python 3.10.12
FROM python:3.10.12-slim

# Step 2: Set environment variables
ENV PYTHONUNBUFFERED 1

# Step 3: Install ffmpeg dependencies and ffmpeg itself
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Step 4: Set the working directory inside the container
WORKDIR /app

# Step 5: Copy the requirements.txt file first, to leverage Docker caching for dependencies
COPY requirements.txt /app/

# Step 6: Install Python dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Step 7: Copy the entire project to the container
COPY . /app/

# Step 8: Expose the port (if applicable, for example 5000 for web applications)
# EXPOSE 5000

# Step 9: Set the default command to run python3 explicitly
CMD ["python3", "main.py"]
