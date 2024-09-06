import requests
from bs4 import BeautifulSoup

url = 'https://pt.wikipedia.org/wiki/Brasil'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    titulos = soup.find_all("h2")

    for titulo in titulos:
        print(titulo.get_text())
else:
    print("Falha ao acessar a página:", response.status_code)
