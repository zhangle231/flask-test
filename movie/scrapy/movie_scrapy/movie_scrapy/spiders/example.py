import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['dygamgs.com']
    start_urls = ['http://www.dygangs.com/ys/']

    def parse(self, response):
        for base in response.xpath('//tr[1]/td[1]/table[1]/tbody/tr/td/a/img'):
            yield { 
                'text' : base.xpath('./@alt').get(),
                'img' : base.xpath('./@src').get(),
            }

        pagination_links = response.xpath('/html/body/table[6]/tbody/tr/td[1]/table/tbody/tr/td/table[3]/tbody/tr/td/a[11]')
        self.log.info(pagination_links)
        yield from response.follow_all(pagination_links, self.parse)
        #yield from response.follow_all(xpath='/html/body/table[6]/tbody/tr/td[1]/table/tbody/tr/td/table[3]/tbody/tr/td/a[11]', callback=self.parse)
