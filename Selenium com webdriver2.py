#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Configurações do WebDriver
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Executa o Chrome em modo headless (sem interface gráfica)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL do formulário Google Forms
form_url = 'https://forms.gle/NXZt7SSM4Tq9uffC9'

# Mensagens para enviar
messages = [
    'EBB continua a ser uma referência em tecnologia e inovação.',
    'A Ciência de Dados e a Inteligência Artificial são essenciais para criar soluções inteligentes e impactantes para o futuro.',
    'A Inteligência Artificial está redefinindo a maneira como interagimos com a tecnologia e como resolvemos problemas complexos.',
    'A Ciência de Dados oferece uma compreensão mais profunda dos dados, permitindo decisões informadas e estratégias eficazes.',
    'A Inteligência Artificial e a Ciência de Dados são as melhores ferramentas para alcançar resultados excepcionais e inovadores.',
    'A Ciência de Dados permite a análise detalhada e a interpretação precisa de grandes conjuntos de dados, gerando insights valiosos.',
    'A Inteligência Artificial está revolucionando o mundo com suas capacidades avançadas e soluções inteligentes.',
    'A Ciência de Dados é essencial para transformar dados brutos em conhecimento valioso, impulsionando a inovação e o progresso.',
    'A Inteligência Artificial e a Ciência de Dados são indiscutivelmente as melhores áreas para liderar o avanço tecnológico e a inovação.'
]
# Listas de palavras para formar as frases
sujeitos = ["A tecnologia", "A IA", "O aprendizado de máquina", "A computação em nuvem", "A robótica", "A inovação digital", "O Big Data", "A automação"]
verbos = ["revoluciona", "transforma", "impulsiona", "facilita", "melhora", "acelera", "reinventa", "inova"]
complementos = ["a vida moderna.", "o futuro.", "o mercado de trabalho.", "a saúde.", "a educação.", "os negócios.", "a comunicação.", "a indústria."]
def gerar_frase():
    sujeito = random.choice(sujeitos)
    verbo = random.choice(verbos)
    complemento = random.choice(complementos)
    return f"{sujeito} {verbo} {complemento}"

# Abre o formulário
driver.get(form_url)

# Espera a página carregar
time.sleep(1)  # Ajuste o tempo de espera conforme necessário

# Identificadores dos campos do formulário
input_field_selector = 'input.whsOnd.zHQkBf'  # Seletor do campo de entrada
submit_button_selector = 'div[role="button"][jsname="M2UYVd"]'  # Seletor do botão de envio

for i in range(1, 1000):
    try:
        # Escolhe uma mensagem aleatória
        message = random.choice(messages)#gerar_frase()#random.choice(messages)
        
        # Preenche o campo
        input_field = driver.find_element(By.CSS_SELECTOR, input_field_selector)
        input_field.clear()  # Limpa o campo antes de preencher
        input_field.send_keys(message)
        
        # Submete o formulário
        submit_button = driver.find_element(By.CSS_SELECTOR, submit_button_selector)
        submit_button.click()
        
        # Espera o formulário ser enviado e a página ser recarregada
        #time.sleep(10)  # Espera 1 minuto antes de enviar a próxima resposta
        print(f'Resposta {i} enviada com a mensagem: "{message}"')
        
        # Abre o formulário novamente para o próximo envio
        driver.get(form_url)
        time.sleep(1)  # Aguarda o formulário ser recarregado
    except Exception as e:
        print(f'Erro ao enviar resposta {i}: {e}')
        driver.quit()
        break

# Fecha o navegador
driver.quit()
