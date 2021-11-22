import requests
from bs4 import BeautifulSoup

url = 'https://rozetka.com.ua/bicycles/c83884/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)
# такой способ для каждой ссылки из розетки