from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv

# Configuração do driver
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Executa o navegador em segundo plano
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")  # Desativa a aceleração gráfica
chrome_options.add_argument("--ignore-certificate-error")
chrome_options.add_argument("--ignore-ssl-errors")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL da página do Google Maps
url = 'https://www.google.com/maps/search/empresas+near+toledo,+PR/@-24.7155043,-53.7771667,13z'
driver.get(url)

driver.execute_script("""
    var div = document.querySelector('#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div');
    div.style.width = '100%';
    div.style.height = '100%';
    div.style.backgroundColor = 'lightblue';  // Apenas para visualização
""")
time.sleep(1000)

# Obter o conteúdo da página
page_content = driver.page_source
soup = BeautifulSoup(page_content, 'html.parser')

# Lista para armazenar os dados
companies = []

for div in soup.find_all('div', class_='UaQhfb fontBodyMedium'):
    name_div = div.find('div', class_='qBF1Pd fontHeadlineSmall')
    nome = name_div.get_text(strip=True) if name_div else 'Nome não encontrado'
    
    fone_span = div.find('span', class_='UsdlK')
    fone_numero = fone_span.get_text(strip=True) if fone_span else 'Telefone não encontrado'
    
    companies.append([nome, fone_numero])


# Fechar o navegador
driver.quit()


csv_filename = 'd:\\Users\\vinic\\Downloads\\company_info.csv'


with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Nome da Empresa', 'Telefone'])
    csv_writer.writerows(companies)

print(f'Dados salvos em {csv_filename}')
