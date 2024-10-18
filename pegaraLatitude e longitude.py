import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time
import re
import requests

# Lista de municípios e seus códigos
municipios = [
    {"nome": "Cascavel", "codigo": 4104808},
    {"nome": "Santa Helena", "codigo": 4123501},
    {"nome": "Vera Cruz do Oeste", "codigo": 4128559},
    {"nome": "Ouro Verde do Oeste", "codigo": 4117453},
    {"nome": "Maripá", "codigo": 4115358},
    {"nome": "Tupãssi", "codigo": 4127957},
    {"nome": "São José das Palmeiras", "codigo": 4125456},
    {"nome": "Quatro Pontes", "codigo": 4120853},
    {"nome": "Palotina", "codigo": 4117909},
    {"nome": "Nova Santa Rosa", "codigo": 4117222},
    {"nome": "Marechal Cândido Rondon", "codigo": 4114609},
    {"nome": "Assis Chateaubriand", "codigo": 4102000},
    {"nome": "Toledo", "codigo": 4127700}
]
dados =[]
def consultar_cnpj(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        return dados
    else:
        print(f"Erro ao consultar CNPJ: {response.status_code}")
        return None
# Função para buscar o nome do município pelo código
def buscar_municipio_por_codigo(codigo, municipios):
    for municipio in municipios:
        if int(municipio["codigo"]) == int(codigo):
            return municipio["nome"]
    return "Município não encontrado"

# Função para geocodificar o endereço e calcular a distância
def get_lat_long_e_calcular_distancia(row, origem):
    geolocator = Nominatim(user_agent="http")
    
    try:
        municipio = buscar_municipio_por_codigo(row['id_municipio'], municipios)

        # Verifica se o município não foi encontrado e, se necessário, consulta o CNPJ
        if municipio == 'Município não encontrado':
            dadosconsulta = consultar_cnpj(row['cnpj'])
            municipio = dadosconsulta.get("municipio")

        # Monta o endereço utilizando a string municipio corretamente
        endereco = f" {row['numero'].strip()} {row['logradouro'].strip()}, {municipio} {row['sigla_uf'].strip()}, Brasil".strip()
        location = geolocator.geocode(endereco)
            
        # Caso não encontre o endereço completo, tenta buscar pelo CEP
        if pd.isnull(location):
            endereco = f"{row['cep']}, {municipio} {row['sigla_uf']}, Brasil"
            location = geolocator.geocode(endereco)
        
        if pd.isnull(location):
            endereco = f"{municipio}, Brasil"
            location = geolocator.geocode(endereco)

        if location:
            latitude, longitude = location.latitude, location.longitude
            print(f"Endereço: {endereco} -> Latitude: {latitude}, Longitude: {longitude}")
            
            # Calcula a distância para o ponto de origem
            destino = (latitude, longitude)
            distancia = geodesic(origem, destino).kilometers  # Distância em quilômetros
            print(f"Distância do ponto de origem para {destino}: {distancia:.2f} km")
            
            return pd.Series([latitude, longitude, f"{distancia:.2f}"])
        else:
            print(f"Endereço: {endereco} -> Não encontrado.")
            return pd.Series([None, None, None])
    except Exception as e:
        print(f"Erro na geocodificação para o endereço: {endereco}. Erro: {e}")
        #return pd.Series([None, None, None])

# Define o ponto de origem (latitude, longitude)
origem = (-24.6175656, -53.7120884)  # Coordenadas de referência

# Carrega o CSV original
arquivo_csv = 'D:\\DriverGoogle\\bq-results-20240919-230736-1726787427669\\TodasCidadesteste_corrigido.csv'
df = pd.read_csv(arquivo_csv, sep = ';', on_bad_lines='warn')

# Aplica a função para obter latitude, longitude e calcular a distância em uma única passada
df[['latitude', 'longitude', 'distancia_km']] = df.apply(get_lat_long_e_calcular_distancia, axis=1, origem=origem)
time.sleep(0.5)   
# Grava os resultados no mesmo arquivo CSV original
df.to_csv(arquivo_csv, index=False)

print(f"Geocodificação, cálculo de distância e gravação dos resultados concluídos no arquivo '{arquivo_csv}'.")
