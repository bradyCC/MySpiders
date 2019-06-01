# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from novel.items import NovelItem

class QuanzhigaoshouSpider(CrawlSpider):
    name = 'quanzhigaoshou'
    # allowed_domains = ['81xzw.com']
    # start_urls = ['https://www.81xzw.com/book/16628/']
    start_urls = ['https://www.qu.la/book/32/']

    def parse_start_url(self, response):
        pass

    rules = (
        # Rule(LinkExtractor(allow=r'/book/16628/\d+.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/book/32/\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        item = NovelItem()
        item['bookName'] = response.xpath('//div[@class="con_top"]/a[2]/text()').get()
        title = response.xpath('//div[@class="bookname"]/h1/text()').get().split(' ', 1)
        if len(title) == 1:
            item['chapterNum'] = ''
            item['chapterName'] = title[0]
        elif len(title) == 2:
            item['chapterNum'] = title[0]
            item['chapterName'] = title[1]
        item['chapterUrl'] = response.url
        item['chapterContent'] = ''.join(response.xpath('//div[contains(@id, "content")]/text()').extract()).strip()

        # title = response.xpath('//div[@class="novel"]/h1/text()').get().split(' ', 2)
        # if len(title) == 3:
        #     item['bookName'] = title[0]
        #     item['chapterNum'] = title[1]
        #     item['chapterName'] = title[2]
        # elif len(title) == 2:
        #     item['bookName'] = title[0]
        #     item['chapterNum'] = '第一千七百二十九章'
        #     item['chapterName'] = title[1]
        # item['chapterUrl'] = response.url
        # item['chapterContent'] = ''.join(response.xpath('//div[@class="yd_text2"]/text()').extract()).strip()
        yield item
