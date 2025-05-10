# Use the official Playwright Python image
FROM mcr.microsoft.com/playwright/python:v1.43.0-jammy

# Set the working directory
WORKDIR /app

# Copy your requirements and install them
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install dotenv package to load environment variables
RUN pip install python-dotenv

# Copy the .env file into the container
COPY .env .env

# Copy your code
COPY . .

# Install the browsers (Chromium, Firefox, WebKit)
RUN playwright install --with-deps

# Default command
CMD ["pytest", "-v"]
