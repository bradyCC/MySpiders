# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo

class NovelPipeline(object):

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        db = client[dbName]
        self.post = db[settings['MONGODB_DOCNAME']]

    def open_spider(self, spider):
        print('This spider is starting!')

    def process_item(self, item, spider):
        if spider.name == 'daomubiji':
            bookInfo = dict(item)
            self.post.insert(bookInfo)
        if spider.name == 'zhuxian':
            print(item)
        return item

    def close_spider(self, spider):
        print('This spider is end!')