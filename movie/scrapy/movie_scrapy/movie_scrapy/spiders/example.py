import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['dygamgs.com']
    start_urls = ['http://www.dygangs.com/ys/']

    def parse(self, response):
        yield { 
                'text' : response.xpath('//table/tbody/tr[1]/td[1]/table/tbody')[0].get()
        }

        #for quote in response.xpath('//tbody/tr/td/table/tbody'):
        #    yield {
        #            'text': quote.xpath("//td[2]/a/text()").getall(),
        #        #'src': quote.xpath("//tr/td/table/tbody/tr/td/a/img").attrib['src']
        #    }
        pass
