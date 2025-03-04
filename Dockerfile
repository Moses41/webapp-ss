# Use Selenium’s official image with Chrome & WebDriver pre-installed
FROM selenium/standalone-chrome:latest

# Switch to root user for package installation
USER root

# Set working directory
WORKDIR /app

# Copy requirements.txt before installing dependencies
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN apt-get update && apt-get install -y python3-venv && \
    python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r /app/requirements.txt

# Switch back to Selenium’s default non-root user
# USER seluser

# Copy necessary files
COPY screenshot.py /app/screenshot.py
COPY tele_reader.py /app/tele_reader.py
COPY .env /app/.env
COPY session_name.session /app/session_name.session
RUN chmod 777 /app/session_name.session
# Set environment variables for Chrome
ENV DISPLAY=:99
ENV PATH="/opt/venv/bin:$PATH"

# Run the Telegram bot script to listen for messages
CMD ["python", "/app/tele_reader.py"]
