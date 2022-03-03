from requests import get, post


headers = {
    "Content-Type:" "application/json"
    "Authorization": "token"
}

data = {

}

response = get(url="https://stage.partner.api.vanongo.com/orders", headers=headers)
response = post(url="https://stage.partner.api.vanongo.com/orders", headers=headers, data=data)

print(response.json())
