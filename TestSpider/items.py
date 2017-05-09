# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    body = scrapy.Field()
    url = scrapy.Field()    
    likes = scrapy.Field()
    ratings = scrapy.Field()    
    commentscount = scrapy.Field()
    pass