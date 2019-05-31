# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from novel.items import NovelItem

class DouluodaluSpider(CrawlSpider):
    name = 'douluodalu'
    # allowed_domains = ['kbiquge.com']
    start_urls = ['http://www.kbiquge.com/104_104216/']

    rules = (
        Rule(LinkExtractor(allow=r'/104_104216/\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        item = NovelItem()
        item['bookName'] = response.xpath('//div[@class="con_top"]/a[3]/text()').get()
        item['chapterNum'] = response.xpath('//div[@class="bookname"]/h1/text()').get().split(' ', 3)[1]
        item['chapterName'] = response.xpath('//div[@class="bookname"]/h1/text()').get().split(' ', 3)[2]
        item['chapterUrl'] = response.url
        item['chapterContent'] = ''.join(response.xpath('//div[contains(@id, "content")]/text()').extract()).strip()
        return item
