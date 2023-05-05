from time import sleep
import scrapy
import json

import datetime as dt

from scrapy.utils.response import open_in_browser
from ..items import *

class FoodySpider(scrapy.Spider):
  name = "foody"
  start_urls = ['https://www.foody.vn/']

  locations = []
  
  categories = []

  restaurants = []

  def parse(self, response):
    locations_url = 'https://www.foody.vn/__get/Common/GetPopupLocation'
    
    yield scrapy.Request(url = locations_url, 
                         headers = {
                                "Accept": "application/json, text/javascript, */*; q=0.01",
                                "Accept-Encoding": "gzip, deflate, br",
                                "Accept-Language": "en-US,en;q=0.9",
                                "Sec-Fetch-Mode": "cors",
                                "Sec-Fetch-Site": "same-origin",
                                "X-Requested-With": "XMLHttpRequest"},
                        callback= self.parse_locations, dont_filter= True)
      
  def parse_locations(self, response):
      ############## LOCATIONS CRAWLING  ##############
      data = json.loads(response.body)
      self.locations = [{"Id": l['Id'], 'Name': l['DisplayName'], 'Slug': l['Url'][1:], "Districts": l['Districts']} 
                   for l in data['AllLocations'] if l["CountryName"] == "Vietnam"]
      
      ############## VISIT ALL LOCATIONS TO GATHER CATEGORIES ##############
      self.location_id = 0
      location_name = self.locations[self.location_id]['Name']                                              
      print(f'🎉🎉🎉 VISIT TO {location_name}: ({self.location_id + 1} / {len(self.locations)})' )
      location_url = self.start_urls[0] + self.locations[self.location_id]['Slug']

      yield response.follow(url = location_url , callback = self.visitAndCrawlLocation)

  def visitAndCrawlLocation (self, response):
    # PARSE AND GATHER CATEGORIES OF THIS LOCATION
    location_name = self.locations[self.location_id]['Name']     
    print(f'🎉🎉🎉 CRAWL_CATEGORIES OF {location_name}')

    yield scrapy.Request(url ='https://www.foody.vn/common/_TopCategoryGroupMenu?isUseForSearch=false',                  
                         callback=self.parse_categories, dont_filter = True)
    
  def parse_categories(self, response):
    ############## PARSE REQUEST TO CATEGORY  ##############
    response_content = scrapy.Selector(response)
    categories = response_content.css('.menu-box li a[rel="nofollow"]::attr(href)').extract()
    if self. location_id == 0:
      categories[0] = '/ho-chi-minh/food'
    self.categories += categories

    # VISIT TO THE NEXT LOCATION
    self.location_id += 1
    
    # if self.location_id < len(self.locations):
    if self.location_id < 1:
      location_name = self.locations[self.location_id]['Name']                                              
      print(f'🎉🎉🎉 VISIT TO {location_name}: ({self.location_id + 1} / {len(self.locations)})' )
      location_url = self.start_urls[0] + self.locations[self.location_id]['Slug']

      yield response.follow(url = location_url , callback = self.visitAndCrawlLocation)

    # FINISH VISIT <=> GET ALL CATEGORIES => PARSE PAGES EVERY CATEGORIES
    else:
      self.category_id = 0
      category_url = self.start_urls[0][:-1] + self.categories[self.category_id]

      self.p = 1
      self.restaurant_urls = []
      print(f'🎉🎉🎉 CRAWL PAGES {self.p} OF ', category_url)
      yield scrapy.Request(url = f'{category_url}/dia-diem?page={self.p}&append=true',                   
                              callback= self.parse_pages)
  

  def parse_pages(self, response):
    ############## PARSE CATEGORY TO GET 12 RESTAURANTS  ##############
    selector = scrapy.Selector(response)
    res_name = selector.css('h2 a::attr(href)').extract()
    # print('🎉🎉🎉 ', len(res_name))

    if len(res_name) != 0:
    # if len(self.restaurant_urls) == 0:
        res_name = [n.strip() for n in res_name]
        self.restaurant_urls += res_name

        self.p += 1
        category_url = self.start_urls[0][:-1] + self.categories[self.category_id]
        print(f'🎉🎉🎉 CRAWL PAGES {self.p} OF ', category_url)
        yield scrapy.Request(url = f'{category_url}/dia-diem?page={self.p}&append=true',                   
                                callback= self.parse_pages)
        
    else:
        print(f'🎉🎉🎉 {self.categories[self.category_id]} HAVE TOTAL', f'{self.p - 1} PAGES.\n\n')

        self.p = 1
        self.category_id += 1
        ############## CRAWL THE NEXT CATEGORY  ##############
        if self.category_id < len(self.categories):
        # if self.category_id < 3:
          category_url = self.start_urls[0][:-1] + self.categories[self.category_id]

          print(f'🎉🎉🎉 CRAWL PAGES {self.p} OF ', category_url)
          yield scrapy.Request(url = f'{category_url}/dia-diem?page={self.p}&append=true',                   
                                  callback= self.parse_pages)

        ############## GET ALL CATEGORIES => CRAWL PARSE EVERY RESTAURANTS  ##############
        else:
          ############## CHECKPOINT (OPTIONAL)  ##############
          resume_index = 6780
          # resume_index = self.restaurant_urls.index('/thuong-hieu/young-coffee-tea?c=ho-chi-minh')
          # print(f"❤️❤️❤️ START AT: {resume_index}")
          # sleep(5)
          self.res_url_id = resume_index
          full_res_url = self.start_urls[0][:-1] + self.restaurant_urls[self.res_url_id]

          if '/thuong-hieu/' not in full_res_url:
            yield response.follow(url = full_res_url,                   
                          callback= self.parse_a_restaurant, dont_filter = True)
          # branch
          else:
            yield response.follow(url = full_res_url, callback=self.parse_a_branch, dont_filter = True)

  def parse_a_branch(self, response):
    print(f'🎉🎉🎉 {response.request.url} IS BRANCH')

    self.branch_res_url_id = 0
    self.branch_res_urls = response.css('div[ng-if=false] .ldc-item h2 a::attr(href)').extract()

    full_res_url = self.start_urls[0][:-1] + self.branch_res_urls[self.branch_res_url_id]
    
    
    yield response.follow(url = full_res_url,                   
                                    callback= self.parse_a_restaurant, dont_filter = True, meta={'isBranch': True})
  
  def parse_a_restaurant(self, response):
    item = FoodcrawlItem()

    item['isBranch'] = response.meta.get('isBranch')

    # print(f'🎉🎉🎉 {response.request.url}')
    if not item['isBranch']:
      print(f'🎉🎉🎉 {response.request.url} IS RESTAURANT')

    name = response.css('h1::text').extract_first()
    if name:
      name = name.strip()
    item['name'] = name

    points = response.css('.microsite-top-points')
    pointObj = {}
    for p in points:
      if p:
        criteria = p.css('.label::text').extract_first()
        if criteria:
          criteria = criteria.strip()

          point = p.css('span::text').extract_first()
          if point:
            point = point.strip()

          pointObj[criteria] = point   

    item['points'] = pointObj
    

    price = ''
    item['price'] = price.join(response.css(".res-common-minmaxprice::text").extract())
    if price:
      price = price.strip()
    item['price'] = price


    opening_time = response.css('.micro-timesopen span:nth-child(3)::text').extract_first()
    if opening_time:
      opening_time = opening_time.strip()
    item['opening_time'] = opening_time
    

    locations = response.css('.breadcrum-microsite span[itemprop="itemListElement"]')
    locations = {str(id) : location.css('a::attr(href)').extract_first() for id,location in enumerate(locations)}
    item['locations'] = locations


    categories = response.css('.category')
    categories = {c.css('::attr(class)').extract_first(): c.css('a::attr(href)').extract_first() for c in categories}
    item['categories'] = categories
    
    numReviews = response.css('.microsite-review-count::text').extract_first()
    if numReviews:
      numReviews = numReviews.strip()
    item['numReviews'] = numReviews

    # print({"name": name, "points": points, "price": price, "opening_time": opening_time, "locations": locations, "categories": categories, "numReviews": numReviews}) 
    
    # Reviews
    reviewUrl = "%s/binh-luan" % response.request.url

    yield scrapy.Request(url=reviewUrl, callback=self.parse_review, meta={'arg': item}, dont_filter=True)
  
  def parse_review(self, response):
    response_content = scrapy.Selector(response)
    item = response.meta.get('arg')

    item['reviews'] = []
    userUrls = response_content.xpath("//div[@class='list-reviews']/div[1]/ul[1]//a[@class='ru-username']/@href").extract()
    createdAts = response_content.xpath("//div[@class='list-reviews']/div[1]/ul[1]//span[@class='ru-time']/text()").extract()
    platforms = response_content.xpath("//div[@class='list-reviews']/div[1]/ul[1]//a[@class='ru-device']/text()").extract() #strip
    titles = response_content.xpath("//div[@class='list-reviews']/div[1]/ul[1]//a[@class='rd-title']//span/text()").extract()
    contents = response_content.xpath("//div[@class='rd-des toggle-height']/span/text()").extract()
    ratings = response_content.xpath("//div[@class='list-reviews']//li/div[2]/div[1]/span/text()").extract()

    temp = response_content.xpath("//div[@class='list-reviews']/div[1]/ul[1]//ul")
    photos = []

    for t in temp:
        photos.append(t.xpath(".//img/@src").extract())

    # print(len(userUrls),len(createdAts),len(platforms),len(titles),len(contents), len(ratings))

    for i in range(len(userUrls)):
        user = userUrls[i]
        createdAt = createdAts[i] if i < len(createdAts) else None
        platform = platforms[i].strip() if i < len(platforms) else None

        if i < len(ratings):
          if ratings[i].isnumeric():
            rating = float(ratings[i])
          else:
            rating = None
        else:
          rating = None

        title = titles[i].strip() if i < len(titles) else None
        content = contents[i] if i < len(contents) else None

        item['reviews'].append({"user": user, "createdAt": createdAt, "platform": platform, "rating": rating, "title": title, "content": content})

    # Photos
    suffix = "/binh-luan"
    galleryUrl = response.url.removesuffix(suffix) + "/album-anh"
    
    yield scrapy.Request(url=galleryUrl, callback=self.parse_photo, meta={'arg': item}, dont_filter=True)

  def parse_photo(self, response):
    response_content = scrapy.Selector(response)
    item = response.meta.get('arg')

    item['photos'] = response_content.xpath("//div[@class='micro-home-album-img']/div[1]/a/@href").extract()
    item['createdAt'] = int(round(dt.datetime.now().timestamp()))

    self.restaurants.append(item)

    if not item['isBranch']:
      ############## STATUS LOG  ##############
      
      print(f'{self.res_url_id} / {len(self.restaurant_urls)}')

      self.res_url_id += 1
      if self.res_url_id < len(self.restaurant_urls):
        full_res_url = self.start_urls[0][:-1] + self.restaurant_urls[self.res_url_id]

        if '/thuong-hieu/' not in full_res_url:
          
          yield response.follow(url = full_res_url,                   
                        callback= self.parse_a_restaurant, dont_filter = True)
        # branch
        else:
          
          yield response.follow(url = full_res_url, callback=self.parse_a_branch, meta={'isBranch': True}, dont_filter = True)
      
      # END
      else:
        for res in self.restaurants:
          yield res
      
    else:
      self.branch_res_url_id += 1

      if self.branch_res_url_id < len(self.branch_res_urls):
        full_res_url = self.start_urls[0][:-1] + self.branch_res_urls[self.branch_res_url_id]
        yield response.follow(url = full_res_url,                   
                                        callback= self.parse_a_restaurant, meta={'isBranch': True}, dont_filter = True)
        
      else:
        self.res_url_id += 1
        if self.res_url_id < len(self.restaurant_urls):
          full_res_url = self.start_urls[0][:-1] + self.restaurant_urls[self.res_url_id]

          if '/thuong-hieu/' not in full_res_url:
            
            yield response.follow(url = full_res_url,                   
                          callback= self.parse_a_restaurant, dont_filter = True)
          # branch
          else:
            
            yield response.follow(url = full_res_url, callback=self.parse_a_branch, meta={'isBranch': True}, dont_filter = True)
        
        # END
        else:
          for res in self.restaurants:
            yield res
