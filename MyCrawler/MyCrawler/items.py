# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class url_node(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    node_url = scrapy.Field()
    node_parent = scrapy.Field()
    node_ele = scrapy.Field()
    node_depth = scrapy.Field()
    node_type = scrapy.Field()

