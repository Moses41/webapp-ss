from telethon import TelegramClient, events
import re
import subprocess
import time
import os
import sys
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env into the environment
# Use the same Python interpreter that runs this script
python_executable = sys.executable

# Your Telegram API credentials (from my.telegram.org)
API_ID = os.environ.get('API_ID')     # Replace with your API ID
API_HASH = os.environ.get('API_HASH')  # Replace with your API Hash
PHONE_NUMBER = os.environ.get('PHONE_NUMBER')   # Example: "+919876543210"

# The group where you receive the links
# GROUP_NAME = "0302 Flypside Daily task team"  # Replace with actual group name
GROUP_NAME = os.environ.get('GROUP_NAME')  # Replace with actual group name
# The person to whom you want to send the screenshot
TARGET_USER_ID = os.environ.get('TARGET_USER_ID')

# Regular expression to find URLs in messages
# URL_REGEX = r"https?://[^\s]+"
URL_REGEX = r"2\.\s*\[?(https?://[^\]\s]+)\]?"


# Use a persistent session file
client = TelegramClient("session_name", API_ID, API_HASH)

async def main():
    # Check if session exists, otherwise prompt for login once
    await client.start(PHONE_NUMBER)

    print("✅ Bot is running and listening for messages...")

    @client.on(events.NewMessage)
    async def handle_new_message(event):
        # Check if the message is from the target group
        if event.chat and event.chat.title == GROUP_NAME:
            message_text = event.message.text
            # print("MESSAGE: "+message_text)
            urls = re.findall(URL_REGEX, message_text)

            if urls:
                url = urls[0]  # Take the first URL from the message
                print(f"🔹 Found URL: {url}")

                # Notify in Telegram that the process has started
                # await event.respond(f"📸 Processing screenshot for: {url}")
                print(f"📸 Processing screenshot for: {url}")

                # Call the screenshot script with the extracted URL
                # process = subprocess.run(["python3", "/app/screenshot.py", url])
                process = subprocess.run([python_executable, "./screenshot.py", url])

                # Wait for the screenshot to be fully generated
                time.sleep(120)  # Delay to ensure screenshot is ready

                # Check if screenshot exists before sending
                screenshot_path = "./screenshots/screenshot_1.png"
                if os.path.exists(screenshot_path):
                    # await client.send_file(TARGET_USER_ID, screenshot_path, caption=f"✅ Screenshot for {url}")
                    await client.send_file(TARGET_USER_ID, screenshot_path)
                    # await event.respond(f"✅ Screenshot sent to user {TARGET_USER_ID}")
                    print(f"✅ Screenshot sent to user {TARGET_USER_ID}")
                else:
                    # await event.respond(f"❌ Failed to generate screenshot for {url}")
                    print(f"❌ Failed to generate screenshot for {url}")

    await client.run_until_disconnected()

# Start the bot
with client:
    client.loop.run_until_complete(main())
