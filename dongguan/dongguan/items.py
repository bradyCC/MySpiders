# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()   # 帖子标题
    number = scrapy.Field()  # 帖子编号
    content = scrapy.Field() # 帖子内容
    url = scrapy.Field()     # 帖子url地址