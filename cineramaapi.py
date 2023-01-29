import requests


url = 'https://api.cinerama.uz/v2/web/home'


response = requests.get(url)
for i in range(len(response.json()['data'])):
    for j in range(12):
        print(response.json()['data'][i]['title'] + ":", response.json()['data'][i]['list'][j]['title'])
