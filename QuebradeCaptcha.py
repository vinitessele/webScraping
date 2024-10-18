import requests
import time

# Sua chave da API do 2Captcha
api_key = '2b8a7e1e96d304430da1eed47d8b9548'

# Enviar CAPTCHA para resolver (supondo que seja uma imagem)
captcha_file = {'file': open('captcha.jpg', 'rb')}
response = requests.post(f'http://2captcha.com/in.php?key={api_key}&method=post', files=captcha_file)

# Extrair o ID do CAPTCHA
captcha_id = response.text.split('|')[1]

# Aguardar e solicitar a solução
time.sleep(20)  # Aguardar 20 segundos para dar tempo de resolver
response = requests.get(f'http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}')

# Pegar a solução do CAPTCHA
captcha_solution = response.text.split('|')[1]
print(f'Solução do CAPTCHA: {captcha_solution}')
