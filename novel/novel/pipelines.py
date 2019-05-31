# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import json
import codecs
import os
from scrapy.conf import settings


class NovelPipeline(object):

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        db = client[dbName]
        self.post = db[settings['MONGODB_DOCNAME']]
        self.file = codecs.open('douluodalu.json', 'w', 'utf-8')
        self.file.write('[')

    def open_spider(self, spider):
        print('This spider is starting!')

    def process_item(self, item, spider):
        if spider.name == 'daomubiji':
            bookInfo = dict(item)
            self.post.insert(bookInfo)
        return item

    def process_item(self, item, spider):
        if spider.name == 'zhuxian':
            bookInfo = dict(item)
            self.post.insert(bookInfo)
        return item

    def process_item(self, item, spider):
        if spider.name == 'quanzhigaoshou':
            # data = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            # self.file.write(data)
            bookInfo = dict(item)
            self.post.insert(bookInfo)
        return item

    def process_item(self, item, spider):
        if spider.name == 'douluodalu':
            data = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.file.write(data)
            # bookInfo = dict(item)
            # self.post.insert(bookInfo)
        return item

    def close_spider(self, spider):
        print('This spider is end!')
        self.file.seek(-2, os.SEEK_END)     # 定位到倒数第二个字符，即最后一个逗号
        self.file.truncate()                # 删除最后一个逗号
        self.file.write(']')
        self.file.close()