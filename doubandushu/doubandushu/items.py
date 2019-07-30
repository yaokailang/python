# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubandushuItem(scrapy.Item):
    title = scrapy.Field()
    grade = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    brief = scrapy.Field()