import urllib3
from bs4 import BeautifulSoup
import json

url = 'https://m.21cineplex.com/gui.list_city.php'

http = urllib3.PoolManager()

response = http.request('GET', url)

soup = BeautifulSoup(response.data, features="lxml")

name_box = soup.find_all("li", attrs={'class': 'list-group-item'})
cities =[]

for x in name_box:
    y = x.find("div")
    cities.append(y.contents[0])

with open("list_of_cities.json" , 'w') as out:
    json.dump(cities, out)

