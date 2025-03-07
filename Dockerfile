# Use Python 3 base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Install dependencies
RUN pip install flask

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "vulnerable_redirect_app.py"]
