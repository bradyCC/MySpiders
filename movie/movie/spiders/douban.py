# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from movie.items import MovieItem

class DoubanSpider(CrawlSpider):
    name = 'douban'
    # allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    def parse_start_url(self, response):
        pass

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+&filter='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MovieItem()
        list = response.xpath('//ol[@class="grid_view"]/li')
        for listItem in list:
            item['img'] = listItem.xpath('.//div[@class="pic"]/a/img/@src').get()
            item['url'] = listItem.xpath('.//div[@class="pic"]/a/@href').get()
            item['title'] = listItem.xpath('.//div[@class="hd"]/a/span[1]/text()').get()
            item['store'] = listItem.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()').get()
            item['content'] = listItem.xpath('.//div[@class="bd"]/p/text()').get(0).strip()
            item['info'] = listItem.xpath('.//p[@class="quote"]/span[@class="inq"]/text()').get()
            yield item
