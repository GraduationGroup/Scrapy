from time import sleep
import scrapy
import json

import datetime as dt
import os
import copy as cp

from scrapy.utils.response import open_in_browser
from ..items import *


class FoodySpider(scrapy.Spider):
  name = "foody_v3"
  start_urls = ['https://www.foody.vn/']

  custom_settings = {
    'DOWNLOAD_DELAY': 0.15 # 0.5 seconds of delay
    }
  
  loadCheckPoint = True
  checkpoint_file = None

  allReviews = {}

  # BẮT ĐẦU CRAWL
  def parse(self, response):
    if self.loadCheckPoint:
      checkPointData = []

      if os.path.exists('checkpoint.txt'):
        with open('checkpoint.txt', 'r') as f:
            sep = ': '
            for line in f:
              number = int(line.split(sep)[1])
              checkPointData.append(number)

        self.cp_province = checkPointData[0]
        self.cp_service = checkPointData[1]
        self.cp_filter = checkPointData[2]
        self.cp_page = checkPointData[3] - 1

      else:
        self.cp_province = 0
        self.cp_service = 0
        self.cp_filter = 1000
        self.cp_page = 1

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
      if self.loadCheckPoint:
        self.province_id = self.cp_province
      else:
        self.province_id = 0

      province_name = self.provinces[self.province_id]['name'] 

      os.system('cls')                                       
      print(f'⭐⭐⭐ PROVINCE: {province_name} ({self.province_id} / {len(self.provinces)})' )

      yield scrapy.Request(url ='https://www.foody.vn/common/_TopCategoryGroupMenu?isUseForSearch=false',                  
                         callback=self.parse_services, dont_filter = True, cookies={"floc": self.provinces[self.province_id]['id']})




  # VISIT SERVICE 
  def parse_services(self, response):
    ############## PARSE SERVICE CỦA LOCATION ĐANG VISIT  ##############
    response_content = scrapy.Selector(response)

    self.service_hrefs = response_content.css('.menu-box li a[rel="nofollow"]::attr(href)').extract()
    self.service_names = response_content.css('.menu-box li a[rel="nofollow"] span:first-child::text').extract()

    if self.loadCheckPoint:
      self.service_id = self.cp_service
    else:
      self.service_id = 0

    service_url = self.start_urls[0][:-1] + self.service_hrefs[self.service_id]
                                            
    ser_name = self.service_names[self.service_id]  

    print(f'✡️✡️✡️ SERVICE: {ser_name} ({self.service_id} / {len(self.service_names)})' ) 

    yield scrapy.Request(url = service_url,                   
                        callback= self.parse_districts)

  


  # CRAWL DISTRICT
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
    cuisines = {d['Id']: {'Name': d['Name'], 'ParentId': d['ParentId']} for d in data['allCuisines']}
    yield scrapy.Request(url ='https://www.foody.vn/__get/Directory/GetSearchFilter?filter=category',                  
              callback=self.visit_all_filters, dont_filter = True, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'}, meta = {'districts': response.meta.get('districts'), 'cuisines': cuisines})
    



  def visit_all_filters(self, response):
    data = json.loads(response.body)

    self.districts = response.meta.get('districts') 
    self.categories = {d['Id']: d['Name'] for d in data['allCategories']}
    self.cuisines = response.meta.get('cuisines')

    self.filters = []

    for d in self.districts.keys():
      for ca in self.categories.keys():
        self.filters.append({'district': d, 'category': ca})
        for cu in self.cuisines.keys():
          if self.cuisines[cu]['ParentId'] == 0:
            self.filters.append({'district': d, 'category': ca, 'cuisine': cu})

    
    if self.loadCheckPoint:
      self.filter_id = self.cp_filter
    else:
      self.filter_id = 0

    # GET CURRENT FILTER
    current_filter = self.filters[self.filter_id]

    d = current_filter['district']
    ca = current_filter['category']

    d_name = self.districts[current_filter['district']]
    ca_name = self.categories[current_filter['category']]                                                         
    
    self.filterPath = d_name + " / " + ca_name

    if len(current_filter.keys()) == 2:
      yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&c={ca}',                  
                callback=self.get_filter_url, meta={'filterPath': self.filterPath}, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})

    else:
      cu = current_filter['cuisine']

      cu_name = self.cuisines[current_filter['cuisine']]['Name']                                                         
      self.filterPath += " / " + cu_name

      yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&c={ca}&cs={cu}',                  
          callback=self.get_filter_url, meta={'filterPath': self.filterPath}, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})




  def get_filter_url(self, response):
    data = json.loads(response.body)

    self.filter_url = self.start_urls[0][:-1] + data['Url']
    
    if self.loadCheckPoint:
      self.p = self.cp_page
      self.loadCheckPoint = False
    else:
      self.p = 1

    # GET FILTER PATH
    self.filterPath = response.meta.get('filterPath') 

    self.checkpoint_file = open('checkpoint.txt', 'w', encoding="utf-8")
    self.checkpoint_file.write(f'PROVINCE: {self.province_id}\nSERVICE: {self.service_id}\nFILTER: {self.filter_id}\nPAGE: {self.p}')
    self.checkpoint_file.close()

    location_name = self.provinces[self.province_id]['name']                                     
    service_name = self.service_names[self.service_id]  
    print("\n")                                           
    print(f'🥩PAGE: {self.p} 🍟PROVINCE: {location_name} ({self.province_id} / {len(self.provinces)}) 🍔SERVICE: {service_name} ({self.service_id} / {len(self.service_names)}) 🍙FILTER: {self.filterPath} ({self.filter_id} / {len(self.filters)})')
    print(self.filter_url + f'&page={self.p}&append=True\n')
    
    yield scrapy.Request(url = self.filter_url + f'&page={self.p}&append=True',                  
              callback=self.parse_filter, cookies={"floc": self.provinces[self.province_id]['id']})




  def parse_filter(self, response):
    ############## PARSE RESTAURANTS ##############
    html = str(response.text.strip())
    c = html.split('var jsonData = ')
    d = c[1]
    d = d.split('var jsonDataSearch')
    a1 = d[0].strip()[:-1]
    data = json.loads(a1)

    
    ###################### PAGE CÓ DATA ######################
    self.restaurants = data['searchItems']
    if len(self.restaurants) != 0:
      ###################### THÔNG TIN CƠ BẢN CỦA RESTAURANT ######################
      for r in self.restaurants:
        item = FoodyItem()
        item['createdAt'] = int(round(dt.datetime.now().timestamp()))
        item['domain'] = 'foody.vn'

        item['Address'] = r['Address']
        item['District'] = r['District']
        item['City'] = r['City']
        item['Phone'] = r['Phone']
        item['Promotions'] = r['Promotions']
        item['Cuisines'] = r['Cuisines']
        item['SpecialDesc'] = r['SpecialDesc']
        item['TotalReview'] = r['TotalReview']
        item['TotalView'] = r['TotalView']
        item['TotalFavourite'] = r['TotalFavourite']
        item['TotalCheckins'] = r['TotalCheckins']
        item['AvgRating'] = r['AvgRating']
        item['AvgRatingOriginal'] = r['AvgRatingOriginal']
        item['ReviewUrl'] = r['ReviewUrl']
        item['AlbumUrl'] = r['AlbumUrl']
        item['Latitude'] = r['Latitude']
        item['Longitude'] = r['Longitude']
        item['MainCategoryId'] = r['MainCategoryId']
        item['PictureCount'] = r['PictureCount']
        item['Status'] = r['Status']
        item['IconUrl'] = r['IconUrl']
        item['FriendAction'] = r['FriendAction']
        item['HasAlredyAddedToList'] = r['HasAlredyAddedToList']
        item['AdsProviders'] = r['AdsProviders']
        item['DistrictId'] = r['DistrictId']
        item['DistrictUrl'] = r['DistrictUrl']         
        item['CategoryGroupKey'] = r['CategoryGroupKey']
        item['Distance'] = r['Distance']
        item['HasBooking'] = r['HasBooking']
        item['HasDelivery'] = r['HasDelivery']
        item['BookingUrl'] = r['BookingUrl']
        item['DeliveryUrl'] = r['DeliveryUrl']
        item['BranchUrl'] = r['BranchUrl']
        item['BranchName'] = r['BranchName']
        item['BankCards'] = r['BankCards']
        item['Location'] = r['Location']
        item['TotalReviewsFormat'] = r['TotalReviewsFormat']
        item['TotalPictures'] = r['TotalPictures']
        item['TotalPicturesFormat'] = r['TotalPicturesFormat']
        item['TotalSaves'] = r['TotalSaves']
        item['Reviews'] = r['Reviews']
        item['ReviewsTest'] = r['ReviewsTest']
        item['IsOpening'] = r['IsOpening']
        item['HasVideo'] = r['HasVideo']
        item['MasterCategoryId'] = r['MasterCategoryId']
        item['Services'] = r['Services']
        item['Floor'] = r['Floor']
        item['Categories'] = r['Categories']
        item['BookingMobileUrl'] = r['BookingMobileUrl']
        item['PromotionPlainTitle'] = r['PromotionPlainTitle']
        item['Id'] = r['Id']
        item['Name'] = r['Name']
        item['UrlRewriteName'] = r['UrlRewriteName']
        item['PicturePath'] = r['PicturePath']
        item['PicturePathLarge'] = r['PicturePathLarge']
        item['MobilePicturePath'] = r['MobilePicturePath']
        item['DetailUrl'] = r['DetailUrl']
        item['DocumentType'] = r['DocumentType']
        item['ShowInSearchResult'] = r['ShowInSearchResult']
        item['IsAd'] = r['IsAd']
        # item['SubItems'] = r['SubItems']
        # yield item

        if item['DetailUrl']:
          print('\t' + self.start_urls[0][:-1] + item['DetailUrl'])
        else:
          print( '\t' + item['Name'])

        yield scrapy.Request(url = 'https://www.foody.vn/__get/Restaurant/GetOpeningTime?resId=' + str(item['Id']),                  
                callback=self.parse_opening_time, meta = {'data': item},  headers={'X-Requested-With':'XMLHttpRequest'})



        branches = r['SubItems']
        if len(branches) > 0:
          print(f"\n\t🏪🏪🏪 {r['BranchName']} CÓ {len(branches)} CHI NHÁNH {self.start_urls[0][:-1] + item['BranchUrl']}")
          
          for br in branches:
            subItem = FoodyItem()
            subItem['createdAt'] = int(round(dt.datetime.now().timestamp()))
            subItem['domain'] = 'foody.vn'


            subItem['Address'] = br['Address']
            subItem['District'] = br['District']
            subItem['City'] = br['City']
            subItem['Phone'] = br['Phone']
            subItem['Promotions'] = br['Promotions']
            subItem['Cuisines'] = br['Cuisines']
            subItem['SpecialDesc'] = br['SpecialDesc']
            subItem['TotalReview'] = br['TotalReview']
            subItem['TotalView'] = br['TotalView']
            subItem['TotalFavourite'] = br['TotalFavourite']
            subItem['TotalCheckins'] = br['TotalCheckins']
            subItem['AvgRating'] = br['AvgRating']
            subItem['AvgRatingOriginal'] = br['AvgRatingOriginal']
            subItem['ReviewUrl'] = br['ReviewUrl']
            subItem['AlbumUrl'] = br['AlbumUrl']
            subItem['Latitude'] = br['Latitude']
            subItem['Longitude'] = br['Longitude']
            subItem['MainCategoryId'] = br['MainCategoryId']
            subItem['PictureCount'] = br['PictureCount']
            subItem['Status'] = br['Status']
            subItem['IconUrl'] = br['IconUrl']
            subItem['FriendAction'] = br['FriendAction']
            subItem['HasAlredyAddedToList'] = br['HasAlredyAddedToList']
            subItem['AdsProviders'] = br['AdsProviders']
            subItem['DistrictId'] = br['DistrictId']
            subItem['DistrictUrl'] = br['DistrictUrl']         
            subItem['CategoryGroupKey'] = br['CategoryGroupKey']
            subItem['Distance'] = br['Distance']
            subItem['HasBooking'] = br['HasBooking']
            subItem['HasDelivery'] = br['HasDelivery']
            subItem['BookingUrl'] = br['BookingUrl']
            subItem['DeliveryUrl'] = br['DeliveryUrl']
            subItem['BranchUrl'] = br['BranchUrl']
            subItem['BranchName'] = br['BranchName']
            subItem['BankCards'] = br['BankCards']
            subItem['Location'] = br['Location']
            subItem['TotalReviewsFormat'] = br['TotalReviewsFormat']
            subItem['TotalPictures'] = br['TotalPictures']
            subItem['TotalPicturesFormat'] = br['TotalPicturesFormat']
            subItem['TotalSaves'] = br['TotalSaves']
            subItem['Reviews'] = br['Reviews']
            subItem['ReviewsTest'] = br['ReviewsTest']
            subItem['IsOpening'] = br['IsOpening']
            subItem['HasVideo'] = br['HasVideo']
            subItem['MasterCategoryId'] = br['MasterCategoryId']
            subItem['Services'] = br['Services']
            subItem['Floor'] = br['Floor']
            subItem['Categories'] = br['Categories']
            subItem['BookingMobileUrl'] = br['BookingMobileUrl']
            subItem['PromotionPlainTitle'] = br['PromotionPlainTitle']
            subItem['Id'] = br['Id']
            subItem['Name'] = br['Name']
            subItem['UrlRewriteName'] = br['UrlRewriteName']
            subItem['PicturePath'] = br['PicturePath']
            subItem['PicturePathLarge'] = br['PicturePathLarge']
            subItem['MobilePicturePath'] = br['MobilePicturePath']
            subItem['DetailUrl'] = br['DetailUrl']
            subItem['DocumentType'] = br['DocumentType']
            subItem['ShowInSearchResult'] = br['ShowInSearchResult']
            subItem['IsAd'] = br['IsAd']
            # subItem['SubItems'] = br['SubItems']

            # yield item
            if subItem['DetailUrl']:
              print('\t\t' + self.start_urls[0][:-1] + subItem['DetailUrl'])
            else:
              print('\t\t' + subItem['Name'])

            yield scrapy.Request(url = 'https://www.foody.vn/__get/Restaurant/GetOpeningTime?resId=' + str(subItem['Id']),                  
                callback=self.parse_opening_time, meta = {'data': subItem},  headers={'X-Requested-With':'XMLHttpRequest'})
              
          print('')

      ###################### CHUYỂN TRANG  ######################
      self.p += 1

      self.checkpoint_file = open('checkpoint.txt', 'w', encoding="utf-8")
      self.checkpoint_file.write(f'PROVINCE: {self.province_id}\nSERVICE: {self.service_id}\nFILTER: {self.filter_id}\nPAGE: {self.p}')
      self.checkpoint_file.close()

      location_name = self.provinces[self.province_id]['name']                                     
      service_name = self.service_names[self.service_id]  

      print("\n")                                                                                
      print(f'🥩PAGE: {self.p} 🍟PROVINCE: {location_name} ({self.province_id} / {len(self.provinces)}) 🍔SERVICE: {service_name} ({self.service_id} / {len(self.service_names)}) 🍙FILTER: {self.filterPath} ({self.filter_id} / {len(self.filters)})')
      print(self.filter_url + f'&page={self.p}&append=True\n')
      yield scrapy.Request(url = self.filter_url + f'&page={self.p}&append=True',                  
                callback=self.parse_filter, cookies={"floc": self.provinces[self.province_id]['id']})


    ###################### PAGE KHÔNG CÓ DATA => CHUYỂN FILTER  ######################
    else:
      ###################### CHUYỂN FILTER ######################
      self.filter_id += 1

      if self.filter_id < len(self.filters):
        # GET CURRENT FILTER
        current_filter = self.filters[self.filter_id]

        d = current_filter['district']
        ca = current_filter['category']

        d_name = self.districts[current_filter['district']]
        ca_name = self.categories[current_filter['category']]                                                         
        
        self.filterPath = d_name + " / " + ca_name

        if len(current_filter.keys()) == 2:
          print("\n")
          print(f"☪️☪️☪️ CHUYỂN FILTER: {self.filterPath} ({self.filter_id} / {len(self.filters)})")
          yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&c={ca}',                  
                    callback=self.get_filter_url, meta={'filterPath': self.filterPath}, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})

        else:
          cu_name = self.cuisines[current_filter['cuisine']]['Name']                                                   
          self.filterPath += " / " + cu_name
          print("\n")
          print(f"☪️☪️☪️ CHUYỂN FILTER: {self.filterPath} ({self.filter_id} / {len(self.filters)})")

          cu = current_filter['cuisine']
          yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&c={ca}&cs={cu}',                  
              callback=self.get_filter_url, meta={'filterPath': self.filterPath}, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})
      

      ###################### HẾT FILTER => CHUYỂN SERVICE ######################
      else:
        ###################### CHUYỂN SERVICE ######################
        self.service_id += 1

        ###################### CÒN SERVICE ######################
        if self.service_id < len(self.service_hrefs):
          service_url = self.start_urls[0][:-1] + self.service_hrefs[self.service_id]

          ser_name = self.service_names[self.service_id]  
          print("\n")
          print(f'✡️✡️✡️ CHUYỂN SERVICE: {ser_name} ({self.service_id} / {len(self.service_names)})' ) 

          yield scrapy.Request(url = service_url,                   
                              callback= self.parse_districts)
        
        ###################### HẾT SERVICE => CHUYỂN LOCATION ######################
        else: 
          ###################### CHUYỂN SERVICE ######################
          self.province_id += 1
          
          ###################### CÒN LOCATION ######################
          if self.province_id < len(self.provinces):
            location_name = self.provinces[self.province_id]['name']    

            print('\n')                                           
            print(f'⭐⭐⭐ PROVINCE: {location_name} ({self.province_id + 1} / {len(self.provinces)})' )

            yield scrapy.Request(url ='https://www.foody.vn/common/_TopCategoryGroupMenu?isUseForSearch=false',                  
                              callback=self.parse_services, dont_filter = True, cookies={"floc": self.provinces[self.province_id]['id']})
            

          ###################### HẾT LOCATION ######################
          else:
            print("🎉🎉🎉 CRAWL XONG")

  def parse_opening_time(self, response):
    item = response.meta.get('data')

    # GET OPENING TIME
    data = json.loads(response.body)
    item['OpeningTime'] = data['Items']

    yield item

    # # Get first 10 reviews
    # resId = item['Id']


    # # https://www.foody.vn/__get/Review/ResLoadMore?ResId=107609&Count=10&Type=1&fromOwner=&isLatest=true
    # yield scrapy.Request(url = f'https://www.foody.vn/__get/Review/ResLoadMore?ResId={resId}&Count=10&Type=1&fromOwner=&isLatest=true',                  
    #     callback=self.parse_reviews, meta = {'data': item},  headers={'X-Requested-With':'XMLHttpRequest'})
  

  def parse_reviews(self, response):
    item = response.meta.get('data')
    resId = item['Id']

    print('\t' + self.start_urls[0][:-1] + item['DetailUrl'])

    # Get reviews from json
    data = json.loads(response.body)
    reviewItems = data['Items']

    if reviewItems:
      if resId in self.allReviews.keys():
        self.allReviews[resId] += reviewItems
      else:
        self.allReviews[resId] = reviewItems

      lastId = reviewItems[-1]['Id']
      yield scrapy.Request(url = f'https://www.foody.vn/__get/Review/ResLoadMore?ResId={resId}&LastId={lastId}&Count=10&Type=1&fromOwner=&isLatest=true', callback=self.parse_reviews, meta = {'data': item},  headers={'X-Requested-With':'XMLHttpRequest'})

    else:
      if resId in self.allReviews.keys():
        item['AllReviews'] = self.allReviews[resId]
      else:
        item['AllReviews'] = None

      yield item

    

    