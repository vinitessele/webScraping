import scrapy
from scrapy.crawler import CrawlerProcess

# Define o Spider
class CotacaoDolarSpider(scrapy.Spider):
    name = "cotacao_dolar"
    start_urls = ['https://www.x-rates.com/calculator/?from=USD&to=BRL&amount=1']  # Exemplo de URL

    def parse(self, response):
        # Extraí a cotação do dólar
        cotacao = response.css('span.ccOutputTrail::text').get()
        valor = response.css('span.ccOutputRslt::text').get()
        
        if cotacao and valor:
            yield {
                'moeda': 'USD/BRL',
                'valor': valor.strip() + cotacao.strip()
            }

# Configura o processo de scraping com opções
process = CrawlerProcess(settings={
    "FEEDS": {
        "cotacao_dolar.json": {"format": "json", "encoding": "utf8", "indent": 4},
    },
    "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    "ROBOTSTXT_OBEY": True,
    "DOWNLOAD_DELAY": 2,
    "CONCURRENT_REQUESTS": 1,
    "LOG_LEVEL": "INFO",
})

# Executa o spider
process.crawl(CotacaoDolarSpider)
process.start()
