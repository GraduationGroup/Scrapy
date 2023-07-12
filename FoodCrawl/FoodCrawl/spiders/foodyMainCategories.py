from time import sleep
import scrapy
import json

import datetime as dt
import os
import copy as cp

from scrapy.utils.response import open_in_browser
from ..items import *


class FoodySpider(scrapy.Spider):
  name = "foody_main_categories"
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
        self.cp_filter = 1650
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
    
    for h in self.service_hrefs:
      sections = h.split('/')

      mainCategoryCode = 'foody'
      if sections[-1]:
        mainCategoryCode = sections[-1]

      yield scrapy.Request(url ='https://www.foody.vn/__get/Directory/GetSearchFilter?filter=category',                  
        callback=self.get_categories, dont_filter = True, cookies={"floc": self.provinces[self.province_id]['id'], "gcat": mainCategoryCode}, headers={'X-Requested-With':'XMLHttpRequest'})
  


  def get_categories(self, response):
    print("\n\n")
    data = json.loads(response.body)
    categories = data['allCategories']

    for c in categories:
      yield c


