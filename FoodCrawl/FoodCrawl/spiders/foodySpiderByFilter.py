from time import sleep
import scrapy
import json

import datetime as dt

from scrapy.utils.response import open_in_browser
from ..items import *

class FoodySpider(scrapy.Spider):
  name = "foody2"
  start_urls = ['https://www.foody.vn/']

  locations = []
  
  categories = []

  restaurants = []

  custom_settings = {
    'DOWNLOAD_DELAY': 0.5 # 2 seconds of delay
    }


  # BẮT ĐẦU CRAWL
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
      


  # CRAWL TẤT CẢ LOCATION
  # CRAWL TẤT CẢ SERVICE LẦN LƯỢT TỪNG LOCATION
  def parse_locations(self, response):
      ############## CRAWL TẤT CẢ LOCATION  ##############
      data = json.loads(response.body)

      ############# TÁI CẤU TRÚC LOCATION #############
      self.locations = [{"id": l['Id'], 'name': l['DisplayName'], 'slug': l['Url'][1:]} 
                   for l in data['AllLocations'] if l["CountryName"] == "Vietnam"]

      ############## VISIT TẤT CẢ LOCATION ##############
      self.location_id = 0
      location_name = self.locations[self.location_id]['name']                                              
      print(f'🎉🎉🎉 VISIT TO {location_name}: ({self.location_id + 1} / {len(self.locations)})' )
      # location_url = self.start_urls[0] + self.locations[self.location_id]['slug']

      yield scrapy.Request(url ='https://www.foody.vn/common/_TopCategoryGroupMenu?isUseForSearch=false',                  
                         callback=self.parse_services, dont_filter = True, cookies={"floc": self.locations[self.location_id]['id']})



  # VISIT SERVICE 
  def parse_services(self, response):
    ############## PARSE SERVVICE CỦA LOCATION ĐANG VISIT  ##############
    response_content = scrapy.Selector(response)

    self.categories = response_content.css('.menu-box li a[rel="nofollow"]::attr(href)').extract()
    # if self.location_id == 0:
    #   self.categories[0] = '/ho-chi-minh/food'

    self.category_id = 0
    category_url = self.start_urls[0][:-1] + self.categories[self.category_id]

    yield scrapy.Request(url = category_url,                   
                        callback= self.parse_districts)


    # ############## VISIT LOCATION TIẾP THEO ( NẾU CÒN ) ##############
    # self.location_id += 1
    
    # if self.location_id < len(self.locations):
    # # if self.location_id < 1:
    #   location_name = self.locations[self.location_id]['name']                                              
    #   print(f'🎉🎉🎉 VISIT TO {location_name}: ({self.location_id + 1} / {len(self.locations)})' )

    #   yield scrapy.Request(url ='https://www.foody.vn/common/_TopCategoryGroupMenu?isUseForSearch=false',                  
    #                 callback=self.parse_services, dont_filter = True, cookies={"floc": self.locations[self.location_id]['id']})

    # ############## VISIT XONG TẤT CẢ LOCATION <=> CRAWL TẤT CẢ CATEGORY CÁC LOCATION ##############
    # ############## VISIT TỪNG CATEGORY ##############
    # else:
    #   print(self.categories)
    #   # self.category_id = 0
    #   # category_url = self.start_urls[0][:-1] + self.categories[self.category_id]

    #   # ############## CRAWL TỪNG PAGE CỦA CATEGORY ĐANG VISIT ##############
    #   # self.p = 1
    #   # self.restaurant_urls = []
    #   # print(f'🎉🎉🎉 CRAWL PAGES {self.p} OF ', category_url)
      
    #   # yield scrapy.Request(url = f'{category_url}/dia-diem?page={self.p}&append=true',                   
    #   #                         callback= self.parse_pages)
  



  # CRAWL FILTER
  def parse_districts(self, response):
    yield scrapy.Request(url ='https://www.foody.vn/__get/Directory/GetSearchFilter?filter=district',                  
              callback=self.parse_cuisines, dont_filter = True, cookies={"floc": self.locations[self.location_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})
  
  
  # CRAWL CUISINES
  def parse_cuisines(self, response):
    data = json.loads(response.body)
    districts = {d['Id']: d['Name'] for d in data['allDistricts']}
    yield scrapy.Request(url ='https://www.foody.vn/__get/Directory/GetSearchFilter?filter=cuisine',                  
              callback=self.parse_categories, dont_filter = True, cookies={"floc": self.locations[self.location_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'}, meta={'districts': districts})
  

  # CRAWL CATEGORIES
  def parse_categories(self, response):
    data = json.loads(response.body)
    cuisines = {d['Id']: d['Name'] for d in data['allCuisines']}
    yield scrapy.Request(url ='https://www.foody.vn/__get/Directory/GetSearchFilter?filter=category',                  
              callback=self.visit_all_filters, dont_filter = True, cookies={"floc": self.locations[self.location_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'}, meta = {'districts': response.meta.get('districts'), 'cuisines': cuisines})
    

  def visit_all_filters(self, response):
    data = json.loads(response.body)

    districts = response.meta.get('districts') 
    cuisines = response.meta.get('cuisines') 
    categories = {d['Id']: d['Name'] for d in data['allCategories']}
    
    self.filters = []
    for d in districts.keys():
      for c in cuisines.keys():
        for ca in categories.keys():
          self.filters.append({'district': d, 'cuisine': c, 'category': ca})

    
    self.filter_id = 0

    d = self.filters[self.filter_id]['district']
    c = self.filters[self.filter_id]['cuisine']
    ca = self.filters[self.filter_id]['category']

    yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&cs={c}&c={ca}',                  
              callback=self.get_filter_url, cookies={"floc": self.locations[self.location_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})



  def get_filter_url(self, response):
    data = json.loads(response.body)
    self.filter_url = self.start_urls[0][:-1] + data['Url']
    
    self.p = 1

    yield scrapy.Request(url = self.filter_url + f'&page={self.p}&append=True',                  
              callback=self.parse_filter, cookies={"floc": self.locations[self.location_id]['id']})



  def parse_filter(self, response):
    ############## PARSE CATEGORY TO GET 12 RESTAURANTS  ##############
    selector = scrapy.Selector(response)
    res_name = selector.css('h2 a::attr(href)').extract()
    # print('🎉🎉🎉 ', len(res_name))

    if len(res_name) != 0:
    # if len(self.restaurant_urls) == 0:
        self.restaurants = [n.strip() for n in res_name]

        self.restaurant_id = 0
        restaurant_url = self.start_urls[0][:-1] + self.restaurants[self.restaurant_id]

        # not branch
        if '/thuong-hieu/' not in restaurant_url:
          yield response.follow(url = restaurant_url,                   
                        callback= self.parse_a_restaurant, dont_filter = True)
          
        # branch
        else:
          yield response.follow(url = restaurant_url, callback=self.parse_a_branch, dont_filter = True)

    else:
      self.filter_id += 1

      if self.filter_id < 3:
        print("CHUYỂN FILTER CỦA LOCATION + SERVICE")

        d = self.filters[self.filter_id]['district']
        c = self.filters[self.filter_id]['cuisine']
        ca = self.filters[self.filter_id]['category']

        yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&cs={c}&c={ca}',                  
                  callback=self.get_filter_url, cookies={"floc": self.locations[self.location_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})
      
      else:
        # HẾT FILTER CỦA LOCATION + SERVICE
        print("HẾT FILTER CỦA LOCATION + SERVICE hiện tại")

        # CHUYỂN ĐẾN LOCATION + SERVICE KẾ TIẾP
        self.category_id += 1

        # VẪN CÒN LOCATION + SERVICE CHƯA FILTER
        if self.category_id < len(self.categories):
          category_url = self.start_urls[0][:-1] + self.categories[self.category_id]

          yield scrapy.Request(url = category_url,                   
                              callback= self.parse_districts)
        
        # HẾT LOCATION + SERVICE => CHUYỂN LOCATION
        else:
          
          # CHUYỂN ĐẾN LOCATION KẾ TIẾP
          self.location_id += 1
          
          if self.location_id < 3:
            location_name = self.locations[self.location_id]['name']                                              
            print(f'🎉🎉🎉 VISIT TO {location_name}: ({self.location_id + 1} / {len(self.locations)})' )

            yield scrapy.Request(url ='https://www.foody.vn/common/_TopCategoryGroupMenu?isUseForSearch=false',                  
                              callback=self.parse_services, dont_filter = True, cookies={"floc": self.locations[self.location_id]['id']})

          # HẾT LOCATION  => XONG
          else:
            print("CRAWL XONGGGGGGGGGGGGGGGGG !!!!!!!!!!!!!!!!!!!")


  def parse_a_branch(self, response):
    print(f'🎉🎉🎉 {response.request.url} IS BRANCH')

    self.branch_res_url_id = 0
    self.branch_res_urls = response.css('div[ng-if=false] .ldc-item h2 a::attr(href)').extract()

    full_res_url = self.start_urls[0][:-1] + self.branch_res_urls[self.branch_res_url_id]
    
    
    yield response.follow(url = full_res_url,                   
                                    callback= self.parse_a_restaurant, dont_filter = True, meta={'isBranch': True})  


  def parse_a_restaurant(self, response):
    item = FoodcrawlItem()

    isBranch = response.meta.get('isBranch')

    # print(f'🎉🎉🎉 {response.request.url}')
    # if not item['isBranch']:
    #   print(f'🎉🎉🎉 {response.request.url} IS RESTAURANT')

    name = response.css('h1::text').extract_first()
    if name:
      name = name.strip()
    item['name'] = name

    yield item


    if not isBranch:
      self.restaurant_id += 1

      if self.restaurant_id < len(self.restaurants):
        restaurant_url = self.start_urls[0][:-1] + self.restaurants[self.restaurant_id]
        # not branch
        if '/thuong-hieu/' not in restaurant_url:
          yield response.follow(url = restaurant_url,                   
                        callback= self.parse_a_restaurant, dont_filter = True)
          
        # branch
        else:
          yield response.follow(url = restaurant_url, callback=self.parse_a_branch, dont_filter = True)  
      
      else:
        self.p += 1

        yield scrapy.Request(url = self.filter_url + f'&page={self.p}&append=True',                  
            callback=self.parse_filter, cookies={"floc": self.locations[self.location_id]['id']})
        
    else:
      self.branch_res_url_id += 1

      if self.branch_res_url_id < len(self.branch_res_urls):
        full_res_url = self.start_urls[0][:-1] + self.branch_res_urls[self.branch_res_url_id]

        yield response.follow(url = full_res_url,                   
                                          callback= self.parse_a_restaurant, dont_filter = True, meta={'isBranch': True})
      
      else:
        self.restaurant_id += 1

        if self.restaurant_id < len(self.restaurants):
          restaurant_url = self.start_urls[0][:-1] + self.restaurants[self.restaurant_id]
          # not branch
          if '/thuong-hieu/' not in restaurant_url:
            yield response.follow(url = restaurant_url,                   
                          callback= self.parse_a_restaurant, dont_filter = True)
            
          # branch
          else:
            yield response.follow(url = restaurant_url, callback=self.parse_a_branch, dont_filter = True)  
        
        else:
          self.p += 1

          yield scrapy.Request(url = self.filter_url + f'&page={self.p}&append=True',                  
              callback=self.parse_filter, cookies={"floc": self.locations[self.location_id]['id']})