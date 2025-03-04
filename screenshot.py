import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Ensure a URL is provided
if len(sys.argv) < 2:
    print("Usage: python screenshot.py <URL>")
    sys.exit(1)

url = sys.argv[1]

# Configure Selenium
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-http2")
chrome_options.add_argument("--disable-features=NetworkService,NetworkServiceInProcess")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Connect to Selenium running in Docker
driver = webdriver.Remote(
    # command_executor="http://selenium-chrome:4444/wd/hub", # For Linux
    command_executor="http://localhost:4444/wd/hub",
    options=chrome_options
)

# Open URL and take a screenshot
driver.get(url)
# screenshot_path = "/screenshots/screenshot_1.png" # For Linux
screenshot_path = "./screenshots/screenshot_1.png"
driver.save_screenshot(screenshot_path)

print(f"Screenshot saved: {screenshot_path}")
driver.quit()
