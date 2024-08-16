import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Send an HTTP request to the website (example news article)
url = "http://example.com/news-article"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Extract specific details from the article
title = soup.find('h1', class_='article-title').text.strip()  # Assuming the title is in an h1 tag with a class
date = soup.find('time', class_='article-date').text.strip()  # Assuming the date is in a time tag with a class
byline = soup.find('span', class_='byline').text.strip()  # Assuming the byline is in a span tag with a class

# Extracting article content (e.g., paragraphs within a certain div)
content = "\n".join([p.text.strip() for p in soup.find_all('p')])

# Step 4: Store the data in a CSV file
with open('data/scraped_article.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Date", "Byline", "Content"])
    writer.writerow([title, date, byline, content])

print("Data has been successfully scraped and saved to data/scraped_article.csv")
