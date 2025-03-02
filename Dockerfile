# Use Selenium’s official image with Chrome & WebDriver pre-installed
FROM selenium/standalone-chrome:latest

# Switch to root user for package installation
USER root

# Install Python dependencies properly
RUN apt-get update && apt-get install -y python3-venv && \
    python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install selenium

# Switch back to Selenium’s default non-root user
USER seluser

# Set working directory
WORKDIR /app

# Copy Python script into the container
COPY screenshot.py .

# Set environment variables for Chrome
ENV DISPLAY=:99
ENV PATH="/opt/venv/bin:$PATH"

# Run the script when the container starts
CMD ["python", "screenshot.py"]
