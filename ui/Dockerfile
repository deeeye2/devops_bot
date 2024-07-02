# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Ensure gunicorn is installed
RUN pip install gunicorn

# Make port 80 available to the world outside this container
EXPOSE 80

# Run gunicorn server
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:80", "app:app"]
