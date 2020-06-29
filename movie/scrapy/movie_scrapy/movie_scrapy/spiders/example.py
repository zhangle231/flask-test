import scrapy
import logging


class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['http://www.dygangs.com/ys/index_2.htm']

    def parse(self, response):
        for base in response.xpath('//tr[1]/td[1]/table[1]/tbody/tr/td/a/img'):
            yield { 
                'text' : base.xpath('./@alt').get(),
                'img' : base.xpath('./@src').get(),
            }

        logging.warning("This is a warning----------------------------------------------------------------------")

        next_page = response.xpath('//td/table/tbody/tr/td/table/tbody/tr/td/a/@href')[-2].get()
        logging.warning(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            logging.warning(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
