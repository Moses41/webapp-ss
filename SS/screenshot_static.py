from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

# Define URLs to capture screenshots from
urls = [
    "https://world.sisley.com/",
]

# Define a folder to save screenshots
screenshot_dir = "/screenshots"
os.makedirs(screenshot_dir, exist_ok=True)

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-http2")
chrome_options.add_argument("--disable-features=NetworkService,NetworkServiceInProcess")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set a user-agent to bypass bot detection
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")

# Connect to the Selenium Grid server running inside the container
selenium_server_url = os.getenv("SELENIUM_REMOTE_URL", "http://selenium-chrome:4444/wd/hub")
driver = webdriver.Remote(command_executor=selenium_server_url, options=chrome_options)

# Loop through URLs and take screenshots
for index, url in enumerate(urls):
    try:
        print(f"Opening: {url}")
        driver.get(url)
        time.sleep(10)  # Wait for page to fully load

        # Save the screenshot
        screenshot_path = os.path.join(screenshot_dir, f"screenshot_{index + 1}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")

    except Exception as e:
        print(f"Error processing {url}: {e}")

# Close browser
driver.quit()
print("All screenshots captured successfully.")
