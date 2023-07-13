from bs4 import  BeautifulSoup
import requests

url = "https://www.newegg.ca/black-msi-gf-series-gf63-thin-11sc-692-gaming/p/N82E16834156308"


result = requests.get(url)
doc = BeautifulSoup(result.text , "html.parser")

prices = doc.find_all(text = "$")
parent = prices[0].parent

strong = parent.find('strong')
print(strong.string)

# print(doc.prettify())

# with open('index.html' , 'r') as f:
#     doc = BeautifulSoup(f , 'html.parser')

# tags = doc.find_all("p")[0]
# # tag.string = 'wassup'
# print(tags.find_all('b'))

