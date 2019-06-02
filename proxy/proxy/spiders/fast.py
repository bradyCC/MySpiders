# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from proxy.items import ProxyItem
from scrapy_redis.spiders import RedisCrawlSpider

class FastSpider(RedisCrawlSpider):
    name = 'fast'
    redis_key = 'myspider:start_urls'
    # allowed_domains = ['kuaidaili.com']
    # start_urls = ['https://www.kuaidaili.com/free/inha/']       # 高匿代理
    # start_urls = ['https://www.kuaidaili.com/free/intr/']     # 透明代理

    def parse_start_url(self, response):
        print(response.url)

    rules = (
        # Rule(LinkExtractor(allow=r'/free/inha/\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/free/intr/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        item = ProxyItem()
        list = response.xpath('//div[@id="list"]//tbody/tr')
        for listItem in list:
            item['ipAddress'] = listItem.xpath('.//td[@data-title="IP"]/text()').get()
            item['port'] = listItem.xpath('.//td[@data-title="PORT"]/text()').get()
            item['type'] = str(listItem.xpath('.//td[@data-title="类型"]/text()').get()).lower()
            item['serverAddress'] = listItem.xpath('.//td[@data-title="位置"]/text()').get()
            item['proofTime'] = listItem.xpath('.//td[@data-title="最后验证时间"]/text()').get()
            yield item
