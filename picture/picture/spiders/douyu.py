# -*- coding: utf-8 -*-
import scrapy
import json
from picture.items import PictureItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    # allowed_domains = ['douyu.com']

    offset = 0
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    start_urls = [url + str(offset)]

    def parse(self, response):
        item = PictureItem()
        data = json.loads(response.text)['data']
        if data:
            for each in data:
                item['name'] = each['nickname']
                item['imageUrl'] = each['vertical_src']
                yield item

            self.offset += 20
            yield scrapy.Request(
                self.url + str(self.offset),
                callback=self.parse
            )

