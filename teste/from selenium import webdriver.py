from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configura o WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# URL do Google Form
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdXgSBM_VwT0COYS_StAvp44Y_Mjpkm_ke7OChuTf31rMfjxw/viewform'
driver.get(form_url)

# Aguarda a página carregar
time.sleep(3)

# Loop para preencher o campo 10.000 vezes
for i in range(1):
    # Preenche o campo de texto com um valor diferente em cada iteração
    campo_texto = driver.find_element(By.XPATH, '//input[@aria-labelledby="i1"]')
    campo_texto.send_keys(f'Entrada {i + 1}')

    # Enviar o formulário
    enviar = driver.find_element(By.XPATH, '//span[text()="Enviar"]/parent::button')
    enviar.click()

    # Aguarda um pouco para garantir que o envio foi processado
    time.sleep(3)

    # Retorna para o formulário para enviar novamente
    driver.get(form_url)
    time.sleep(3)

# Fecha o navegador após completar o loop
driver.quit()
