from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.binary_location = "/snap/bin/chromium"

options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-software-rasterizer")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--user-data-dir=/tmp/selenium-chrome")

driver = webdriver.Chrome(options=options)

print("Browser:", driver.capabilities["browserVersion"])
print("Driver:", driver.capabilities["chrome"]["chromedriverVersion"])

driver.get("https://example.com")
print("Title:", driver.title)

driver.quit()