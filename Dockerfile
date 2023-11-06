# Use the official Python base image
FROM python:3.11-slim

# Set the working directory in the Docker container
WORKDIR /app

# Copy the content of the local src directory to the working directory
COPY . .

# Install pipenv
RUN pip install -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8080

ENTRYPOINT ["streamlit", "run", "docker_app.py", "--server.port=8080", "--server.address=0.0.0.0"]
