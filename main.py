import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from halo import Halo

# Initialize vars
query = input("Input your query: ")
url = "https://www.phind.com/search?q=" + query

# suppress logging
chrome_options = Options()
chrome_options.add_argument("--log-level=3")
# make the browser not open
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# init the webdriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Start the spinner 
    spinner = Halo("Getting Answer from Phind...\n\n\n\n\n \n", spinner="dots")
    spinner.start()

    # Get the page content
    driver.get(url)

    # wait until its all loaded
    WebDriverWait(driver, timeout=50).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(15)

    # Get the elements
    answer_elements = driver.find_elements(By.CSS_SELECTOR, "main div.fs-5")

    # init the list
    paragraph_texts = []

    # get content
    for answer_element in answer_elements:
        paragraph_texts.append(answer_element.text.strip())

    # print it
    for text in paragraph_texts:
        # Stop spinner
        spinner.stop()
        print(text)

finally:
    # Close the browser
    driver.quit()
