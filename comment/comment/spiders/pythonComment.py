# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from comment.items import CommentItem


class PythoncommentSpider(CrawlSpider):
    name = 'pythonComment'
    allowed_domains = ['liaoxuefeng.com']
    start_urls = ['https://www.liaoxuefeng.com/wiki/1016959663602400']

    def parse_start_url(self, response):
        print(response.url)
        pass

    rules = (
        Rule(LinkExtractor(allow=r'/wiki/1016959663602400/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        url = response.url.split('wiki/1016959663602400')[1]
        commentUrl = 'https://www.liaoxuefeng.com/api/ref/' + url + '/topics'
        item = CommentItem()
        item['url'] = commentUrl
        yield scrapy.Request(
            commentUrl,
            callback=self.parse_detail,
            meta = {'item': item}
        )

    def parse_detail(self, response):
        item = response.meta['item']
        item['comment'] = json.loads(response.text)['results']
        yield item
