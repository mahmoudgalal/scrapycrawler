"""
Written by Mahmoud AbdelFattah
"""
import scrapy
import datetime
import time
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from TestSpider.items import TestspiderItem
class TestSpider(CrawlSpider):
    name = 'pages'
    #put here all the urls for data sources
    start_urls = ['http://www.foodnavigator.com',
            'http://foodnewsinternational.com' ]
    rules = ( Rule(LinkExtractor(), callback='parse_item' ),)
    # def parse_item(self,response):
        # self.logger.info('Hi, this is an item page! %s', response.url)
        # page = int(round(time.time() * 1000))
        # filename = 'page-%s.html' % page
        # with open(filename, 'wb') as f:
             # f.write(response.body)
        # self.log('Saved file %s' % filename)
    def parse_item(self,response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        page = int(round(time.time() * 1000))
        filename = 'output/page-%s.html' % page
        with open(filename, 'wb') as f:
              f.write(response.body)        
        item = TestspiderItem()
        item['url'] = response.url
        item['name'] = response.url
        item['description'] = response.body.decode(response.encoding)
        return item