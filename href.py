from bs4 import BeautifulSoup
import requests
taha = requests.get("www.gogle.com")
bs = BEautifulSoup(req.text, "html.parser")
for x in bs.findall("a")
print(x.get("href"))
findAll()
