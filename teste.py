from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://g1.globo.com/")

# Espera até que as manchetes sejam carregadas
headlines = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".feed-post-link"))
)

# Extrai os títulos das manchetes
for headline in headlines[:5]:  # Pegamos apenas as 5 primeiras para este exemplo
    print(headline.text)

driver.quit()