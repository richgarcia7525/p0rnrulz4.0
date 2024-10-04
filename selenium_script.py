from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import json
import time

# Set up the Edge WebDriver with the correct service object
service = Service("C:\\Users\\richg\\Downloads\\edgedriver_win64\\msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Open the target page
driver.get("https://www.xnxx.com/todays-selection")

# Give the page some time to load
time.sleep(5)

# Find video elements
videos = driver.find_elements(By.CLASS_NAME, 'thumb-block')

# List to hold video data
data = []

# Loop through each video element and extract the data
for video in videos:
    title = video.find_element(By.TAG_NAME, 'a').get_attribute('title')
    link = video.find_element(By.TAG_NAME, 'a').get_attribute('href')
    thumbnail = video.find_element(By.TAG_NAME, 'img').get_attribute('src')

    data.append({
        'title': title if title else 'No title',
        'url': link,
        'thumbnail': thumbnail
    })

# Save the data to a JSON file
with open('videos.json', 'w') as f:
    json.dump(data, f)

# Close the driver
driver.quit()



