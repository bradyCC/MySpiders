# -*- coding: utf-8 -*-
import scrapy
import json

class CustomerSpider(scrapy.Spider):
    name = 'customer'
    # allowed_domains = ['customer.com']
    # start_urls = ['http://customer.com/']


    # 登录
    def start_requests(self):
        url = 'http://test.58shiduoduo.com/crm/php/hrims/login/login'
        formdata={'username':'SY00001','password':'shangchen@881','user_url':'http://test.58shiduoduo.com/crm/html/login/'}

        # url = 'http://crmapi.58shiduoduo.com/hrims/login/login'
        # formdata = {'username': 'SY00002', 'password': '******', 'user_url': 'http://crm.58shiduoduo.com/login/'}

        yield scrapy.FormRequest(
            url,
            formdata=formdata,
            callback=self.parse
        )

    # 获取数据
    def parse(self, response):
        length = 0
        if response.url == 'http://test.58shiduoduo.com/crm/php/hrims/login/login':
        # if response.url == 'http://crmapi.58shiduoduo.com/hrims/login/login':
            token = json.loads(response.text)['data']['token']
            formdata = {'draw':'', 'start': '0', 'length': '10', 'isadmin': '1', 'token': token}
        else:
            token = json.loads(response.text)['token']
            length = json.loads(response.text)['recordsTotal']
            formdata = {'draw': '', 'start': '0', 'length': str(length), 'isadmin': '1', 'token': token}

        url = 'http://test.58shiduoduo.com/crm/php/customer/Customer/getCustomerList'
        # url = 'http://crmapi.58shiduoduo.com/customer/Customer/getCustomerList'

        if length:
            yield scrapy.FormRequest(
                url,
                formdata=formdata,
                callback=self.parse_item
            )
        else:
            yield scrapy.FormRequest(
                url,
                formdata=formdata,
                callback=self.parse
            )

    # 分析数据
    def parse_item(self, response):
        item = {}
        list = json.loads(response.text)['data']
        for listItem in list:
            item = listItem
            yield item
