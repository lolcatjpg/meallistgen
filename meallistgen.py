import requests

url = "https://pastebin.com/raw/sKNP6999"

data = requests.get(url)

print(data.text)
