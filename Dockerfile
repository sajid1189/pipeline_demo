# Use an official Python runtime as a parent image
FROM python:latest

# Set environment variables for Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY . /app/

# Expose a port (if your Django app needs to listen on a specific port)
EXPOSE 8000

# Run the Django app (adjust the command as needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
