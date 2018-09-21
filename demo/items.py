# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiBoItem(scrapy.Item):
    page = scrapy.Field()
    tag = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    update_time = scrapy.Field()
