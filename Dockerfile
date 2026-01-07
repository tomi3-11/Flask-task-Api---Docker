# Use official python image
FROM  python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the app code
COPY . .

# Expose the port your app listens on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

