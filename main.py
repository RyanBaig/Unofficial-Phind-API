from selenium import webdriver
from bs4 import BeautifulSoup
from halo import Halo
import time

# Initialize vars
query = input("Input your query: ")
url = "https://phind.com/agent?q=" + query

# Initialize the webdriver
driver = webdriver.Chrome()

try:
    # Start the spinner 
    spinner = Halo("Getting Answer from Phind...\n\n\n\n\n \n", spinner="dots")
    spinner.start()

    # Get the page content
    driver.get(url)

    # Set a maximum waiting time just in case it doesnt work
    max_wait_time = 30  

    # Wait for content to load
    start_time = time.time()
    while time.time() - start_time < max_wait_time:
        if driver.execute_script("return document.readyState") == "complete":
            break
        time.sleep(1)

    # Get the page source
    html_content = driver.page_source

    # Stop spinner
    spinner.stop()

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all paragraphs
    paragraphs = soup.select('div.fs-5 p.text-black.mb-2.text-break')

    # Print the text content of each paragraph
    for paragraph in paragraphs:
        print("\n")
        print(paragraph.text)

finally:
    # Close the browser
    driver.quit()
