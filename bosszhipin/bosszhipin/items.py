# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BosszhipinItem(scrapy.Item):
    # define the fields for your item here like:
    position = scrapy.Field()   # 职位
    pay = scrapy.Field()        # 薪资
    address = scrapy.Field()    # 公司地址
    experience = scrapy.Field() # 经验年限
    education = scrapy.Field()  # 学历
    company = scrapy.Field()    # 公司
    business = scrapy.Field()   # 行业
    financing = scrapy.Field()  # 融资
    scale = scrapy.Field()      # 规模
    contact = scrapy.Field()    # 联系人
    post = scrapy.Field()       # 联系人职务
    detailUrl = scrapy.Field()  # 详情页URL地址