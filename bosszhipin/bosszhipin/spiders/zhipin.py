# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bosszhipin.items import BosszhipinItem

class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    # allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101120100-p100901/?page=1']

    def parse_start_url(self, response):
        pass

    rules = (
        Rule(LinkExtractor(allow=r'page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        item = BosszhipinItem()
        list = response.xpath('//div[@class="job-list"]//ul/li')
        for listItem in list:
            item['position'] = listItem.xpath('.//div[@class="info-primary"]//div[@class="job-title"]/text()').get()
            item['pay'] = listItem.xpath('.//div[@class="info-primary"]//span[@class="red"]/text()').get()
            item['address'] = listItem.xpath('.//div[@class="info-primary"]//p/text()').get()
            if len(str(listItem.xpath('.//div[@class="info-primary"]/p').get()).split('<em class="vline"></em>')) == 2:
                item['education'] = str(listItem.xpath('.//div[@class="info-primary"]/p').get().replace('</p>', '')).split('<em class="vline"></em>')[1]
            elif len(str(listItem.xpath('.//div[@class="info-primary"]/p').get()).split('<em class="vline"></em>')) == 3:
                item['experience'] = str(listItem.xpath('.//div[@class="info-primary"]/p').get()).split('<em class="vline"></em>')[1]
                item['education'] = str(listItem.xpath('.//div[@class="info-primary"]/p').get().replace('</p>', '')).split('<em class="vline"></em>')[2]
            item['company'] = listItem.xpath('.//div[@class="company-text"]//a/text()').get()
            item['business'] = listItem.xpath('.//div[@class="company-text"]//p/text()').get()
            if len(str(listItem.xpath('.//div[@class="company-text"]/p').get()).split('<em class="vline"></em>')) == 2:
                item['scale'] = str(listItem.xpath('.//div[@class="company-text"]/p').get().replace('</p>', '')).split('<em class="vline"></em>')[1]
            elif len(str(listItem.xpath('.//div[@class="company-text"]/p').get()).split('<em class="vline"></em>')) == 3:
                item['financing'] = str(listItem.xpath('.//div[@class="company-text"]/p').get()).split('<em class="vline"></em>')[1]
                item['scale'] = str(listItem.xpath('.//div[@class="company-text"]/p').get().replace('</p>', '')).split('<em class="vline"></em>')[2]
            item['contact'] = listItem.xpath('.//div[@class="info-publis"]/h3/text()').get()
            if len(str(listItem.xpath('.//div[@class="info-publis"]/h3').get()).split('<em class="vline"></em>')) == 2:
                item['post'] = str(listItem.xpath('.//div[@class="info-publis"]/h3').get().replace('</h3>', '')).split('<em class="vline"></em>')[1]
            else:
                item['post'] = ''
            item['detailUrl'] = 'https://www.zhipin.com' + str(listItem.xpath('.//div[@class="info-primary"]//a/@href').get())
            yield item
