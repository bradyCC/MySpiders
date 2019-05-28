# -*- coding: utf-8 -*-
import scrapy
from sina.items import SinaItem
import os

# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")


class SinaclassSpider(scrapy.Spider):
    name = 'sinaClass'
    # allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        items = []
        parentTitle = response.xpath('//div[contains(@id,"XX_conts")]//h3[@class="tit02"]/a/text()').extract()    # 获取所有大分类标题
        parentUrls = response.xpath('//div[contains(@id,"XX_conts")]//h3[@class="tit02"]/a/@href').extract()      # 获取所有大分类URL地址
        subTitle = response.xpath('//div[contains(@id,"XX_conts")]//ul[@class="list01"]/li/a/text()').extract()   # 获取所有中分类标题
        subUrls = response.xpath('//div[contains(@id,"XX_conts")]//ul[@class="list01"]/li/a/@href').extract()       # 获取所有中分类URL地址

        # 爬取所有大分类
        for i in range(0, len(parentTitle)):
            # 设置大分类目录的路径和目录名
            parentFileName = "./Data/" + parentTitle[i]

            # 如果目录不存在，则创建目录
            if (not os.path.exists(parentFileName)):
                os.makedirs(parentFileName)

            # 爬取所有中分类
            for j in range(0, len(subUrls)):
                item = SinaItem()
                item['parentTitle'] = parentTitle[i]
                item['parentUrls'] = parentUrls[i]

                # 判断中分类是否属于同一大分类
                if_belong = subUrls[i].startswith(item['parentUrls'])

                if (if_belong):
                    # 设置中分类目录的路径和目录名
                    subFileName = parentFileName + '/' + subTitle[i]

                    # 如果目录不存在，则创建目录
                    if (not os.path.exists(subFileName)):
                        os.makedirs(subFileName)

                    item['subTitle'] = subTitle[j]
                    item['subUrls'] = subUrls[j]
                    item['subFileName'] = subFileName
                    items.append(item)

        # 处理小分类
        for item in items:
            yield scrapy.Request(
                url=item['subUrls'],
                meta={'meta_1':item},
                callback=self.second_parse
            )

    def second_parse(self, response):
        meta_1 = response.meta['meta_1']
        sonUrls = response.xpath('//a/@href').extract()
        items = []
        for i in range(0, len(sonUrls)):
            # 判断小分类是否属于同一大分类
            if_belong = sonUrls[i].endswith('.shtml') and sonUrls[i].startswith(meta_1['parentUrls'])

            if (if_belong):
                item = SinaItem()
                item['parentTitle'] = meta_1['parentTitle']
                item['parentUrls'] = meta_1['parentUrls']
                item['subUrls'] = meta_1['subUrls']
                item['subTitle'] = meta_1['subTitle']
                item['subFileName'] = meta_1['subFileName']
                item['sonUrls'] = sonUrls[i]
                items.append(item)

        # 处理文章标题和内容
        for item in items:
            yield scrapy.Request(
                url=item['sonUrls'],
                meta={'meta_2':item},
                callback=self.detail_parse
            )

    def detail_parse(self, response):
        item = response.meta['meta_2']
        content = ""
        head = response.xpath('//h1[@id=\"main_title\"]/text()')
        content_list = response.xpath('//div[@id=\"artibody\"]/p/text()').extract()

        # 将p标签里的文本内容合并到一起
        for content_one in content_list:
            content += content_one

        item['head'] = head
        item['content'] = content

        yield item