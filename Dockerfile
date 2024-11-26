# Use the official Python image from Docker Hub
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install the necessary Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for the application
EXPOSE 8080

# Set environment variable to tell Flask to run in production mode
ENV FLASK_ENV=production

# Run the Flask app
CMD ["python", "app.py"]
