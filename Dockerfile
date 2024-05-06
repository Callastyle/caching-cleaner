# Use an official Python runtime as a parent image based on Alpine
FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python script into the container
COPY script.py .

# Install the Redis package using pip
# Also, ensure necessary build tools are installed if needed for the Redis package
RUN apk add --no-cache gcc musl-dev libffi-dev && \
    pip install --no-cache-dir redis

# Run script.py when the container launches
CMD ["python", "./script.py"]
