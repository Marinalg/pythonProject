url_dict= {}
new_list =[]
find_url2 =soup.find_all(class_="portal-grid_cell ng-star-interested")
new_list.append(i.text)
for i in find url:
    url_dict.update({i.get("title"):i.get("href")})


for key, lvalue in zip(url_dict,new_list):
    url_dict[key]= url_dict[key]+" "+ lvalue