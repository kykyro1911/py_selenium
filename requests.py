import requests

a = requests.get("https://chromedriver.storage.googleapis.com/")

print(a.text)
