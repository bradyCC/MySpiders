# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    parentTitle = scrapy.Field()    # 大分类标题
    parentUrls = scrapy.Field()     # 大分类URL地址
    subTitle = scrapy.Field()       # 中分类标题
    subUrls = scrapy.Field()        # 中分类URL地址
    subFileName = scrapy.Field()    # 中分类目录存储路径
    sonUrls = scrapy.Field()        # 小分类URL地址
    head = scrapy.Field()           # 文章标题
    content = scrapy.Field()        # 文章内容
