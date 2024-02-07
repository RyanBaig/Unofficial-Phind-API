import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize vars
query = input("Input your query: ")
url = "https://www.phind.com/search?q=" + query

# Configure ChromeOptions to suppress logging
chrome_options = Options()
chrome_options.add_argument("--log-level=3")  # Fatal errors only
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Initialize the webdriver with the modified options
driver = webdriver.Chrome(options=chrome_options)

try:
    # Get the page content
    driver.get(url)

    # Wait for the DOM to be fully loaded
    WebDriverWait(driver, timeout=50).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(10)
    # Get the element with the specific CSS selector
    answer_element = driver.find_element(By.CSS_SELECTOR, "main div.fs-5 p.text-black.mb-2.text-break")

    # Extract text content of the paragraph element
    desired_text = answer_element.text

    # Print the extracted text
    print("Desired text:", desired_text.strip())

finally:
    # Close the browser
    driver.quit()
