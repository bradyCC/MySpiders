# -*- coding: utf-8 -*-
import scrapy
from shopping.items import ShoppingItem

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    # allowed_domains = ['taobao.com']
    start_urls = ['https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w14556238-21645496201.2.6c6337e4PRygrk&id=565542711942']

    def parse(self, response):
        item = ShoppingItem()
        item['name'] = response.xpath('//div[@class="tb-item-info-r"]//h3[@class="tb-main-title"]/text()').get().strip()
        item['img'] = response.xpath('//div[@class="tb-item-info-l"]//ul/li[1]//img/@data-src').get()
        yield item

