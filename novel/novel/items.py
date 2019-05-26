# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    bookName = scrapy.Field()
    bookTitle = scrapy.Field()
    chapterNum = scrapy.Field()
    chapterName = scrapy.Field()
    chapterUrl = scrapy.Field()
    pass