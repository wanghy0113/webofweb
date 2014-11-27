# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class url_node(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url_string = scrapy.Field()
    origin_url_string = scrapy.Field()
    pass
