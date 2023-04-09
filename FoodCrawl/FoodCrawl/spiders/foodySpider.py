from time import sleep
import scrapy
import json

from scrapy.utils.response import open_in_browser
from ..items import *

class FoodySpider(scrapy.Spider):
  name = "foody"
  start_urls = ['https://www.foody.vn/']

  categoryCookie = "flg=vn; _fbp=fb.1.1679824797377.1569686720; _ga=GA1.2.1955675188.1679824798; __utmz=257500956.1679824798.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); fbm_395614663835338=base_domain=.foody.vn; FOODY.AUTH.UDID=fdbef944-aaef-4a2f-baaa-02e44d6af04c; FOODY.AUTH=E1DC1985A08865250AA951B7A52A6423954299F35FE80A4FAEDB5E764FC8ABDC71CB25D050C5012EF6D58D9BD4C81C0B662B5D06BE29A63790A8799C6593E481F344D412B95ED9BE2207AC492BAA5625DACD0877E2A8B45C4F5FF1C7DBE6CC538EBCD44BBD4DA517985A568058B15A8382D9CEE2CE4CF8DA0E9C7A36E68316F3F7417933E001845023507965809E03A73C83F548AF4A2202C3F58DAE2DFD199CDAA283EAE41A26343353DA8B9A6D03795C306871BB1CF076A07674CAD6C5D79BEB55CAD9025E565738A8ED5C3807C994BEF968C37CA7F7ACB03689EC6A85E0BAC3E1F92940634D712C9A2D8C5EA48B76; _gid=GA1.2.506892632.1681014257; gcat=food; fd.keys=Beefsteak+Ciao+V%e1%bb%a3+%c4%90%e1%ba%b9p+-+Italian+Cuisine; fd.res.view.217=17455,32742,700,46616,752607,957857,1002004,1608,847795; __ondemand_sessionid=okxxd0szhssko5r3uppc41ym; __utma=257500956.1955675188.1679824798.1681039525.1681053144.11; __utmc=257500956; __utmt_UA-33292184-1=1; fbsr_395614663835338=28se5OrfOtoIA08VlGdf0v3hMMIpEgaY1oDXeb2uTXA.eyJ1c2VyX2lkIjoiNjA4NzE3NDI2MTYzOTYwIiwiY29kZSI6IkFRQmsxZG90VFQ5N0lMdFVycHZ5NWpNVWpJT1M5NmVNVk1RNG42UEtWMktHcWVpRUcwZ1N5VnBHLWQ3Z0FjWlRfbFE1VGdGaXJVeWtNTlJrWDg5dWh3aW05bUg4bzgzZVVheFN1Q005Q1I5c1pUSU1BeGlsS2tTczk1ckxZY1FaWDU4aEdTbzU0RTJQcU8yU3Bjd2VrV0dQQ2NpcGFVYmZoaHhGYzZKR1NiOVY0dVloazlBdGhqTU1aeVhtZnZaT3BDT3Q2S2xIb1hhSWxTdTFFYWhkdkdxRUJFVVpzZU8tbzFCMUNyZndkSFpieVRrUjgteHZKTjNLbktoY0xJTG05M3BtSGZkcEwzeWVkRXFNUnBsenhpbFBQSDZhOHJ3UXVQTkgzYVlFUy1hSlJ6R2JHM0phTlVjanRPalMwQnNUOTJiTEdka2NvSjBiZ1doTzlQYWFrTXEtVWp2MEZQamMyZGhKbnFUSENhTjFlWW55Ry1UemNSbzA1XzZhdkNDamwtUSIsIm9hdXRoX3Rva2VuIjoiRUFBRm56emVCZnNvQkFFT201N2ZNZ0FNdVA4VUN4SnZvUmNkU24ya0Z4eW9GZ28wbDFMck04ZWE4c0k0MmdsRDJaQ1lUY0xmZVpCRFhFNXl1b3pZWGVVblpCTnpaQ3FOMnlHNXFpb3ViOHVIeWVCc3NGN0E4a0NVQnBvMm1sWWVnMHZxYzlpNThJbXJzaFhaQzhZREIzSXJjbjRMSjdQdzIxN1pCeXp2RmllUW42WkFIZnVZUlgyTDBwTmVaQlBtd0ZaQVRFVEdZdmFYWkJHbmdaRFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2ODEwNTMxNDd9; fbsr_395614663835338=28se5OrfOtoIA08VlGdf0v3hMMIpEgaY1oDXeb2uTXA.eyJ1c2VyX2lkIjoiNjA4NzE3NDI2MTYzOTYwIiwiY29kZSI6IkFRQmsxZG90VFQ5N0lMdFVycHZ5NWpNVWpJT1M5NmVNVk1RNG42UEtWMktHcWVpRUcwZ1N5VnBHLWQ3Z0FjWlRfbFE1VGdGaXJVeWtNTlJrWDg5dWh3aW05bUg4bzgzZVVheFN1Q005Q1I5c1pUSU1BeGlsS2tTczk1ckxZY1FaWDU4aEdTbzU0RTJQcU8yU3Bjd2VrV0dQQ2NpcGFVYmZoaHhGYzZKR1NiOVY0dVloazlBdGhqTU1aeVhtZnZaT3BDT3Q2S2xIb1hhSWxTdTFFYWhkdkdxRUJFVVpzZU8tbzFCMUNyZndkSFpieVRrUjgteHZKTjNLbktoY0xJTG05M3BtSGZkcEwzeWVkRXFNUnBsenhpbFBQSDZhOHJ3UXVQTkgzYVlFUy1hSlJ6R2JHM0phTlVjanRPalMwQnNUOTJiTEdka2NvSjBiZ1doTzlQYWFrTXEtVWp2MEZQamMyZGhKbnFUSENhTjFlWW55Ry1UemNSbzA1XzZhdkNDamwtUSIsIm9hdXRoX3Rva2VuIjoiRUFBRm56emVCZnNvQkFFT201N2ZNZ0FNdVA4VUN4SnZvUmNkU24ya0Z4eW9GZ28wbDFMck04ZWE4c0k0MmdsRDJaQ1lUY0xmZVpCRFhFNXl1b3pZWGVVblpCTnpaQ3FOMnlHNXFpb3ViOHVIeWVCc3NGN0E4a0NVQnBvMm1sWWVnMHZxYzlpNThJbXJzaFhaQzhZREIzSXJjbjRMSjdQdzIxN1pCeXp2RmllUW42WkFIZnVZUlgyTDBwTmVaQlBtd0ZaQVRFVEdZdmFYWkJHbmdaRFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2ODEwNTMxNDd9; floc={0}; _gat=1; _gat_ads=1; __utmb=257500956.4.10.1681053144"

  loginCookie = "bc-jcb=1; flg=vn; _fbp=fb.1.1679824797377.1569686720; _ga=GA1.2.1955675188.1679824798; __utmz=257500956.1679824798.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not provided); fbm_395614663835338=base_domain=.foody.vn; FOODY.AUTH.UDID=fdbef944-aaef-4a2f-baaa-02e44d6af04c; FOODY.AUTH=E1DC1985A08865250AA951B7A52A6423954299F35FE80A4FAEDB5E764FC8ABDC71CB25D050C5012EF6D58D9BD4C81C0B662B5D06BE29A63790A8799C6593E481F344D412B95ED9BE2207AC492BAA5625DACD0877E2A8B45C4F5FF1C7DBE6CC538EBCD44BBD4DA517985A568058B15A8382D9CEE2CE4CF8DA0E9C7A36E68316F3F7417933E001845023507965809E03A73C83F548AF4A2202C3F58DAE2DFD199CDAA283EAE41A26343353DA8B9A6D03795C306871BB1CF076A07674CAD6C5D79BEB55CAD9025E565738A8ED5C3807C994BEF968C37CA7F7ACB03689EC6A85E0BAC3E1F92940634D712C9A2D8C5EA48B76; _gid=GA1.2.506892632.1681014257; gcat=food; fd.res.view.217=17455,32742,700,46616,752607,957857,1002004,1608,847795; __ondemand_sessionid=okxxd0szhssko5r3uppc41ym; __utma=257500956.1955675188.1679824798.1681039525.1681053144.11; __utmc=257500956; fd.keys=#Beefsteak+Ciao+Vợ+Đẹp+-+Italian+Cuisine; floc=217; fbsr_395614663835338=UVEq7lgAlKz63tO73DU8mhjJFHGjl6TESDK5ZXR5PQc.eyJ1c2VyX2lkIjoiNjA4NzE3NDI2MTYzOTYwIiwiY29kZSI6IkFRQXZNUlA3dU1HdzNxSkkxdHVTbW1OMkhqX2tMMFhacEZuNEc3WjFmNERIeUcyTWJtYWphdnR3UUdnbW5qRnVQaEV4N0tBdi13N2Q1MGhmNzdaX0RGMmwtYXZLc3hCWDVDYU1DMy1Xd0l6VzFEclFWdHlPR0F4bVZ6M0dDLVFaV3F6Y3IzM2FDSlZiMlF2aXRnTlVjS05BdXU4S2ZjcEctS0pjMlA1MTlkcS1QeDdBVmpVOHdGRkV5ZXY5cWJwU3B4YklYb01WTElkdkFEQm5fSXdYYjQtMEtvaTdPYnFQSTBUVlFsQ3RQb2JnZVprQUMyM2g4SkdPVDVOX2ZPbnlteGVLUHctUGU2UEVrdU1WMWtjSGlVTzFaRnFIVncxbXMzdXRxcWp2Sjk3OFMzNnRmQ25KRjBVSkpEeXZpSUNkN0dlXzNnbHI5cWVUNUQ2UWNYc3F5NTB4MkZOMVEzQWFDU3FFT0hwMVpjdmZ4cXY5TGpZNG92di1COVQ3ck1DeTZhMCIsIm9hdXRoX3Rva2VuIjoiRUFBRm56emVCZnNvQkFCWkNsTndVVTBIU0RGR3E3ZFZyWExGNXY5WGpWUUgyc3o1d1dWY2JaQjh6eGJxd0FCbzBwMFlBS0tFdGtkY1J3VjJub3NUcFJ3eGQybWFaQkxqRmxWRk5yVnV2OXh1YzlLZzZyczFDUVIyZGxYeXBXRGFWUzk5TVpDU2x6aURaQTV2ck82Nk9pSmlldHVLSUtOWkFNYnJ5dGdMaU04ZEQ4c29mTGExbXRKRkNtOEc1U3AxNVdBZjJZcUw2QXZiTDlrZkluSVpDNWdrIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2ODEwNTUyODl9; fbsr_395614663835338=UVEq7lgAlKz63tO73DU8mhjJFHGjl6TESDK5ZXR5PQc.eyJ1c2VyX2lkIjoiNjA4NzE3NDI2MTYzOTYwIiwiY29kZSI6IkFRQXZNUlA3dU1HdzNxSkkxdHVTbW1OMkhqX2tMMFhacEZuNEc3WjFmNERIeUcyTWJtYWphdnR3UUdnbW5qRnVQaEV4N0tBdi13N2Q1MGhmNzdaX0RGMmwtYXZLc3hCWDVDYU1DMy1Xd0l6VzFEclFWdHlPR0F4bVZ6M0dDLVFaV3F6Y3IzM2FDSlZiMlF2aXRnTlVjS05BdXU4S2ZjcEctS0pjMlA1MTlkcS1QeDdBVmpVOHdGRkV5ZXY5cWJwU3B4YklYb01WTElkdkFEQm5fSXdYYjQtMEtvaTdPYnFQSTBUVlFsQ3RQb2JnZVprQUMyM2g4SkdPVDVOX2ZPbnlteGVLUHctUGU2UEVrdU1WMWtjSGlVTzFaRnFIVncxbXMzdXRxcWp2Sjk3OFMzNnRmQ25KRjBVSkpEeXZpSUNkN0dlXzNnbHI5cWVUNUQ2UWNYc3F5NTB4MkZOMVEzQWFDU3FFT0hwMVpjdmZ4cXY5TGpZNG92di1COVQ3ck1DeTZhMCIsIm9hdXRoX3Rva2VuIjoiRUFBRm56emVCZnNvQkFCWkNsTndVVTBIU0RGR3E3ZFZyWExGNXY5WGpWUUgyc3o1d1dWY2JaQjh6eGJxd0FCbzBwMFlBS0tFdGtkY1J3VjJub3NUcFJ3eGQybWFaQkxqRmxWRk5yVnV2OXh1YzlLZzZyczFDUVIyZGxYeXBXRGFWUzk5TVpDU2x6aURaQTV2ck82Nk9pSmlldHVLSUtOWkFNYnJ5dGdMaU04ZEQ4c29mTGExbXRKRkNtOEc1U3AxNVdBZjJZcUw2QXZiTDlrZkluSVpDNWdrIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2ODEwNTUyODl9; __utmt_UA-33292184-1=1; __utmb=257500956.10.10.1681053144"

  loginToken = "SzRjJwACgPI8ia8mzcxDeYJErUAaY8YMNd6VPf7weHyzAcrKIrvHNlNdpp10"
        
  
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
                        callback= self.parse_locations)
      
  def parse_locations(self, response):
      ############## LOCATIONS CRAWLING  ##############
      data = json.loads(response.body)
      self.locations = [{"Id": l['Id'], 'Name': l['DisplayName'], 'Slug': l['Url'][1:], "Districts": l['Districts']} 
                   for l in data['AllLocations'] if l["CountryName"] == "Vietnam"]
      
      ############## GETTING CATEGORIES JSON ##############
      self.location_id = 0
                                                  
      print(f'🎉🎉🎉 CRAWL CATEGORY URLS: ({self.location_id} / {len(self.locations)})', self.locations[self.location_id]['Name'])
      # yield response.follow(self.start_urls[0] + location['Slug'], callback= self.req_categories)
      yield scrapy.Request(url ='https://www.foody.vn/common/_TopCategoryGroupMenu?isUseForSearch=false', 
                    headers = {
                        "Accept": "application/json, text/javascript, */*; q=0.01",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Site": "same-origin",
                        "X-Requested-With": "XMLHttpRequest",
                        "Cookie": str(self.categoryCookie.format(str(self.locations[self.location_id]['Id'])))
                    }, callback=self.parse_categories, dont_filter= True)

  def parse_categories(self, response):
    ############## PARSE REQUEST TO CATEGORY  ##############
    response_content = scrapy.Selector(response)
    self.categories += response_content.xpath('//li[@data-id="1"]/ul[1]//li/a[1]/@href').extract()
    
    ############## TRAVERSE LOCATIONS TO GET CATEGORIES ##############
    self.location_id += 1

    if self.location_id < 5:
      print(f'🎉🎉🎉 CRAWL CATEGORY URLS: ({self.location_id} / {len(self.locations)})', self.locations[self.location_id]['Name'])

      yield scrapy.Request(url ='https://www.foody.vn/common/_TopCategoryGroupMenu?isUseForSearch=false', 
                    headers = {
                        "Accept": "application/json, text/javascript, */*; q=0.01",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Site": "same-origin",
                        "X-Requested-With": "XMLHttpRequest",
                        "Cookie": str(self.categoryCookie.format(str(self.locations[self.location_id]['Id'])))
                    }, callback=self.parse_categories, dont_filter= True)

    ############## CATEGORY CRAWLING IS DONE HERE => PARSE CATEGORY INTO PAGES ##############
    else:
      self.category_id = 0
      self.page = 1

      print(f'🎉🎉🎉 CRAWL_CATEGORIES: ({self.category_id} / {len(self.categories)})', f'\t{self.start_urls[0][:-1]}{self.categories[self.category_id]}')
      print(f'🎉🎉🎉 CRAWL_RES_IN_PAGE: ({self.page} / 50)')
      yield scrapy.Request(url = f"{self.start_urls[0][:-1]}{self.categories[self.category_id]}?page={self.page}",
                            headers = {
                                  "Accept": "application/json, text/javascript, */*; q=0.01",
                                  "Accept-Encoding": "gzip, deflate, br",
                                  "Accept-Language": "en-US,en;q=0.9",
                                  "Sec-Fetch-Mode": "cors",
                                  "Sec-Fetch-Site": "same-origin",
                                  "X-Requested-With": "XMLHttpRequest",
                                  "Cookie": self.loginCookie,
                                  "X-Foody-User-Token": self.loginToken },
                            callback= self.parse_pages)
  
  def parse_pages(self, response):
    ############## PARSE CATEGORY REQUEST TO 12 RESTAURANTS  ##############
    data = json.loads(response.body)['searchItems']

    self.restaurants_of_page = [{'Id': r['Id'], 'Name': r['Name'], 'Categories': [{'Id' : c['Id'], 'Name': c['Name']} for c in r['Categories']], 'Address': r['Address'] ,'Latitude': r['Latitude'], 'Longitude': r['Longitude'] , 'DetailUrl': r['DetailUrl'], 'DistrictUrl': r['DistrictUrl'], 'BranchUrl': r['BranchUrl'], 'isBranch': True if r['BranchUrl'] != '' else False} for r in data]

    if self.restaurants_of_page:
      self.restaurants += self.restaurants_of_page

    print('🚨🚨🚨 ',response.request.url)
    print(len(self.restaurants_of_page))

    # RECURSIVE TO CRAWL ALL PAGES
    self.page +=1 
    if self.page < 6:
      print(f'🎉🎉🎉 CRAWL_RES_IN_PAGE: ({self.page} / 50)')
      # print(f'{self.start_urls[0]}{self.categories[self.category_id]}?page={self.page}')

      yield scrapy.Request(url = f"{self.start_urls[0][:-1]}{self.categories[self.category_id]}?page={self.page}",
                            headers = {
                                  "Accept": "application/json, text/javascript, */*; q=0.01",
                                  "Accept-Encoding": "gzip, deflate, br",
                                  "Accept-Language": "en-US,en;q=0.9",
                                  "Sec-Fetch-Mode": "cors",
                                  "Sec-Fetch-Site": "same-origin",
                                  "X-Requested-With": "XMLHttpRequest",
                                  "Cookie": self.loginCookie,
                                  "X-Foody-User-Token": self.loginToken },
                            callback= self.parse_pages)
    
    ############## PARSE REMAINED CATEGORIES INTO PAGES ##############
    else:
      self.category_id += 1
      self.page = 1
      if self.category_id < 14:
        print(f'🎉🎉🎉 CRAWL_CATEGORIES: ({self.category_id} / {len(self.categories)})', f'\t{self.start_urls[0][:-1]}{self.categories[self.category_id]}')
        print(f'🎉🎉🎉 CRAWL_RES_IN_PAGE: ({self.page} / 50)')
        yield scrapy.Request(url = f"{self.start_urls[0][:-1]}{self.categories[self.category_id]}?page={self.page}",
                              headers = {
                                    "Accept": "application/json, text/javascript, */*; q=0.01",
                                    "Accept-Encoding": "gzip, deflate, br",
                                    "Accept-Language": "en-US,en;q=0.9",
                                    "Sec-Fetch-Mode": "cors",
                                    "Sec-Fetch-Site": "same-origin",
                                    "X-Requested-With": "XMLHttpRequest",
                                    "Cookie": self.loginCookie,
                                    "X-Foody-User-Token": self.loginToken },
                              callback= self.parse_pages)
      
      ############## FINISH PARSE ALL CATEGORIES => INSERT TO DATABASE ##############
      else:
        for id, res in enumerate(self.restaurants):
          print(f'🎉🎉🎉 PARSE RESTAURANTS OF PAGE: ({id}/ {len(self.restaurants)})')
          if res['isBranch']:
            yield response.follow(url = self.start_urls[0][:-1] + res['BranchUrl'], callback=self.parse_a_branch)
          else:
            if res['DetailUrl']:
              yield response.follow(url = self.start_urls[0][:-1] + res['DetailUrl'], callback=self.parse_a_restaurant)
          


    # print(f'🎉🎉🎉 CRAWL_RES_IN_PAGE: ({self.page} / 50)')
    # yield scrapy.Request(url = f'{self.start_urls[0]}{self.categories[self.category_id]}?page={self.page}',
    #                     headers = self.moreHeaders,
    #                     callback=self.parse_pages)
    
  #   # RECURSIVE TO CRAWL ALL CATEGORIES
  #   self.category_id += 1
  #   category = self.categories[self.category_id]

  #   if self.category_id < len(self.categories):
  #   # if self.category_id < 2:
  #     print(f'🎉🎉🎉 CRAWL_CATEGORIES: ({self.category_id} / {len(self.categories)})')
  #     print(category)
  #     category = self.categories[self.category_id]
  #     yield response.follow(f"{self.start_urls[0]}{category}", callback= self.parse_a_category)

  #   # THE END
  #   else:
  #     yield {"restaurants": self.restaurants}


  # def parse_pages(self, response):
  #   print(f"🚨🚨🚨 {response.request.url}")
  #   data = json.loads(response.body)['searchItems']
  #   self.restaurants_of_page = [{'Id': r['Id'], 'Name': r['Name'], 'Categories': [{'Id' : c['Id'], 'Name': c['Name']} for c in r['Categories']], 'Address': r['Address'] ,'Latitude': r['Latitude'], 'Longitude': r['Longitude'] , 'DetailUrl': r['DetailUrl'], 'DistrictUrl': r['DistrictUrl'], 'BranchUrl': r['BranchUrl'], 'isBranch': True if r['BranchUrl'] != '' else False} for r in data]

  #   # parse restaurants of pages
  #   self.res_id = 0
  #   res = self.restaurants_of_page[self.res_id]
  #   print(f'🎉🎉🎉 PARSE RESTAURANTS OF PAGE: ({self.res_id} / {len(self.restaurants_of_page)})')
  #   url = self.start_urls[0] + res['DetailUrl']

  #   if res['isBranch']:
  #     pass
  #   else:
  #     yield response.follow(url = f'{url}',
  #                       callback=self.parse_restaurants_of_page)


  #   # RECURSIVE TO CRAWL ALL PAGES
  #   self.page +=1 
  #   if self.page < 50:
  #     print(f'🎉🎉🎉 CRAWL_RES_IN_PAGE: ({self.page} / 50)')
  #     # print(f'{self.start_urls[0]}{self.categories[self.category_id]}?page={self.page}')

  #     yield scrapy.Request(url = f'{self.start_urls[0]}{self.categories[self.category_id]}?page={self.page}',
  #                       headers = self.moreHeaders,
  #                       callback=self.parse_pages)
    
  #   else:
  #     pass

      
  # def parse_restaurants_of_page(self,response):
  #   restaurant = self.parse_a_restaurant(response)
  #   print(restaurant)
  #   self.restaurants.append(restaurant)

  #   # RECURSIVE TO CRAWL ALL RESTAURANTS
  #   self.res_id += 1

  #   if self.res_id < len(self.restaurants_of_page):
  #     res = self.restaurants_of_page[self.res_id]
  #     print(f'🎉🎉🎉 PARSE RESTAURANTS OF PAGE: ({self.res_id} / {len(self.restaurants_of_page)})')
  #     url = self.start_urls[0] + res['DetailUrl']

  #     if res['isBranch']:
  #       pass
  #     else:
  #       yield response.follow(url = f'{url}',
  #                         callback=self.parse_restaurants_of_page)
  
  def parse_a_branch(self, response):
    restaurants = response.css('.ldc-item-h-name .ng-binding::attr(href)').extract()
    for r in restaurants:
      yield response.follow(url = self.start_urls[0][:-1] + r, callback=self.parse_a_restaurant)
 

  def parse_a_restaurant(self, res_data):
    item = FoodcrawlItem()

    name = res_data.css('h1::text').extract_first().strip()
    item['name'] = name

    points = res_data.css('.microsite-top-points')
    if points:
      points = {p.css('.label::text').extract_first().strip() : p.css('span::text').extract_first().strip() for p in points}
    item['points'] = points
    
    price = ''
    item['price'] = price.join(res_data.xpath("//div[@class='res-common-minmaxprice']/span[2]//text()").extract())
    if price:
      price = price.strip()
    item['price'] = price


    opening_time = res_data.css('.micro-timesopen span:nth-child(3)::text').extract_first()
    if opening_time:
      opening_time = opening_time.strip()
    item['opening_time'] = opening_time
    

    locations = res_data.css('.breadcrum-microsite span[itemprop="itemListElement"]')
    locations = {str(id) : location.css('a::attr(href)').extract_first() for id,location in enumerate(locations)}
    item['locations'] = locations

    categories = res_data.css('.category')
    categories = {c.css('::attr(class)').extract_first(): c.css('a::attr(href)').extract_first() for c in categories}
    item['categories'] = categories
    
    numReviews = res_data.css('.microsite-review-count::text').extract_first()
    if numReviews:
      numReviews = numReviews.strip()
    item['numReviews'] = numReviews

    # yield {"name": name, "points": points, "price": price, "opening_time": opening_time, "locations": locations, "categories": categories, "numReviews": numReviews}
    
    # Reviews
    reviewUrl = "%s/binh-luan" % res_data.request.url
    yield scrapy.Request(url=reviewUrl, callback=self.parse_review, meta={'arg': item})
  
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

        for i in range(len(userUrls)):
            item['reviews'].append({"user": userUrls[i], "createdAt": createdAts[i],"platform": platforms[i].strip(), "rating": float(ratings[i]), "title": titles[i], "content": contents[i]})

        # Photos
        suffix = "/binh-luan"
        galleryUrl = response.url.removesuffix(suffix) + "/album-anh"
        
        yield scrapy.Request(url=galleryUrl, callback=self.parse_photo, meta={'arg': item})

        
  def parse_photo(self, response):
    response_content = scrapy.Selector(response)
    item = response.meta.get('arg')
    item['photos'] = response_content.xpath("//div[@class='micro-home-album-img']/div[1]/a/@href").extract()
    yield item