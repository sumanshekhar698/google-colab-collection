import requests

url = "https://quotes.toscrape.com/"

response = requests.get(url, timeout=10)
print(type(response))
print(response)

print(response.status_code)
# print(response.text)
print(response.text[:300])