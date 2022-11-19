from bs4 import BeautifulSoup
import requests

response = requests.get("https://privatbank.ua/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td", {"id" : "USD_sell"})
for elem in soup_list:
    print(elem.text)
