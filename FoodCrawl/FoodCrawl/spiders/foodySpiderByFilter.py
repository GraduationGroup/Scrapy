from time import sleep
import scrapy
import json

import datetime as dt
import os
import copy as cp

from scrapy.utils.response import open_in_browser
from ..items import *


class FoodySpider(scrapy.Spider):
  name = "foody2"
  start_urls = ['https://www.foody.vn/']

  custom_settings = {
    'DOWNLOAD_DELAY': 0.5 # 2 seconds of delay
    }
  
  # configure_logging(install_root_handler=False)
  # logging.basicConfig(
  #     filename='log.txt',
  #     format='%(levelname)s: %(message)s',
  #     level=logging.INFO
  # )
  
  checkpoint = True
  cp_province = 0
  cp_service = 0
  cp_filter = 5
  cp_page = 1

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
    print("\n")
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
    cuisines = {d['Id']: {"Name": d['Name'], "ParentId": d['ParentId']} for d in data['allCuisines']}
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
    
    if self.checkpoint:
      self.filter_id = self.cp_filter
    else:
      self.filter_id = 0

    dis_name = self.districts[self.filters[self.filter_id]['district']]
    cat_name = self.categories[self.filters[self.filter_id]['category']]                                                         
    

    print("\n")
    self.filterPath = dis_name + " / " + cat_name
    print(f'🚨🚨🚨 FILTER: {self.filterPath} ({self.filter_id} / {len(self.filters)})')


    d = self.filters[self.filter_id]['district']
    # c = self.filters[self.filter_id]['cuisine']
    ca = self.filters[self.filter_id]['category']

    yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&c={ca}',                  
              callback=self.get_filter_url, meta={'filterPath': self.filterPath}, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})




  def get_filter_url(self, response):
    data = json.loads(response.body)
    self.filter_url = self.start_urls[0][:-1] + data['Url']
    
    if self.checkpoint:
      self.p = self.cp_page
      self.checkpoint = False
    else:
      self.p = 1

    location_name = self.provinces[self.province_id]['name']                                     
    service_name = self.service_names[self.service_id]  

    self.filterPath = response.meta.get('filterPath') 

    self.checkpoint_file = open('checkpoint.txt', 'w')
    self.checkpoint_file.write(f'PROVINCE: {self.province_id}\nSERVICE: {self.service_id}\nFILTER: {self.filter_id}\nPAGE: {self.p}')
    self.checkpoint_file.close()

    print('\n')                                           
    print(f'🥩PAGE: {self.p} 🍟PROVINCE: {location_name} ({self.province_id} / {len(self.provinces)}) 🍔SERVICE: {service_name} ({self.service_id} / {len(self.service_names)}) 🍙FILTER: {self.filterPath} ({self.filter_id} / {len(self.filters)})')
    print(self.filter_url + f'&page={self.p}&append=True')
    yield scrapy.Request(url = self.filter_url + f'&page={self.p}&append=True',                  
              callback=self.parse_filter, cookies={"floc": self.provinces[self.province_id]['id']})




  def parse_filter(self, response):
    # sleep(1)
    ############## PARSE RESTAURANTS ##############
    html = str(response.text.strip())
    c = html.split('var jsonData = ')
    d = c[1]
    d = d.split('var jsonDataSearch')
    a1 = d[0].strip()[:-1]
    data = json.loads(a1)


    totalResult = data['totalResult']
    
    # Lớn hơn 166 trang
    if totalResult > 12 * 166:
      print("😊😊😊😊 Nhiều hơn 2k item")
      sleep(10)

      rev_cuisines = list(self.cuisines.keys())
      rev_cuisines.reverse()

      # Thêm Món Việt, Món Âu, ...
      if len(self.filters[self.filter_id].keys()) == 2:
        current_filter = cp.deepcopy(self.filters[self.filter_id])
        del self.filters[self.filter_id]

        for c in rev_cuisines:
          parentId = self.cuisines[c]['ParentId']
          if parentId == 0:
            temp = cp.deepcopy(current_filter)
            temp['cuisine'] = c
            self.filters.insert(self.filter_id, temp)


        d = self.filters[self.filter_id]['district']
        c = self.filters[self.filter_id]['cuisine']
        ca = self.filters[self.filter_id]['category']

        cui_name = self.cuisines[self.filters[self.filter_id]['cuisine']]['Name']
        self.filterPath += " / " + cui_name

        yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&cs={c}&c={ca}',                  
                callback=self.get_filter_url, meta={'filterPath': self.filterPath}, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})      
        

      # Thêm Miền Nam, Miền Bắc, ...
      elif len(self.filters[self.filter_id].keys()) == 3:
        current_filter = cp.deepcopy(self.filters[self.filter_id])
        del self.filters[self.filter_id]

        for c in rev_cuisines:
          parentId = self.cuisines[c]['ParentId']
          if parentId != 0:
            temp = cp.deepcopy(current_filter)
            temp['d_cuisine'] = c
            self.filters.insert(self.filter_id, temp)

        d = self.filters[self.filter_id]['district']
        c = self.filters[self.filter_id]['d_cuisine']
        ca = self.filters[self.filter_id]['category']

        cui_name = self.cuisines[self.filters[self.filter_id]['d_cuisine']]['Name']
        self.filterPath += " / " + cui_name

        yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&cs={c}&c={ca}',                  
                callback=self.get_filter_url, meta={'filterPath': self.filterPath}, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'}) 

      # Không thêm chỉ gửi request
      elif len(self.filters[self.filter_id].keys()) == 4:
        self.restaurants = data['searchItems']

        ###################### PAGE CÓ DATA ######################
        if len(self.restaurants) != 0:
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
              print(f"🏪🏪🏪 {r['BranchName']} CÓ {len(branches)} CỬA HÀNG")

              for br in branches:
                item = FoodyItem()
                item['slug'] = br['DetailUrl']
                item['name'] = br['Name']
                item['district'] = br['District']
                item['latitude'] = br['Latitude']
                item['longitude'] = br['Longitude']
                item['rating'] = br['AvgRating']

                yield item
          print("\n")


          ###################### CHUYỂN TRANG  ######################
          self.p += 1
          location_name = self.provinces[self.province_id]['name']                                     
          service_name = self.service_names[self.service_id]  


          self.checkpoint_file = open('checkpoint.txt', 'w')
          self.checkpoint_file.write(f'PROVINCE: {self.province_id}\nSERVICE: {self.service_id}\nFILTER: {self.filter_id}\nPAGE: {self.p}')
          self.checkpoint_file.close()
          print('\n')                                           
          print(f'🥩PAGE: {self.p} 🍟PROVINCE: {location_name} ({self.province_id} / {len(self.provinces)}) 🍔SERVICE: {service_name} ({self.service_id} / {len(self.service_names)}) 🍙FILTER: {self.filterPath} ({self.filter_id} / {len(self.filters)})')
          print(self.filter_url + f'&page={self.p}&append=True')
          yield scrapy.Request(url = self.filter_url + f'&page={self.p}&append=True',                  
                    callback=self.parse_filter, cookies={"floc": self.provinces[self.province_id]['id']})


        ###################### PAGE KHÔNG CÓ DATA => CHUYỂN FILTER  ######################
        else:
          ###################### CHUYỂN FILTER ######################
          self.filter_id += 1

          ###################### CÒN FILTER ######################
          if self.filter_id < len(self.filters):
            dis_name = self.districts[self.filters[self.filter_id]['district']]
            cat_name = self.categories[self.filters[self.filter_id]['category']]    

            if len(self.filters[self.filter_id].keys()) == 2:
              d = self.filters[self.filter_id]['district']
              ca = self.filters[self.filter_id]['category']

              self.filterPath = dis_name + " / " + cat_name
              
              print("\n")
              print(f'🚨🚨🚨 CHUYỂN FILTER: {self.filterPath} ({self.filter_id} / {len(self.filters)})')

              yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&c={ca}',                  
                        callback=self.get_filter_url, meta={'filterPath': self.filterPath}, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})

            elif len(self.filters[self.filter_id].keys()) == 3:
              cui_name = self.cuisines[self.filters[self.filter_id]['cuisine']]['Name']
              self.filterPath = dis_name + " / "  + cat_name + " / " + cui_name

              print("\n")
              print(f'🚨🚨🚨 CHUYỂN FILTER: {self.filterPath} ({self.filter_id} / {len(self.filters)})')                                    

              d = self.filters[self.filter_id]['district']
              c = self.filters[self.filter_id]['cuisine']
              ca = self.filters[self.filter_id]['category']

              yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&cs={c}&c={ca}',                  
                        callback=self.get_filter_url, meta={'filterPath': self.filterPath}, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})

            else:
              cui_name = self.cuisines[self.filters[self.filter_id]['cuisine']]['Name']
              d_cui_name = self.cuisines[self.filters[self.filter_id]['d_cuisine']]['Name']
              self.filterPath = dis_name + " / "  + cat_name + " / " + cui_name + " / " + d_cui_name

              print("\n")
              print(f'🚨🚨🚨 CHUYỂN FILTER: {self.filterPath} ({self.filter_id} / {len(self.filters)})') 

              d = self.filters[self.filter_id]['district']
              c = self.filters[self.filter_id]['d_cuisine']
              ca = self.filters[self.filter_id]['category']

              yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&cs={c}&c={ca}',                  
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
              print(f'🚨🚨🚨 CHUYỂN SERVICE: {ser_name} ({self.service_id} / {len(self.service_names)})' ) 

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
    
    # Nhỏ hơn 166 trang
    else:
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
      if len(self.restaurants) != 0:
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
            print(f"🏪🏪🏪 {r['BranchName']} CÓ {len(branches)} CỬA HÀNG")
            for br in branches:
              item = FoodyItem()
              item['slug'] = br['DetailUrl']
              item['name'] = br['Name']
              item['district'] = br['District']
              item['latitude'] = br['Latitude']
              item['longitude'] = br['Longitude']
              item['rating'] = br['AvgRating']

              yield item

        print("\n")


        ###################### CHUYỂN TRANG  ######################
        self.p += 1
        location_name = self.provinces[self.province_id]['name']                                     
        service_name = self.service_names[self.service_id]  

        self.checkpoint_file = open('checkpoint.txt', 'w')
        self.checkpoint_file.write(f'PROVINCE: {self.province_id}\nSERVICE: {self.service_id}\nFILTER: {self.filter_id}\nPAGE: {self.p}')
        self.checkpoint_file.close()
        print('\n')                                           
        print(f'🥩PAGE: {self.p} 🍟PROVINCE: {location_name} ({self.province_id} / {len(self.provinces)}) 🍔SERVICE: {service_name} ({self.service_id} / {len(self.service_names)}) 🍙FILTER: {self.filterPath} ({self.filter_id} / {len(self.filters)})')
        print(self.filter_url + f'&page={self.p}&append=True')
        yield scrapy.Request(url = self.filter_url + f'&page={self.p}&append=True',                  
                  callback=self.parse_filter, cookies={"floc": self.provinces[self.province_id]['id']})


      ###################### PAGE KHÔNG CÓ DATA => CHUYỂN FILTER  ######################
      else:
        ###################### CHUYỂN FILTER ######################
        self.filter_id += 1

        ###################### CÒN FILTER ######################
        if self.filter_id < len(self.filters):
          dis_name = self.districts[self.filters[self.filter_id]['district']]
          cat_name = self.categories[self.filters[self.filter_id]['category']]     

          if len(self.filters[self.filter_id].keys()) == 2:
            d = self.filters[self.filter_id]['district']
            ca = self.filters[self.filter_id]['category']

            self.filterPath = dis_name + " / " + cat_name
            
            print("\n")
            print(f'🚨🚨🚨 CHUYỂN FILTER: {self.filterPath} ({self.filter_id} / {len(self.filters)})')

            yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&c={ca}',                  
                      callback=self.get_filter_url, meta={'filterPath': self.filterPath}, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})

          elif len(self.filters[self.filter_id].keys()) == 3:
            cui_name = self.cuisines[self.filters[self.filter_id]['cuisine']]['Name']
            self.filterPath = dis_name + " / "  + cat_name + " / " + cui_name

            print("\n")
            print(f'🚨🚨🚨 CHUYỂN FILTER: {self.filterPath} ({self.filter_id} / {len(self.filters)})')                                    

            d = self.filters[self.filter_id]['district']
            c = self.filters[self.filter_id]['cuisine']
            ca = self.filters[self.filter_id]['category']

            yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&cs={c}&c={ca}',                  
                      callback=self.get_filter_url, meta={'filterPath': self.filterPath}, cookies={"floc": self.provinces[self.province_id]['id']}, headers={'X-Requested-With':'XMLHttpRequest'})

          else:
            cui_name = self.cuisines[self.filters[self.filter_id]['cuisine']]['Name']
            d_cui_name = self.cuisines[self.filters[self.filter_id]['d_cuisine']]['Name']
            self.filterPath = dis_name + " / "  + cat_name + " / " + cui_name + " / " + d_cui_name

            print("\n")
            print(f'🚨🚨🚨 CHUYỂN FILTER: {self.filterPath} ({self.filter_id} / {len(self.filters)})') 

            d = self.filters[self.filter_id]['district']
            c = self.filters[self.filter_id]['d_cuisine']
            ca = self.filters[self.filter_id]['category']

            yield scrapy.Request(url =f'https://www.foody.vn/__get/Directory/GetSearchUrl?dtids={d}&cs={c}&c={ca}',                  
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
            print(f'🚨🚨🚨 CHUYỂN SERVICE: {ser_name} ({self.service_id} / {len(self.service_names)})' ) 

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