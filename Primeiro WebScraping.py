import requests

url = 'http://example.com/tabela'
response = requests.get(url)

if response.status_code == 200:
    print('Solicitação bem-sucedida!')
    html_content = response.text
else:
    print('Falha na solicitação:', response.status_code)