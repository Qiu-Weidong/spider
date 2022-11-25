# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    translate = scrapy.Field()
    pass


class HwxnetItem(scrapy.Item):
    key = scrapy.Field()
    value = scrapy.Field()
    pass


class HanyuguoxueItem(scrapy.Item):
    key = scrapy.Field()
    variant = scrapy.Field()
    basic = scrapy.Field()
    detail = scrapy.Field()
    translate = scrapy.Field()
    pass

