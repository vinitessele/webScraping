import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Definindo URL para fazer web scraping
url = 'https://www.imdb.com/chart/top'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
resp = requests.get(url, headers=headers)

soup = BeautifulSoup(resp.text, 'html.parser')

# Encontrar todos os elementos de filmes e suas informações
movie_elements = soup.find_all('div', class_='sc-b189961a-0 iqHBGn cli-children')

names = []
years = []
scores = []

for movie in movie_elements:
    # Encontrar o nome do filme
    title_element = movie.find('h3', class_='ipc-title__text')
    if title_element:
        title = title_element.text.strip()
        # Encontrar o ano do filme
        year_element = movie.find('span', class_='sc-b189961a-8 hCbzGp cli-title-metadata-item')
        if year_element:
            year = year_element.text.strip()
            # Encontrar a nota do filme
            score_element = movie.find('span', class_='ipc-rating-star--rating')
            if score_element:
                score = score_element.text.strip()
                names.append(title)
                years.append(re.sub('[()]', '', year))  # Limpar o ano dos parênteses
                scores.append(score)

# Criar DataFrame
imdb_dataset = pd.DataFrame({
    'rank': range(1, len(names) + 1),
    'movie': names,
    'year': years,
    'score': scores
})

# Mostrar as primeiras linhas do DataFrame
print(imdb_dataset.head())

# Salvar em um arquivo Excel
imdb_dataset.to_excel("imdb.xlsx", index=False, sheet_name='Top Movies')
