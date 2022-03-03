import requests
url =""
respond_text = ""
respond = requests.get(url)

if respond.ok:
    respond_text =respond.text
soup = BeautifulSoup(response_text, "lxml")
find_url = soup.find_all(class_='title-cats_headling ng-star-inserted')