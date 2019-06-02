# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from skill.items import SkillItem

class PybaseSpider(CrawlSpider):
    name = 'pyBase'
    # allowed_domains = ['pythontab.com']
    start_urls = ['https://www.pythontab.com/html/pythonjichu/']

    def parse_start_url(self, response):
        print(response)

    rules = (
        Rule(LinkExtractor(allow=r'/html/pythonjichu/\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        item = SkillItem()
        list = response.xpath('//ul[@id="catlist"]/li')
        for listItem in list:
            item['title'] = listItem.xpath('.//a/text()').get()
            item['info'] = listItem.xpath('.//p/text()').get().strip()
            item['detailUrl'] = listItem.xpath('.//a/@href').get()
            yield item
