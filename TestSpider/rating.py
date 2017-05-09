# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestspiderRatingItem(scrapy.Item):
    # define the fields for your item here like:
     ratingval=scrapy.Field()
     onestarcount=scrapy.Field()
     twostarcount=scrapy.Field()
     threestarcount=scrapy.Field()
     fourstarcount=scrapy.Field()
     fivestarcount=scrapy.Field()
     pass