import scrapy
from scrapy.crawler import CrawlerProcess

class CitaçõesSpider(scrapy.Spider):
    name = "citações"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'texto': quote.css('span.text::text').get(),
                'autor': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

process = CrawlerProcess(settings={
    "FEEDS": {
        "citações.json": {"format": "json"}, 
    },
})

process.crawl(CitaçõesSpider)
process.start() 
