# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import os
import pymongo
from scrapy.conf import settings
from scrapy.pipelines.images import ImagesPipeline

class PicturePipeline(object):

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
        imageInfo = dict(item)
        self.post.insert(imageInfo)
        return item

    def close_spider(self, spider):
        print('This spider is end!')

# 处理图片 - 存储在本地
# class PicturePipeline(ImagesPipeline):
#     IMAGES_STORE = settings['IMAGES_STORE']
#
#     def get_media_requests(self, item, info):
#         image_url = item["imageUrl"]
#         yield scrapy.Request(image_url)
#
#     def item_completed(self, results, item, info):
#         # 固定写法，获取图片路径，同时判断这个路径是否正确，如果正确，就放到 image_path里，ImagesPipeline源码剖析可见
#         image_path = [x["path"] for ok, x in results if ok]
#
#         os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + item["name"] + ".jpg")
#         item["imagePath"] = self.IMAGES_STORE + "/" + item["name"]
#
#         return item