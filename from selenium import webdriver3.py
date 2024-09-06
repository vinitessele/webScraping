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

# Inicializa o WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Acessa a página inicial da Wikipedia
    driver.get("https://www.wikipedia.org/")
    
    # Aguarda até que o campo de busca esteja presente
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "searchInput"))
    )

    # Envia uma consulta para o campo de busca
    search_box.send_keys("Selenium (software)")

    # Envia o formulário de busca
    search_box.submit()

    # Aguarda a página de resultados carregar
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstHeading"))
    )

    # Extrai o título da página de resultados
    page_title = driver.find_element(By.ID, "firstHeading").text

    # Imprime o título da página
    print(f"Título da Página: {page_title}")

finally:
    # Fecha o navegador
    driver.quit()
