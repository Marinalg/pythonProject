import requests
url = "https://rozetka.com.ua/ua/sport-i-uvlecheniya/"
respond_text = ''

respond = requests.get(url)

if respond.ok:
    respond_text = respond.text
soup = BeautifulSoup(response_text, "lxml")
find_url = soup.find_all(class_="tile-cats_heading ng-star-inserted")