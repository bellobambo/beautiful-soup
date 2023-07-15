from bs4 import BeautifulSoup
import requests
import re

gpu = input("What product do you want? ")

items_found = {}  # Initialize the items_found dictionary

# Get number of pages
url = f'https://www.newegg.ca/p/pl?d={gpu}&N=4808'
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")
page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split('/')[-2].split(">")[-1][:-1])
print(pages)

# Looping through the pages to get the items
for page in range(1, pages + 1):
    url = f'https://www.newegg.ca/p/pl?d={gpu}&N=4808&page={page}'
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    # Searching for name, price, and link
    div = doc.find(class_='item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell')
    items = div.find_all(string=re.compile(gpu))

    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue

        link = parent['href']
        next_parent = item.find_parent(class_="item-container")
        try:
            price = next_parent.find(class_="price-current").strong.string
            items_found[item] = {"price": int(price.replace(",", "")), "link": link}
        except:
            pass

sorted_items = sorted(items_found.values(), key=lambda x: x['price'])

for item in sorted_items:
    print(list(items_found.keys())[list(items_found.values()).index(item)])
    print(f"${item['price']}")
    print(item['link'])
    print('-----------------')
