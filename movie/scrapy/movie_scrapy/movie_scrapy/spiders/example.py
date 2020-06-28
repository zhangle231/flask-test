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
    
        #for quote in response.xpath('//tbody/tr/td/table/tbody'):
        #    yield {
        #            'text': quote.xpath("//td[2]/a/text()").getall(),
        #        #'src': quote.xpath("//tr/td/table/tbody/tr/td/a/img").attrib['src']
        #    }
        pass
