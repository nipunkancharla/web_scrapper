import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Send an HTTP request to the website
url = "http://example.com"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Extract data (for example, all the links on the page)
all_links = soup.find_all('a')

# Step 4: Store the data in a CSV file
with open('data/scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Link Text", "URL"])
    
    for link in all_links:
        link_text = link.text
        link_url = link.get('href')
        writer.writerow([link_text, link_url])

print("Data has been successfully scraped and saved to data/scraped_data.csv")
