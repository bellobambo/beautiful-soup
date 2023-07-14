from bs4 import BeautifulSoup
import requests
import re

gpu = input("what Product do you want? ")


# Get number of pages
url = f'https://www.newegg.ca/p/pl?d={gpu}&N=4808'
page = requests.get(url).text
doc = BeautifulSoup(page , "html.parser")
page_text = doc.find(class_="list-tool-pagination-text" ).strong
pages = int(str(page_text).split('/')[-2].split(">")[-1][:-1])
print(pages)

# looping through the pages to get the number
for page in range(pages):
    url = f'https://www.newegg.ca/p/pl?d={gpu}&N=4808'
    page = requests.get(url).text
    doc = BeautifulSoup(page , "html.parser")

