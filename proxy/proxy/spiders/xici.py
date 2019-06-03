# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from proxy.items import ProxyItem
from scrapy_redis.spiders import RedisCrawlSpider

class XiciSpider(RedisCrawlSpider):
    name = 'xici'
    redis_key = 'myspider:start_urls'
    # allowed_domains = ['xicidaili.com']
    # start_urls = ['http://www.xicidaili.com']

    def parse_start_url(self, response):
        print(response)

    rules = (
        Rule(LinkExtractor(allow=r'/nt/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        item = ProxyItem()
        list = response.xpath('//table[@id="ip_list"]/tr')
        for listItem in list:
            item['country'] = listItem.xpath('.//td[1]/img/@alt').get()
            item['ipAddress'] = listItem.xpath('.//td[2]/text()').get()
            item['port'] = listItem.xpath('.//td[3]/text()').get()
            item['serverAddress'] = listItem.xpath('.//td[4]/a/text()').get()
            item['type'] = str(listItem.xpath('.//td[6]/text()').get()).lower()
            item['timeToLive'] = listItem.xpath('.//td[9]/text()').get()
            item['proofTime'] = listItem.xpath('.//td[10]/text()').get()
            yield item
