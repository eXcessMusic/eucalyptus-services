# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE eucalyptus_services.settings

# Set work directory
WORKDIR /app/eucalyptus_services

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy project
COPY . /app/

# Run gunicorn
CMD gunicorn wsgi:application --bind 0.0.0.0:$PORT