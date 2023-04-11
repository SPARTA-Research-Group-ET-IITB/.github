import requests
from bs4 import BeautifulSoup
import os

# URL of the website to scrape
url = 'https://syaamantak-das.carrd.co/'

# Request the website content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the desired content from the HTML using BeautifulSoup
content = soup.find_all()

# Create a string with the extracted content
content_str = ''
for paragraph in content:
    content_str += str(paragraph) + '\n'

# Write the content to a README.md file in the GitHub repository
with open('README.md', 'w') as f:
    f.write(content_str)

# Add and commit the changes to the GitHub repository
os.system('git add README.md')
os.system('git commit -m "Update README.md with latest content"')
os.system('git push')
