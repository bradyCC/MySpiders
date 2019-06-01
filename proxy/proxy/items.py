# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyItem(scrapy.Item):
    # define the fields for your item here like:
    country = scrapy.Field()        # 国家
    ipAddress = scrapy.Field()      # IP地址
    port = scrapy.Field()           # 端口
    serverAddress = scrapy.Field()  # 服务器地址
    type = scrapy.Field()           # 协议类型
    timeToLive = scrapy.Field()     # 存活时间
    proofTime = scrapy.Field()      # 验证时间
