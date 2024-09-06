from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configuração do Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa o navegador em segundo plano
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")  # Desativa a aceleração gráfica

# Inicializa o WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Acessa o Google (ou outro site que use o campo de pesquisa)
    driver.get("https://www.google.com")

    # Aguarda até que o campo de pesquisa esteja presente
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="q"]'))
    )

    # Envia uma consulta e submete o formulário
    search_box.send_keys("Selenium Python")
    search_box.submit()

    # Aguarda os resultados da pesquisa carregarem
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h3'))
    )

    # Localiza os títulos dos resultados da pesquisa
    results = driver.find_elements(By.CSS_SELECTOR, 'h3')

    # Extrai e imprime os títulos dos resultados
    for result in results:
        print(result.text)

finally:
    # Fecha o navegador
    driver.quit()
