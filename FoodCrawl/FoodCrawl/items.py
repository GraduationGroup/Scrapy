# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodyItem(scrapy.Item):
    createdAt = scrapy.Field()
    domain = scrapy.Field()
    
    Address = scrapy.Field()
    District = scrapy.Field()
    City = scrapy.Field()
    Phone = scrapy.Field()
    Promotions = scrapy.Field()
    Cuisines = scrapy.Field()
    SpecialDesc = scrapy.Field()
    TotalReview = scrapy.Field()
    TotalView = scrapy.Field()
    TotalFavourite = scrapy.Field()
    TotalCheckins = scrapy.Field()
    AvgRating = scrapy.Field()
    AvgRatingOriginal = scrapy.Field()
    ReviewUrl = scrapy.Field()
    AlbumUrl = scrapy.Field()
    Latitude = scrapy.Field()
    Longitude = scrapy.Field()
    MainCategoryId = scrapy.Field()
    PictureCount = scrapy.Field()
    Status = scrapy.Field()
    IconUrl = scrapy.Field()
    FriendAction = scrapy.Field()
    HasAlredyAddedToList = scrapy.Field()
    AdsProviders = scrapy.Field()
    DistrictId = scrapy.Field()
    DistrictUrl = scrapy.Field()
    CategoryGroupKey = scrapy.Field()
    Distance = scrapy.Field()
    HasBooking = scrapy.Field()
    HasDelivery = scrapy.Field()
    BookingUrl = scrapy.Field()
    DeliveryUrl = scrapy.Field()
    BranchUrl = scrapy.Field()
    BranchName = scrapy.Field()
    BankCards = scrapy.Field()
    Location = scrapy.Field()
    TotalReviewsFormat = scrapy.Field()
    TotalPictures = scrapy.Field()
    TotalPicturesFormat = scrapy.Field()
    TotalSaves = scrapy.Field()
    Reviews = scrapy.Field()
    ReviewsTest = scrapy.Field()
    IsOpening = scrapy.Field()
    HasVideo = scrapy.Field()
    MasterCategoryId = scrapy.Field()
    Services = scrapy.Field()
    Floor = scrapy.Field()
    Categories = scrapy.Field()
    BookingMobileUrl = scrapy.Field()
    PromotionPlainTitle = scrapy.Field()
    Id = scrapy.Field()
    Name = scrapy.Field()
    UrlRewriteName = scrapy.Field()
    PicturePath = scrapy.Field()
    PicturePathLarge = scrapy.Field()
    MobilePicturePath = scrapy.Field()
    DetailUrl = scrapy.Field()
    DocumentType = scrapy.Field()
    ShowInSearchResult = scrapy.Field()
    IsAd = scrapy.Field()
    SubItems = scrapy.Field()
    
    OpeningTime = scrapy.Field()
    AllReviews = scrapy.Field()
    
    # # review
    # reviews = scrapy.Field()

    # # gallery
    # photos = scrapy.Field()


    
    
