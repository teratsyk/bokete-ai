from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from boketeScrapy.items import BoketescrapyItem

class BoketeSpider(CrawlSpider):
    name = 'bokete'
    allowed_domains = ["bokete.jp"]
    start_urls = ["https://bokete.jp"]
    rules = [Rule(LinkExtractor(allow=('boke/legend','boke/popular', 'boke/select', 'boke/pickup'), unique=True), callback='parse_item', follow=True)]

    def parse_item(self, response):
        self.logger.info('this is an item page! %s', response.url)

        item = BoketescrapyItem()
        img_src = response.css('.content-boke > .boke > .boke-photo > .boke-photo-content > a > img::attr(src)').extract()
        item['image_urls'] = []
        for image_url in img_src:
            item['image_urls'].append('http:' + image_url)
        item['txt'] = response.css('.content-boke > .boke > a.boke-text::text').extract()

        yield item
