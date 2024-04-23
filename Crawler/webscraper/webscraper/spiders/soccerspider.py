from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from pathlib import Path
import scrapy


class SoccerspiderSpider(scrapy.Spider):
    name = "soccerspider"
    allowed_domains = ["en.wikipedia.org"]
    custom_settings = {
        'DEPTH_LIMIT': 3,
        'MAX_PAGES': 100
    }

    def __init__(self, *args, **kwargs):
        super(SoccerspiderSpider, self).__init__(*args, **kwargs)
        self.n_pages = 0



    def start_requests(self):
        start_urls = ["https://en.wikipedia.org/wiki/Association_football"]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if self.n_pages >= self.custom_settings.get('MAX_PAGES'):
            self.logger.info(f"Reached the maximum number of pages: {self.custom_settings['MAX_PAGES']}")
            return

        details = response.css("div.mw-content-ltr")
        page = response.url.split("/")[-1]
        
        dir = f"/Users/rahulmansharamani/Desktop/Files/Spring 2024/CS429/Project/information-retrieval-system/Crawler/webscraper/new_files"
        filename = f"webpage-{page}.html"
        file_path = Path(f'{dir}/{filename}')
        file_path.write_bytes(response.body)
        self.log(f"----------------------{response.url}----------------------")
        self.n_pages += 1

        for link in response.css("div.mw-content-ltr p a::attr(href)").extract()[:10]:
            if link.startswith("/wiki/") and ':' not in link:
                nextPage = response.urljoin(link)
                yield scrapy.Request(nextPage, callback=self.parse)