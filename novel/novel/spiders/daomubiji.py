# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from novel.items import NovelItem

class DaomubijiSpider(CrawlSpider):
    name = 'daomubiji'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse_start_url(self, response):
        pass

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//article[@class="article-content"]//a'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = NovelItem()
        list = response.xpath('//body')
        for listItem in list:
            item['bookName'] = listItem.xpath('.//h1[@class="focusbox-title"]/text()').get().split('：')[0]
            subList = listItem.xpath('.//div[@class="excerpts"]//article')
            for subListItem in subList:
                item['bookTitle'] = subListItem.xpath('.//a/text()').get().split(' ')[0]
                item['chapterNum'] = subListItem.xpath('.//a/text()').get().split(' ')[1]
                item['chapterName'] = subListItem.xpath('.//a/text()').get().split(' ')[2]
                item['chapterUrl'] = subListItem.xpath('.//a/@href').get()
                yield item
