import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializando o lemmatizer
nltk.download('punkt')  # Certifique-se de que a biblioteca NLTK está instalada
lemmatizer = WordNetLemmatizer()

# Definindo algumas respostas
responses = {
    "oi": ["Olá!", "Oi, como posso ajudar?", "Oi! Tudo bem?"],
    "como você está?": ["Estou aqui para ajudar!"],
    "adeus": ["Tchau! Tenha um bom dia!", "Até logo!"],
}

def preprocess_input(user_input):
    """Processa a entrada do usuário para normalizá-la."""
    tokens = word_tokenize(user_input.lower())
    return [lemmatizer.lemmatize(token) for token in tokens]

def get_response(user_input):
    """Retorna uma resposta apropriada com base na entrada do usuário."""
    lemmatized_input = preprocess_input(user_input)
    for word in lemmatized_input:
        if word in responses:
            return random.choice(responses[word])
    return "Desculpe, não entendi. Pode reformular a pergunta?"

def chat():
    """Inicia a conversa com o chatbot."""
    print("Bem-vindo ao Chatbot! (Digite 'sair' para encerrar a conversa)")
    user_data = {}
    user_input = input("Você: ")
    while True:
        if user_input.lower() == "sair":
            print("Chatbot: Tchau! Tenha um bom dia!")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

        # Verificar se o nome foi fornecido, se não, perguntar
        if 'name' not in user_data:
            user_data['name'] = input("Chatbot: Qual é o seu nome? ")
            continue  
        
        # Verificar se a idade foi fornecida, se não, perguntar
        if 'age' not in user_data:
            user_data['age'] = input("Chatbot: Qual é a sua idade? ")
            continue  
        
        if 'name' in user_data and 'age' in user_data:
            print("Chatbot: Agora vou preencher um formulário com suas informações.")
            fill_form(user_data['name'], user_data['age'])
            break  # Interromper o loop após o formulário se
def fill_form(name, age):
    """Preenche um formulário online usando Selenium."""
    # Configurações do WebDriver
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Executa o Chrome em modo headless (sem interface gráfica)
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get('https://forms.gle/YASQApxH2ngoDrAV7')  
        time.sleep(3)

          # Preencher o nome
        name_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i1"]')  
        name_field.send_keys(name)


        age_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i5"]')
        age_field.send_keys(age)

        submit_button = driver.find_element(By.CSS_SELECTOR, 'div[role="button"][jsname="M2UYVd"]')
        submit_button.click()

        print("Formulário enviado com sucesso!")
        time.sleep(2)
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
    finally:
        driver.quit()

# Inicia o chatbot
if __name__ == "__main__":
    chat()
