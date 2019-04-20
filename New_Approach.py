import requests
from bs4 import BeautifulSoup

url_to_scrape = 'https://newzhook.com/'
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text, 'lxml')
# print(soup.prettify())
print(soup.get_text())
# print(soup.find_all('p'))

