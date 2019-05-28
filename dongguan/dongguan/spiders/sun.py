# -*- coding: utf-8 -*-
import scrapy


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://sun0769.com/']

    def parse(self, response):
        pass
