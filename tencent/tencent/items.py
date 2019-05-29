# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    recruitPostName = scrapy.Field()    # 职位
    countryName = scrapy.Field()        # 国家
    locationName = scrapy.Field()       # 城市
    categoryName = scrapy.Field()       # 部门
    lastUpdateTime = scrapy.Field()     # 最后更新时间
    responsibility = scrapy.Field()     # 职责
    postUrl =scrapy.Field()             # 详情URL地址