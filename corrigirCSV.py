import csv
import pandas as pd

# Defina o número esperado de colunas
numero_esperado_de_colunas = 14  # Ajuste conforme necessário

# Lista para armazenar linhas corrigidas
linhas_corrigidas = []

# Lê o arquivo CSV original
with open('D:\\DriverGoogle\\bq-results-20240919-230736-1726787427669\\TodasCidades.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f,delimiter=';')
    for i, linha in enumerate(reader):
        # Verifica se a linha tem o número esperado de colunas
        if len(linha) == numero_esperado_de_colunas:
            linhas_corrigidas.append(linha)  # Adiciona linha correta
        elif len(linha) > numero_esperado_de_colunas:
            # Corrigir: remove colunas extras e imprime o erro
            print(f"Linha {i} com excesso de colunas ({len(linha)} colunas): {linha}")  # Imprime a linha problemática
            linhas_corrigidas.append(linha[:numero_esperado_de_colunas])  # Mantém as colunas esperadas
        else:
            # Corrigir: adiciona valores padrão (por exemplo, None)
            while len(linha) < numero_esperado_de_colunas:
                linha.append(None)  # Adiciona valores padrão
            linhas_corrigidas.append(linha)  # Adiciona a linha corrigida

# Cria um DataFrame a partir das linhas corrigidas
df_corrigido = pd.DataFrame(linhas_corrigidas[1:], columns=linhas_corrigidas[0])  # Usa a primeira linha como cabeçalho

# Salva o DataFrame corrigido em um novo CSV
df_corrigido.to_csv('D:\\DriverGoogle\\bq-results-20240919-230736-1726787427669\\TodasCidadesteste_corrigido.csv', index=False)

print("Arquivo corrigido salvo com sucesso.")
