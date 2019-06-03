# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SkillItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()          # 标题
    info = scrapy.Field()           # 摘要
    detailUrl = scrapy.Field()      # 详情URL地址
