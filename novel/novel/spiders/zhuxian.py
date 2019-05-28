# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from novel.items import NovelItem


class ZhuxianSpider(CrawlSpider):
    name = 'zhuxian'
    allowed_domains = ['swang8.com']
    start_urls = ['http://www.swang8.com/72']

    def parse_start_url(self, response):
        pass

    rules = (
        Rule(LinkExtractor(allow=r'/72/\d+.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r"/novelsearch/reader/transcode/siteid/(.*?)'"), callback='parse_detail'),
    )


    def parse_item(self, response):
        # content = response.xpath('//script//text()').re(r"'/(.*?)',{}")
        item = NovelItem()
        # list = response.xpath('//body')
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    def parse_detail(self, response):
        print(json.loads(response.text)['info'])
        item = NovelItem()
        return item
