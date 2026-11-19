import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"


response = requests.get(url, timeout=10)
print(type(response))
print(response)

print(response.status_code)
# print(response.text)
# print(response.text[:300])


soup = BeautifulSoup(response.text,"html.parser")

quotes = soup.find_all("div", class_= "quote")# _class is CSS class
print(type(quotes))
print(len(quotes))
# print(quotes)


for quote in quotes:
    quote_txt=quote.find("span",class_="text").get_text()
    quote_author=quote.find("small",class_="author").get_text()
    tags_list=[tag.get_text() for tag in quote.find_all("a", class_="tag")]
    
    print(f"Author: {quote_author} \n Quote: {quote_txt} \n Tags: {tags_list}",end="\n\n")
