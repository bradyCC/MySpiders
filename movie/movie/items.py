# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    img = scrapy.Field()        # 电影图片
    url = scrapy.Field()        # 电影详情URL地址
    title = scrapy.Field()      # 电影标题
    store = scrapy.Field()      # 电影评分
    content = scrapy.Field()    # 电影信息
    info = scrapy.Field()       # 电影简介

