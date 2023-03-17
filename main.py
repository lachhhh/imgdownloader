from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import urllib.request

# Set the search query
search_query = input("Enter search query: ")

# Set up the webdriver with headless option and navigate to the Google Images search results page
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(f"https://www.google.com/search?q={search_query}&tbm=isch")

# Find the first image in the search results
img = driver.find_element(By.CSS_SELECTOR, ".rg_i")

# Get the URL of the image
img_url = img.get_attribute("src")

# Download the image and save it as "img.png"
urllib.request.urlretrieve(img_url, "img.png")

print("Image saved as img.png")

# Close the webdriver
driver.quit()
