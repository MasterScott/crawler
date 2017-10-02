from scrapy.spiders  import Spider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from metaua.items import MetauaItemLoader, MetauaItem

class MetauaSpider(Spider):
    name = 'meta_spider'
    start_url = ['http://dir.meta.ua/']
    allowed_domains = ['meta.ua']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths = ['.//*[@id="wrap"]/div[4]/div[2]/div[2]/table']            
                ,allow = ['dir.meta.ua/\w+/\w+']
            ),
            callback = 'parse_item'
        ),
        
    )

    def parse_item(self, response):
        selector = Selector(response)
        l = MetauaItemLoader(MetauaItem, selector)
        l.add_value('url', response.url)
