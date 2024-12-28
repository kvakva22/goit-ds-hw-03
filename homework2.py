import requests
from bs4 import BeautifulSoup
import json



links = []

for pagenum in range(1, 11):
    url = requests.get(f"http://quotes.toscrape.com/page/{pagenum}")
    soup = BeautifulSoup(url.text, 'lxml')
    authors = soup.find_all("small", class_="author")
    for author in authors:
        link = author.find_next("a")['href']
        if link not in links:
            links.append(link)

data=[]

for link in links: 
    source = requests.get(f"http://quotes.toscrape.com{link}")
    soup = BeautifulSoup(source.text, 'lxml')

    fullname = soup.find('h3', class_="author-title").next_element
    borndate = soup.find('span', class_="author-born-date").next_element
    bornlocation = soup.find('span', class_="author-born-location").next_element
    description = soup.find('div', class_="author-description").next_element.strip()

    data.append({"fullname": fullname,
         "borndate": borndate,
         "bornlocation": bornlocation,
         "description": description})

with open("authors.json", 'w') as file:
    json.dump(data, file)




dataquotes = []
for pagenum in range(1, 11):
    url = requests.get(f'http://quotes.toscrape.com/page/{pagenum}')
    soup = BeautifulSoup(url.text, 'lxml')

    quotes = soup.find_all('div', class_='quote')
    for el in quotes:
        tags = el.find('div', class_='tags').find_all('a')
        tags = [tag.text for tag in tags]
        author = el.find('small', class_='author').text
        quote = el.find('span', class_='text').text

        dataquotes.append({"tags": tags,
                           "author": author,
                           "quote":quote})  

with open('quotes.json', 'w') as file:
    json.dump(dataquotes, file)

