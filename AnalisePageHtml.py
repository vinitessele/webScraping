import requests
from bs4 import BeautifulSoup

# URL
url = 'https://www.wikipedia.org/'

# Fazer a solicitação HTTP
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    page_title = soup.title.string
    print('Título da página:', page_title)
else:
    print('Falha na solicitação:', response.status_code)