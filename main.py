import requests
url = "https://randomuser.me/api/"
print(requests.get(url).text)