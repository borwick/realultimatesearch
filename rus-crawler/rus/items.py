# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RusItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    contenttype = scrapy.Field()
    excerpt = scrapy.Field()
    url = scrapy.Field()
    fulltext = scrapy.Field()
    netloc = scrapy.Field()