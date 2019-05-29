# -*- coding: utf-8 -*-
import scrapy
import json
from tencent.items import TencentItem

class RecruitSpider(scrapy.Spider):
    name = 'recruit'
    # allowed_domains = ['tencent.com']
    pageIndex = 1
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageSize=10&pageIndex='
    start_urls = [url + str(pageIndex)]

    def parse(self, response):
        data = json.loads(response.text)['Data']['Posts']
        if data:
            item = TencentItem()
            for dataItem in data:
                item['recruitPostName'] = dataItem['RecruitPostName']
                item['countryName'] = dataItem['CountryName']
                item['locationName'] = dataItem['LocationName']
                item['categoryName'] = dataItem['CategoryName']
                item['lastUpdateTime'] = dataItem['LastUpdateTime']
                item['responsibility'] = dataItem['Responsibility']
                item['postUrl'] = dataItem['PostURL']
                yield item
        self.pageIndex += 1
        yield scrapy.Request(
            self.url + str(self.pageIndex),
            callback=self.parse
        )
