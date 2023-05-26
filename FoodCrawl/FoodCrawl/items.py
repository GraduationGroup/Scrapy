# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodyItem(scrapy.Item):
    # id
    slug = scrapy.Field()

    # define the fields for your item here like:
    name = scrapy.Field()
    district = scrapy.Field()

    latitude = scrapy.Field()
    longitude = scrapy.Field()

    rating = scrapy.Field()

    # points = scrapy.Field()
    # price = scrapy.Field()
    # opening_time = scrapy.Field()
    # locations = scrapy.Field()
    # categories = scrapy.Field()
    # numReviews = scrapy.Field()

    # isBranch = scrapy.Field()
    # createdAt = scrapy.Field()
    
    # review
    reviews = scrapy.Field()

    # gallery
    photos = scrapy.Field()


    
    
