# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from novel.items import NovelItem


class ZhuxianSpider(CrawlSpider):
    name = 'zhuxian'
    allowed_domains = ['swang8.com']
    start_urls = ['http://swang8.com/72/1.html']

    def parse_start_url(self, response):
        content = response.xpath('//body/script/text()').extract()
        print(content)
        pass

    rules = (
        # Rule(LinkExtractor(allow=r'/72/\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = NovelItem
        # list = response.xpath('//body')
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
