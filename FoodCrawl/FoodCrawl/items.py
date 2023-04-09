# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    points = scrapy.Field()
    price = scrapy.Field()
    opening_time = scrapy.Field()
    locations = scrapy.Field()
    categories = scrapy.Field()
    numReviews = scrapy.Field()
    
    # review
    reviews = scrapy.Field()

    # gallery
    photos = scrapy.Field()
    
    
