from time import sleep
import scrapy
import json

import datetime as dt
import os

from scrapy.utils.response import open_in_browser
from ..items import *

class FoodySpider(scrapy.Spider):
  name = "foody2"
  start_urls = ['https://www.foody.vn/']

  custom_settings = {
    'DOWNLOAD_DELAY': 0.5 # 2 seconds of delay
    }
  
  checkpoint = False
  cp_province = 5
  cp_service = 2
  cp_filter = 99
  cp_page = 0

  checkpoint_file = None

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
      self.provinces = [{"id": l['Id'], 'name': l['DisplayName'], 'slug': l['Url'][1:]} 
                   for l in data['AllLocations'] if l["CountryName"] == "Vietnam"]

      ############## VISIT TẤT CẢ LOCATION ##############
      if self.checkpoint:
        self.province_id = self.cp_province
      else:
        self.province_id = 0

      province_name = self.provinces[self.province_id]['name'] 

      os.system('cls')                                       
      print(f'🚨🚨🚨 PROVINCE: {province_name} ({self.province_id} / {len(self.provinces)})' )

      yield scrapy.Request(url ='https://www.foody.vn/common/_TopCategoryGroupMenu?isUseForSearch=false',                  
                         callback=self.parse_services, dont_filter = True, cookies={"floc": self.provinces[self.province_id]['id']})




  # VISIT SERVICE 
  def parse_services(self, response):
    ############## PARSE SERVICE CỦA LOCATION ĐANG VISIT  ##############
    response_content = scrapy.Selector(response)

    self.service_hrefs = response_content.css('.menu-box li a[rel="nofollow"]::attr(href)').extract()
    self.service_names = response_content.css('.menu-box li a[rel="nofollow"] span:first-child::text').extract()

    if self.checkpoint:
      self.service_id = self.cp_service
    else:
      self.service_id = 0

    service_url = self.start_urls[0][:-1] + self.service_hrefs[self.service_id]
                                            
    ser_name = self.service_names[self.service_id]  
    print("\n\n")
    print(f'🚨🚨🚨 SERVICE: {ser_name} ({self.service_id} / {len(self.service_names)})' ) 

    yield scrapy.Request(url = service_url,                   
                        callback= self.parse_districts)

  


  # CRAWL FILTER
  def parse_districts(self, response):
    yield scrapy.Request(url ='https://www.foody.vn/__get/Directory/GetSearchFilter?filter=district',                  
              callback=self.parse_cuisines, dont_filter = True, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})
  
  


  # CRAWL CUISINES
  def parse_cuisines(self, response):
    data = json.loads(response.body)
    districts = {d['Id']: d['Name'] for d in data['allDistricts']}
    yield scrapy.Request(url ='https://www.foody.vn/__get/Directory/GetSearchFilter?filter=cuisine',                  
              callback=self.parse_categories, dont_filter = True, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'}, meta={'districts': districts})
  


  # CRAWL CATEGORIES
  def parse_categories(self, response):
    data = json.loads(response.body)
    cuisines = {d['Id']: d['Name'] for d in data['allCuisines']}
    yield scrapy.Request(url ='https://www.foody.vn/__get/Directory/GetSearchFilter?filter=category',                  
              callback=self.visit_all_filters, dont_filter = True, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'}, meta = {'districts': response.meta.get('districts'), 'cuisines': cuisines})
    



  def visit_all_filters(self, response):
    data = json.loads(response.body)

    districts = response.meta.get('districts') 
    cuisines = response.meta.get('cuisines') 
    categories = {d['Id']: d['Name'] for d in data['allCategories']}
    
    self.filters = []
    for d in districts.keys():
      for c in cuisines.keys():
        for ca in categories.keys():
          self.filters.append({'district': d, 'districtName': districts[d] , 'cuisine': c, 'cuisineName': cuisines[c], 'category': ca, 'categoryName': categories[ca]})

    
    if self.checkpoint:
      self.filter_id = self.cp_filter
    else:
      self.filter_id = 0

    dis_name = self.filters[self.filter_id]['districtName']                                       
    cui_name = self.filters[self.filter_id]['cuisineName']                                       
    cat_name = self.filters[self.filter_id]['categoryName']     

    print("\n\n")
    filter_str = dis_name + " / " + cui_name + " / " + cat_name
    print(f'🚨🚨🚨 FILTER: {filter_str} ({self.filter_id} / {len(self.filters)})')


    d = self.filters[self.filter_id]['district']
    c = self.filters[self.filter_id]['cuisine']
    ca = self.filters[self.filter_id]['category']

    yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&cs={c}&c={ca}',                  
              callback=self.get_filter_url, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})




  def get_filter_url(self, response):
    data = json.loads(response.body)
    self.filter_url = self.start_urls[0][:-1] + data['Url']
    

    if self.checkpoint:
      self.p = self.cp_page
    else:
      self.p = 1

    location_name = self.provinces[self.province_id]['name']                                     
    service_name = self.service_names[self.service_id]  

    dis_name = self.filters[self.filter_id]['districtName']                                       
    cui_name = self.filters[self.filter_id]['cuisineName']                                       
    cat_name = self.filters[self.filter_id]['categoryName']
    filter_str = dis_name + " / " + cui_name + " / " + cat_name

    self.checkpoint_file = open('checkpoint.txt', 'w')
    self.checkpoint_file.write(f'PROVINCE: {self.province_id}\nSERVICE: {self.service_id}\nFILTER: {self.filter_id}\nPAGE: {self.p}')
    self.checkpoint_file.close()

    print('\n')                                           
    print(f'🥩PAGE: {self.p} 🍟PROVINCE: {location_name} ({self.province_id} / {len(self.provinces)}) 🍔SERVICE: {service_name} ({self.service_id} / {len(self.service_names)}) 🍙FILTER: {filter_str} ({self.filter_id} / {len(self.filters)})')
    yield scrapy.Request(url = self.filter_url + f'&page={self.p}&append=True',                  
              callback=self.parse_filter, cookies={"floc": self.provinces[self.province_id]['id']})




  def json_to_item(self, json):
    name = json['Name']
    district = json['District']
    lat = json['Latitude']
    long = json['Longitude']

    rating = json['AvgRating']
    branches = json['SubItems']

    return name, district, lat, long, rating, branches
  
    item = FoodyItem()
    item['name'] = name
    item['district'] = district
    item['latitude '] = lat
    item['longitude'] = long
    item['rating'] = avgOriginal

    print(name, district, lat, long, avg, avgOriginal)
    yield item

    for br in branches:
      name = br['Name']
      district = br['District']
      lat = br['Latitude']
      long = br['Longitude']

      avg = br['AvgRating']
      avgOriginal = br['AvgRatingOriginal']

      item = FoodyItem()
      item['name'] = name
      item['district'] = district
      item['latitude '] = lat
      item['longitude'] = long
      item['rating'] = avgOriginal

      print(name, district, lat, long, avg, avgOriginal)
      yield item




  def parse_filter(self, response):
    ############## PARSE CATEGORY TO GET 12 RESTAURANTS  ##############
    html = str(response.text.strip())
    c = html.split('var jsonData = ')
    d = c[1]
    d = d.split('var jsonDataSearch')
    a1 = d[0].strip()[:-1]
      
    data = json.loads(a1)
    self.restaurants = data['searchItems']

    # selectedCuisines
    # searchItems
      # BranchUrl
      # SubItems (chi nhánh)
    
      # Name
      # District

      # Latitude
      # Longitude
      
      # ReviewUrl & AlbumUrl
      # AvgRating & AvgRatingOriginal
      
    
    ###################### PAGE CÓ DATA ######################
    if self.restaurants:
      ###################### THÔNG TIN CƠ BẢN CỦA RESTAURANT ######################
      for r in self.restaurants:
        item = FoodyItem()
        item['slug'] = r['DetailUrl']
        item['name'] = r['Name']
        item['district'] = r['District']
        item['latitude'] = r['Latitude']
        item['longitude'] = r['Longitude']
        item['rating'] = r['AvgRating']

        yield item

        branches = r['SubItems']

        if len(branches) > 0:
          print(f"💕💕💕 {r['BranchName']} CÓ {len(branches)} CỬA HÀNG")
          for br in branches:
            item = FoodyItem()
            item['slug'] = br['DetailUrl']
            item['name'] = br['Name']
            item['district'] = br['District']
            item['latitude'] = br['Latitude']
            item['longitude'] = br['Longitude']
            item['rating'] = br['AvgRating']

            yield item
          print(f"💕💕💕")
          print("\n")
          # sleep(10)


      ###################### CHUYỂN TRANG  ######################
      self.p += 1
      location_name = self.provinces[self.province_id]['name']                                     
      service_name = self.service_names[self.service_id]  

      dis_name = self.filters[self.filter_id]['districtName']                                       
      cui_name = self.filters[self.filter_id]['cuisineName']                                       
      cat_name = self.filters[self.filter_id]['categoryName']
      filter_str = dis_name + " / " + cui_name + " / " + cat_name

      self.checkpoint_file = open('checkpoint.txt', 'w')
      self.checkpoint_file.write(f'PROVINCE: {self.province_id}\nSERVICE: {self.service_id}\nFILTER: {self.filter_id}\nPAGE: {self.p}')
      self.checkpoint_file.close()
      print('\n')                                           
      print(f'🥩PAGE: {self.p} 🍟PROVINCE: {location_name} ({self.province_id} / {len(self.provinces)}) 🍔SERVICE: {service_name} ({self.service_id} / {len(self.service_names)}) 🍙FILTER: {filter_str} ({self.filter_id} / {len(self.filters)})')
      yield scrapy.Request(url = self.filter_url + f'&page={self.p}&append=True',                  
                callback=self.parse_filter, cookies={"floc": self.provinces[self.province_id]['id']})


    ###################### PAGE KHÔNG CÓ DATA => CHUYỂN FILTER  ######################
    else:
      ###################### CHUYỂN FILTER ######################
      self.filter_id += 1

      ###################### CÒN FILTER ######################
      if self.filter_id < len(self.filters):
        dis_name = self.filters[self.filter_id]['districtName']                                       
        cui_name = self.filters[self.filter_id]['cuisineName']                                       
        cat_name = self.filters[self.filter_id]['categoryName']     

        print("\n\n")
        filter_str = dis_name + " / " + cui_name + " / " + cat_name
        print(f'🚨🚨🚨 CHUYỂN FILTER: {filter_str} ({self.filter_id} / {len(self.filters)})')


        d = self.filters[self.filter_id]['district']
        c = self.filters[self.filter_id]['cuisine']
        ca = self.filters[self.filter_id]['category']

        yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&cs={c}&c={ca}',                  
                  callback=self.get_filter_url, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})
      

      ###################### HẾT FILTER => CHUYỂN SERVICE ######################
      else:
        ###################### CHUYỂN SERVICE ######################
        self.service_id += 1

        ###################### CÒN SERVICE ######################
        if self.service_id < len(self.service_hrefs):
          service_url = self.start_urls[0][:-1] + self.service_hrefs[self.service_id]

          ser_name = self.service_names[self.service_id]  
          print("\n\n")
          print(f'🚨🚨🚨 SERVICE: {ser_name} ({self.service_id} / {len(self.service_names)})' ) 

          yield scrapy.Request(url = service_url,                   
                              callback= self.parse_districts)
        
        ###################### HẾT SERVICE => CHUYỂN LOCATION ######################
        else: 
          ###################### CHUYỂN SERVICE ######################
          self.province_id += 1
          
          ###################### CÒN LOCATION ######################
          if self.province_id < len(self.provinces):
            location_name = self.provinces[self.province_id]['name']    

            print('\n\n')                                           
            print(f'🚨🚨🚨 CHUYỂN PROVINCE: {location_name} ({self.province_id + 1} / {len(self.provinces)})' )

            yield scrapy.Request(url ='https://www.foody.vn/common/_TopCategoryGroupMenu?isUseForSearch=false',                  
                              callback=self.parse_services, dont_filter = True, cookies={"floc": self.provinces[self.province_id]['id']})
            

          ###################### HẾT LOCATION ######################
          else:
            print("🎉🎉🎉 CRAWL XONG")