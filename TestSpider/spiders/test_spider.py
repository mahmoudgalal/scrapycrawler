"""
Written by Mahmoud AbdelFattah
"""
import scrapy
import datetime
import time
import os
import StringIO
import pkgutil
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from TestSpider.items import TestspiderItem
class TestSpider(CrawlSpider):
    name = 'pages'
    #put here all the corporate urls for data sources
    start_urls = ['http://www.lamberti.com/news/news_events.cfm',
           'https://www.cpkelco.com/news/',
           'http://phx.corporate-ir.net/phoenix.zhtml?c=117919&p=irol-news']
    #start_urls = []
    rules = ( Rule(LinkExtractor(), callback='parse_item' ),)
    # def parse_item(self,response):
        # self.logger.info('Hi, this is an item page! %s', response.url)
        # page = int(round(time.time() * 1000))
        # filename = 'page-%s.html' % page
        # with open(filename, 'wb') as f:
             # f.write(response.body)
        # self.log('Saved file %s' % filename)
    def __init__(self, *args, **kwargs):
        super(TestSpider, self).__init__(*args, **kwargs)
        #stringinput  = pkgutil.get_data("scrapycrawler", "resources/urllist.txt")
        #for line in StringIO.StringIO(stringinput):
         # self.start_urls.append(line)
        #with open(os.path.join(os.path.dirname(__file__), 'urllist.txt'),'r') as file:
          #for line in file:
        #      line = line.strip() #or someother preprocessing
         #     self.start_urls.append(line)
    def parse_item(self,response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        page = int(round(time.time() * 1000))
        filename = 'output/page-%s.html' % page
        #Exclude caching visited pages for now
        #with open(filename, 'wb') as f:
        #      f.write(response.body)        
        item = TestspiderItem()
        item['url'] = response.url
        item['name'] = response.url
        paragraphs = ""
        for listItem in response.xpath('//body//p//text()').extract():
                 paragraphs += unicode(listItem+'\n')
        item['body'] = paragraphs
        item['description'] = response.body.decode(response.encoding)
        item['ratingval'] = 0
        item['ratings'] = 0
        item['commentscount'] = 0
        item['likes'] = 0
        return item