# -*- coding: utf-8 -*-
import scrapy
from itcast.items import ItcastItem

class TeacherSpider(scrapy.Spider):
    name = 'teacher'
    # allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        item = ItcastItem()
        list = response.xpath('//div[@class="tea_con"]/div[contains(@class,"tea_txt")]//ul/li')
        for listItem in list:
            item['name'] = listItem.xpath('.//div[@class="li_txt"]/h3/text()').get().strip()
            item['img'] = 'http://www.itcast.cn' + listItem.xpath('.//div[@class="li_img"]/img/@data-original').get()
            item['title'] = listItem.xpath('.//div[@class="li_txt"]/h4/text()').get().strip()
            item['info'] = listItem.xpath('.//div[@class="li_txt"]/p/text()').get().strip()
            yield item
