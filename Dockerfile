# Use Python 3 base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Install dependencies
RUN pip install flask

# Expose ports for both applications
EXPOSE 5000 5001

# Copy the startup script
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Run the startup script
CMD ["/app/start.sh"]
