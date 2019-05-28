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
        print(response.url)
        pass

    rules = (
        Rule(LinkExtractor(allow=r'/72/\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = NovelItem()
        title = response.xpath('//title/text()')
        item['bookName'] = title.get().split(' ')[0]
        item['chapterNum'] = title.get().split(' ')[1]
        item['chapterName'] = title.get().split(' ')[2]
        content = response.xpath('//script//text()').re(r"'/(.*?)',{}")
        for contentItem in content:
            nextUrl = 'http://www.swang8.com/' + contentItem
            # item['chapterUrl'] = nextUrl
            yield scrapy.Request(
                nextUrl,
                callback=self.parse_detail,
                meta={'item': item}
            )

    def parse_detail(self, response):
        item = response.meta['item']
        item['chapterContent'] = json.loads(response.text)['info']
        yield item
