FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install ffmpeg using apt-get
RUN apt-get update && apt-get install -y ffmpeg

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
