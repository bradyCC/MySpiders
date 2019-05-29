# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from novel.items import NovelItem

class QuanzhigaoshouSpider(CrawlSpider):
    name = 'quanzhigaoshou'
    # allowed_domains = ['81xzw.com']
    start_urls = ['https://www.81xzw.com/book/16628/']

    def parse_start_url(self, response):
        print(response.url)
        pass

    rules = (
        Rule(LinkExtractor(allow=r'/book/16628/1.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        item = NovelItem()
        item['bookName'] = response.xpath('//div[@class="novel"]/h1/text()').get().split(' ')[0]
        item['chapterNum'] = response.xpath('//div[@class="novel"]/h1/text()').get().split(' ')[1]
        item['chapterName'] = response.xpath('//div[@class="novel"]/h1/text()').get().split(' ')[2]
        item['chapterUrl'] = response.url
        item['chapterContent'] = response.xpath('//div[@class="yd_text2"]').xpath('string(.)').extract()
        yield item
