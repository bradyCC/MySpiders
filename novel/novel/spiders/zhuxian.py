# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from novel.items import NovelItem


class ZhuxianSpider(CrawlSpider):
    name = 'zhuxian'
    # allowed_domains = ['swang8.com']
    # start_urls = ['http://www.swang8.com/72']
    start_urls = ['https://www.qu.la/book/116/']

    def parse_start_url(self, response):
        pass

    rules = (
        # Rule(LinkExtractor(allow=r'/72/\d+.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/book/116/\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # item = NovelItem()
        # title = response.xpath('//title/text()')
        # item['bookName'] = title.get().split(' ')[0]
        # item['chapterNum'] = title.get().split(' ')[1]
        # item['chapterName'] = title.get().split(' ')[2]
        # content = response.xpath('//script//text()').re(r"'/(.*?)',{}")
        # for contentItem in content:
        #     nextUrl = 'http://www.swang8.com/' + contentItem
        #     # item['chapterUrl'] = nextUrl
        #     yield scrapy.Request(
        #         nextUrl,
        #         callback=self.parse_detail,
        #         meta={'item': item}
        #     )

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
        yield item

    # def parse_detail(self, response):
        # item = response.meta['item']
        # item['chapterContent'] = json.loads(response.text)['info']
        # yield item
