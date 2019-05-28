# -*- coding: utf-8 -*-
import scrapy
from dongguan.items import DongguanItem

class SunSpider(scrapy.Spider):
    name = 'sun'
    # allowed_domains = ['sun0769.com']

    offset = 0
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    start_urls = [url + str(offset)]

    def parse(self, response):
        links = response.xpath('//div[@class="greyframe"]/table//td/a[@class="news14"]/@href').extract()
        if links:
            for link in links:
                yield scrapy.Request(
                    link,
                    callback=self.parse_detail
                )

            self.offset += 30
            yield scrapy.Request(
                self.url + str(self.offset),
                callback=self.parse
            )

    def parse_detail(self, response):
        item = DongguanItem()
        item['title'] = response.xpath('//div[@class="wzy1"]//span[@class="niae2_top"]/text()').get().split('：')[1]
        item['number'] = response.xpath('//div[@class="wzy1"]//span[contains(@style, "color:#444")]/text()').get().split(':')[1]
        item['content'] = response.xpath('//div[@class="wzy1"]//td[@class="txt16_3"]/text()').get().strip()
        item['url'] = response.url
        yield item
