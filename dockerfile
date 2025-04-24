# Use an official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app code into the container
COPY app.py .

# Install Flask
RUN pip install flask

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
