import json    # or `import simplejson as json` if on Python < 2.6

a = r"""{"photoCollectionResultCount":8741,"provinceId":218,"categoryId":3,"districtId":21,"districtName":"Quận Cầu Giấy","searchUrl":"/ha-noi/quan-an","searchDefaultUrl":"/ha-noi/dia-diem","keyword":"","viewType":"row","sortType":1,"priceMin":0,"priceMax":5000000,"districts":[{"Id":20,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Ba Đình","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Ba Dinh"},{"Id":690,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Bắc Từ Liêm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Bac Tu Liem"},{"Id":21,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Cầu Giấy","UrlRewriteName":null,"ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Cau Giay"},{"Id":22,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Đống Đa","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Dong Da"},{"Id":23,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hà Đông","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Ha Dong"},{"Id":24,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hai Bà Trưng","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hai Ba Trung"},{"Id":25,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hoàn Kiếm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hoan Kiem"},{"Id":26,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hoàng Mai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hoang Mai"},{"Id":27,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Long Biên","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Long Bien"},{"Id":945,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Nam Từ Liêm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Nam Tu Liem"},{"Id":28,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Tây Hồ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Tay Ho"},{"Id":29,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Thanh Xuân","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Thanh Xuan"},{"Id":692,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Thị Xã Sơn Tây","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Thi Xa Son Tay"},{"Id":674,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Ba Vì","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Ba Vi"},{"Id":675,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Chương Mỹ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Chuong My"},{"Id":676,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Đan Phượng","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Dan Phuong"},{"Id":677,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Đông Anh","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Dong Anh"},{"Id":678,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Gia Lâm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Gia Lam"},{"Id":679,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Hoài Đức","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Hoai Duc"},{"Id":680,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Mê Linh","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Me Linh"},{"Id":681,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Mỹ Đức","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen My Duc"},{"Id":682,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Phú Xuyên","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Phu Xuyen"},{"Id":683,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Phúc Thọ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Phuc Tho"},{"Id":684,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Quốc Oai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Quoc Oai"},{"Id":685,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Sóc Sơn","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Soc Son"},{"Id":686,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thạch Thất","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thach That"},{"Id":687,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thanh Oai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thanh Oai"},{"Id":688,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thanh Trì","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thanh Tri"},{"Id":689,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thường Tín","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thuong Tin"},{"Id":691,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Ứng Hòa","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Ung Hoa"}],"allAreas":[],"allDistricts":[],"allPurposes":[],"allCategories":[],"allCuisines":[],"allDishCategories":[],"allProperties":[],"allDinings":[],"selectedAreas":[],"selectedDistricts":[{"Id":21,"Avatar":null,"ParentId":218,"ParentName":null,"Name":"Quận Cầu Giấy","UrlRewriteName":"quan-cau-giay","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":1,"AsciiName":"Quan Cau Giay"}],"selectedPurposes":[],"selectedCategories":[{"Id":3,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quán ăn","UrlRewriteName":"quan-an","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":8,"AsciiName":"Quan an"}],"selectedCuisines":[{"Id":1,"Avatar":"foody-01-vietnam-635950402447733778.png","ParentId":0,"ParentName":null,"Name":"Món Việt","UrlRewriteName":"viet-nam","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[{"Id":12,"Avatar":"foody-12-miennam-635950401085583984.png","ParentId":1,"ParentName":null,"Name":"Món Miền Nam","UrlRewriteName":"mien-nam","ResultCount":24495,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Mien Nam"},{"Id":2,"Avatar":"foody-02-mienbac-635950402329745934.png","ParentId":1,"ParentName":null,"Name":"Món Bắc","UrlRewriteName":"mien-bac","ResultCount":27554,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Bac"},{"Id":7,"Avatar":"foody-07-mientrung-635950401707280292.png","ParentId":1,"ParentName":null,"Name":"Món Miền Trung","UrlRewriteName":"mien-trung","ResultCount":24634,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Mien Trung"},{"Id":29,"Avatar":"foody-29-taynguyen-635950400755089030.png","ParentId":1,"ParentName":null,"Name":"Tây Nguyên","UrlRewriteName":"tay-nguyen","ResultCount":4555,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Tay Nguyen"}],"FilterType":4,"AsciiName":"Mon Viet"}],"selectedDishCategories":[],"selectedProperties":[],"selectedPrices":[],"selectedDinings":[],"searchItems":[{"Address":"223 Tô Hiệu, P. Nghĩa Tân","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":47,"TotalView":5964,"TotalFavourite":40,"TotalCheckins":1,"AvgRating":"7.1","AvgRatingOriginal":7.054000,"ReviewUrl":"/ha-noi/tuyet-nhung-com-ga-phu-yen/binh-luan","AlbumUrl":"/ha-noi/tuyet-nhung-com-ga-phu-yen/album-anh","Latitude":21.0415890000000,"Longitude":105.7924980000000,"MainCategoryId":3,"PictureCount":142,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/tuyet-nhung-com-ga-phu-yen","BranchUrl":"/thuong-hieu/tuyet-nhung-com-ga-phu-yen?c=ha-noi","BranchName":"Hệ thống Tuyết Nhung - Cơm Gà Phú Yên","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"47","TotalPictures":142,"TotalPicturesFormat":"142","TotalSaves":0,"Reviews":[{"Id":14924525,"RestaurantID":0,"RestaurantStatus":0,"UserID":19859387,"Title":"Đắt, chất lượng trung b\u0026#236;nh","Comment":"Quá đắt so với mức giá. Món nộm thì tốt nhất đừng gọi, toàn giá với rau, trà đá cũng thế.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":2.000000,"OwnerUserName":"foodee_kilxyjpk","OwnerFirstName":"Hồng","OwnerLastName":"","OwnerFullName":"Hồng","OwnerAvatar":"https://images.foody.vn/default/s50/user-default-female.png","OwnerGender":"male","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_kilxyjpk","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/tuyet-nhung-com-ga-phu-yen/binh-luan-14924525"},{"Id":8794725,"RestaurantID":0,"RestaurantStatus":0,"UserID":352254,"Title":"Cơm v\u0026#224; g\u0026#224; kh\u0026#244;ng n\u0026#243;ng, gi\u0026#225; cao so với chất lượng","Comment":"Mình đến ăn lúc 5h30 chiều, thấy ăn cơm nguội, gà xé cũng ít và không ngon nóng. Suất cơm gà 40k mà có quá ít cơm và gà. Đồ ăn lại không có gì đặc biệt nữa.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":4.400000,"OwnerUserName":"tungvu3196","OwnerFirstName":"Tung Vu","OwnerLastName":"","OwnerFullName":"Tung Vu","OwnerAvatar":"https://images.foody.vn/usr/g36/352254/avt/c50x50/foody-avatar-981-637145531689255321.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/tungvu3196","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/tuyet-nhung-com-ga-phu-yen/binh-luan-8794725"}],"ReviewsTest":null,"IsOpening":false,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/tuyet-nhung-com-ga-phu-yen/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":737094,"Name":"Tuyết Nhung - Cơm Gà Phú Yên - Tô Hiệu","UrlRewriteName":"tuyet-nhung-com-ga-phu-yen","PicturePath":"https://images.foody.vn/res/g74/737094/prof/s180x180/foody-upload-api-foody-mobile-phu-yen-jpg-180503093800.jpg","PicturePathLarge":"https://images.foody.vn/res/g74/737094/prof/s640x400/foody-upload-api-foody-mobile-phu-yen-jpg-180503093800.jpg","MobilePicturePath":"https://images.foody.vn/res/g74/737094/prof/s640x400/foody-upload-api-foody-mobile-phu-yen-jpg-180503093800.jpg","DetailUrl":"/ha-noi/tuyet-nhung-com-ga-phu-yen","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"25 Nguyễn Phong Sắc, P. Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":32,"TotalView":16155,"TotalFavourite":25,"TotalCheckins":8,"AvgRating":"7.0","AvgRatingOriginal":6.962000,"ReviewUrl":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/binh-luan","AlbumUrl":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/album-anh","Latitude":21.0368480000000,"Longitude":105.7897550000000,"MainCategoryId":3,"PictureCount":153,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/che-dua-thai-lan-nguyen-phong-sac","BranchUrl":"/thuong-hieu/che-dua-thai-lan-nguyen-phong-sac?c=ha-noi","BranchName":"Hệ thống Chè Dừa Thái Lan - Nguyễn Phong Sắc","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"32","TotalPictures":153,"TotalPicturesFormat":"153","TotalSaves":0,"Reviews":[{"Id":2921035,"RestaurantID":0,"RestaurantStatus":0,"UserID":616780,"Title":"Qu\u0026#225; ch\u0026#225;n ng\u0026#224;y thất tịch","Comment":"Hôm nay gấu bảo ngày ngưu lang chức nữ gặp nhau nên ăn chè đỗ đỏ, mình mới đặt chè đỗ đỏ với 1 số loại chè khác. Grab đến quán bảo đợi 10p vì phải nấu, uh thì mình đợi. Xong grab gọi lại bảo hết tất c...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":1.000000,"OwnerUserName":"thang0208","OwnerFirstName":"Thang","OwnerLastName":"Ngoc","OwnerFullName":"Thang Ngoc","OwnerAvatar":"https://images.foody.vn/usr/g62/616780/avt/c50x50/beauty-upload-api-foody-avatar-69fb5139-a52b-40d4-95d7-efa8a0cd871b-191020213924.jpg","OwnerGender":"male","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/thang0208","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/binh-luan-2921035"},{"Id":2790695,"RestaurantID":0,"RestaurantStatus":0,"UserID":8610623,"Title":"Ch\u0026#232; Dừa Th\u0026#225;i Lan - Nguyễn Phong Sắc","Comment":"Quán nhỏ xinh nằm ngay đầu đường nguyễn phong sắc,ngã 4 trần thái tông xuân thủy cầu giấy.\n\nMenu đa dạng với các loại chè như chè sầu,dừa dầm đến những loại chè truyền thống như chè bưởi,chè đỗ đen..v...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.600000,"OwnerUserName":"xjuzoyr","OwnerFirstName":"Linh","OwnerLastName":"Chi","OwnerFullName":"Linh Chi","OwnerAvatar":"https://images.foody.vn/usr/g862/8610623/avt/c50x50/xjuzoyr-avatar-373-636750583830011143.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/xjuzoyr","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/binh-luan-2790695"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":214084,"Name":"Chè Dừa Thái Lan - Nguyễn Phong Sắc","UrlRewriteName":"che-dua-thai-lan-nguyen-phong-sac","PicturePath":"https://images.foody.vn/res/g22/214084/prof/s180x180/foody-mobile-dua640-jpg-631-635953770711301483.jpg","PicturePathLarge":"https://images.foody.vn/res/g22/214084/prof/s640x400/foody-mobile-dua640-jpg-631-635953770711301483.jpg","MobilePicturePath":"https://images.foody.vn/res/g22/214084/prof/s640x400/foody-mobile-dua640-jpg-631-635953770711301483.jpg","DetailUrl":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"P105A C7 Nghĩa Tân, Ngõ 140 Trần Tử Bình, P. Nghĩa Tân","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":36,"TotalView":42685,"TotalFavourite":13,"TotalCheckins":8,"AvgRating":"7.3","AvgRatingOriginal":7.316000,"ReviewUrl":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/binh-luan","AlbumUrl":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/album-anh","Latitude":21.0425066000000,"Longitude":105.7910876000000,"MainCategoryId":3,"PictureCount":133,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"36","TotalPictures":133,"TotalPicturesFormat":"133","TotalSaves":0,"Reviews":[{"Id":11798200,"RestaurantID":0,"RestaurantStatus":0,"UserID":11579565,"Title":"H\u0026#249;ng B\u0026#233;o - Lẩu Cua Đồng - Trần Tử B\u0026#236;nh","Comment":"Thi thoảng đi ăn lại thì thấy chất lượng quán tốt hơn so vs lần trước mình ăn rồi.😛","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.000000,"OwnerUserName":"Chi2k","OwnerFirstName":"Quỳnhchi","OwnerLastName":"Nguyễn","OwnerFullName":"Quỳnhchi Nguyễn","OwnerAvatar":"https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Chi2k","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/binh-luan-11798200"},{"Id":10567766,"RestaurantID":0,"RestaurantStatus":0,"UserID":11579565,"Title":"H\u0026#249;ng B\u0026#233;o - Lẩu Cua Đồng - Trần Tử B\u0026#236;nh","Comment":"Quán mới đổi người  nấu hay sao ấy mà hôm mình ăn lẩu ếch lại đắt hơn mà nấu siêu nhiều mỡ, thề lần đầu tiên ăn thấy chán như thế😔","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":7.000000,"OwnerUserName":"Chi2k","OwnerFirstName":"Quỳnhchi","OwnerLastName":"Nguyễn","OwnerFullName":"Quỳnhchi Nguyễn","OwnerAvatar":"https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Chi2k","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/binh-luan-10567766"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":160574,"Name":"Hùng Béo - Lẩu Cua Đồng - Trần Tử Bình","UrlRewriteName":"hung-beo-lau-cua-dong-tran-tu-binh","PicturePath":"https://images.foody.vn/res/g17/160574/prof/s180x180/foody-mobile-960x600_hung-beo-lau-533-636147262410516048.jpg","PicturePathLarge":"https://images.foody.vn/res/g17/160574/prof/s640x400/foody-mobile-960x600_hung-beo-lau-533-636147262410516048.jpg","MobilePicturePath":"https://images.foody.vn/res/g17/160574/prof/s640x400/foody-mobile-960x600_hung-beo-lau-533-636147262410516048.jpg","DetailUrl":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"15 Trần Bình","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":23,"TotalView":37441,"TotalFavourite":37,"TotalCheckins":15,"AvgRating":"7.3","AvgRatingOriginal":7.320000,"ReviewUrl":"/ha-noi/ole-banh-truyen-thong-nhat-ban/binh-luan","AlbumUrl":"/ha-noi/ole-banh-truyen-thong-nhat-ban/album-anh","Latitude":21.0361150000000,"Longitude":105.7788790000000,"MainCategoryId":3,"PictureCount":171,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":false,"BookingUrl":"","DeliveryUrl":"","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"23","TotalPictures":171,"TotalPicturesFormat":"171","TotalSaves":0,"Reviews":[{"Id":2053668,"RestaurantID":0,"RestaurantStatus":0,"UserID":512100,"Title":"Ole - B\u0026#225;nh Truyền Thống Nhật Bản","Comment":"Ngon sạch. Vọ trí hơi nóng. Nhân viên nhanh nhẹn vui vẻ. Cần trang trí không gian quán cho phù hợp hơn đẻ tránh tình trạng nóng quá tải khách","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.600000,"OwnerUserName":"Cuongmy","OwnerFirstName":"Cường","OwnerLastName":"My","OwnerFullName":"Cường My","OwnerAvatar":"https://images.foody.vn/usr/g52/512100/avt/c50x50/beauty-upload-api-foody-avatar-5734e3fe-3efd-4703-aeec-083401b954c1-190814200612.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Cuongmy","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/ole-banh-truyen-thong-nhat-ban/binh-luan-2053668"},{"Id":2051031,"RestaurantID":0,"RestaurantStatus":0,"UserID":9123375,"Title":"Hot Dog khổng lồ","Comment":"Hot dog khổng lồ ăn mãi hết. Vỏ rất giòn, nếu bạn nào sợ ngất thì cứ vô tư ăn vì dù chiên dầu nhưng k ngấy đâu nhé. Chị chủ chiên rất khéo vỏ vàng ruộm, sốt ngon cực đỉnh lun.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.800000,"OwnerUserName":"Hien_nt","OwnerFirstName":"Hien_nt","OwnerLastName":"","OwnerFullName":"Hien_nt","OwnerAvatar":"https://images.foody.vn/usr/g913/9123375/avt/c50x50/beauty-upload-api-foody-avatar-394d790d-d30a-4769-a330-363891ecd622-191215142508.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Hien_nt","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/ole-banh-truyen-thong-nhat-ban/binh-luan-2051031"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":214740,"Name":"Ole - Bánh Truyền Thống Nhật Bản","UrlRewriteName":"ole-banh-truyen-thong-nhat-ban","PicturePath":"https://images.foody.vn/res/g22/214740/prof/s180x180/foody-mobile-ole640-jpg-850-635949570629965289.jpg","PicturePathLarge":"https://images.foody.vn/res/g22/214740/prof/s640x400/foody-mobile-ole640-jpg-850-635949570629965289.jpg","MobilePicturePath":"https://images.foody.vn/res/g22/214740/prof/s640x400/foody-mobile-ole640-jpg-850-635949570629965289.jpg","DetailUrl":"/ha-noi/ole-banh-truyen-thong-nhat-ban","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"67 Yên Hòa, P. Yên Hòa","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":35,"TotalView":2696,"TotalFavourite":20,"TotalCheckins":6,"AvgRating":"7.2","AvgRatingOriginal":7.162000,"ReviewUrl":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/binh-luan","AlbumUrl":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/album-anh","Latitude":21.0233415000000,"Longitude":105.7958695000000,"MainCategoryId":3,"PictureCount":104,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/bun-cha-nem-cua-be-yen-hoa","BranchUrl":"/thuong-hieu/bun-cha-nem-cua-be?c=ha-noi","BranchName":"Hệ thống Bún Chả \u0026 Nem Cua Bể","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"35","TotalPictures":104,"TotalPicturesFormat":"104","TotalSaves":0,"Reviews":[{"Id":14908494,"RestaurantID":0,"RestaurantStatus":0,"UserID":19869596,"Title":"Bố xin ch\u0026#250;ng m\u0026#224;y đấyyyyy","Comment":"Làm ăn bát nháo vãi l, rau đéo có, bát đéo có đũa đéo có. ĂN BỐC À.\nBÚN THÌ CHUA, DC 3 CÁI MIẾNG THỊT LÀM ANH bố m đói.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":1.000000,"OwnerUserName":"foodee_x1j5uvj3","OwnerFirstName":"Hiếu","OwnerLastName":"PCI","OwnerFullName":"Hiếu PCI","OwnerAvatar":"https://images.foody.vn/usr/g1987/19869596/avt/c50x50/foody-avatar-654-637777768251432573.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_x1j5uvj3","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/binh-luan-14908494"},{"Id":12985559,"RestaurantID":0,"RestaurantStatus":0,"UserID":11579565,"Title":"B\u0026#250;n Chả \u0026amp; Nem Cua Bể - Y\u0026#234;n H\u0026#242;a","Comment":"Mình đặt 1 bún chả đầy đủ . Bún chả ăn ngon. Nước chấm để trong hộp nắp chắc chắn.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.200000,"OwnerUserName":"Chi2k","OwnerFirstName":"Quỳnhchi","OwnerLastName":"Nguyễn","OwnerFullName":"Quỳnhchi Nguyễn","OwnerAvatar":"https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Chi2k","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/binh-luan-12985559"}],"ReviewsTest":null,"IsOpening":false,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":264770,"Name":"Bún Chả \u0026 Nem Cua Bể - Yên Hòa","UrlRewriteName":"bun-cha-nem-cua-be-yen-hoa","PicturePath":"https://images.foody.vn/res/g27/264770/prof/s180x180/foody-mobile-nem-cua-be-6831-1432-565-636064356571448314.jpg","PicturePathLarge":"https://images.foody.vn/res/g27/264770/prof/s640x400/foody-mobile-nem-cua-be-6831-1432-565-636064356571448314.jpg","MobilePicturePath":"https://images.foody.vn/res/g27/264770/prof/s640x400/foody-mobile-nem-cua-be-6831-1432-565-636064356571448314.jpg","DetailUrl":"/ha-noi/bun-cha-nem-cua-be-yen-hoa","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"2/421 Hoàng Quốc Việt, P. Nghĩa Tân","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":42,"TotalView":1701,"TotalFavourite":14,"TotalCheckins":8,"AvgRating":"7.9","AvgRatingOriginal":7.882000,"ReviewUrl":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/binh-luan","AlbumUrl":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/album-anh","Latitude":21.0458140000000,"Longitude":105.7860350000000,"MainCategoryId":3,"PictureCount":104,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"42","TotalPictures":104,"TotalPicturesFormat":"104","TotalSaves":0,"Reviews":[{"Id":6659403,"RestaurantID":0,"RestaurantStatus":0,"UserID":18306374,"Title":"Ch\u0026#225;n","Comment":"Rau sống héo úa hỏng, quất thì toàn thối, thiếu dưa chuột. Ăn bún đậu mắm tôm mà k có quất thì mất vị quá. Quán làm chán quá!","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":3.400000,"OwnerUserName":"foodee_pxcljj8i","OwnerFirstName":"Nguyễn","OwnerLastName":"Linh","OwnerFullName":"Nguyễn Linh","OwnerAvatar":"https://images.foody.vn/usr/g1831/18306374/avt/c50x50/beauty-upload-api-foody-avatar-423ea137-da03-4d9c-b025-3c1d959dd4d6-191130193559.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_pxcljj8i","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/binh-luan-6659403"},{"Id":4754815,"RestaurantID":0,"RestaurantStatus":0,"UserID":18004183,"Title":"B\u0026#250;n Đậu C\u0026#250;c***- Ho\u0026#224;ng Quốc Việt","Comment":"Ngon , vừa miệng❤️giá cả hợp lí                                                ","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":10.000000,"OwnerUserName":"foodee_9dicnbry","OwnerFirstName":"Quỳnh","OwnerLastName":null,"OwnerFullName":"Quỳnh","OwnerAvatar":"https://images.foody.vn/default/s50/user-default-female.png","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_9dicnbry","OwnerDisplayName":null,"ShortReview":true,"Url":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/binh-luan-4754815"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":762583,"Name":"Bún Đậu Cúc Cu - Hoàng Quốc Việt","UrlRewriteName":"bun-dau-met-cuc-cu-hoang-quoc-viet","PicturePath":"https://images.foody.vn/res/g77/762583/prof/s180x180/image-e3bc5f75-200910115833.jpeg","PicturePathLarge":"https://images.foody.vn/res/g77/762583/prof/s640x400/image-e3bc5f75-200910115833.jpeg","MobilePicturePath":"https://images.foody.vn/res/g77/762583/prof/s640x400/image-e3bc5f75-200910115833.jpeg","DetailUrl":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"66 Duy Tân, P. Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":31,"TotalView":13690,"TotalFavourite":38,"TotalCheckins":6,"AvgRating":"6.4","AvgRatingOriginal":6.388000,"ReviewUrl":"/ha-noi/pho-cuon-ngu-xa-duy-tan/binh-luan","AlbumUrl":"/ha-noi/pho-cuon-ngu-xa-duy-tan/album-anh","Latitude":21.0312530000000,"Longitude":105.7822150000000,"MainCategoryId":3,"PictureCount":106,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/pho-cuon-ngu-xa-duy-tan","BranchUrl":"/thuong-hieu/pho-cuon-ngu-xa?c=ha-noi","BranchName":"Hệ thống Phở Cuốn Ngũ Xã","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"31","TotalPictures":106,"TotalPicturesFormat":"106","TotalSaves":0,"Reviews":[{"Id":13742585,"RestaurantID":0,"RestaurantStatus":0,"UserID":19365772,"Title":"Đồ ăn oke - vừa gi\u0026#225;","Comment":"Ngày trước chưa dịch, buổi trưa ra đây ăn rất đông. Đợt này chỉ đc bán mang về nên chắc cũng đỡ, mình thấy ship nhanh và khá cẩn thận. Đồ ăn vẫn ổn, phù hợp giá tiền. Mình gọi phở chiên phồng và 1 cốc...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":7.600000,"OwnerUserName":"foodee_u32az83y","OwnerFirstName":"Trang Hoàng","OwnerLastName":"","OwnerFullName":"Trang Hoàng","OwnerAvatar":"https://images.foody.vn/default/s50/user-default-female.png","OwnerGender":"female","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_u32az83y","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/pho-cuon-ngu-xa-duy-tan/binh-luan-13742585"},{"Id":10262683,"RestaurantID":0,"RestaurantStatus":0,"UserID":11579565,"Title":"Phở Cuốn Ngũ X\u0026#227; - Duy T\u0026#226;n","Comment":"-phở cuốn ở đây ăn khá đầy, ăn 10 cái là no căng bụng luôn ấy. Thấy review khen chê thất thường , nhưng mình thấy ăn ở quán vẫn oke .","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.000000,"OwnerUserName":"Chi2k","OwnerFirstName":"Quỳnhchi","OwnerLastName":"Nguyễn","OwnerFullName":"Quỳnhchi Nguyễn","OwnerAvatar":"https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Chi2k","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/pho-cuon-ngu-xa-duy-tan/binh-luan-10262683"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/pho-cuon-ngu-xa-duy-tan/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":109338,"Name":"Phở Cuốn Ngũ Xã - Duy Tân","UrlRewriteName":"pho-cuon-ngu-xa-duy-tan","PicturePath":"https://images.foody.vn/res/g11/109338/prof/s180x180/foody-mobile-pho-cuon2-jpg-934-635550098425249236.jpg","PicturePathLarge":"https://images.foody.vn/res/g11/109338/prof/s640x400/foody-mobile-pho-cuon2-jpg-934-635550098425249236.jpg","MobilePicturePath":"https://images.foody.vn/res/g11/109338/prof/s640x400/foody-mobile-pho-cuon2-jpg-934-635550098425249236.jpg","DetailUrl":"/ha-noi/pho-cuon-ngu-xa-duy-tan","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"2 Hẻm 32 Ngách 5 Ngõ 204 Trần Duy Hưng, P. Trung Hòa","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":28,"TotalView":3144,"TotalFavourite":36,"TotalCheckins":7,"AvgRating":"6.4","AvgRatingOriginal":6.418000,"ReviewUrl":"/ha-noi/xoi-tam-thai-ha/binh-luan","AlbumUrl":"/ha-noi/xoi-tam-thai-ha/album-anh","Latitude":21.0089670000000,"Longitude":105.7966910000000,"MainCategoryId":3,"PictureCount":111,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/xoi-tam-thai-ha","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"28","TotalPictures":111,"TotalPicturesFormat":"111","TotalSaves":0,"Reviews":[{"Id":3732556,"RestaurantID":0,"RestaurantStatus":0,"UserID":1662701,"Title":"X\u0026#244;i T\u0026#225;m - Th\u0026#225;i H\u0026#224;","Comment":"Xôi Tám - 322 Thái Hà \n\nBạn sẽ order các topping và xôi theo ý muốn , có hai loại xôi là xôi xéo (15k) và xôi trắng(10k) xôi dẻo và ngon lắm nha. CÒn topping thì giá dao động từ 8k-15k tuỳ loại : xá x...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.600000,"OwnerUserName":"hoanganh8790","OwnerFirstName":"Trang","OwnerLastName":"Hoang","OwnerFullName":"Trang Hoang","OwnerAvatar":"https://images.foody.vn/usr/g167/1662701/avt/c50x50/beauty-upload-api-foody-avatar-62f86f2f-250c-407d-be57-92ccccc540d9-191025131450.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/hoanganh8790","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/xoi-tam-thai-ha/binh-luan-3732556"},{"Id":3713181,"RestaurantID":0,"RestaurantStatus":0,"UserID":15480563,"Title":"X\u0026#244;i T\u0026#225;m - Th\u0026#225;i H\u0026#224;","Comment":"Thật không thể tin vào mắt mình..! Xôi chưa bằng 1 nắm tay :(( sẽ không có lần t2 hic","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":1.000000,"OwnerUserName":"foodee_667zapgi","OwnerFirstName":"Anhh","OwnerLastName":"Linhh","OwnerFullName":"Anhh Linhh","OwnerAvatar":"https://images.foody.vn/usr/g1549/15480563/avt/c50x50/beauty-upload-api-foody-avatar-482e93a1-e57a-4ff9-bf2d-b6d7e3176eb0-191216001840.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_667zapgi","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/xoi-tam-thai-ha/binh-luan-3713181"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/xoi-tam-thai-ha/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":647491,"Name":"Xôi Tám - Trần Duy Hưng","UrlRewriteName":"xoi-tam-thai-ha","PicturePath":"https://images.foody.vn/res/g65/647491/prof/s180x180/foody-mobile-xoi-tam-jpg-523-636410905562883010.jpg","PicturePathLarge":"https://images.foody.vn/res/g65/647491/prof/s640x400/foody-mobile-xoi-tam-jpg-523-636410905562883010.jpg","MobilePicturePath":"https://images.foody.vn/res/g65/647491/prof/s640x400/foody-mobile-xoi-tam-jpg-523-636410905562883010.jpg","DetailUrl":"/ha-noi/xoi-tam-thai-ha","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"273 Tô Hiệu, P. Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":30,"TotalView":1281,"TotalFavourite":38,"TotalCheckins":4,"AvgRating":"8.7","AvgRatingOriginal":8.700000,"ReviewUrl":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/binh-luan","AlbumUrl":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/album-anh","Latitude":21.0415730000000,"Longitude":105.7914360000000,"MainCategoryId":3,"PictureCount":29,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/safodi-buffet-lau-hoi-lau-nuong","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"30","TotalPictures":29,"TotalPicturesFormat":"29","TotalSaves":0,"Reviews":[{"Id":9996039,"RestaurantID":0,"RestaurantStatus":0,"UserID":20049115,"Title":"Lẩu ở đ\u0026#226;y ok","Comment":"Mình đến lúc gần 8h tối, khách vãng lai may vẫn còn bàn. Phục vụ tận tình, lẩu ra nhanh, lên đồ cũng nhanh. Mình gọi suất 99k có cá viên bò viên, ba chỉ bò, thịt lợn, ngao, đậu, váng đậu, xúc xích, ra...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.400000,"OwnerUserName":"foodee_d9s9jwjp","OwnerFirstName":"Hiền","OwnerLastName":"Lê","OwnerFullName":"Hiền Lê","OwnerAvatar":"https://images.foody.vn/usr/g2005/20049115/avt/c50x50/beauty-upload-api-foody-avatar-723ab79f-3a4f-4453-a455-948d19f153fd-200504094741.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_d9s9jwjp","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/binh-luan-9996039"},{"Id":9399442,"RestaurantID":0,"RestaurantStatus":0,"UserID":22274735,"Title":"Safodi - Buffet Lẩu Hơi \u0026amp; Lẩu Nướng","Comment":"Với mình thì lẩu ở đây khá ngon , vị đậm đà . Chiều buồn buồn se mát thế này mà húp nước lẩu chua ngọt bên quán thì quá đã . Giá cũng hợp lí . Khá hài lòng .","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.000000,"OwnerUserName":"terrycjtroller","OwnerFirstName":"Huyen Hoa","OwnerLastName":"Nguyen","OwnerFullName":"Huyen Hoa Nguyen","OwnerAvatar":"https://images.foody.vn/usr/g2228/22274735/avt/c50x50/foody-avatar-445-637449429964270545.jpg","OwnerGender":"female","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/terrycjtroller","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/binh-luan-9399442"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":1042834,"Name":"Safodi - Buffet Lẩu Hơi \u0026 Lẩu Nướng","UrlRewriteName":"safodi-buffet-lau-hoi-lau-nuong","PicturePath":"https://images.foody.vn/res/g105/1042834/prof/s180x180/file_restaurant_photo_tbzf_16576-bf99d9bf-220712134254.jpg","PicturePathLarge":"https://images.foody.vn/res/g105/1042834/prof/s640x400/file_restaurant_photo_tbzf_16576-bf99d9bf-220712134254.jpg","MobilePicturePath":"https://images.foody.vn/res/g105/1042834/prof/s640x400/file_restaurant_photo_tbzf_16576-bf99d9bf-220712134254.jpg","DetailUrl":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"36 Phố Dịch Vọng Hậu, P. Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":34,"TotalView":8162,"TotalFavourite":25,"TotalCheckins":9,"AvgRating":"7.1","AvgRatingOriginal":7.078000,"ReviewUrl":"/ha-noi/pho-dinh-3-dich-vong-hau/binh-luan","AlbumUrl":"/ha-noi/pho-dinh-3-dich-vong-hau/album-anh","Latitude":21.0325152000000,"Longitude":105.7870686000000,"MainCategoryId":3,"PictureCount":98,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/pho-dinh-3-dich-vong-hau","BranchUrl":"/thuong-hieu/pho-dinh-3?c=ha-noi","BranchName":"Hệ thống Phở Định 3","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"34","TotalPictures":98,"TotalPicturesFormat":"98","TotalSaves":0,"Reviews":[{"Id":16123956,"RestaurantID":0,"RestaurantStatus":0,"UserID":14880419,"Title":"Qu\u0026#225; tệ anh em ạ !","Comment":"Phở định giờ ăn chán , thái độ từ nhân viên đến chủ lồi lõm ! \nHôm mình đi ăn 3 ngừoi là gần cuối canh , bánh phở cứng , nước mặn ko sắc đc như xưa ! \nĐang ăn thì chủ quán tắt điện đánh phụp như đuổi ...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":5.000000,"OwnerUserName":"billgates_2028","OwnerFirstName":"Khánh","OwnerLastName":"Nguyễn Gia","OwnerFullName":"Khánh Nguyễn Gia","OwnerAvatar":"https://images.foody.vn/usr/g1489/14880419/avt/c50x50/beauty-upload-api-foody-avatar-7f2bc26c-9b7d-411d-ad51-e8a66585c493-191122121319.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/billgates_2028","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/pho-dinh-3-dich-vong-hau/binh-luan-16123956"},{"Id":7099955,"RestaurantID":0,"RestaurantStatus":0,"UserID":1301649,"Title":"Phở Định 3 - Đồng B\u0026#244;ng","Comment":"sáng nay đi ăn phở nạm gầu, thấy quán vẫn tấp nập khách ra vào mặc kệ covid 😀 menu có nhiều lựa chọn, giá trung bình 50k, phở lõi thì 70k. còn có cả phở không thịt và phở cho trẻ em, quẩy 1 người và ...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":7.800000,"OwnerUserName":"rosecloud121","OwnerFirstName":"Mint","OwnerLastName":"Ng","OwnerFullName":"Mint Ng","OwnerAvatar":"https://images.foody.vn/usr/g131/1301649/avt/c50x50/ruka-avatar-711-637173934938683397.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/rosecloud121","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/pho-dinh-3-dich-vong-hau/binh-luan-7099955"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/pho-dinh-3-dich-vong-hau/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":29272,"Name":"Phở Định 3 - Dịch Vọng Hậu","UrlRewriteName":"pho-dinh-3-dich-vong-hau","PicturePath":"https://images.foody.vn/res/g3/29272/prof/s180x180/foody-mobile-pho-jpg-932-635917368774327730.jpg","PicturePathLarge":"https://images.foody.vn/res/g3/29272/prof/s640x400/foody-mobile-pho-jpg-932-635917368774327730.jpg","MobilePicturePath":"https://images.foody.vn/res/g3/29272/prof/s640x400/foody-mobile-pho-jpg-932-635917368774327730.jpg","DetailUrl":"/ha-noi/pho-dinh-3-dich-vong-hau","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"115 B7 Tô Hiệu, P. Nghĩa Tân","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":12,"Name":"Món Miền Nam","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-mien-nam"}],"SpecialDesc":null,"TotalReview":32,"TotalView":9671,"TotalFavourite":35,"TotalCheckins":3,"AvgRating":"7.0","AvgRatingOriginal":6.950000,"ReviewUrl":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/binh-luan","AlbumUrl":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/album-anh","Latitude":21.0438417000000,"Longitude":105.7965615000000,"MainCategoryId":3,"PictureCount":74,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"32","TotalPictures":74,"TotalPicturesFormat":"74","TotalSaves":0,"Reviews":[{"Id":6940305,"RestaurantID":0,"RestaurantStatus":0,"UserID":20196225,"Title":"B\u0026#225;nh X\u0026#232;o \u0026amp; Nem Lụi -***","Comment":"Quán hơi bị ngon nha. Giao hàng nhanh. Bánh xèo chuẩn vị, giòn, ít dầu so với quán khác. Ngon nhất vẫn là nem lụi","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":10.000000,"OwnerUserName":"foodee_om9w0plt","OwnerFirstName":"Duy","OwnerLastName":"","OwnerFullName":"Duy","OwnerAvatar":"https://images.foody.vn/default/s50/user-default-female.png","OwnerGender":"male","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_om9w0plt","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/binh-luan-6940305"},{"Id":4004457,"RestaurantID":0,"RestaurantStatus":0,"UserID":19046663,"Title":"B\u0026#225;nh X\u0026#232;o \u0026amp; Nem Lụi -***","Comment":"Ngày xưa đây là quán tủ của  mình, từ hồi nem còn 5k 1 cái, mà về sau tăng lên 6k vẫn ok, nhưng dạo gần đây mấy lát xoài cắt quá dày nên ăn ko đc ngon, đỉnh điểm lad hôm qua gọi đĩa nem ăn vừa nguội v...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":4.600000,"OwnerUserName":"foodee_fohig9fa","OwnerFirstName":"Dũng","OwnerLastName":"Thái Việt","OwnerFullName":"Dũng Thái Việt","OwnerAvatar":"https://images.foody.vn/usr/g1905/19046663/avt/c50x50/beauty-upload-api-foody-avatar-bee17315-9f84-4ab5-9c7a-04e0f40d6617-200207173213.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_fohig9fa","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/binh-luan-4004457"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":231953,"Name":"Song Nguyệt - Bánh Xèo \u0026 Nem Lụi - Tô Hiệu","UrlRewriteName":"song-nguyet-banh-xeo-nem-lui-to-hieu","PicturePath":"https://images.foody.vn/res/g24/231953/prof/s180x180/foody-mobile-34-jpg-265-635974352692854698.jpg","PicturePathLarge":"https://images.foody.vn/res/g24/231953/prof/s640x400/foody-mobile-34-jpg-265-635974352692854698.jpg","MobilePicturePath":"https://images.foody.vn/res/g24/231953/prof/s640x400/foody-mobile-34-jpg-265-635974352692854698.jpg","DetailUrl":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"36 ngõ 24  Phan Văn Trường, P.Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"},{"Id":21,"Name":"Món Nhật","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-nhat-ban"},{"Id":36,"Name":"Món Á","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-chau-a"}],"SpecialDesc":null,"TotalReview":172,"TotalView":561,"TotalFavourite":4,"TotalCheckins":0,"AvgRating":"9.6","AvgRatingOriginal":9.626000,"ReviewUrl":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/binh-luan","AlbumUrl":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/album-anh","Latitude":21.0410136000000,"Longitude":105.7875145000000,"MainCategoryId":3,"PictureCount":9,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"172","TotalPictures":9,"TotalPicturesFormat":"9","TotalSaves":0,"Reviews":[{"Id":16780209,"RestaurantID":0,"RestaurantStatus":0,"UserID":1001288,"Title":"Rất ngonnnn","Comment":"Mình đặt cho anh xã ăn mà anh khen nức nở                                      ","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.000000,"OwnerUserName":"giangxoan11112706","OwnerFirstName":"Nguyễn","OwnerLastName":"T.Giang","OwnerFullName":"Nguyễn T.Giang","OwnerAvatar":"https://images.foody.vn/usr/g101/1001288/avt/c50x50/beauty-upload-api-foody-avatar-e4ff95c4-6f91-4152-b32f-99773576b5ce-191025125259.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/giangxoan11112706","OwnerDisplayName":null,"ShortReview":true,"Url":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/binh-luan-16780209"},{"Id":16107545,"RestaurantID":0,"RestaurantStatus":0,"UserID":23299868,"Title":"Phong Th\u0026#224;nhh Qu\u0026#225;n - Qu\u0026#225;n Ăn - Phan Văn Trường","Comment":"Cơm rất ngon , sạch sẽ , làm nhanh , nước sốt rất chi là ưnggg nhé 🍗🍗🍗🍗    ","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.400000,"OwnerUserName":"Thanh_tam_pham_thi","OwnerFirstName":"Thanh Tâm Phạm Thị","OwnerLastName":"","OwnerFullName":"Thanh Tâm Phạm Thị","OwnerAvatar":"https://images.foody.vn/usr/g2330/23299868/avt/c50x50/thanh_tam_pham_thi-avatar-342-637506191180367188.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Thanh_tam_pham_thi","OwnerDisplayName":null,"ShortReview":true,"Url":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/binh-luan-16107545"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null},{"Id":28,"Name":"Giao cơm văn phòng","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":1000027868,"Name":"Phong Thànhh Quán - Quán Ăn - Phan Văn Trường","UrlRewriteName":"phong-thanhh-quan-quan-an-phan-van-truong.glrxgp","PicturePath":"https://images.foody.vn/res/g100003/1000027868/prof/s180x180/file_restaurant_photo_ykxn_16254-2fdda806-210705174327.jpeg","PicturePathLarge":"https://images.foody.vn/res/g100003/1000027868/prof/s640x400/file_restaurant_photo_ykxn_16254-2fdda806-210705174327.jpeg","MobilePicturePath":"https://images.foody.vn/res/g100003/1000027868/prof/s640x400/file_restaurant_photo_ykxn_16254-2fdda806-210705174327.jpeg","DetailUrl":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]}],"adItems":[],"totalResult":2455,"currentPage":4,"locationQuery":null,"maxPageToLoad":5,"brand":"","providerList":[],"book":false,"totalSubItems":59,"documentSource":"Restaurant","listResultCount":93042,"restaurantResultCount":2514,"userResultCount":7330050,"articleResultCount":4395,"pictureResultCount":20947};"""








b = r"""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:fb="http://www.facebook.com/2008/fbml">

<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>Địa điểm Quán ăn phong cách Món Việt tại Quận Cầu Giấy, Hà Nội | Foody.vn</title>

	<meta http-equiv="Content-type" content="text/html;charset=UTF-8" />
	<meta name="description"
		content="Danh sách > 2514 địa điểm Quán ăn phong cách Món Việt tại Quận Cầu Giấy, Hà Nội. Foody.vn là website #1 tại VN về tìm kiếm địa điểm, có hàng ngàn bình luận, hình ảnh" />
	<meta name="keywords"
		content="Foody.vn là nơi chia sẻ và đánh giá địa điểm, với hàng ngàn địa điểm về ẩm thực, giải trí cùng hàng ngàn bình luận. Tham gia để chia sẻ trải nghiệm với cộng đồng" />

	<meta name="apple-itunes-app" content="app-id=1218739449">
	<link rel="manifest" href="/manifest.json">



	<meta name="robots" content="index, follow" />



	<meta name="msvalidate.01" content="9F288B3B53D32225CE6A70FA2DB2BF6D" />

	<link rel="SHORTCUT ICON" href="/favicon.ico" />

	<meta property="og:title" content="Địa điểm Quán ăn phong cách Món Việt tại Quận Cầu Giấy, Hà Nội" />
	<meta property="og:description"
		content="Danh sách > 2514 địa điểm Quán ăn phong cách Món Việt tại Quận Cầu Giấy, Hà Nội. Foody.vn là website #1 tại VN về tìm kiếm địa điểm, có hàng ngàn bình luận, hình ảnh" />
	<meta property="og:type" content="foodyvn:restaurant" />
	<meta property="og:url" content="" />
	<meta property="og:site_name" content="Foody" />
	<meta property="fb:app_id" content="395614663835338" />
	<meta property="og:image" content="" />
	<meta property="og:image:url" content="" />


	<meta property="og:title" content="Địa điểm Quán ăn phong cách Món Việt tại Quận Cầu Giấy, Hà Nội | Foody.vn" />
	<meta property="og:image" content="/style/images/logofoody.jpg" />
	<meta property="fb:app_id" content="395614663835338" />
	<meta property="og:description"
		content="Danh sách > 2514 địa điểm Quán ăn phong cách Món Việt tại Quận Cầu Giấy, Hà Nội. Foody.vn là website #1 tại VN về tìm kiếm địa điểm, có hàng ngàn bình luận, hình ảnh" />
	<meta property="og:type" content="website" />
	<meta property="og:url"
		content="http://www.foody.vn/ha-noi/quan-an-phong-cach-viet-nam-tai-quan-cau-giay?c=quan-an&amp;categorygroup=food&amp;page=4&amp;append=True" />
	<meta property="og:site_name" content="Foody" />



	<link rel="canonical"
		href="https://www.foody.vn/ha-noi/quan-an-phong-cach-viet-nam-tai-quan-cau-giay?cquan-an&categorygroupfood&page4&appendtrue" />





	<link href="/style/css/public.main.new.min.css?6b6fe8" rel="stylesheet" />





	<script type="text/javascript">
		var staticPath = '/';
    var province = 'ha-noi';
    var provinceId = '218';
    var fbAppId = '395614663835338';
    var defaultLatgitude = '21.033333' * 1;
    var defaultLongitude = '105.850000' * 1;
    var logoutUrl='/dang-xuat';
    var globalLanguages = {
        Comment_User_Like_Empty: 'Chưa có thành viên nào',
        Comment_User_DisLike_Empty: 'Chưa có ai không thích'
    }

    var ssoUrl = 'https://id.foody.vn/account/login';
    var defaultUrl = '';
    var ssoEnable = true;
    var ssoDomainAuthorize = ssoUrl + 'Account/SocialAuthLogin?provider=';
    var defualtDomainAuthorize = '/Account/SocialAuthLogin?provider=';
    var CONST_MEDIA_UPLOAD_URL = "https://images.foody.vn/";
    var CountryId = '86';
    var LanguageId = '1';
    var IsIndo = CountryId == '42' ? true : false;
    var CONST_MEDIA_XUSER_TOKEN = '';

    var NowPythonSetting = {
        ApiHost:'https://gappapi.deliverynow.vn/',
        AuthenHost: 'https://gsso.deliverynow.vn/',
        SecrectKey: 'a3f713fe2494ded5c1e609db3fc9e72c59724443e410006ef224c8adcffce0e0'
    }
    var TableNowSetting = {
        Host: 'https://gappapi.tablenow.vn',
        WebHost: 'https://shopeefood.vn',
        WebHostUrl: 'table',
        ConfigUrl: '',
        Version: 1,
        AppType: 2000,
        ClientType: 1,
        ApiVersion: 1,
        ClientLanguage: 'vn'
    }
	</script>

	<script>
		var routeConfig = {};
    routeConfig.defaultCategory = 'dia-diem';
    routeConfig.microsite = {
        reviewPath: 'binh-luan',
        prPath: 'quang-cao',
        qaPath: 'hoi-dap',
        albumPath: 'album-anh',
        menuPath: 'thuc-don',
        checkinPath: 'check-in'
    };
    routeConfig.account = {
        loginUrl: '/dang-nhap',
        logoutUrl: '/dang-xuat?returnUrl=%2F',
        lookedAccount: '/khoa-tai-khoan'
    }
    window.ReviewLanguages = {
        Common_You_Have: 'Bạn có',
        Common_Points: 'điểm',
        Review_You_Lose: 'Bạn bị trừ',
        Redeem_OrderStatus_Pending: 'Chờ duyệt'
    };
    routeConfig.micrositeUrlTemplate = '/_LOCATION_/_URL_REWRITE_';
    routeConfig.micrositeReviewUrlTemplate = '/_LOCATION_/_URL_REWRITE_/binh-luan';
	</script>





	<script src="/scripts/public.resources.min.js?6b6fe8" type="text/javascript"></script>
	<script src="/scripts/public.core.new.min.js?6b6fe8" type="text/javascript"></script>
	<script src="/scripts/public.foody.min.js?6b6fe8" type="text/javascript"></script>
	<script src="/scripts/public.account.update.profile.min.js?6b6fe8" type="text/javascript"></script>
	<script src="/scripts/wishlist/public.foody.wishlist.context.min.js?6b6fe8" type="text/javascript"></script>

	<script src="/scripts/public.angular.min.js?6b6fe8" type="text/javascript"></script>

	<script src="/scripts/public.angular.core.min.js?6b6fe8" type="text/javascript"></script>




	<link href="/style/css/public.place.min.css?6b6fe8" rel="stylesheet" />
	<link href="/style/css/public.search.min.css?6b6fe8" rel="stylesheet" />
	<link href="/style/css/preload.css" rel="stylesheet" />




	<!-- Google Tag Manager -->
	<script>
		(function (w, d, s, l, i) {
            w[l] = w[l] || []; w[l].push({
                'gtm.start':
                    new Date().getTime(), event: 'gtm.js'
            }); var f = d.getElementsByTagName(s)[0],
                j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : ''; j.async = true; j.src =
                    'https://www.googletagmanager.com/gtm.js?id=' + i + dl; f.parentNode.insertBefore(j, f);
        })(window, document, 'script', 'dataLayer', 'GTM-5FMV7KK');
	</script>
	<!-- End Google Tag Manager -->



	<!-- foody 2 -->


	<script>
		(function (i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
            (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date(); a = s.createElement(o),
        m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
    })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-33292184-1', 'auto');
    ga('create', 'UA-33292184-1', { 'name': 'ads' });

    
    ga('send', 'pageview');
    //ga('sr.send', 'pageview');
	</script>



	<!-- Facebook Pixel Code -->
	<script>
		!function (f, b, e, v, n, t, s) {
            if (f.fbq) return; n = f.fbq = function () {
                n.callMethod ?
                n.callMethod.apply(n, arguments) : n.queue.push(arguments)
            }; if (!f._fbq) f._fbq = n;
            n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = []; t = b.createElement(e); t.async = !0;
            t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s)
        }(window,
        document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');

        fbq('init', '869522799763514');
        fbq('track', "PageView");
        fbq('track', "ViewContent");
	</script>
	<noscript>
		<img height="1" width="1" style="display:none"
                 src="https://www.facebook.com/tr?id=869522799763514&ev=PageView&noscript=1" />
        </noscript>
		<!-- End Facebook Pixel Code -->

</head>

<body itemscope itemtype="http://schema.org/WebPage">
	<!-- Google Tag Manager (noscript) -->
	<noscript>
		<iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5FMV7KK" height="0" width="0"
			style="display:none;visibility:hidden"></iframe>
	</noscript>
	<!-- End Google Tag Manager (noscript) -->


	<script type="application/ld+json">
		{
    "@context" : "https://schema.org",
    "@type" : "Website",
    "name" : "Foody",
    "alternateName": "Foody Vietnam",
    "url" : "https://www.foody.vn",
    "sameAs" : [ "https://www.facebook.com/FoodyVietnam","https://twitter.com/foodyvn","https://plus.google.com/+FoodyVn","https://www.instagram.com/foodysaigon"]
    
    }
	</script>
	<div id="fb-root"></div>


	<div id="FoodyApp" ng-app="FoodyApp">



		<header class="header">





			<script>
				$(function () {
            $('.rootcategory-right').width($('.rootcategory-menu').width() - $('.nearby-button').width() - $('.dropdown1').width() - 630);
            

            if ($("#pkeywords").val().length == 0) {
                $('#pkeywords').addClass('watermark');
            } else {
                $('#pkeywords').removeClass('watermark');
            }
            $("#pkeywords").watermark('Địa điểm, món ăn, loại hình...', {
                useNative: true,
                className: 'watermark'
            })
                .focus(function () {
                    if ($(this).val().length == 0)
                        $(this).addClass('watermark');
                    else
                        $(this).removeClass('watermark');
                })
                .keyup(function () {
                    if ($(this).val().length == 0)
                        $(this).addClass('watermark');
                    else
                        $(this).removeClass('watermark');
                })
                .blur(function () {
                    if ($(this).val().length == 0)
                        $(this).addClass('watermark');
                    else
                        $(this).removeClass('watermark');
                });
        })
			</script>
			<div class="container-topbar">
				<div class="topbar">
					<a href="https://www.foody.vn" class="current" rel="home">Khám Phá</a>

					<a href="https://shopeefood.vn?utm_source=FoodyWeb&utm_medium=topbar_link_click&utm_campaign=FoodyRef"
						target="_blank" rel="nofollow">Đặt Giao Hàng</a>
					<a href="https://shopeefood.vn/ha-noi/fresh?utm_source=FoodyWeb&utm_medium=topbar_link_click&utm_campaign=FoodyRef"
						style="position:relative" target="_blank" rel="nofollow">Đi chợ
						<img style="position: absolute;top: 0px;right: -5px;border-radius: 7px;" src="/style/css/strongbow/images/sb-new.gif" /></a>





				</div>
			</div>
			<div class="header-toolbar">
				<div class="foody-wapper">
					<a href="/" class="logo foody-logo" rel="home" alt="foody-logo">
						<img src="/style/images/logo/foody-vn.png" alt="Foody.vn" />
            </a>
						<div class="root-cate" id="head-province" ng-controller="LocationCtrl"
							ng-init="Init({Name:'H&#224; Nội',Id:'218'})" ng-class="{'fl-show':IsShow}">
							<div class="rn-nav-name" ng-click="Show()">
								<span style="white-space: nowrap;overflow: hidden;text-overflow: ellipsis;max-width: 85px;">H&#224; Nội</span>
								<span class="fa fa-sort-desc"></span>
							</div>
							<div id="popupLocation" class="foody-location" ng-class="{'fl-loading':IsLoading}"
								style="display:none;">
								<div class="arrow"></div>
								<ul class="fl-panel">
									<li ng-if="Model.TopCities.length>0 || Model.OtherCities.length>0">
										<div class="flp-title">
											<i class="fa fa-globe"></i>
											Tỉnh thành
										</div>
										<div class="loc-contain">
											<div class="fa fa-search loc-search"></div>
											<input type="text" class="loc-query" placeholder="Tìm tỉnh thành" ng-model="Query" ng-change="FilterLocation(Query)"/>
            </div>
											<ul class="flp-countries" ng-if="Query">
												<li>
													<ul>
														<li ng-repeat="item in Locations">
															<a data-id="{{item.Id}}" href="{{item.Url}}">
																<label>{{item.DisplayName}}</label>
																<span>{{item.RestaurantCount|formatN}}</span>
															</a>
														</li>
													</ul>
												</li>
											</ul>
											<ul class="flp-countries" ng-if="!Query">
												<li ng-if="Model.TopCities.length>0">
													<ul>
														<li ng-repeat="item in Model.TopCities">
															<a data-id="{{item.Id}}" href="{{item.Url}}">
																<label>{{item.DisplayName}}</label>
																<span>{{item.RestaurantCount|formatN}}</span>
															</a>
														</li>
													</ul>
												</li>
												<li ng-if="Model.OtherCities.length>0">
													<label>Tỉnh thành khác</label>
													<ul>
														<li ng-repeat="item in Model.OtherCities">
															<a data-id="{{item.Id}}" href="{{item.Url}}">
																<label>{{item.DisplayName}}</label>
																<span>{{item.RestaurantCount|formatN}}</span>
															</a>
														</li>
													</ul>
												</li>
												<li ng-if="Model.WorldWideCountries.length>0"
													ng-repeat="item in Model.WorldWideCountries">
													<label data-id="{{item.Id}}">{{item.Name}}</label>
													<ul>
														<li ng-repeat="c in item.Cities">
															<a data-id="{{c.Id}}" href="{{c.Url}}">
																<label>{{c.DisplayName}}</label>
																<span>{{c.RestaurantCount|formatN}}</span>
															</a>
														</li>
													</ul>
												</li>
											</ul>
									</li>
								</ul>
								<div class="fl-summary"
									ng-show="Model.TopCities.length>0 || Model.OtherCities.length>0">

									<a href="/ha-noi/o-dau" title="{{Model.FoodyStat.TotalRes|formatN}}">
										<i class="fa fa-map-marker"></i>
										<span>{{Model.FoodyStat.TotalRes|formatNK}}</span>
									</a>

									<a href="/ha-noi/quan-an/binh-luan"
										title="{{Model.FoodyStat.TotalReviews|formatN}}">
										<i class="fa fa-comment"></i>
										<span>{{Model.FoodyStat.TotalReviews|formatNK}}</span>
									</a>

									<a href="/ha-noi/hinh-anh" title="{{Model.FoodyStat.TotalPics|formatN}}">
										<i class="fa fa-camera"></i>
										<span>{{Model.FoodyStat.TotalPics|formatNK}}</span>
									</a>
									<a href="/ha-noi/bo-suu-tap" title="{{Model.FoodyStat.TotalLists|formatN}}">
										<i class="fa fa-bookmark"></i>
										<span>{{Model.FoodyStat.TotalLists|formatNK}}</span>
									</a>
								</div>
							</div>


						</div>
						<div class="root-cate" id="head-navigation">

							<div class="rn-nav-name">
								<span data-value="1">Ăn uống</span> <span class="fa fa-sort-desc"></span>
							</div>

							<script>
								$('#head-navigation').on('click', function () {
                            if ($('#head-navigation .menu-frame-category').length == 0) {
                                $('#head-navigation').load('/common/_TopCategoryGroupMenu?isUseForSearch=true', function () {
                                    $('#head-navigation .menu-frame-category').show();
                                });
                                return;
                            }
                            $('#head-navigation .menu-frame-category').toggle();
                        });
							</script>
						</div>

						<div class="search-bar-top" id="FoodySearchApp" ng-controller="DlgSearchFilterCtrl"
							ng-init="Init({CityId:'218',Url:'/ha-noi/dia-diem'})">
							<form id="searchFormTop" action="/ha-noi/quan-an" method="get">
								<div
									style="float: left;position: relative;border: 1px solid #eee;border-right:none; width: 415px;box-sizing: border-box;">
									<input ng-model="Filter.Keyword" ng-change="LoadCategory()" style="vertical-align: middle" name="q" type="text" id="pkeywords" data-autocomplete-type="keywords" data-autocomplete-url="/__get/AutoComplete/Keywords?provinceId=218" data-autocomplete-minlength="2" />


									<a href="javascript:void(0)" class="ico-nofilter" ng-click="Show()"
										ng-class="{'ico-filter':FilterCount>0}" style="padding: 6px 10px 0 0;">
										<div ng-class="{'fa-sliders':FilterCount==0,'filtercount':FilterCount>0}"
											ng-cloak class="fa">
											<div ng-if="FilterCount>0" class="count">{{FilterCount}}</div>
										</div>
										Bộ lọc
									</a>
									<input type="hidden" name="ss" value="header_search_form" />



									<script type="text/javascript">
										var searchBoxDropdown = new DropDownCategoryHelper3();

    $(function () {
        searchBoxDropdown.Init({
            btnCategory: $("#pkeywords")[0],
            category: $(".search-bar-top .suggestion-box")[0],
            clickBtnToClose: false
        });
        var keywords = $.cookie('fd.sk');
        if (keywords) {
            var buff = keywords.split('#');

            for (var i = 0; i < 2 ; i++) {
                if (buff[i]) {
                    var ele = '<li><a href="/ha-noi/quan-an?q=' + buff[i].replace('<s', '< s').replace('<S', '< S') + '" class="suggestion-box-item"><span style="float:left;padding-right:5px;color:#666" class="fa fa-search"></span>' +
                                                  buff[i].replace('<s', '< s').replace('<S', '< S') + '<span class="fa fa-angle-right" style="font-size: 14px;"></span>' +
                                            '</a></li>'
                    $('.sb-list-items').append($(ele));
                }

            }

        }
        //$("#pkeywords").on("input", function () {
        //    //$(".search-bar-top .suggestion-box").hide();
        //});

    });
									</script>
									<div class="suggestion-box">


										<!-- res ads -->

										<!-- banner -->

										<div
											style="padding: 5px 10px;font-size: 11px; color: #aaa;background: #FCFCFC;border-bottom: #eee 1px solid;">
											Từ khoá đã tìm</div>

										<ul class="sb-list-items">


											<!-- normal -->

										</ul>
									</div>

								</div>
							</form>

							<a class="ico-search" onclick="$('#searchFormTop').submit()">
								<span class="fa fa-search"></span>
							</a>
							<div bind-unsafe-html="Html">

							</div>
						</div>
						<div class="menu-header">

							<ul class="nav-place-menu">
								<li>
									<a href="javascript:void(0)">
										<span class="fa fa-bars"></span>
									</a>

									<div class="menu-frame">
										<div class="arrow"></div>
										<ul class="menu-box" style="display: block">
											<li>
												<a href="/ha-noi/o-dau" title="Ở đ&#226;u">
													<span>Ở đ&#226;u</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi#/delivery" title="Giao h&#224;ng">
													<span>Giao h&#224;ng</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/hinh-anh" title="Ăn g&#236;">
													<span>Ăn g&#236;</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/bo-suu-tap" title="Sưu tập">
													<span>Sưu tập</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/bo-suu-tap-hinh-anh" title="Bộ sưu tập h&#236;nh ảnh">
													<span>Bộ sưu tập h&#236;nh ảnh</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/coupon" title="Coupons">
													<span>Coupons</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/video" title="TV">
													<span>TV</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/binh-luan" title="B&#236;nh luận">
													<span>B&#236;nh luận</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/food/bai-viet" title="Blogs">
													<span>Blogs</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/khuyen-mai" title="Khuyến m&#227;i">
													<span>Khuyến m&#227;i</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/su-kien" title="Miễn ph&#237;">
													<span>Miễn ph&#237;</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/top-thanh-vien" title="Top th&#224;nh vi&#234;n">
													<span>Top th&#224;nh vi&#234;n</span>
												</a>

											</li>
										</ul>
									</div>
								</li>

							</ul>


						</div>
						<div class="header-apps test">
							<a href="/ung-dung-mobile" target="_blank"><span class="fa fa-mobile"></span>&nbsp;Apps</a>
						</div>
						<div class="nav-place" ng-controller="MenuLoginCtrl">
							<div class="account-manage" id="accountmanager">
								<a class="fd-btn-login-new" ng-click="Login()" ng-class="{'loading':IsLoading}">
									<span>Đăng nhập</span>
								</a>




								<div id="update-profile-popup" style="display: none">
								</div>
								<div id="update-profile-popup-loading" style="display: none">
									Loading...
								</div>
								<div id="loginPopup" style="display: none">
									<div id="loginPopupPH" style="text-align:center; line-height:30px;">
										<img style="display:inline" src="/style/images/icons/ajax-loader.gif">
    </div>
									</div>
									<div id="loginFacebookPopup" style="display: none">Loading...</div>

									<input type="hidden" id="encryptedlogin" />


                </div>
									<div id="NotificationCtrl" style="position: relative; float: left;"
										ng-controller="NotificationCtrl" ng-init="Init('')">
										<div class="" style="float: right;">
											<div class="notificationBox" ng-cloak>
												<div ng-click="Show()"
													ng-class="SummaryTotalUnread()>0?'notification-new-none notification-new-have':'notification-new-none'">
													{{SummaryTotalUnread()}}
												</div>
												<div class="notificationsFlyout" ng-show="IsShow">
													<span class="arrow"></span>
													<div style="display: block">
														<div>
															<div class="notify-header">
																<ul class="tabs">
																	<li ng-class="{'show-news':IsShowNews}">
																		<a style="border-radius: 3px 0px 0px 3px;"
																			href="javascript:void(0)"
																			ng-click="TabClick(1)"
																			ng-class="{'active':ActiveTab==1}">
																			Dịch vụ
																			<span style="color: #fff;background: #cc0000;border-radius: 10px;font-size:11px;padding: 2px 6px;text-align: center;" ng-show="SummaryOrder>0">{{SummaryOrder}}</span>
																		</a>
																	</li>
																	<li ng-class="{'show-news':IsShowNews}">
																		<a style="border-radius: 0px 3px 3px 0px; border-left: #ccc 1px solid;"
																			href="javascript:void(0)"
																			ng-click="TabClick(2)"
																			ng-class="{'active':ActiveTab==2}">
																			Của tôi
																			<span style="color: #fff;background: #cc0000;border-radius: 10px;font-size:11px;padding: 2px 6px;text-align: center;" ng-show="SummarySocial>0">{{SummarySocial}}</span>
																		</a>
																	</li>
																	<li ng-show="IsShowNews"
																		ng-class="{'show-news':IsShowNews}">
																		<a style="border-radius: 0px 3px 3px 0px; border-left: #ccc 1px solid;"
																			href="javascript:void(0)"
																			ng-click="TabClick(3)"
																			ng-class="{'active':ActiveTab==3}">
																			Tin mới
																			<span style="color: #fff;background: #cc0000;border-radius: 10px;font-size:11px;padding: 2px 6px;text-align: center;" ng-show="SummaryNews>0">{{SummaryNews}}</span>
																		</a>
																	</li>
																</ul>
															</div>
															<div class="clear"></div>
															<div class="notifications-box tab-idx-1" id="tab-order"
																ng-show="ActiveTab==1">
																<div ng-show="!IsLoginRequire">
																	<a ng-repeat="item in ListOrder.Items "
																		href="{{item.Url ? item.Url : 'javascript:void(0)' }}">
																		<div class="notification-message-item"
																			ng-class="{'new-notification': Unread}">
																			<div style="float: left; text-align: left;">
																				<div
																					class="notification-message-item-avatar">
																					<img ng-src="{{item.RepresentImg}}" style="border-radius:unset"/>
                                    </div>
																					<div
																						class="notification-message-content">
																						<div
																							ng-bind-html="item.Content">
																						</div>
																						<div>
																							<!-- Tablenow, type 20: cancel -->
																							<div ng-if="item.ObjectType==42 && item.ActionType!=20"
																								class="notification-icon tablenow-icon">
																							</div>
																							<!-- Delivery, type 20: cancel -->
																							<div ng-if="item.ObjectType==44 && item.ActionType!=20"
																								class="notification-icon delivery-icon">
																							</div>
																							<!-- follow -->
																							<span ng-if="item.ActionType==20" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-times-circle" style="color: #cc0000;font-size: 16px;"></span>
																							</span>
																							<span class="notification-posted-time" style="float:left" utime="{{item.DateStamp}}" title="{{item.DateString}}">{{item.DateDisplay}}</span>
																						</div>
																					</div>
																				</div>
																				<div class="clear"></div>
																			</div>
																	</a>
																</div>
																<div class="notification-message-item item-msg"
																	ng-show="ListOrder.Items.length==0 && IsInit && !IsLoginRequire">
																	Chưa có thông báo!
																</div>
																<div class="notification-message-item item-msg"
																	ng-show="IsLoginRequire" ng-click="Login()">
																	<span class="fa fa-lock"></span>
																	Đăng nhập để xem
																</div>
																<div style="text-align: center"
																	class="notification-message-item"
																	ng-show="ListOrder.Total - ListOrder.Items.length>0">
																	<img class="loading" src="/style/images/icons/ajax-loader.gif" ng-show="ListOrder.IsLoading" />
                        Xem thêm
                    </div>
																</div>
																<div class="notifications-box tab-idx-2" id="tab-social"
																	ng-show="ActiveTab==2">
																	<div ng-show="!IsLoginRequire">
																		<a ng-repeat="item in ListSocial.Items"
																			href="{{item.Url ? item.Url : 'javascript:void(0)' }}"
																			target="{{item.Target}}"
																			ng-show="item.Content.length > 0">
																			<div class="notification-message-item"
																				ng-class="{'new-notification': Unread}">
																				<div
																					style="float: left; text-align: left;">
																					<div
																						class="notification-message-item-avatar">
																						<img ng-src="{{item.RepresentImg}}" />
                                    </div>
																						<div
																							class="notification-message-content">
																							<div
																								ng-bind-html="item.Content">
																							</div>
																							<div>
																								<span ng-if="item.ActionType==5" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-user"></span>
																								</span>
																								<span ng-if="item.ActionType==2" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-comment" style="color: #009a59"></span>
																								</span>
																								<span ng-if="item.ActionType==1" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-thumbs-up" style="color: #3b5998"></span>
																								</span>
																								<!-- follow -->
																								<span ng-if="item.ActionType==10" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-bookmark" style="color: #cc0000"></span>
																								</span>
																								<!-- follow -->
																								<!-- follow User-->
																								<span ng-if="item.ActionType==17" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-plus" style="color: #cc0000"></span>
																								</span>
																								<!-- follow -->
																								<!-- update list -->
																								<span ng-if="item.ActionType==12" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-check-circle" style="color: #03ae03"></span>
																								</span>
																								<!-- update list -->
																								<!-- using foody -->
																								<span ng-if="item.ActionType==14" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-facebook-square" style="color: #3b5998"></span>
																								</span>
																								<!-- using foody -->
																								<span ng-if="item.ActionType==15" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-check-circle" style="color: #03ae03"></span>
																								</span>
																								<span ng-if="item.ActionType==18 || item.ActionType==27" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-list" style="color: #ce8b0d"></span>
																								</span>
																								<span ng-if="item.ActionType==33" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-tag" style="color: #1b95e0"></span>
																								</span>
																								<span ng-if="item.ActionType==34" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-tag" style="color: #1b95e0"></span>
																								</span>

																								<span class="notification-posted-time" utime="{{item.DateStamp}}" title="{{item.DateString}}">{{item.DateDisplay}}</span>
																							</div>
																						</div>

																					</div>
																					<div class="clear"></div>
																				</div>
																		</a>
																	</div>

																	<div class="notification-message-item item-msg"
																		ng-show="ListSocial.Items.length==0 && IsInit && !IsLoginRequire">
																		Chưa có thông báo!
																	</div>
																	<div class="notification-message-item item-msg"
																		ng-show="IsLoginRequire" ng-click="Login()">
																		<span class="fa fa-lock"></span>
																		Đăng nhập để xem
																	</div>
																	<div style="text-align: center"
																		class="notification-message-item"
																		ng-show="ListSocial.Total>ListSocial.Items.length">
																		<img class="loading" src="/style/images/icons/ajax-loader.gif" ng-show="IsInit" />
                            Xem thêm
                        </div>
																	</div>
																	<div class="notifications-box tab-idx-3"
																		id="tab-news" ng-show="ActiveTab==3">

																		<a ng-repeat="item in ListNews.Items "
																			href="{{item.Url ? item.Url : 'javascript:void(0)' }}">
																			<div class="notification-message-item"
																				ng-class="{'new-notification': Unread}">
																				<div
																					style="float: left; text-align: left;">
																					<div
																						class="notification-message-item-avatar">
																						<img ng-src="{{item.RepresentImg}}" />
                                    </div>
																						<div
																							class="notification-message-content">
																							<div>
																								<span style="font-weight: bold; color: #333;">{{item.Title}}</span>
																							</div>
																							<div class="notification-message-text"
																								ng-bind-html="item.Message">
																							</div>
																							<div>

																								<span class="notification-posted-time" utime="{{item.DateTimestamp}}" title="{{item.DateString}}">{{item.DateDisplay}}</span>
																							</div>
																						</div>

																					</div>
																					<div class="clear"></div>
																				</div>
																		</a>
																		<div class="notification-message-item item-msg"
																			ng-show="ListNews.Items.length==0 && IsInit && !IsLoginRequire">
																			Chưa có thông báo!
																		</div>
																		<div style="text-align: center"
																			class="notification-message-item"
																			ng-show="ListNews.Total - ListNews.Items.length>0">
																			<img class="loading" src="/style/images/icons/ajax-loader.gif" ng-show="ListNews.IsLoading" />
                        Xem thêm
                    </div>
																		</div>
																		<div class="notification-message-item item-msg"
																			ng-show="!IsInit">
																			<img class="loading" src="/style/images/icons/ajax-loader.gif" />
                    Đang tải
                </div>
																		</div>

																	</div>
																</div>
															</div>


														</div>

													</div>



													<div class="nav-add-buttons">
														<a>+</a>
														<div id="add-buttons">
															<span class="arrow" style="left: 257px;"></span>
															<ul>
																<li
																	style="padding: 8px 15px 6px 15px; border-bottom: #ddd 1px solid;">
																	Bạn có thể</li>

																<li>
																	<a href="javascript:void(0)"
																		ng-click="ActionUrl('/them-dia-diem')">
																		<span class="fa fa-map-marker icons" style="font-size: 26px;"></span>
																		<span class="add-buttons-text">
                                        <span class="text-main">Tạo địa điểm</span><br />
																		<span class="text-desc">Sẽ được duyệt trong vòng 48 tiếng</span>
																		</span>
																	</a>
																</li>
																<li>
																	<a href="javascript:void(0)"
																		class="add-new-reviews">
																		<span class="fa fa-comment icons"></span>
																		<span class="add-buttons-text">
                                        <span class="text-main">Viết bình luận</span><br />
																		<span class="text-desc">Để chia sẻ trải nghiệm cho cộng đồng</span>
																		</span>
																	</a>
																</li>
																<li>
																	<a href="javascript:void(0)" class="add-new-list">
																		<span class="fa fa-bars icons"></span>
																		<span class="add-buttons-text">
                                        <span class="text-main">Tạo bộ sưu tập</span><br />
																		<span class="text-desc">Để lưu trữ địa điểm của bạn</span>
																		</span>

																	</a>
																</li>

																<li>
																	<a href="javascript:void(0)"
																		ng-click="ActionUrl('/gop-y')"
																		class="add-feedback">
																		<span class="fa fa-thumbs-down icons"></span>
																		<span class="add-buttons-text">
                                        <span class="text-main">Góp ý</span><br />
																		<span class="text-desc">Để phục vụ bạn tốt hơn</span>
																		</span>

																	</a>
																</li>
															</ul>
														</div>
													</div>
													<div class="language-dropdown-container">
														<a href="javascript:void(0);" class="language-dropdown-btn">
															<img src="/style/images/icons/lang/vn.png"  style="float:left;"/>
        </a>

															<div class="language-dropdown-list" style="display: none;">

																<a onclick="return changeLanguage('en')" rel="nofollow"
																	href="/__get/common/changelanguage?code=en&amp;returnUrl=http%3A%2F%2Fwww.foody.vn%2Fha-noi%2Fquan-an-phong-cach-viet-nam-tai-quan-cau-giay%3Fc%3Dquan-an%26categorygroup%3Dfood%26page%3D4%26append%3DTrue"
																	title="en">
																	<img src="/style/images/icons/lang/us.png" alt="en" title="en" style="float:left;"/>
																	<span style="float:left; line-height:21px; padding-left:4px;font-size:12px; font-weight:normal; text-transform:uppercase;">en</span>
																</a>
																<div class="clear"></div>
															</div>
													</div>
													<script type="text/javascript">
														function changeLanguage(code) {
            var languageUrl = '/__get/common/changelanguage';
            languageUrl = languageUrl + '?code=' + code + '&returnUrl' + location.href;
            location.href = languageUrl;

            return false;
        }

        var languageDropdown = new DropDownCategoryHelper3();

        $(function () {
            languageDropdown.Init({
                btnCategory: $(".language-dropdown-container .language-dropdown-btn")[0],
                category: $(".language-dropdown-container .language-dropdown-list")[0]
            });
        });
													</script>

												</div>

											</div>
										</div>
		</header>

		<div class="t_clear" style="display: none"></div>



		<script type="text/javascript">
			$(function () {
        // top search form
        $("#searchFormTop input[data-autocomplete-url]").foodyAutocomplete({
            offsetTop: 0,
            offsetLeft: 0,
            offsetWidth: 250,
            minLength: 1,
            showImg: true,
            showAddress: true,
            goDetailsOnSelect: true,
            viewMoreLinkText: 'Xem thêm',
            detailsLinkText: 'Chi tiết',
            allResultLinkText: 'Xem tất cả kết quả',
            closedLinkText: 'Đóng cửa',
            onItemSelected: function (data, event) {
                $('#searchFormTop').submit();
            }
        });
    });
		</script>








		<!-- Start Banner Ads -->



		<script type="text/javascript">
			$(function () {
        if ($("#catfish-banner").find("div").length > 0) {
            if ($.cookie("hideCatfishBanner")=="true") {
                $("#catfish-banner").hide();
            }
            else {
                $("#catfish-banner").css("opacity", "1");
                $("#catfish-banner").css("overflow", "inherit");
            }

            $(".catfish-banner-btn").live("click", function () {
                $("#catfish-banner").hide();
                //var date = new Date();
                //var days = 1;
                //date.setTime(date.getTime() + (days*24*60*60* 1000));
                //$.cookie("hideCatfishBanner", true, { expires: date });
                //$.cookie("hideCatfishBanner", true);
                $.cookie('hideCatfishBanner', true, { path: '/' });
            });
        }
    });
		</script>
		<!-- End Banner Ads -->



		<script src="/scripts/infobox.js"></script>
		<link href="/style/css/video.css" rel="stylesheet" />
		<link href="/style/css/micro.css" rel="stylesheet" />
		<script type="text/javascript">
			if(window.fbq)
        window.fbq('track', 'Search');
		</script>

		<!--Start of Main section -->

		<section class="search-page directory-page" id="directorypage">
			<div id="GalleryPopupApp" ng-controller="GalleryPopupController">
				<div class="fd-popup" id="search-filter-poup">
					<div class="fd-popup-frame">
						<div class="dlgc-btn-close"></div>
						<div class="dlgc-title">
							<span>Bộ lọc nâng cao</span>
						</div>
						<div class="dlgc-content-frame">
							<div class="dlgcf-content">
								<div id="float-filter-container" class="pn-filter"
									data-bind="if: true, style: { display: 'block' }" style="display: none;">
									<div id="float-filter">
										<ul class="filter-tab">
											<li>
												<a class="header-text"
													data-bind="css: { 'act': currentShownFilter() == 'category' }, click: function () { showFilter('category') }"
													href="#filter-category">
													<span class="fa fa-bars" style="padding-right:8px;padding-top:1px;"></span>
													<span>Phân loại</span>
													<span style="float: right;font-weight: normal;font-size: 16px;color: #999;padding-right: 5px;" class="fa fa-angle-right"></span>
												</a>
											</li>
											<li>
												<a class="header-text"
													data-bind="css: { 'act': currentShownFilter() == 'area' }, click: function () { showFilter('area') }"
													href="#filter-area">
													<span class="fa fa-location-arrow" style="padding-right:8px;padding-top:1px;"></span>
													<span>Khu vực</span>
													<span style="float: right;font-weight: normal;font-size: 16px;color: #999;padding-right: 5px;" class="fa fa-angle-right"></span>
												</a>
											</li>
											<li>
												<a class="header-text"
													data-bind="css: { 'act': currentShownFilter() == 'purpose' }, click: function () { showFilter('purpose') }"
													href="#filter-purpose">
													<span class="fa fa-thumbs-up" style="padding-right:8px;padding-top:1px;"></span>
													<span>Mục đích</span>
													<span style="float: right;font-weight: normal;font-size: 16px;color: #999;padding-right: 5px;" class="fa fa-angle-right"></span>
												</a>
											</li>
											<li>
												<a class="header-text"
													data-bind="css: { 'act': currentShownFilter() == 'cuisine' }, click: function () { showFilter('cuisine') }"
													href="#filter-cuisine">
													<span class="fa fa-cutlery" style="padding-right:8px;padding-top:1px;"></span>
													<span>Ẩm thực</span>
													<span style="float: right;font-weight: normal;font-size: 16px;color: #999;padding-right: 5px;" class="fa fa-angle-right"></span>
												</a>
											</li>
											<li>
												<a class="header-text"
													data-bind="css: { 'act': currentShownFilter() == 'property' }, click: function () { showFilter('property') }"
													href="#filter-property">
													<span class="fa fa-check-square" style="padding-right:8px;padding-top:1px;"></span>
													<span>Tiện nghi</span>
													<span style="float: right;font-weight: normal;font-size: 16px;color: #999;padding-right: 5px;" class="fa fa-angle-right"></span>
												</a>
											</li>
											<li>
												<a class="header-text" style="border-bottom:#e6e6e6 1px solid;"
													data-bind="css: { 'act': currentShownFilter() == 'dining' }, click: function () { showFilter('dining') }"
													href="#filter-dining">
													<span class="fa fa-certificate" style="padding-right:8px;padding-top:1px;"></span>
													<span>Thích hợp</span>
													<span style="float: right;font-weight: normal;font-size: 16px;color: #999;padding-right: 5px;" class="fa fa-angle-right"></span>
												</a>
											</li>
										</ul>
										<div data-bind="visible: currentShownFilter() == 'category'"
											class="directory-left-filter-itembox" style="display: none;">
											<div data-bind="visible: $root.isFilterLoading() == false || allCategories().length > 0"
												class="left-filters">
												<div class="list-filters">
													<!-- ko foreach: allCategories() -->
													<div class="list-filters-item"
														data-bind="click: $root.handleClickFilter">
														<div class="left" data-checkbox="checkbox">
															<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span>
															<span data-bind="text: Name"></span>
														</div>
														<div data-bind="text: ResultCount" class="right">
														</div>
													</div>
													<!-- /ko -->
												</div>
											</div>
											<div style="display: none"
												data-bind="visible: $root.isFilterLoading() && allCategories().length == 0">
												<img style="margin: 102px auto; padding: 0;"
                                     src="/style/images/icons/ajax-loader.gif" />
                            </div>

											</div>
											<div data-bind="visible: currentShownFilter() == 'area'"
												class="directory-left-filter-itembox" style="display: none;">
												<div data-bind="visible: $root.isFilterLoading() == false || allAreas().length > 0"
													class="left-filters">
													<div style="float: left; width: 100%;">
														<div class="left-filters-h1">H&#224; Nội</div>
														<input data-bind="value: districtId()" type="hidden" name="districtId" />

														<div class="district-change">
															<select style="border: #e5e5e5 1px solid; padding:7px 2px;margin:0;margin-right:10px; " data-bind="event:{change: $root.handleClickDistrict}, options: $root.districts, optionsText: 'Name', optionsValue: 'Id', value: districtId, optionsCaption: '[chọn quận]    '"></select>
														</div>
														<div data-bind="visible: allAreas().length > $root.maxItemsToShowFilterKeyword"
															class="filter-keyword-filter">
															<input data-bind="value: areaKeywordFilter, valueUpdate: 'keyup'" type="text" placeholder="Nhập từ khóa để tìm khu vực" style="border: #e5e5e5 1px solid; padding: 9px 4px 8px 4px; width: 380px; " />
                                    </div>
														</div>

														<div class="list-filters">
															<!-- ko foreach: areaGroups() -->
															<h3 style="margin: 15px 0 5px 0; clear: both; font-size: 15px;font-weight:bold; float: left; width: 100%; border-bottom: 1px #f6f6f6 solid; padding-bottom: 3px;"
																data-bind="text: name, visible: $root.areaGroups().length > 1 && !IsHidden()">
															</h3>
															<!-- ko foreach: items() -->
															<div class="list-filters-item"
																data-bind="click: $root.handleClickFilter, visible: !IsHidden()">
																<div class="left" data-checkbox="checkbox">
																	<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span>
																	<span data-bind="text: Name"></span>
																	<span class="external-links">
                                                <a rel="nofollow" data-bind="click: $root.gotoAreaLandingPage, attr: { href: getAreaLandingPageUrl(UrlRewriteName) }" href="#" target="_blank"></a>
                                            </span>
																</div>
																<div data-bind="text: ResultCount" class="right">
																</div>
															</div>
															<!-- /ko -->
															<!-- /ko -->
														</div>
													</div>
													<div style="display: none"
														data-bind="visible: $root.isFilterLoading() && allAreas().length == 0">
														<img style="margin: 102px auto; padding: 0;"
                                     src="/style/images/icons/ajax-loader.gif" />
                            </div>

													</div>
													<div data-bind="visible: currentShownFilter() == 'purpose'"
														class="directory-left-filter-itembox" style="display: none;">
														<div data-bind="visible: $root.isFilterLoading() == false || allPurposes().length > 0"
															class="left-filters">
															<div data-bind="visible: allPurposes().length > $root.maxItemsToShowFilterKeyword"
																class="filter-keyword">
																<input data-bind="value: purposeKeywordFilter, valueUpdate: 'keyup'" type="text" placeholder="Nhập từ khóa để tìm mục đích" style="border: #e5e5e5 1px solid; padding:8px 4px; width: 700px;" />
                                </div>
																<div class="list-filters" style="margin-top: 5px;">
																	<!-- ko foreach: allPurposes() -->
																	<div class="list-filters-item"
																		data-bind="click: $root.handleClickFilter, visible: !IsHidden()">
																		<div class="left" data-checkbox="checkbox">
																			<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { test: '', check: Selected() }"></span>
																			<span data-bind="text: Name"></span>
																		</div>
																		<div data-bind="text: ResultCount"
																			class="right">
																		</div>
																	</div>
																	<!-- /ko -->
																</div>
															</div>
															<div style="display: none"
																data-bind="visible: $root.isFilterLoading() && allPurposes().length == 0">
																<img style="margin: 102px auto; padding: 0;"
                                     src="/style/images/icons/ajax-loader.gif" />
                            </div>

															</div>
															<div data-bind="visible: currentShownFilter() == 'cuisine'"
																class="directory-left-filter-itembox"
																style="display: none;">
																<div data-bind="visible: $root.isFilterLoading() == false || allCuisines().length > 0"
																	data-bind="    visible: $root.isFilterLoading() == false || allCuisines().length > 0"
																	class="left-filters">
																	<div data-bind="visible: allCuisines().length > $root.maxItemsToShowFilterKeyword"
																		class="filter-keyword">
																		<input data-bind="value: cuisineKeywordFilter, valueUpdate: 'keyup'" type="text" />
                                </div>
																		<div class="list-filters">
																			<!-- ko foreach: allCuisines -->
																			<div class="list-filters-item"
																				data-bind="click: $root.handleClickCuisine, visible: !IsHidden()">
																				<div class="left"
																					data-checkbox="checkbox">
																					<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span><span data-bind="    text: Name"></span>
																				</div>
																				<div data-bind="text: ResultCount"
																					class="right">
																				</div>
																				<div data-bind="foreach: children(), visible: Selected()"
																					class="filters-item-children"
																					style="margin-left: 18px;">
																					<div style="clear: both;"
																						class="list-filters-item"
																						data-bind="click: $root.handleClickCuisine">
																						<div class="left"
																							data-checkbox="checkbox">
																							<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span><span data-bind="    text: Name"></span>
																						</div>
																					</div>
																					<div data-bind="foreach: children(), visible: Selected()"
																						class="filters-item-children"
																						style="margin-left: 18px">
																						<div class="list-filters-item"
																							data-bind="click: $root.handleClickCuisine">
																							<div class="left"
																								data-checkbox="checkbox">
																								<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span><span data-bind="    text: Name"></span>
																							</div>
																						</div>
																					</div>
																				</div>
																			</div>
																			<!-- /ko -->
																		</div>
																	</div>
																	<div style="display: none"
																		data-bind="visible: $root.isFilterLoading() && allCuisines().length == 0">
																		<img style="margin: 102px auto; padding: 0;"
                                     src="/style/images/icons/ajax-loader.gif" />
                            </div>

																	</div>
																	<div data-bind="visible: currentShownFilter() == 'dish'"
																		class="directory-left-filter-itembox"
																		style="display: none;">
																		<div data-bind="visible: $root.isFilterLoading() == false || allDishCategories().length > 0"
																			class="left-filters">
																			<div data-bind="visible: allDishCategories().length > $root.maxItemsToShowFilterKeyword"
																				class="filter-keyword">
																				<input data-bind="value: dishCategoryKeywordFilter, valueUpdate: 'keyup'" type="text" placeholder="Nhập từ khóa để tìm loại món" style="border: #e5e5e5 1px solid; padding: 8px 4px; width: 700px;" />
                                </div>
																				<div class="list-filters"
																					style="margin-top: 5px;">
																					<!-- ko foreach: allDishCategories -->
																					<div class="list-filters-item"
																						data-bind="click: $root.handleClickDishCategory, visible: !IsHidden()">
																						<div class="left"
																							data-checkbox="checkbox">
																							<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span><span data-bind="    text: Name"></span>
																						</div>
																						<div data-bind="text: ResultCount"
																							class="right">
																						</div>
																						<div data-bind="foreach: children(), visible: Selected()"
																							class="filters-item-children"
																							style="margin-left: 18px">
																							<div style="clear: both;"
																								class="list-filters-item"
																								data-bind="click: $root.handleClickDishCategory">
																								<div class="left"
																									data-checkbox="checkbox">
																									<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span><span data-bind="    text: Name"></span>
																								</div>
																							</div>
																							<div data-bind="foreach: children(), visible: Selected()"
																								class="filters-item-children"
																								style="margin-left: 18px">
																								<div class="list-filters-item"
																									data-bind="click: $root.handleClickDishCategory">
																									<div class="left"
																										data-checkbox="checkbox">
																										<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span><span data-bind="    text: Name"></span>
																									</div>
																								</div>
																							</div>
																						</div>
																					</div>
																					<!-- /ko -->
																				</div>
																			</div>
																			<div style="display: none"
																				data-bind="visible: $root.isFilterLoading() && allDishCategories().length == 0">
																				<img style="margin: 102px auto; padding: 0;"
                                     src="/style/images/icons/ajax-loader.gif" />
                            </div>

																			</div>
																			<div data-bind="visible: currentShownFilter() == 'property'"
																				class="directory-left-filter-itembox"
																				style="display: none;">
																				<div data-bind="visible: $root.isFilterLoading() == false || allProperties().length > 0"
																					class="left-filters">
																					<div data-bind="visible: allProperties().length > $root.maxItemsToShowFilterKeyword"
																						class="filter-keyword">
																						<input data-bind="value: propertyKeywordFilter, valueUpdate: 'keyup'" type="text" placeholder="Nhập từ khóa để tìm tiện nghi" style="border: #e5e5e5 1px solid; padding:8px 4px; width: 700px;" />
                                </div>
																						<div class="list-filters"
																							style="margin-top: 5px;">
																							<!-- ko foreach: allProperties -->
																							<div class="list-filters-item"
																								data-bind="click: $root.handleClickFilter, visible: !IsHidden()">
																								<div class="left"
																									data-checkbox="checkbox">
																									<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span>
																									<span data-bind="text: Name"></span>
																								</div>
																								<div data-bind="text: ResultCount"
																									class="right">
																								</div>
																							</div>
																							<!-- /ko -->
																						</div>
																					</div>
																					<div style="display: none"
																						data-bind="visible: $root.isFilterLoading() && allProperties().length == 0">
																						<img style="margin: 102px auto; padding: 0;"
                                     src="/style/images/icons/ajax-loader.gif" />
                            </div>

																					</div>
																					<div data-bind="visible: currentShownFilter() == 'dining'"
																						class="directory-left-filter-itembox"
																						style="border-right: #ddd 1px solid; display: none">
																						<div data-bind="visible: $root.isFilterLoading() == false || allDinings().length > 0"
																							class="left-filters">
																							<div data-bind="visible: allDinings().length > $root.maxItemsToShowFilterKeyword"
																								class="filter-keyword">
																								<input data-bind="value: diningKeywordFilter, valueUpdate: 'keyup'" type="text" />
                                </div>
																								<div
																									class="list-filters">
																									<!-- ko foreach: allDinings() -->
																									<div class="list-filters-item"
																										data-bind="click: $root.handleClickFilter, visible: !IsHidden()">
																										<div class="left"
																											data-checkbox="checkbox">
																											<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { test: '', check: Selected() }"></span>
																											<span data-bind="text: Name"></span>
																										</div>
																										<div data-bind="text: ResultCount"
																											class="right">
																										</div>
																									</div>
																									<!-- /ko -->
																								</div>
																							</div>
																							<div style="display: none"
																								data-bind="visible: $root.isFilterLoading() && allDinings().length == 0">
																								<img style="margin: 102px auto; padding: 0;"
                                     src="/style/images/icons/ajax-loader.gif" />
                            </div>

																							</div>
																						</div>
																					</div>
																				</div>

																			</div>
																		</div>
																	</div>

																	<script>
																		function getAreaLandingPageUrl(url) {
        return '/'+'ha-noi'+'/khu-vuc-' + url;
    }
																	</script>

																	<div class="directory-container">
																		<div class="directory-content">
																			<!--End of search Tool-->
																			<!--Start left filters-->
																			<div class="search-result directory-area">

																				<div class="right"
																					style="clear: both; width: 1170px;">
																					<div class="column-left">
																						<div class="directory-search-resulttab foody-toolbar"
																							id="directory-search-resulttab">
																							<div
																								style="background:none;">
																								<ul>
																									<li>
																										<a data-bind="css:{'current':documentSource()=='Restaurant'}"
																											href="/ha-noi/food/dia-diem?ds=Restaurant"
																											class="current">
																											Địa điểm
																										</a>
																									</li>
																									<li>
																										<a data-bind="visible:listResultCount()>0,css:{'current':documentSource()=='List'}"
																											href="/ha-noi/food/list?ds=List">
																											Bộ sưu tập
																										</a>
																									</li>
																									<li>
																										<a data-bind="visible:pictureResultCount()>0, css:{'current':documentSource()=='Picture'}"
																											href="/ha-noi/food/picture?ds=Picture">
																											Hình ảnh
																										</a>
																									</li>
																									<li>
																										<a data-bind="visible:photoCollectionResultCount()>0, css:{'current':documentSource()=='PhotoCollection'}"
																											href="/ha-noi/food/photo-collection?ds=PhotoCollection">
																											Bộ sưu tập
																											hình
																										</a>
																									</li>
																									<li>
																										<a data-bind="visible:articleResultCount()>0, css:{'current':documentSource()=='Article'}"
																											href="/ha-noi/food/article-list?ds=Article">
																											Blogs
																										</a>
																									</li>

																								</ul>
																								<style>
																									.directory-search-resulttab .foody-banner ul {
																										height: 400px;
																									}

																									.directory-search-resulttab .foody-banner ul li a {
																										padding: 0;
																										display: block;
																										float: left;
																									}
																								</style>




																							</div>

																						</div>
																						<div class="result-side">
																							<!--Filter Keywords-->
																							<!--End of filter keywords-->
																							<div class="directory-places-sorts foody-toolbar"
																								data-bind="visible:documentSource()=='Restaurant'"
																								style="display: none;">
																								<div
																									class="fd-clearbox">
																									<ul>
																										<li>
																											<a href="javascript:void(0)"
																												class="current"
																												data-bind="click:handleClickSortType.bind(this,1),css:{'current':sortType()==1}">Đúng
																												nhất</a>
																										</li>
																										<li>
																											<a href="javascript:void(0)"
																												data-bind="click:handleClickSortType.bind(this,7),css:{'current':sortType()==7}">Gần
																												tôi
																												nhất</a>
																										</li>
																										<li>
																											<a href="javascript:void(0)"
																												data-bind="click:handleClickSortType.bind(this,5),css:{'current':sortType()==5}">Phổ
																												biến</a>
																										</li>
																										<li>
																											<a href="javascript:void(0)"
																												data-bind="click:handleClickSortType.bind(this,2),css:{'current':sortType()==2}">Xem
																												nhiều
																												nhất</a>
																										</li>
																										<li>
																											<a href="javascript:void(0)"
																												data-bind="click:handleClickSortType.bind(this,4),css:{'current':sortType()==4}">Đánh
																												giá tốt
																												nhất</a>
																										</li>
																									</ul>

																								</div>
																								<div data-bind="visible:documentSource()=='Restaurant'"
																									class="view-types"
																									style="margin-left: 935px;position:absolute">
																									<a rel="nofollow"
																										href="https://www.foody.vn/ha-noi/quan-an-phong-cach-viet-nam-tai-quan-cau-giay?c=quan-an&amp;categorygroup=food&amp;page=4&amp;append=true&amp;vt=row"
																										class="row-view active"
																										data-bind="css: { active: viewType() == 'row' }, click: function (data, event) { changeViewType('row', data, event) }, attr: { href: rowViewUrl }"
																										title="List View"></a>

																									<a rel="nofollow"
																										href="https://www.foody.vn/ha-noi/quan-an-phong-cach-viet-nam-tai-quan-cau-giay?c=quan-an&amp;categorygroup=food&amp;page=4&amp;append=true&amp;vt=map"
																										class="map-view "
																										data-bind="css: { active: viewType() == 'map' }, click: function (data, event) { changeViewType('map', data, event) }, attr: { href: mapViewUrl }"
																										title="Map View"></a>
																								</div>
																							</div>
																							<div class="directory-places-sorts foody-toolbar"
																								data-bind="visible:false">
																								<div
																									class="fd-clearbox">
																									<ul>
																										<li>
																											<a
																												href="javascript:void(0)">Đúng
																												nhất</a>
																										</li>
																										<li>
																											<a
																												href="javascript:void(0)">Gần
																												tôi
																												nhất</a>
																										</li>
																										<li>
																											<a
																												href="javascript:void(0)">Phổ
																												biến</a>
																										</li>
																										<li>
																											<a
																												href="javascript:void(0)">Xem
																												nhiều
																												nhất</a>
																										</li>
																										<li>
																											<a
																												href="javascript:void(0)">Đánh
																												giá tốt
																												nhất</a>
																										</li>
																									</ul>
																								</div>

																							</div>
																							<div
																								class="head-result d_resultfilter">
																								<div
																									class="result-counts">
																									<div
																										class="number-msg">
																										<div
																											class="result-status-count">
																											<div
																												style="float: left;">
																												<span data-bind="text: (totalResult()).format('n0')">2.455</span>
																												Kết quả
																											</div>
																											<h1
																												data-bind="html:metaTitle">
																												Địa điểm
																												Qu&#225;n
																												ăn phong
																												c&#225;ch
																												M&#243;n
																												Việt tại
																												Quận Cầu
																												Giấy,
																												H&#224;
																												Nội
																											</h1>

																										</div>
																									</div>


																								</div>
																							</div>
																							<!--Result msg-->

																							<div class="resultnumber"
																								style="overflow:visible">


																								<div data-bind="if: true, style: { display: 'block' }"
																									style="display: none; clear: left;">

																									<!--ko foreach: filtedLists()-->
																									<div data-bind="visible: items().length > 0"
																										style="position: relative"
																										class="selectedkeyword"
																										onmouseover="$(this).children('ul, div.line').show()"
																										onmouseout="$(this).children('ul, div.line').hide()">
																										<div class="keyword"
																											data-bind="text: name">
																										</div>

																										<ul class="filter-list"
																											data-bind="foreach: items">
																											<li>
																												<span data-bind="text: Name" style="color:#333;"></span>
																												<div
																													data-bind="if: $parent.hasChildren">
																													<ul style="padding-left: 10px"
																														data-bind="foreach: children">
																														<li
																															data-bind="visible: Selected">
																															<span data-bind="text: Name" style="color:#333;"></span>
																															<ul style="padding-left: 10px"
																																data-bind="foreach: children">
																																<li data-bind="visible: Selected, text: Name"
																																	style="color:#333;">
																																</li>
																															</ul>
																														</li>
																													</ul>
																												</div>
																											</li>
																										</ul>
																										<div
																											class="closebut">
																											<a href=""
																												data-bind="click: $root.handleRemoveFilterClick">
																												<img src="/style/images/icons/keyword-close-icon.png" width="10" alt="Bỏ lọc" /></a>
																										</div>
																									</div>
																									<!--/ko-->
																								</div>
																								<div
																									data-bind="if: false">
																								</div>

																							</div>
																							<!--End of result msg-->
																							<div data-bind="if: true, style: { display: 'block' }"
																								id="result-box"
																								class="frame-result"
																								style="display: none; margin:inherit;padding-bottom:0">
																								<script>
																									var bannerAdsUrl = '/__get/Common/BannerList?bannerGroupKey=TIMKIEM&width=1000&height=90&count=1'
    var bannerAdsIndex = 0;
																								</script>
																								<div class="row-view"
																									data-bind="if: viewType() == 'row', fadeVisible: viewType() == 'row'">
																									<div
																										class="filter-results">
																										<div
																											data-bind="template: { foreach: searchItems(), name: $root.itemTemplateName() }">

																										</div>
																									</div>

																								</div>

																								<script>
																									function showDeliver(el) {
        $(el).next().toggle();
    }
																								</script>

																								<script
																									id="RestaurantItem"
																									type="text/html">
																									<div data-bind="attr:{'style':!IsAd?'':'background: #fffee2;'}"
																										class="row-item filter-result-item">
																										<div class="ri-avatar result-image">
																											<!-- ko ifnot:SubItems.length>0-->
																											<a data-bind="attr: { href: DetailUrl, title: Name }, click:$root.trackGAClick"
																												target="_blank">
																												<img data-bind="attr: { src: MobilePicturePath, alt: Name }" />
            </a>
																												<!-- /ko -->
																												<!-- ko if:SubItems.length>0-->
																												<a data-bind="attr: { href: BranchUrl, title: BranchName }, click:$root.trackGAClick"
																													target="_blank">
																													<img data-bind="attr: { src: MobilePicturePath, alt: BranchName }" onerror="this.onerror=null;this.src='/Style/images/deli-dish-no-image.png';" />
            </a>
																													<!-- /ko -->

																													<ul class="service-list" data-bind="visible:HasBooking||HasDelivery">
																														<li style="width: 100%" class="ser-type-2"
																															data-bind="visible:HasDelivery,css:{'ser-width-1': HasDelivery && !HasBooking,'ser-width-2': HasDelivery && HasBooking}">
																															<a data-bind="attr:{href:DeliveryUrl}" target="_blank">
																																<span data-bind="visible:MasterCategoryId!=2&&MasterCategoryId!=3">Đặt Giao Hàng</span>
																																<span data-bind="visible:MasterCategoryId==2||MasterCategoryId==3">Đặt Dịch Vụ</span>
																															</a>
																														</li>

																													</ul>
																													<div class="has-video" data-bind="visible:HasVideo">
																														<span class="fa fa-video-camera"></span>
																													</div>
																													<div data-bind="if: Status == 4">
																														<div class="red-label-highlight">
																															<span>Đang đóng cửa</span>
																														</div>
																													</div>
																													<div data-bind="if: Status == 6">
																														<div class="red-label-highlight">
																															<span>Cần xác thực</span>
																														</div>
																													</div>
																										</div>
																										<div class="row-view-right">
																											<div class="result-name">
																												<div class="status">
																													<div data-bind="css:{'highlight-text':AvgRating*1 >= 6,'no-point':AvgRating == '_._'},text: AvgRating, attr: { 'data-tooltip': '#ratingtooltip_' + Id, 'data-restaurantid': Id }, event: { mouseover: $root.handleRatingMouseOver, mouseout: $root.handleRatingMouseOut }"
																														class="point">
																													</div>
																												</div>
																												<div class="resname">
																													<h2>
																														<!-- ko ifnot:SubItems.length>0-->
																														<a data-bind="text: Name, attr: { href: DetailUrl, title: Name }, click:$root.trackGAClick"
																															target="_blank"></a>
																														<!-- /ko -->
																														<!-- ko if:SubItems.length>0-->
																														<a data-bind="text: BranchName, attr: { href: BranchUrl, title: BranchName }, click:$root.trackGAClick"
																															target="_blank"></a>
																														<!-- /ko -->
																													</h2>
																													<div class="result-address">
																														<div class="address">
																															<!-- ko ifnot:SubItems.length>0-->
																															<span data-bind="text: Address"></span>,
																															<a data-bind="attr:{href: DistrictUrl}">
																																<span data-bind="text: District"></span>,
																															</a>
																															<span data-bind="text: City"></span>
																															<!-- /ko -->
																															<!-- ko if:SubItems.length>0-->
																															<span class="branch-address">
                                <span class="branch-btn-ico-blue"></span>
																															<span data-bind="text:SubItems.length + 1"></span>&nbsp;chi nhánh
																															</span>
																															<!-- /ko -->
																														</div>
																														<div class="distants"
																															data-bind="text:Distance!=null?Distance.format('N1') +' KM':''">1km
																														</div>
																													</div>
																												</div>
																											</div>


																											<div data-bind="foreach:Reviews,visible:Reviews.length>0" class="row-view-reviews">
																												<div class="items">
																													<a class="avatar" data-bind="attr:{href:OwnerProfileUrl}">
																														<img data-bind="attr:{src:OwnerAvatar}" />
                    </a>
																														<div class="content block-with-text"
																															data-bind="css: { 'not-align': ShortReview }">
																															<a
																																data-bind="attr:{href:OwnerProfileUrl}"><b style="display:inherit" data-bind="text:OwnerFullName"></b></a>
																															<span data-bind="html:Comment"></span>
																														</div>
																												</div>
																											</div>
																											<div data-bind="visible:Reviews.length==0" class="row-view-reviews">
																												<div class="items">
																													<a class="avatar" href="javascript:void(0);">
																														<div class="not-review-yet"></div>
																													</a>
																													<div class="content not-review-content">
																														<a href="javascript:void(0);" style="width: 100%;display: block;">
																															<b data-bind="text:'Foody'"></b>
																															Chưa có bình luận/đánh giá về địa điểm này!&nbsp;Hãy là người đầu tiên
																															đóng góp bình luận & đánh giá về địa điểm này.
																														</a>

																													</div>
																												</div>
																											</div>
																											<div class="result-stats" style="border-bottom: 1px solid #eee;height:24px;">
																												<div data-bind="if:IsOpening" class="opentime-status">
																													<span class="online"></span>
																													Đang mở cửa
																												</div>
																												<div data-bind="if:!IsOpening" class="opentime-status" style="color: #959595">
																													<span class="offline"></span>
																													Chưa mở cửa
																												</div>

																											</div>
																											<div class="result-stats">
																												<div data-bind="attr: { 'style': !IsAd ? '' : 'background-color: #fffee2;' }"
																													class="row-view-users">
																													<div class="stats">
																														<a href="javascript:void(0)"
																															data-bind="click: function () { $root.LoadReviewPopup(Id); }">
																															<span class="fa fa-comment" style="font-weight: normal;"></span>
																															<span data-bind="text: TotalReview.formatK(1)"></span>
																														</a>
																														<a class="link"
																															data-bind="click: function () { $root.LoadGalleryPopup(Id); }">
																															<span class="fa fa-camera" style="font-weight: normal;padding-left:10px;"></span>
																															<span data-bind="text: PictureCount.formatK(1)"></span>
																														</a>
																														<a href="javascript:void(0)" data-bind="attr: { resid: Id }">
																															<span class="fa fa-bookmark" style="font-weight: normal; padding-left: 10px;"></span>
																															<span data-bind="text: TotalSaves.formatK(1)"></span>
																														</a>

																													</div>
																													<div class="row-view-right2 reviews">
																														<div class="directory-items-shortcut">
																															<div>
																																<a class="tool-custom-list-add otherlist"
																																	data-bind="attr: { 'data-id': Id }, css: { 'added': HasAlredyAddedToList }"
																																	data-core="true" style="float:right">
																																	<span class="fa fa-bookmark"></span>
																																	<!-- ko if:HasAlredyAddedToList-->
																																	<span>Đã lưu</span>
																																	<!-- /ko -->
																																	<!-- ko if:!HasAlredyAddedToList-->
																																	<span>Lưu</span>
																																	<!-- /ko -->
																																</a>
																															</div>
																														</div>
																													</div>


																												</div>
																											</div>

																										</div>





																									</div>
																								</script>


																								<div class="map-view"
																									data-bind="if: viewType()=='map', fadeVisible: viewType()=='map'">
																									<noscript>
																										<h3>
																											Trình duyệt
																											không hỗ trợ
																											javascript!
																										</h3>
																									</noscript>
																									<div id="mapLarge"
																										class="map-container">
																									</div>
																								</div>

																							</div>
																							<div data-bind="if: false"
																								class="frame-result"
																								style="margin-top:0;padding-bottom:0;">


																								<div class="row-view">

																									<div
																										class="filter-results">
																										<div class="filter-result-item"
																											style="padding:0; margin: 5px 0 20px 0;">


																										</div>

																										<div style=""
																											class="row-item filter-result-item">
																											<div
																												class="ri-avatar result-image">
																												<a title="Tuyết Nhung - Cơm G&#224; Ph&#250; Y&#234;n - T&#244; Hiệu"
																													href="/ha-noi/tuyet-nhung-com-ga-phu-yen"
																													target="_blank">
																													<img alt="Tuyết Nhung - Cơm G&#224; Ph&#250; Y&#234;n - T&#244; Hiệu" src="https://images.foody.vn/res/g74/737094/prof/s640x400/foody-upload-api-foody-mobile-phu-yen-jpg-180503093800.jpg" />
                    </a>

																											</div>
																											<div
																												class="row-view-right">
																												<div
																													class="result-name">
																													<div
																														class="status">
																														<div
																															class="point highlight-text">
																															7.1
																														</div>
																														<div
																															class="ratingtooltip">
																															<div
																																class="top-arrow">
																																<img alt="" src="/style/images/icons/arrow-top.png">
                                </div>
																															</div>
																														</div>
																														<div
																															class="resname">
																															<h2>
																																<a title="Tuyết Nhung - Cơm G&#224; Ph&#250; Y&#234;n - T&#244; Hiệu"
																																	href="/ha-noi/tuyet-nhung-com-ga-phu-yen"
																																	target="_blank">
																																	Tuyết
																																	Nhung
																																	-
																																	Cơm
																																	G&#224;
																																	Ph&#250;
																																	Y&#234;n
																																	-
																																	T&#244;
																																	Hiệu
																																</a>
																															</h2>
																															<div
																																class="result-address">
																																<div
																																	class="address">
																																	<span>
                                            <span>223 T&#244; Hiệu, P. Nghĩa T&#226;n</span>,
																																	<a
																																		href="/ha-noi/khu-vuc-quan-cau-giay">
																																		<span>Quận Cầu Giấy</span>
																																	</a>,
																																	<span>H&#224; Nội</span>
																																	</span>

																																</div>
																															</div>
																														</div>
																													</div>
																													<div
																														class="row-view-reviews">
																														<div
																															class="items">
																															<a class="avatar"
																																href="/thanh-vien/foodee_kilxyjpk">
																																<img src="https://images.foody.vn/default/s50/user-default-female.png" />
                                    </a>
																																<div
																																	class="content">
																																	<a
																																		href="/thanh-vien/foodee_kilxyjpk">
																																		<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Hồng&nbsp;
                                            </b>
																																	</a>
																																	<span>Quá đắt so với mức giá. Món nộm thì tốt nhất đừng gọi, toàn giá với rau, trà đá cũng thế.</span>
																																</div>
																														</div>
																														<div
																															class="items">
																															<a class="avatar"
																																href="/thanh-vien/tungvu3196">
																																<img src="https://images.foody.vn/usr/g36/352254/avt/c50x50/foody-avatar-981-637145531689255321.jpg" />
                                    </a>
																																<div
																																	class="content">
																																	<a
																																		href="/thanh-vien/tungvu3196">
																																		<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Tung Vu&nbsp;
                                            </b>
																																	</a>
																																	<span>Mình đến ăn lúc 5h30 chiều, thấy ăn cơm nguội, gà xé cũng ít và không ngon nóng. Suất cơm gà 40k mà có quá ít cơm và gà. Đồ ăn lại không có gì đặc biệt nữa.</span>
																																</div>
																														</div>
																													</div>
																													<div class="result-stats"
																														style="border-bottom: 1px solid #eee;height:24px;">
																														<div class="opentime-status"
																															style="color: #959595">
																															<span class="offline"></span>
																															Chưa
																															mở
																															cửa
																														</div>

																													</div>
																													<div
																														class="result-stats">
																														<div
																															class="row-view-users">
																															<div
																																class="stats">
																																<a
																																	href="javascript:void(0)">
																																	<span class="fa fa-comment" style="font-weight: normal;"></span>
																																	<span>47</span>
																																</a>
																																<a
																																	class="link">
																																	<span class="fa fa-camera" style="font-weight: normal;padding-left:10px;"></span>
																																	<span>142</span>
																																</a>
																																<a
																																	href="javascript:void(0)">
																																	<span class="fa fa-bookmark" style="font-weight: normal; padding-left: 10px;"></span>
																																	<span>40</span>
																																</a>
																															</div>
																															<div
																																class="row-view-right2 reviews">
																																<div
																																	class="directory-items-shortcut">
																																	<div>
																																		<a class="tool-custom-list-add otherlist "
																																			style=" float right;">
																																			<span class="fa fa-bookmark"></span>
																																			<span>Lưu</span>
																																		</a>
																																	</div>
																																</div>
																															</div>
																														</div>
																													</div>
																												</div>
																											</div>
																											<div style=""
																												class="row-item filter-result-item">
																												<div
																													class="ri-avatar result-image">
																													<a title="Ch&#232; Dừa Th&#225;i Lan - Nguyễn Phong Sắc"
																														href="/ha-noi/che-dua-thai-lan-nguyen-phong-sac"
																														target="_blank">
																														<img alt="Ch&#232; Dừa Th&#225;i Lan - Nguyễn Phong Sắc" src="https://images.foody.vn/res/g22/214084/prof/s640x400/foody-mobile-dua640-jpg-631-635953770711301483.jpg" />
                    </a>

																												</div>
																												<div
																													class="row-view-right">
																													<div
																														class="result-name">
																														<div
																															class="status">
																															<div
																																class="point highlight-text">
																																7.0
																															</div>
																															<div
																																class="ratingtooltip">
																																<div
																																	class="top-arrow">
																																	<img alt="" src="/style/images/icons/arrow-top.png">
                                </div>
																																</div>
																															</div>
																															<div
																																class="resname">
																																<h2>
																																	<a title="Ch&#232; Dừa Th&#225;i Lan - Nguyễn Phong Sắc"
																																		href="/ha-noi/che-dua-thai-lan-nguyen-phong-sac"
																																		target="_blank">
																																		Ch&#232;
																																		Dừa
																																		Th&#225;i
																																		Lan
																																		-
																																		Nguyễn
																																		Phong
																																		Sắc
																																	</a>
																																</h2>
																																<div
																																	class="result-address">
																																	<div
																																		class="address">
																																		<span>
                                            <span>25 Nguyễn Phong Sắc, P. Dịch Vọng Hậu</span>,
																																		<a
																																			href="/ha-noi/khu-vuc-quan-cau-giay">
																																			<span>Quận Cầu Giấy</span>
																																		</a>,
																																		<span>H&#224; Nội</span>
																																		</span>

																																	</div>
																																</div>
																															</div>
																														</div>
																														<div
																															class="row-view-reviews">
																															<div
																																class="items">
																																<a class="avatar"
																																	href="/thanh-vien/thang0208">
																																	<img src="https://images.foody.vn/usr/g62/616780/avt/c50x50/beauty-upload-api-foody-avatar-69fb5139-a52b-40d4-95d7-efa8a0cd871b-191020213924.jpg" />
                                    </a>
																																	<div
																																		class="content">
																																		<a
																																			href="/thanh-vien/thang0208">
																																			<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Thang&nbsp;Ngoc
                                            </b>
																																		</a>
																																		<span>Hôm nay gấu bảo ngày ngưu lang chức nữ gặp nhau nên ăn chè đỗ đỏ, mình mới đặt chè đỗ đỏ với 1 số loại chè khác. Grab đến quán bảo đợi 10p vì phải nấu, uh thì mình đợi. Xong grab gọi lại bảo hết tất c...</span>
																																	</div>
																															</div>
																															<div
																																class="items">
																																<a class="avatar"
																																	href="/thanh-vien/xjuzoyr">
																																	<img src="https://images.foody.vn/usr/g862/8610623/avt/c50x50/xjuzoyr-avatar-373-636750583830011143.jpg" />
                                    </a>
																																	<div
																																		class="content">
																																		<a
																																			href="/thanh-vien/xjuzoyr">
																																			<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Linh&nbsp;Chi
                                            </b>
																																		</a>
																																		<span>Quán nhỏ xinh nằm ngay đầu đường nguyễn phong sắc,ngã 4 trần thái tông xuân thủy cầu giấy.

Menu đa dạng với các loại chè như chè sầu,dừa dầm đến những loại chè truyền thống như chè bưởi,chè đỗ đen..v...</span>
																																	</div>
																															</div>
																														</div>
																														<div class="result-stats"
																															style="border-bottom: 1px solid #eee;height:24px;">
																															<div
																																class="opentime-status">
																																<span class="online"></span>
																																Đang
																																mở
																																cửa
																															</div>

																														</div>
																														<div
																															class="result-stats">
																															<div
																																class="row-view-users">
																																<div
																																	class="stats">
																																	<a
																																		href="javascript:void(0)">
																																		<span class="fa fa-comment" style="font-weight: normal;"></span>
																																		<span>32</span>
																																	</a>
																																	<a
																																		class="link">
																																		<span class="fa fa-camera" style="font-weight: normal;padding-left:10px;"></span>
																																		<span>153</span>
																																	</a>
																																	<a
																																		href="javascript:void(0)">
																																		<span class="fa fa-bookmark" style="font-weight: normal; padding-left: 10px;"></span>
																																		<span>25</span>
																																	</a>
																																</div>
																																<div
																																	class="row-view-right2 reviews">
																																	<div
																																		class="directory-items-shortcut">
																																		<div>
																																			<a class="tool-custom-list-add otherlist "
																																				style=" float right;">
																																				<span class="fa fa-bookmark"></span>
																																				<span>Lưu</span>
																																			</a>
																																		</div>
																																	</div>
																																</div>
																															</div>
																														</div>
																													</div>
																												</div>
																												<div style=""
																													class="row-item filter-result-item">
																													<div
																														class="ri-avatar result-image">
																														<a title="H&#249;ng B&#233;o - Lẩu Cua Đồng - Trần Tử B&#236;nh"
																															href="/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh"
																															target="_blank">
																															<img alt="H&#249;ng B&#233;o - Lẩu Cua Đồng - Trần Tử B&#236;nh" src="https://images.foody.vn/res/g17/160574/prof/s640x400/foody-mobile-960x600_hung-beo-lau-533-636147262410516048.jpg" />
                    </a>

																													</div>
																													<div
																														class="row-view-right">
																														<div
																															class="result-name">
																															<div
																																class="status">
																																<div
																																	class="point highlight-text">
																																	7.3
																																</div>
																																<div
																																	class="ratingtooltip">
																																	<div
																																		class="top-arrow">
																																		<img alt="" src="/style/images/icons/arrow-top.png">
                                </div>
																																	</div>
																																</div>
																																<div
																																	class="resname">
																																	<h2>
																																		<a title="H&#249;ng B&#233;o - Lẩu Cua Đồng - Trần Tử B&#236;nh"
																																			href="/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh"
																																			target="_blank">
																																			H&#249;ng
																																			B&#233;o
																																			-
																																			Lẩu
																																			Cua
																																			Đồng
																																			-
																																			Trần
																																			Tử
																																			B&#236;nh
																																		</a>
																																	</h2>
																																	<div
																																		class="result-address">
																																		<div
																																			class="address">
																																			<span>
                                            <span>P105A C7 Nghĩa T&#226;n, Ng&#245; 140 Trần Tử B&#236;nh, P. Nghĩa T&#226;n</span>,
																																			<a
																																				href="/ha-noi/khu-vuc-quan-cau-giay">
																																				<span>Quận Cầu Giấy</span>
																																			</a>,
																																			<span>H&#224; Nội</span>
																																			</span>

																																		</div>
																																	</div>
																																</div>
																															</div>
																															<div
																																class="row-view-reviews">
																																<div
																																	class="items">
																																	<a class="avatar"
																																		href="/thanh-vien/Chi2k">
																																		<img src="https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg" />
                                    </a>
																																		<div
																																			class="content">
																																			<a
																																				href="/thanh-vien/Chi2k">
																																				<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Quỳnhchi&nbsp;Nguyễn
                                            </b>
																																			</a>
																																			<span>Thi thoảng đi ăn lại thì thấy chất lượng quán tốt hơn so vs lần trước mình ăn rồi.😛</span>
																																		</div>
																																</div>
																																<div
																																	class="items">
																																	<a class="avatar"
																																		href="/thanh-vien/Chi2k">
																																		<img src="https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg" />
                                    </a>
																																		<div
																																			class="content">
																																			<a
																																				href="/thanh-vien/Chi2k">
																																				<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Quỳnhchi&nbsp;Nguyễn
                                            </b>
																																			</a>
																																			<span>Quán mới đổi người  nấu hay sao ấy mà hôm mình ăn lẩu ếch lại đắt hơn mà nấu siêu nhiều mỡ, thề lần đầu tiên ăn thấy chán như thế😔</span>
																																		</div>
																																</div>
																															</div>
																															<div class="result-stats"
																																style="border-bottom: 1px solid #eee;height:24px;">
																																<div
																																	class="opentime-status">
																																	<span class="online"></span>
																																	Đang
																																	mở
																																	cửa
																																</div>

																															</div>
																															<div
																																class="result-stats">
																																<div
																																	class="row-view-users">
																																	<div
																																		class="stats">
																																		<a
																																			href="javascript:void(0)">
																																			<span class="fa fa-comment" style="font-weight: normal;"></span>
																																			<span>36</span>
																																		</a>
																																		<a
																																			class="link">
																																			<span class="fa fa-camera" style="font-weight: normal;padding-left:10px;"></span>
																																			<span>133</span>
																																		</a>
																																		<a
																																			href="javascript:void(0)">
																																			<span class="fa fa-bookmark" style="font-weight: normal; padding-left: 10px;"></span>
																																			<span>13</span>
																																		</a>
																																	</div>
																																	<div
																																		class="row-view-right2 reviews">
																																		<div
																																			class="directory-items-shortcut">
																																			<div>
																																				<a class="tool-custom-list-add otherlist "
																																					style=" float right;">
																																					<span class="fa fa-bookmark"></span>
																																					<span>Lưu</span>
																																				</a>
																																			</div>
																																		</div>
																																	</div>
																																</div>
																															</div>
																														</div>
																													</div>
																													<div style=""
																														class="row-item filter-result-item">
																														<div
																															class="ri-avatar result-image">
																															<a title="Ole - B&#225;nh Truyền Thống Nhật Bản"
																																href="/ha-noi/ole-banh-truyen-thong-nhat-ban"
																																target="_blank">
																																<img alt="Ole - B&#225;nh Truyền Thống Nhật Bản" src="https://images.foody.vn/res/g22/214740/prof/s640x400/foody-mobile-ole640-jpg-850-635949570629965289.jpg" />
                    </a>

																														</div>
																														<div
																															class="row-view-right">
																															<div
																																class="result-name">
																																<div
																																	class="status">
																																	<div
																																		class="point highlight-text">
																																		7.3
																																	</div>
																																	<div
																																		class="ratingtooltip">
																																		<div
																																			class="top-arrow">
																																			<img alt="" src="/style/images/icons/arrow-top.png">
                                </div>
																																		</div>
																																	</div>
																																	<div
																																		class="resname">
																																		<h2>
																																			<a title="Ole - B&#225;nh Truyền Thống Nhật Bản"
																																				href="/ha-noi/ole-banh-truyen-thong-nhat-ban"
																																				target="_blank">
																																				Ole
																																				-
																																				B&#225;nh
																																				Truyền
																																				Thống
																																				Nhật
																																				Bản
																																			</a>
																																		</h2>
																																		<div
																																			class="result-address">
																																			<div
																																				class="address">
																																				<span>
                                            <span>15 Trần B&#236;nh</span>,
																																				<a
																																					href="/ha-noi/khu-vuc-quan-cau-giay">
																																					<span>Quận Cầu Giấy</span>
																																				</a>,
																																				<span>H&#224; Nội</span>
																																				</span>

																																			</div>
																																		</div>
																																	</div>
																																</div>
																																<div
																																	class="row-view-reviews">
																																	<div
																																		class="items">
																																		<a class="avatar"
																																			href="/thanh-vien/Cuongmy">
																																			<img src="https://images.foody.vn/usr/g52/512100/avt/c50x50/beauty-upload-api-foody-avatar-5734e3fe-3efd-4703-aeec-083401b954c1-190814200612.jpg" />
                                    </a>
																																			<div
																																				class="content">
																																				<a
																																					href="/thanh-vien/Cuongmy">
																																					<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Cường&nbsp;My
                                            </b>
																																				</a>
																																				<span>Ngon sạch. Vọ trí hơi nóng. Nhân viên nhanh nhẹn vui vẻ. Cần trang trí không gian quán cho phù hợp hơn đẻ tránh tình trạng nóng quá tải khách</span>
																																			</div>
																																	</div>
																																	<div
																																		class="items">
																																		<a class="avatar"
																																			href="/thanh-vien/Hien_nt">
																																			<img src="https://images.foody.vn/usr/g913/9123375/avt/c50x50/beauty-upload-api-foody-avatar-394d790d-d30a-4769-a330-363891ecd622-191215142508.jpg" />
                                    </a>
																																			<div
																																				class="content">
																																				<a
																																					href="/thanh-vien/Hien_nt">
																																					<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Hien_nt&nbsp;
                                            </b>
																																				</a>
																																				<span>Hot dog khổng lồ ăn mãi hết. Vỏ rất giòn, nếu bạn nào sợ ngất thì cứ vô tư ăn vì dù chiên dầu nhưng k ngấy đâu nhé. Chị chủ chiên rất khéo vỏ vàng ruộm, sốt ngon cực đỉnh lun.</span>
																																			</div>
																																	</div>
																																</div>
																																<div class="result-stats"
																																	style="border-bottom: 1px solid #eee;height:24px;">
																																	<div
																																		class="opentime-status">
																																		<span class="online"></span>
																																		Đang
																																		mở
																																		cửa
																																	</div>

																																</div>
																																<div
																																	class="result-stats">
																																	<div
																																		class="row-view-users">
																																		<div
																																			class="stats">
																																			<a
																																				href="javascript:void(0)">
																																				<span class="fa fa-comment" style="font-weight: normal;"></span>
																																				<span>23</span>
																																			</a>
																																			<a
																																				class="link">
																																				<span class="fa fa-camera" style="font-weight: normal;padding-left:10px;"></span>
																																				<span>171</span>
																																			</a>
																																			<a
																																				href="javascript:void(0)">
																																				<span class="fa fa-bookmark" style="font-weight: normal; padding-left: 10px;"></span>
																																				<span>37</span>
																																			</a>
																																		</div>
																																		<div
																																			class="row-view-right2 reviews">
																																			<div
																																				class="directory-items-shortcut">
																																				<div>
																																					<a class="tool-custom-list-add otherlist "
																																						style=" float right;">
																																						<span class="fa fa-bookmark"></span>
																																						<span>Lưu</span>
																																					</a>
																																				</div>
																																			</div>
																																		</div>
																																	</div>
																																</div>
																															</div>
																														</div>
																														<div style=""
																															class="row-item filter-result-item">
																															<div
																																class="ri-avatar result-image">
																																<a title="B&#250;n Chả &amp; Nem Cua Bể - Y&#234;n H&#242;a"
																																	href="/ha-noi/bun-cha-nem-cua-be-yen-hoa"
																																	target="_blank">
																																	<img alt="B&#250;n Chả &amp; Nem Cua Bể - Y&#234;n H&#242;a" src="https://images.foody.vn/res/g27/264770/prof/s640x400/foody-mobile-nem-cua-be-6831-1432-565-636064356571448314.jpg" />
                    </a>

																															</div>
																															<div
																																class="row-view-right">
																																<div
																																	class="result-name">
																																	<div
																																		class="status">
																																		<div
																																			class="point highlight-text">
																																			7.2
																																		</div>
																																		<div
																																			class="ratingtooltip">
																																			<div
																																				class="top-arrow">
																																				<img alt="" src="/style/images/icons/arrow-top.png">
                                </div>
																																			</div>
																																		</div>
																																		<div
																																			class="resname">
																																			<h2>
																																				<a title="B&#250;n Chả &amp; Nem Cua Bể - Y&#234;n H&#242;a"
																																					href="/ha-noi/bun-cha-nem-cua-be-yen-hoa"
																																					target="_blank">
																																					B&#250;n
																																					Chả
																																					&amp;
																																					Nem
																																					Cua
																																					Bể
																																					-
																																					Y&#234;n
																																					H&#242;a
																																				</a>
																																			</h2>
																																			<div
																																				class="result-address">
																																				<div
																																					class="address">
																																					<span>
                                            <span>67 Y&#234;n H&#242;a, P. Y&#234;n H&#242;a</span>,
																																					<a
																																						href="/ha-noi/khu-vuc-quan-cau-giay">
																																						<span>Quận Cầu Giấy</span>
																																					</a>,
																																					<span>H&#224; Nội</span>
																																					</span>

																																				</div>
																																			</div>
																																		</div>
																																	</div>
																																	<div
																																		class="row-view-reviews">
																																		<div
																																			class="items">
																																			<a class="avatar"
																																				href="/thanh-vien/foodee_x1j5uvj3">
																																				<img src="https://images.foody.vn/usr/g1987/19869596/avt/c50x50/foody-avatar-654-637777768251432573.jpg" />
                                    </a>
																																				<div
																																					class="content">
																																					<a
																																						href="/thanh-vien/foodee_x1j5uvj3">
																																						<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Hiếu&nbsp;PCI
                                            </b>
																																					</a>
																																					<span>Làm ăn bát nháo vãi l, rau đéo có, bát đéo có đũa đéo có. ĂN BỐC À.
BÚN THÌ CHUA, DC 3 CÁI MIẾNG THỊT LÀM ANH bố m đói.</span>
																																				</div>
																																		</div>
																																		<div
																																			class="items">
																																			<a class="avatar"
																																				href="/thanh-vien/Chi2k">
																																				<img src="https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg" />
                                    </a>
																																				<div
																																					class="content">
																																					<a
																																						href="/thanh-vien/Chi2k">
																																						<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Quỳnhchi&nbsp;Nguyễn
                                            </b>
																																					</a>
																																					<span>Mình đặt 1 bún chả đầy đủ . Bún chả ăn ngon. Nước chấm để trong hộp nắp chắc chắn.</span>
																																				</div>
																																		</div>
																																	</div>
																																	<div class="result-stats"
																																		style="border-bottom: 1px solid #eee;height:24px;">
																																		<div class="opentime-status"
																																			style="color: #959595">
																																			<span class="offline"></span>
																																			Chưa
																																			mở
																																			cửa
																																		</div>

																																	</div>
																																	<div
																																		class="result-stats">
																																		<div
																																			class="row-view-users">
																																			<div
																																				class="stats">
																																				<a
																																					href="javascript:void(0)">
																																					<span class="fa fa-comment" style="font-weight: normal;"></span>
																																					<span>35</span>
																																				</a>
																																				<a
																																					class="link">
																																					<span class="fa fa-camera" style="font-weight: normal;padding-left:10px;"></span>
																																					<span>104</span>
																																				</a>
																																				<a
																																					href="javascript:void(0)">
																																					<span class="fa fa-bookmark" style="font-weight: normal; padding-left: 10px;"></span>
																																					<span>20</span>
																																				</a>
																																			</div>
																																			<div
																																				class="row-view-right2 reviews">
																																				<div
																																					class="directory-items-shortcut">
																																					<div>
																																						<a class="tool-custom-list-add otherlist "
																																							style=" float right;">
																																							<span class="fa fa-bookmark"></span>
																																							<span>Lưu</span>
																																						</a>
																																					</div>
																																				</div>
																																			</div>
																																		</div>
																																	</div>
																																</div>
																															</div>
																															<div style=""
																																class="row-item filter-result-item">
																																<div
																																	class="ri-avatar result-image">
																																	<a title="B&#250;n Đậu C&#250;c Cu - Ho&#224;ng Quốc Việt"
																																		href="/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet"
																																		target="_blank">
																																		<img alt="B&#250;n Đậu C&#250;c Cu - Ho&#224;ng Quốc Việt" src="https://images.foody.vn/res/g77/762583/prof/s640x400/image-e3bc5f75-200910115833.jpeg" />
                    </a>

																																</div>
																																<div
																																	class="row-view-right">
																																	<div
																																		class="result-name">
																																		<div
																																			class="status">
																																			<div
																																				class="point highlight-text">
																																				7.9
																																			</div>
																																			<div
																																				class="ratingtooltip">
																																				<div
																																					class="top-arrow">
																																					<img alt="" src="/style/images/icons/arrow-top.png">
                                </div>
																																				</div>
																																			</div>
																																			<div
																																				class="resname">
																																				<h2>
																																					<a title="B&#250;n Đậu C&#250;c Cu - Ho&#224;ng Quốc Việt"
																																						href="/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet"
																																						target="_blank">
																																						B&#250;n
																																						Đậu
																																						C&#250;c
																																						Cu
																																						-
																																						Ho&#224;ng
																																						Quốc
																																						Việt
																																					</a>
																																				</h2>
																																				<div
																																					class="result-address">
																																					<div
																																						class="address">
																																						<span>
                                            <span>2/421 Ho&#224;ng Quốc Việt, P. Nghĩa T&#226;n</span>,
																																						<a
																																							href="/ha-noi/khu-vuc-quan-cau-giay">
																																							<span>Quận Cầu Giấy</span>
																																						</a>,
																																						<span>H&#224; Nội</span>
																																						</span>

																																					</div>
																																				</div>
																																			</div>
																																		</div>
																																		<div
																																			class="row-view-reviews">
																																			<div
																																				class="items">
																																				<a class="avatar"
																																					href="/thanh-vien/foodee_pxcljj8i">
																																					<img src="https://images.foody.vn/usr/g1831/18306374/avt/c50x50/beauty-upload-api-foody-avatar-423ea137-da03-4d9c-b025-3c1d959dd4d6-191130193559.jpg" />
                                    </a>
																																					<div
																																						class="content">
																																						<a
																																							href="/thanh-vien/foodee_pxcljj8i">
																																							<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Nguyễn&nbsp;Linh
                                            </b>
																																						</a>
																																						<span>Rau sống héo úa hỏng, quất thì toàn thối, thiếu dưa chuột. Ăn bún đậu mắm tôm mà k có quất thì mất vị quá. Quán làm chán quá!</span>
																																					</div>
																																			</div>
																																			<div
																																				class="items">
																																				<a class="avatar"
																																					href="/thanh-vien/foodee_9dicnbry">
																																					<img src="https://images.foody.vn/default/s50/user-default-female.png" />
                                    </a>
																																					<div
																																						class="content">
																																						<a
																																							href="/thanh-vien/foodee_9dicnbry">
																																							<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Quỳnh&nbsp;
                                            </b>
																																						</a>
																																						<span>Ngon , vừa miệng❤️giá cả hợp lí                                                </span>
																																					</div>
																																			</div>
																																		</div>
																																		<div class="result-stats"
																																			style="border-bottom: 1px solid #eee;height:24px;">
																																			<div
																																				class="opentime-status">
																																				<span class="online"></span>
																																				Đang
																																				mở
																																				cửa
																																			</div>

																																		</div>
																																		<div
																																			class="result-stats">
																																			<div
																																				class="row-view-users">
																																				<div
																																					class="stats">
																																					<a
																																						href="javascript:void(0)">
																																						<span class="fa fa-comment" style="font-weight: normal;"></span>
																																						<span>42</span>
																																					</a>
																																					<a
																																						class="link">
																																						<span class="fa fa-camera" style="font-weight: normal;padding-left:10px;"></span>
																																						<span>104</span>
																																					</a>
																																					<a
																																						href="javascript:void(0)">
																																						<span class="fa fa-bookmark" style="font-weight: normal; padding-left: 10px;"></span>
																																						<span>14</span>
																																					</a>
																																				</div>
																																				<div
																																					class="row-view-right2 reviews">
																																					<div
																																						class="directory-items-shortcut">
																																						<div>
																																							<a class="tool-custom-list-add otherlist "
																																								style=" float right;">
																																								<span class="fa fa-bookmark"></span>
																																								<span>Lưu</span>
																																							</a>
																																						</div>
																																					</div>
																																				</div>
																																			</div>
																																		</div>
																																	</div>
																																</div>
																																<div style=""
																																	class="row-item filter-result-item">
																																	<div
																																		class="ri-avatar result-image">
																																		<a title="Phở Cuốn Ngũ X&#227; - Duy T&#226;n"
																																			href="/ha-noi/pho-cuon-ngu-xa-duy-tan"
																																			target="_blank">
																																			<img alt="Phở Cuốn Ngũ X&#227; - Duy T&#226;n" src="https://images.foody.vn/res/g11/109338/prof/s640x400/foody-mobile-pho-cuon2-jpg-934-635550098425249236.jpg" />
                    </a>

																																	</div>
																																	<div
																																		class="row-view-right">
																																		<div
																																			class="result-name">
																																			<div
																																				class="status">
																																				<div
																																					class="point highlight-text">
																																					6.4
																																				</div>
																																				<div
																																					class="ratingtooltip">
																																					<div
																																						class="top-arrow">
																																						<img alt="" src="/style/images/icons/arrow-top.png">
                                </div>
																																					</div>
																																				</div>
																																				<div
																																					class="resname">
																																					<h2>
																																						<a title="Phở Cuốn Ngũ X&#227; - Duy T&#226;n"
																																							href="/ha-noi/pho-cuon-ngu-xa-duy-tan"
																																							target="_blank">
																																							Phở
																																							Cuốn
																																							Ngũ
																																							X&#227;
																																							-
																																							Duy
																																							T&#226;n
																																						</a>
																																					</h2>
																																					<div
																																						class="result-address">
																																						<div
																																							class="address">
																																							<span>
                                            <span>66 Duy T&#226;n, P. Dịch Vọng Hậu</span>,
																																							<a
																																								href="/ha-noi/khu-vuc-quan-cau-giay">
																																								<span>Quận Cầu Giấy</span>
																																							</a>,
																																							<span>H&#224; Nội</span>
																																							</span>

																																						</div>
																																					</div>
																																				</div>
																																			</div>
																																			<div
																																				class="row-view-reviews">
																																				<div
																																					class="items">
																																					<a class="avatar"
																																						href="/thanh-vien/foodee_u32az83y">
																																						<img src="https://images.foody.vn/default/s50/user-default-female.png" />
                                    </a>
																																						<div
																																							class="content">
																																							<a
																																								href="/thanh-vien/foodee_u32az83y">
																																								<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Trang Ho&#224;ng&nbsp;
                                            </b>
																																							</a>
																																							<span>Ngày trước chưa dịch, buổi trưa ra đây ăn rất đông. Đợt này chỉ đc bán mang về nên chắc cũng đỡ, mình thấy ship nhanh và khá cẩn thận. Đồ ăn vẫn ổn, phù hợp giá tiền. Mình gọi phở chiên phồng và 1 cốc...</span>
																																						</div>
																																				</div>
																																				<div
																																					class="items">
																																					<a class="avatar"
																																						href="/thanh-vien/Chi2k">
																																						<img src="https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg" />
                                    </a>
																																						<div
																																							class="content">
																																							<a
																																								href="/thanh-vien/Chi2k">
																																								<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Quỳnhchi&nbsp;Nguyễn
                                            </b>
																																							</a>
																																							<span>-phở cuốn ở đây ăn khá đầy, ăn 10 cái là no căng bụng luôn ấy. Thấy review khen chê thất thường , nhưng mình thấy ăn ở quán vẫn oke .</span>
																																						</div>
																																				</div>
																																			</div>
																																			<div class="result-stats"
																																				style="border-bottom: 1px solid #eee;height:24px;">
																																				<div
																																					class="opentime-status">
																																					<span class="online"></span>
																																					Đang
																																					mở
																																					cửa
																																				</div>

																																			</div>
																																			<div
																																				class="result-stats">
																																				<div
																																					class="row-view-users">
																																					<div
																																						class="stats">
																																						<a
																																							href="javascript:void(0)">
																																							<span class="fa fa-comment" style="font-weight: normal;"></span>
																																							<span>31</span>
																																						</a>
																																						<a
																																							class="link">
																																							<span class="fa fa-camera" style="font-weight: normal;padding-left:10px;"></span>
																																							<span>106</span>
																																						</a>
																																						<a
																																							href="javascript:void(0)">
																																							<span class="fa fa-bookmark" style="font-weight: normal; padding-left: 10px;"></span>
																																							<span>38</span>
																																						</a>
																																					</div>
																																					<div
																																						class="row-view-right2 reviews">
																																						<div
																																							class="directory-items-shortcut">
																																							<div>
																																								<a class="tool-custom-list-add otherlist "
																																									style=" float right;">
																																									<span class="fa fa-bookmark"></span>
																																									<span>Lưu</span>
																																								</a>
																																							</div>
																																						</div>
																																					</div>
																																				</div>
																																			</div>
																																		</div>
																																	</div>
																																	<div style=""
																																		class="row-item filter-result-item">
																																		<div
																																			class="ri-avatar result-image">
																																			<a title="X&#244;i T&#225;m - Trần Duy Hưng"
																																				href="/ha-noi/xoi-tam-thai-ha"
																																				target="_blank">
																																				<img alt="X&#244;i T&#225;m - Trần Duy Hưng" src="https://images.foody.vn/res/g65/647491/prof/s640x400/foody-mobile-xoi-tam-jpg-523-636410905562883010.jpg" />
                    </a>

																																		</div>
																																		<div
																																			class="row-view-right">
																																			<div
																																				class="result-name">
																																				<div
																																					class="status">
																																					<div
																																						class="point highlight-text">
																																						6.4
																																					</div>
																																					<div
																																						class="ratingtooltip">
																																						<div
																																							class="top-arrow">
																																							<img alt="" src="/style/images/icons/arrow-top.png">
                                </div>
																																						</div>
																																					</div>
																																					<div
																																						class="resname">
																																						<h2>
																																							<a title="X&#244;i T&#225;m - Trần Duy Hưng"
																																								href="/ha-noi/xoi-tam-thai-ha"
																																								target="_blank">
																																								X&#244;i
																																								T&#225;m
																																								-
																																								Trần
																																								Duy
																																								Hưng
																																							</a>
																																						</h2>
																																						<div
																																							class="result-address">
																																							<div
																																								class="address">
																																								<span>
                                            <span>2 Hẻm 32 Ng&#225;ch 5 Ng&#245; 204 Trần Duy Hưng, P. Trung H&#242;a</span>,
																																								<a
																																									href="/ha-noi/khu-vuc-quan-cau-giay">
																																									<span>Quận Cầu Giấy</span>
																																								</a>,
																																								<span>H&#224; Nội</span>
																																								</span>

																																							</div>
																																						</div>
																																					</div>
																																				</div>
																																				<div
																																					class="row-view-reviews">
																																					<div
																																						class="items">
																																						<a class="avatar"
																																							href="/thanh-vien/hoanganh8790">
																																							<img src="https://images.foody.vn/usr/g167/1662701/avt/c50x50/beauty-upload-api-foody-avatar-62f86f2f-250c-407d-be57-92ccccc540d9-191025131450.jpg" />
                                    </a>
																																							<div
																																								class="content">
																																								<a
																																									href="/thanh-vien/hoanganh8790">
																																									<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Trang&nbsp;Hoang
                                            </b>
																																								</a>
																																								<span>Xôi Tám - 322 Thái Hà 

Bạn sẽ order các topping và xôi theo ý muốn , có hai loại xôi là xôi xéo (15k) và xôi trắng(10k) xôi dẻo và ngon lắm nha. CÒn topping thì giá dao động từ 8k-15k tuỳ loại : xá x...</span>
																																							</div>
																																					</div>
																																					<div
																																						class="items">
																																						<a class="avatar"
																																							href="/thanh-vien/foodee_667zapgi">
																																							<img src="https://images.foody.vn/usr/g1549/15480563/avt/c50x50/beauty-upload-api-foody-avatar-482e93a1-e57a-4ff9-bf2d-b6d7e3176eb0-191216001840.jpg" />
                                    </a>
																																							<div
																																								class="content">
																																								<a
																																									href="/thanh-vien/foodee_667zapgi">
																																									<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Anhh&nbsp;Linhh
                                            </b>
																																								</a>
																																								<span>Thật không thể tin vào mắt mình..! Xôi chưa bằng 1 nắm tay :(( sẽ không có lần t2 hic</span>
																																							</div>
																																					</div>
																																				</div>
																																				<div class="result-stats"
																																					style="border-bottom: 1px solid #eee;height:24px;">
																																					<div
																																						class="opentime-status">
																																						<span class="online"></span>
																																						Đang
																																						mở
																																						cửa
																																					</div>

																																				</div>
																																				<div
																																					class="result-stats">
																																					<div
																																						class="row-view-users">
																																						<div
																																							class="stats">
																																							<a
																																								href="javascript:void(0)">
																																								<span class="fa fa-comment" style="font-weight: normal;"></span>
																																								<span>28</span>
																																							</a>
																																							<a
																																								class="link">
																																								<span class="fa fa-camera" style="font-weight: normal;padding-left:10px;"></span>
																																								<span>111</span>
																																							</a>
																																							<a
																																								href="javascript:void(0)">
																																								<span class="fa fa-bookmark" style="font-weight: normal; padding-left: 10px;"></span>
																																								<span>36</span>
																																							</a>
																																						</div>
																																						<div
																																							class="row-view-right2 reviews">
																																							<div
																																								class="directory-items-shortcut">
																																								<div>
																																									<a class="tool-custom-list-add otherlist "
																																										style=" float right;">
																																										<span class="fa fa-bookmark"></span>
																																										<span>Lưu</span>
																																									</a>
																																								</div>
																																							</div>
																																						</div>
																																					</div>
																																				</div>
																																			</div>
																																		</div>
																																		<div style=""
																																			class="row-item filter-result-item">
																																			<div
																																				class="ri-avatar result-image">
																																				<a title="Safodi - Buffet Lẩu Hơi &amp; Lẩu Nướng"
																																					href="/ha-noi/safodi-buffet-lau-hoi-lau-nuong"
																																					target="_blank">
																																					<img alt="Safodi - Buffet Lẩu Hơi &amp; Lẩu Nướng" src="https://images.foody.vn/res/g105/1042834/prof/s640x400/file_restaurant_photo_tbzf_16576-bf99d9bf-220712134254.jpg" />
                    </a>

																																			</div>
																																			<div
																																				class="row-view-right">
																																				<div
																																					class="result-name">
																																					<div
																																						class="status">
																																						<div
																																							class="point highlight-text">
																																							8.7
																																						</div>
																																						<div
																																							class="ratingtooltip">
																																							<div
																																								class="top-arrow">
																																								<img alt="" src="/style/images/icons/arrow-top.png">
                                </div>
																																							</div>
																																						</div>
																																						<div
																																							class="resname">
																																							<h2>
																																								<a title="Safodi - Buffet Lẩu Hơi &amp; Lẩu Nướng"
																																									href="/ha-noi/safodi-buffet-lau-hoi-lau-nuong"
																																									target="_blank">
																																									Safodi
																																									-
																																									Buffet
																																									Lẩu
																																									Hơi
																																									&amp;
																																									Lẩu
																																									Nướng
																																								</a>
																																							</h2>
																																							<div
																																								class="result-address">
																																								<div
																																									class="address">
																																									<span>
                                            <span>273 T&#244; Hiệu, P. Dịch Vọng Hậu</span>,
																																									<a
																																										href="/ha-noi/khu-vuc-quan-cau-giay">
																																										<span>Quận Cầu Giấy</span>
																																									</a>,
																																									<span>H&#224; Nội</span>
																																									</span>

																																								</div>
																																							</div>
																																						</div>
																																					</div>
																																					<div
																																						class="row-view-reviews">
																																						<div
																																							class="items">
																																							<a class="avatar"
																																								href="/thanh-vien/foodee_d9s9jwjp">
																																								<img src="https://images.foody.vn/usr/g2005/20049115/avt/c50x50/beauty-upload-api-foody-avatar-723ab79f-3a4f-4453-a455-948d19f153fd-200504094741.jpg" />
                                    </a>
																																								<div
																																									class="content">
																																									<a
																																										href="/thanh-vien/foodee_d9s9jwjp">
																																										<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Hiền&nbsp;L&#234;
                                            </b>
																																									</a>
																																									<span>Mình đến lúc gần 8h tối, khách vãng lai may vẫn còn bàn. Phục vụ tận tình, lẩu ra nhanh, lên đồ cũng nhanh. Mình gọi suất 99k có cá viên bò viên, ba chỉ bò, thịt lợn, ngao, đậu, váng đậu, xúc xích, ra...</span>
																																								</div>
																																						</div>
																																						<div
																																							class="items">
																																							<a class="avatar"
																																								href="/thanh-vien/terrycjtroller">
																																								<img src="https://images.foody.vn/usr/g2228/22274735/avt/c50x50/foody-avatar-445-637449429964270545.jpg" />
                                    </a>
																																								<div
																																									class="content">
																																									<a
																																										href="/thanh-vien/terrycjtroller">
																																										<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Huyen Hoa&nbsp;Nguyen
                                            </b>
																																									</a>
																																									<span>Với mình thì lẩu ở đây khá ngon , vị đậm đà . Chiều buồn buồn se mát thế này mà húp nước lẩu chua ngọt bên quán thì quá đã . Giá cũng hợp lí . Khá hài lòng .</span>
																																								</div>
																																						</div>
																																					</div>
																																					<div class="result-stats"
																																						style="border-bottom: 1px solid #eee;height:24px;">
																																						<div
																																							class="opentime-status">
																																							<span class="online"></span>
																																							Đang
																																							mở
																																							cửa
																																						</div>

																																					</div>
																																					<div
																																						class="result-stats">
																																						<div
																																							class="row-view-users">
																																							<div
																																								class="stats">
																																								<a
																																									href="javascript:void(0)">
																																									<span class="fa fa-comment" style="font-weight: normal;"></span>
																																									<span>30</span>
																																								</a>
																																								<a
																																									class="link">
																																									<span class="fa fa-camera" style="font-weight: normal;padding-left:10px;"></span>
																																									<span>29</span>
																																								</a>
																																								<a
																																									href="javascript:void(0)">
																																									<span class="fa fa-bookmark" style="font-weight: normal; padding-left: 10px;"></span>
																																									<span>38</span>
																																								</a>
																																							</div>
																																							<div
																																								class="row-view-right2 reviews">
																																								<div
																																									class="directory-items-shortcut">
																																									<div>
																																										<a class="tool-custom-list-add otherlist "
																																											style=" float right;">
																																											<span class="fa fa-bookmark"></span>
																																											<span>Lưu</span>
																																										</a>
																																									</div>
																																								</div>
																																							</div>
																																						</div>
																																					</div>
																																				</div>
																																			</div>
																																			<div style=""
																																				class="row-item filter-result-item">
																																				<div
																																					class="ri-avatar result-image">
																																					<a title="Phở Định 3 - Dịch Vọng Hậu"
																																						href="/ha-noi/pho-dinh-3-dich-vong-hau"
																																						target="_blank">
																																						<img alt="Phở Định 3 - Dịch Vọng Hậu" src="https://images.foody.vn/res/g3/29272/prof/s640x400/foody-mobile-pho-jpg-932-635917368774327730.jpg" />
                    </a>

																																				</div>
																																				<div
																																					class="row-view-right">
																																					<div
																																						class="result-name">
																																						<div
																																							class="status">
																																							<div
																																								class="point highlight-text">
																																								7.1
																																							</div>
																																							<div
																																								class="ratingtooltip">
																																								<div
																																									class="top-arrow">
																																									<img alt="" src="/style/images/icons/arrow-top.png">
                                </div>
																																								</div>
																																							</div>
																																							<div
																																								class="resname">
																																								<h2>
																																									<a title="Phở Định 3 - Dịch Vọng Hậu"
																																										href="/ha-noi/pho-dinh-3-dich-vong-hau"
																																										target="_blank">
																																										Phở
																																										Định
																																										3
																																										-
																																										Dịch
																																										Vọng
																																										Hậu
																																									</a>
																																								</h2>
																																								<div
																																									class="result-address">
																																									<div
																																										class="address">
																																										<span>
                                            <span>36 Phố Dịch Vọng Hậu, P. Dịch Vọng Hậu</span>,
																																										<a
																																											href="/ha-noi/khu-vuc-quan-cau-giay">
																																											<span>Quận Cầu Giấy</span>
																																										</a>,
																																										<span>H&#224; Nội</span>
																																										</span>

																																									</div>
																																								</div>
																																							</div>
																																						</div>
																																						<div
																																							class="row-view-reviews">
																																							<div
																																								class="items">
																																								<a class="avatar"
																																									href="/thanh-vien/billgates_2028">
																																									<img src="https://images.foody.vn/usr/g1489/14880419/avt/c50x50/beauty-upload-api-foody-avatar-7f2bc26c-9b7d-411d-ad51-e8a66585c493-191122121319.jpg" />
                                    </a>
																																									<div
																																										class="content">
																																										<a
																																											href="/thanh-vien/billgates_2028">
																																											<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Kh&#225;nh&nbsp;Nguyễn Gia
                                            </b>
																																										</a>
																																										<span>Phở định giờ ăn chán , thái độ từ nhân viên đến chủ lồi lõm ! 
Hôm mình đi ăn 3 ngừoi là gần cuối canh , bánh phở cứng , nước mặn ko sắc đc như xưa ! 
Đang ăn thì chủ quán tắt điện đánh phụp như đuổi ...</span>
																																									</div>
																																							</div>
																																							<div
																																								class="items">
																																								<a class="avatar"
																																									href="/thanh-vien/rosecloud121">
																																									<img src="https://images.foody.vn/usr/g131/1301649/avt/c50x50/ruka-avatar-711-637173934938683397.jpg" />
                                    </a>
																																									<div
																																										class="content">
																																										<a
																																											href="/thanh-vien/rosecloud121">
																																											<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Mint&nbsp;Ng
                                            </b>
																																										</a>
																																										<span>sáng nay đi ăn phở nạm gầu, thấy quán vẫn tấp nập khách ra vào mặc kệ covid 😀 menu có nhiều lựa chọn, giá trung bình 50k, phở lõi thì 70k. còn có cả phở không thịt và phở cho trẻ em, quẩy 1 người và ...</span>
																																									</div>
																																							</div>
																																						</div>
																																						<div class="result-stats"
																																							style="border-bottom: 1px solid #eee;height:24px;">
																																							<div
																																								class="opentime-status">
																																								<span class="online"></span>
																																								Đang
																																								mở
																																								cửa
																																							</div>

																																						</div>
																																						<div
																																							class="result-stats">
																																							<div
																																								class="row-view-users">
																																								<div
																																									class="stats">
																																									<a
																																										href="javascript:void(0)">
																																										<span class="fa fa-comment" style="font-weight: normal;"></span>
																																										<span>34</span>
																																									</a>
																																									<a
																																										class="link">
																																										<span class="fa fa-camera" style="font-weight: normal;padding-left:10px;"></span>
																																										<span>98</span>
																																									</a>
																																									<a
																																										href="javascript:void(0)">
																																										<span class="fa fa-bookmark" style="font-weight: normal; padding-left: 10px;"></span>
																																										<span>25</span>
																																									</a>
																																								</div>
																																								<div
																																									class="row-view-right2 reviews">
																																									<div
																																										class="directory-items-shortcut">
																																										<div>
																																											<a class="tool-custom-list-add otherlist "
																																												style=" float right;">
																																												<span class="fa fa-bookmark"></span>
																																												<span>Lưu</span>
																																											</a>
																																										</div>
																																									</div>
																																								</div>
																																							</div>
																																						</div>
																																					</div>
																																				</div>
																																				<div style=""
																																					class="row-item filter-result-item">
																																					<div
																																						class="ri-avatar result-image">
																																						<a title="Song Nguyệt - B&#225;nh X&#232;o &amp; Nem Lụi - T&#244; Hiệu"
																																							href="/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu"
																																							target="_blank">
																																							<img alt="Song Nguyệt - B&#225;nh X&#232;o &amp; Nem Lụi - T&#244; Hiệu" src="https://images.foody.vn/res/g24/231953/prof/s640x400/foody-mobile-34-jpg-265-635974352692854698.jpg" />
                    </a>

																																					</div>
																																					<div
																																						class="row-view-right">
																																						<div
																																							class="result-name">
																																							<div
																																								class="status">
																																								<div
																																									class="point highlight-text">
																																									7.0
																																								</div>
																																								<div
																																									class="ratingtooltip">
																																									<div
																																										class="top-arrow">
																																										<img alt="" src="/style/images/icons/arrow-top.png">
                                </div>
																																									</div>
																																								</div>
																																								<div
																																									class="resname">
																																									<h2>
																																										<a title="Song Nguyệt - B&#225;nh X&#232;o &amp; Nem Lụi - T&#244; Hiệu"
																																											href="/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu"
																																											target="_blank">
																																											Song
																																											Nguyệt
																																											-
																																											B&#225;nh
																																											X&#232;o
																																											&amp;
																																											Nem
																																											Lụi
																																											-
																																											T&#244;
																																											Hiệu
																																										</a>
																																									</h2>
																																									<div
																																										class="result-address">
																																										<div
																																											class="address">
																																											<span>
                                            <span>115 B7 T&#244; Hiệu, P. Nghĩa T&#226;n</span>,
																																											<a
																																												href="/ha-noi/khu-vuc-quan-cau-giay">
																																												<span>Quận Cầu Giấy</span>
																																											</a>,
																																											<span>H&#224; Nội</span>
																																											</span>

																																										</div>
																																									</div>
																																								</div>
																																							</div>
																																							<div
																																								class="row-view-reviews">
																																								<div
																																									class="items">
																																									<a class="avatar"
																																										href="/thanh-vien/foodee_om9w0plt">
																																										<img src="https://images.foody.vn/default/s50/user-default-female.png" />
                                    </a>
																																										<div
																																											class="content">
																																											<a
																																												href="/thanh-vien/foodee_om9w0plt">
																																												<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Duy&nbsp;
                                            </b>
																																											</a>
																																											<span>Quán hơi bị ngon nha. Giao hàng nhanh. Bánh xèo chuẩn vị, giòn, ít dầu so với quán khác. Ngon nhất vẫn là nem lụi</span>
																																										</div>
																																								</div>
																																								<div
																																									class="items">
																																									<a class="avatar"
																																										href="/thanh-vien/foodee_fohig9fa">
																																										<img src="https://images.foody.vn/usr/g1905/19046663/avt/c50x50/beauty-upload-api-foody-avatar-bee17315-9f84-4ab5-9c7a-04e0f40d6617-200207173213.jpg" />
                                    </a>
																																										<div
																																											class="content">
																																											<a
																																												href="/thanh-vien/foodee_fohig9fa">
																																												<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Dũng&nbsp;Th&#225;i Việt
                                            </b>
																																											</a>
																																											<span>Ngày xưa đây là quán tủ của  mình, từ hồi nem còn 5k 1 cái, mà về sau tăng lên 6k vẫn ok, nhưng dạo gần đây mấy lát xoài cắt quá dày nên ăn ko đc ngon, đỉnh điểm lad hôm qua gọi đĩa nem ăn vừa nguội v...</span>
																																										</div>
																																								</div>
																																							</div>
																																							<div class="result-stats"
																																								style="border-bottom: 1px solid #eee;height:24px;">
																																								<div
																																									class="opentime-status">
																																									<span class="online"></span>
																																									Đang
																																									mở
																																									cửa
																																								</div>

																																							</div>
																																							<div
																																								class="result-stats">
																																								<div
																																									class="row-view-users">
																																									<div
																																										class="stats">
																																										<a
																																											href="javascript:void(0)">
																																											<span class="fa fa-comment" style="font-weight: normal;"></span>
																																											<span>32</span>
																																										</a>
																																										<a
																																											class="link">
																																											<span class="fa fa-camera" style="font-weight: normal;padding-left:10px;"></span>
																																											<span>74</span>
																																										</a>
																																										<a
																																											href="javascript:void(0)">
																																											<span class="fa fa-bookmark" style="font-weight: normal; padding-left: 10px;"></span>
																																											<span>35</span>
																																										</a>
																																									</div>
																																									<div
																																										class="row-view-right2 reviews">
																																										<div
																																											class="directory-items-shortcut">
																																											<div>
																																												<a class="tool-custom-list-add otherlist "
																																													style=" float right;">
																																													<span class="fa fa-bookmark"></span>
																																													<span>Lưu</span>
																																												</a>
																																											</div>
																																										</div>
																																									</div>
																																								</div>
																																							</div>
																																						</div>
																																					</div>
																																					<div style=""
																																						class="row-item filter-result-item">
																																						<div
																																							class="ri-avatar result-image">
																																							<a title="Phong Th&#224;nhh Qu&#225;n - Qu&#225;n Ăn - Phan Văn Trường"
																																								href="/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp"
																																								target="_blank">
																																								<img alt="Phong Th&#224;nhh Qu&#225;n - Qu&#225;n Ăn - Phan Văn Trường" src="https://images.foody.vn/res/g100003/1000027868/prof/s640x400/file_restaurant_photo_ykxn_16254-2fdda806-210705174327.jpeg" />
                    </a>

																																						</div>
																																						<div
																																							class="row-view-right">
																																							<div
																																								class="result-name">
																																								<div
																																									class="status">
																																									<div
																																										class="point highlight-text">
																																										9.6
																																									</div>
																																									<div
																																										class="ratingtooltip">
																																										<div
																																											class="top-arrow">
																																											<img alt="" src="/style/images/icons/arrow-top.png">
                                </div>
																																										</div>
																																									</div>
																																									<div
																																										class="resname">
																																										<h2>
																																											<a title="Phong Th&#224;nhh Qu&#225;n - Qu&#225;n Ăn - Phan Văn Trường"
																																												href="/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp"
																																												target="_blank">
																																												Phong
																																												Th&#224;nhh
																																												Qu&#225;n
																																												-
																																												Qu&#225;n
																																												Ăn
																																												-
																																												Phan
																																												Văn
																																												Trường
																																											</a>
																																										</h2>
																																										<div
																																											class="result-address">
																																											<div
																																												class="address">
																																												<span>
                                            <span>36 ng&#245; 24  Phan Văn Trường, P.Dịch Vọng Hậu</span>,
																																												<a
																																													href="/ha-noi/khu-vuc-quan-cau-giay">
																																													<span>Quận Cầu Giấy</span>
																																												</a>,
																																												<span>H&#224; Nội</span>
																																												</span>

																																											</div>
																																										</div>
																																									</div>
																																								</div>
																																								<div
																																									class="row-view-reviews">
																																									<div
																																										class="items">
																																										<a class="avatar"
																																											href="/thanh-vien/giangxoan11112706">
																																											<img src="https://images.foody.vn/usr/g101/1001288/avt/c50x50/beauty-upload-api-foody-avatar-e4ff95c4-6f91-4152-b32f-99773576b5ce-191025125259.jpg" />
                                    </a>
																																											<div
																																												class="content">
																																												<a
																																													href="/thanh-vien/giangxoan11112706">
																																													<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Nguyễn&nbsp;T.Giang
                                            </b>
																																												</a>
																																												<span>Mình đặt cho anh xã ăn mà anh khen nức nở                                      </span>
																																											</div>
																																									</div>
																																									<div
																																										class="items">
																																										<a class="avatar"
																																											href="/thanh-vien/Thanh_tam_pham_thi">
																																											<img src="https://images.foody.vn/usr/g2330/23299868/avt/c50x50/thanh_tam_pham_thi-avatar-342-637506191180367188.jpg" />
                                    </a>
																																											<div
																																												class="content">
																																												<a
																																													href="/thanh-vien/Thanh_tam_pham_thi">
																																													<b style="display:inherit" data-bind="text:OwnerFullName">
                                                Thanh T&#226;m Phạm Thị&nbsp;
                                            </b>
																																												</a>
																																												<span>Cơm rất ngon , sạch sẽ , làm nhanh , nước sốt rất chi là ưnggg nhé 🍗🍗🍗🍗    </span>
																																											</div>
																																									</div>
																																								</div>
																																								<div class="result-stats"
																																									style="border-bottom: 1px solid #eee;height:24px;">
																																									<div
																																										class="opentime-status">
																																										<span class="online"></span>
																																										Đang
																																										mở
																																										cửa
																																									</div>

																																								</div>
																																								<div
																																									class="result-stats">
																																									<div
																																										class="row-view-users">
																																										<div
																																											class="stats">
																																											<a
																																												href="javascript:void(0)">
																																												<span class="fa fa-comment" style="font-weight: normal;"></span>
																																												<span>172</span>
																																											</a>
																																											<a
																																												class="link">
																																												<span class="fa fa-camera" style="font-weight: normal;padding-left:10px;"></span>
																																												<span>9</span>
																																											</a>
																																											<a
																																												href="javascript:void(0)">
																																												<span class="fa fa-bookmark" style="font-weight: normal; padding-left: 10px;"></span>
																																												<span>4</span>
																																											</a>
																																										</div>
																																										<div
																																											class="row-view-right2 reviews">
																																											<div
																																												class="directory-items-shortcut">
																																												<div>
																																													<a class="tool-custom-list-add otherlist "
																																														style=" float right;">
																																														<span class="fa fa-bookmark"></span>
																																														<span>Lưu</span>
																																													</a>
																																												</div>
																																											</div>
																																										</div>
																																									</div>
																																								</div>
																																							</div>
																																						</div>
																																					</div>
																																				</div>
																																			</div>
																																			<div style="width:1025px"
																																				data-bind="visible:appending()">
																																				<div
																																					class="row-view">
																																					<div
																																						class="filter-results">
																																						<div
																																							class="pre-row-item filter-result-item">
																																							<div
																																								class="pre-avatar animated-bg-light">
																																							</div>
																																							<div
																																								class="pre-items-content">
																																								<div
																																									class="pre-review-points animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar medium animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar long animated-bg">
																																								</div>
																																							</div>
																																							<div
																																								class="pre-items-content">
																																								<div
																																									class="pre-review-points animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar medium animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar long animated-bg">
																																								</div>
																																							</div>
																																						</div>
																																						<div
																																							class="pre-row-item filter-result-item">
																																							<div
																																								class="pre-avatar animated-bg-light">
																																							</div>
																																							<div
																																								class="pre-items-content">
																																								<div
																																									class="pre-review-points animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar medium animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar long animated-bg">
																																								</div>
																																							</div>
																																							<div
																																								class="pre-items-content">
																																								<div
																																									class="pre-review-points animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar medium animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar long animated-bg">
																																								</div>
																																							</div>
																																						</div>
																																						<div
																																							class="pre-row-item filter-result-item">
																																							<div
																																								class="pre-avatar animated-bg-light">
																																							</div>
																																							<div
																																								class="pre-items-content">
																																								<div
																																									class="pre-review-points animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar medium animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar long animated-bg">
																																								</div>
																																							</div>
																																							<div
																																								class="pre-items-content">
																																								<div
																																									class="pre-review-points animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar medium animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar long animated-bg">
																																								</div>
																																							</div>
																																						</div>
																																						<div
																																							class="pre-row-item filter-result-item">
																																							<div
																																								class="pre-avatar animated-bg-light">
																																							</div>
																																							<div
																																								class="pre-items-content">
																																								<div
																																									class="pre-review-points animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar medium animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar long animated-bg">
																																								</div>
																																							</div>
																																							<div
																																								class="pre-items-content">
																																								<div
																																									class="pre-review-points animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar medium animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar long animated-bg">
																																								</div>
																																							</div>
																																						</div>
																																						<div
																																							class="pre-row-item filter-result-item">
																																							<div
																																								class="pre-avatar animated-bg-light">
																																							</div>
																																							<div
																																								class="pre-items-content">
																																								<div
																																									class="pre-review-points animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar medium animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar long animated-bg">
																																								</div>
																																							</div>
																																							<div
																																								class="pre-items-content">
																																								<div
																																									class="pre-review-points animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar medium animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar long animated-bg">
																																								</div>
																																							</div>
																																						</div>
																																						<div
																																							class="pre-row-item filter-result-item">
																																							<div
																																								class="pre-avatar animated-bg-light">
																																							</div>
																																							<div
																																								class="pre-items-content">
																																								<div
																																									class="pre-review-points animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar medium animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar long animated-bg">
																																								</div>
																																							</div>
																																							<div
																																								class="pre-items-content">
																																								<div
																																									class="pre-review-points animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar medium animated-bg">
																																								</div>
																																								<div
																																									class="preload-bar long animated-bg">
																																								</div>
																																							</div>
																																						</div>

																																					</div>
																																				</div>
																																			</div>
																																			<div id="scrollLoadingPage"
																																				class="btn-load-more full-width"
																																				data-bind="click: handleClickLoadMoreResult, visible: hasMorePage() && viewType() != 'map'"
																																				style="margin-bottom:10px">
																																				<a href="https://www.foody.vn/ha-noi/quan-an-phong-cach-viet-nam-tai-quan-cau-giay?c=quan-an&amp;categorygroup=food&amp;page=5&amp;append=true#page5"
																																					rel="next">

																																					Xem
																																					tiếp
																																					kết
																																					quả
																																					...
																																					<span data-bind="text: searchItems().length+totalSubItems()">
                                                    48
                                                </span>/<span data-bind="text: totalResult().format('n0')">2,455</span>&nbsp;(<span data-bind="text: currentPage()">4</span>)
																																				</a>
																																			</div>
																																			<div
																																				class="add-more-places">
																																				<a
																																					href="/them-dia-diem"><span class="fa fa-plus-circle"></span>
																																					Không
																																					tìm
																																					thấy
																																					địa
																																					điểm?
																																					Tạo
																																					mới!</a>
																																			</div>
																																		</div>

																																	</div>



																																	<!-- End Banner Ads -->
																																</div>
																															</div>
																															<!--End of left filters-->
																															<!--End Ads Footer 728X90-->
																														</div>
																													</div>
																												</div>
		</section>
		<div id="advanceSearchPopup" class="advanceSearchbox">
			<div id="advanceSearchDiv">
				<div data-bind="visible: isLoading"
					style="text-align:center;float:left; margin-left:400px; margin-top:220px;">
					<div style="padding-left:5px;"><img src="/style/images/icons/ajax-loader.gif" /></div>
						<div style="padding-top:5px;">Đang tải ...</div>

					</div>
					<!-- ko if: !isLoading() &&  !requestSuccess()-->
					<h3 class="oes">Tôi muốn tìm địa điểm</h3>
					<div style="float: left; width: 550px;margin-top:10px;">
						<div class="row-item-request">
							<span>Mục đích của bạn</span>
							<input data-bind="value: purpose" name="Purpose" type="text" placeholder="Ví dụ: tổ chức tiệc sinh nhật, tiệc cưới" />
							<span data-bind="visible: $.trim(purpose()) == ''" class="error">*</span>
						</div>
						<div class="row-item-request">
							<span>Khu vực</span>
							<input data-bind="value: areas" name="Areas" type="text" placeholder="Ví dụ: Quận 1, 3..." />
							<span data-bind="visible: $.trim(areas()) == ''" class="error">*</span>
						</div>
						<div class="row-item-request">
							<span>Thời gian dự tính</span>
							<input data-bind="value: time" name="Time" type="text" placeholder="Ví dụ: cuối tháng 10" />
							<span data-bind="visible: $.trim(time()) == ''" class="error">*</span>
						</div>
						<div class="row-item-request">
							<span>Số người tham gia</span>
							<input data-bind="value: people" name="People" type="text" placeholder="Ví dụ: 10 người" />
							<span data-bind="visible: $.trim(people()) == ''" class="error">*</span>
						</div>
						<div class="row-item-request">
							<span>Chi phí dự tính/người</span>
							<input data-bind="value: price" name="Price" type="text" placeholder="Ví dụ: 200 ngàn/người" />
							<span data-bind="visible: $.trim(price()) == ''" class="error">*</span>
						</div>
						<div class="row-item-request">
							<span>Yêu cầu khác</span>
							<textarea data-bind="value: more" name="More" rows="5" placeholder="Ví dụ: yêu cầu về không gian, loại món ăn, phong cách quán..."></textarea>
						</div>
						<div class="row-item-request">
							<span>Điện thoại của bạn</span>
							<input data-bind="value: phone" name="Phone" onkeypress="return isNumberKey(event)" type="text" style="background:#f8f8f8;"/>
							<span data-bind="visible: $.trim(phone())==''" class="error">*</span>
						</div>
						<div class="row-item-request">
							<span>Email của bạn</span>
							<input data-bind="value: email" name="Email" type="text" style="background:#f8f8f8;"/>
							<span data-bind="visible: !isValidEmail()" class="error">*</span>
						</div>
						<div class="row-item-request" style="display:none;">
							<span>Public</span>
							<input data-bind="checked: isPublic" name="IsPublic" type="checkbox" />
            </div>
						</div>
						<div class="advanceSearchNote">
							<h3>Ghi chú</h3>
							<ul>
								<li>Form này chỉ dùng để gửi yêu cầu khi nhu cầu của bạn rất phức tạp, và bạn không thể
									tìm thấy bằng công cụ search.</li>
								<li>Foody đang thử nghiệm tính năng này, trước mắt đội ngũ Foody sẽ giúp bạn bằng cách
									gợi ý danh sách các địa điểm phù hợp.
									Sau đó, Foody sẽ phát triển rộng hơn để cộng đồng thành viên hoặc chủ địa điểm có
									thể tham gia cùng gợi ý giúp bạn. </li>
								<li>Thời gian để xử lý yêu cầu trong vòng từ 1 - 24 tiếng hoặc lâu hơn tùy theo mức độ
									phức tạp của yêu cầu</li>
								<li>Thông tin tư vấn hoàn toàn miễn phí. Foody sẽ gửi danh sách gợi ý qua Email của bạn,
									vui lòng cập nhật đầy đủ Email liên hệ.</li>
								<li>Tính năng này hiện tại chỉ áp dụng cho tìm địa điểm tại TP. HCM</li>
							</ul>
						</div>
						<div class="bottom-buttons">
							<label>
                <span style="float: left; margin-top: 1px; padding-right: 5px;">
                    <input type="checkbox" checked="checked" disabled="disabled"/></span>
                Foody gửi danh sách các địa điểm phù hợp với yêu cầu qua <b>Email</b> của tôi</label>
							<a data-bind="click: post" href="javascript:void(0)">Gửi yêu cầu</a>
							<span data-bind="visible: isposting" style="position: absolute;right: 140px;top: 21px;"><img src="/style/images/icons/ajax-loader.gif" /></span>
						</div>
						<!-- /ko -->

						<div data-bind="visible: requestSuccess" class="request-sent-success">
							<b>Gửi yêu cầu thành công!</b> Foody sẽ phản hồi qua Email của bạn!<br />
							<a href="javascript:void(0)" data-bind="click: reset">Tiếp tục</a> gửi yêu cầu hoặc <a
								data-bind="click: close" href="javascript:void(0)">đóng lại</a></div>
						<div data-bind="visible: hasError">Đã có lỗi, vui lòng <a href="javascript:void(0)"
								data-bind="click: reset">thử lại</a></div>

					</div>
				</div>


				<script type="text/javascript">
					var loadingElement = $('<div class="search-loading"><b>Đang tải...</b></div>')
        .appendTo('body')
        .hide();
    var localize = {
        areaText: 'Khu vực',
        purposeText: 'Mục đích',
        cuisineText: 'Ẩm thực',
        dishCategoryText: 'Loại món',
        categoryText: 'Phân loại',
        propertyText: 'Tiện nghi',
        diningText: 'Thích hợp',
        metaTitleText: "Địa điểm Qu&#225;n ăn phong c&#225;ch M&#243;n Việt tại Quận Cầu Giấy, H&#224; Nội"
    };
    var jsonData = {"photoCollectionResultCount":8741,"provinceId":218,"categoryId":3,"districtId":21,"districtName":"Quận Cầu Giấy","searchUrl":"/ha-noi/quan-an","searchDefaultUrl":"/ha-noi/dia-diem","keyword":"","viewType":"row","sortType":1,"priceMin":0,"priceMax":5000000,"districts":[{"Id":20,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Ba Đình","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Ba Dinh"},{"Id":690,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Bắc Từ Liêm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Bac Tu Liem"},{"Id":21,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Cầu Giấy","UrlRewriteName":null,"ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Cau Giay"},{"Id":22,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Đống Đa","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Dong Da"},{"Id":23,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hà Đông","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Ha Dong"},{"Id":24,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hai Bà Trưng","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hai Ba Trung"},{"Id":25,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hoàn Kiếm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hoan Kiem"},{"Id":26,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hoàng Mai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hoang Mai"},{"Id":27,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Long Biên","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Long Bien"},{"Id":945,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Nam Từ Liêm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Nam Tu Liem"},{"Id":28,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Tây Hồ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Tay Ho"},{"Id":29,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Thanh Xuân","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Thanh Xuan"},{"Id":692,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Thị Xã Sơn Tây","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Thi Xa Son Tay"},{"Id":674,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Ba Vì","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Ba Vi"},{"Id":675,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Chương Mỹ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Chuong My"},{"Id":676,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Đan Phượng","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Dan Phuong"},{"Id":677,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Đông Anh","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Dong Anh"},{"Id":678,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Gia Lâm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Gia Lam"},{"Id":679,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Hoài Đức","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Hoai Duc"},{"Id":680,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Mê Linh","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Me Linh"},{"Id":681,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Mỹ Đức","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen My Duc"},{"Id":682,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Phú Xuyên","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Phu Xuyen"},{"Id":683,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Phúc Thọ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Phuc Tho"},{"Id":684,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Quốc Oai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Quoc Oai"},{"Id":685,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Sóc Sơn","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Soc Son"},{"Id":686,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thạch Thất","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thach That"},{"Id":687,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thanh Oai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thanh Oai"},{"Id":688,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thanh Trì","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thanh Tri"},{"Id":689,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thường Tín","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thuong Tin"},{"Id":691,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Ứng Hòa","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Ung Hoa"}],"allAreas":[],"allDistricts":[],"allPurposes":[],"allCategories":[],"allCuisines":[],"allDishCategories":[],"allProperties":[],"allDinings":[],"selectedAreas":[],"selectedDistricts":[{"Id":21,"Avatar":null,"ParentId":218,"ParentName":null,"Name":"Quận Cầu Giấy","UrlRewriteName":"quan-cau-giay","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":1,"AsciiName":"Quan Cau Giay"}],"selectedPurposes":[],"selectedCategories":[{"Id":3,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quán ăn","UrlRewriteName":"quan-an","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":8,"AsciiName":"Quan an"}],"selectedCuisines":[{"Id":1,"Avatar":"foody-01-vietnam-635950402447733778.png","ParentId":0,"ParentName":null,"Name":"Món Việt","UrlRewriteName":"viet-nam","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[{"Id":12,"Avatar":"foody-12-miennam-635950401085583984.png","ParentId":1,"ParentName":null,"Name":"Món Miền Nam","UrlRewriteName":"mien-nam","ResultCount":24495,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Mien Nam"},{"Id":2,"Avatar":"foody-02-mienbac-635950402329745934.png","ParentId":1,"ParentName":null,"Name":"Món Bắc","UrlRewriteName":"mien-bac","ResultCount":27554,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Bac"},{"Id":7,"Avatar":"foody-07-mientrung-635950401707280292.png","ParentId":1,"ParentName":null,"Name":"Món Miền Trung","UrlRewriteName":"mien-trung","ResultCount":24634,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Mien Trung"},{"Id":29,"Avatar":"foody-29-taynguyen-635950400755089030.png","ParentId":1,"ParentName":null,"Name":"Tây Nguyên","UrlRewriteName":"tay-nguyen","ResultCount":4555,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Tay Nguyen"}],"FilterType":4,"AsciiName":"Mon Viet"}],"selectedDishCategories":[],"selectedProperties":[],"selectedPrices":[],"selectedDinings":[],"searchItems":[{"Address":"223 Tô Hiệu, P. Nghĩa Tân","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":47,"TotalView":5964,"TotalFavourite":40,"TotalCheckins":1,"AvgRating":"7.1","AvgRatingOriginal":7.054000,"ReviewUrl":"/ha-noi/tuyet-nhung-com-ga-phu-yen/binh-luan","AlbumUrl":"/ha-noi/tuyet-nhung-com-ga-phu-yen/album-anh","Latitude":21.0415890000000,"Longitude":105.7924980000000,"MainCategoryId":3,"PictureCount":142,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/tuyet-nhung-com-ga-phu-yen","BranchUrl":"/thuong-hieu/tuyet-nhung-com-ga-phu-yen?c=ha-noi","BranchName":"Hệ thống Tuyết Nhung - Cơm Gà Phú Yên","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"47","TotalPictures":142,"TotalPicturesFormat":"142","TotalSaves":0,"Reviews":[{"Id":14924525,"RestaurantID":0,"RestaurantStatus":0,"UserID":19859387,"Title":"Đắt, chất lượng trung b\u0026#236;nh","Comment":"Quá đắt so với mức giá. Món nộm thì tốt nhất đừng gọi, toàn giá với rau, trà đá cũng thế.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":2.000000,"OwnerUserName":"foodee_kilxyjpk","OwnerFirstName":"Hồng","OwnerLastName":"","OwnerFullName":"Hồng","OwnerAvatar":"https://images.foody.vn/default/s50/user-default-female.png","OwnerGender":"male","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_kilxyjpk","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/tuyet-nhung-com-ga-phu-yen/binh-luan-14924525"},{"Id":8794725,"RestaurantID":0,"RestaurantStatus":0,"UserID":352254,"Title":"Cơm v\u0026#224; g\u0026#224; kh\u0026#244;ng n\u0026#243;ng, gi\u0026#225; cao so với chất lượng","Comment":"Mình đến ăn lúc 5h30 chiều, thấy ăn cơm nguội, gà xé cũng ít và không ngon nóng. Suất cơm gà 40k mà có quá ít cơm và gà. Đồ ăn lại không có gì đặc biệt nữa.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":4.400000,"OwnerUserName":"tungvu3196","OwnerFirstName":"Tung Vu","OwnerLastName":"","OwnerFullName":"Tung Vu","OwnerAvatar":"https://images.foody.vn/usr/g36/352254/avt/c50x50/foody-avatar-981-637145531689255321.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/tungvu3196","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/tuyet-nhung-com-ga-phu-yen/binh-luan-8794725"}],"ReviewsTest":null,"IsOpening":false,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/tuyet-nhung-com-ga-phu-yen/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":737094,"Name":"Tuyết Nhung - Cơm Gà Phú Yên - Tô Hiệu","UrlRewriteName":"tuyet-nhung-com-ga-phu-yen","PicturePath":"https://images.foody.vn/res/g74/737094/prof/s180x180/foody-upload-api-foody-mobile-phu-yen-jpg-180503093800.jpg","PicturePathLarge":"https://images.foody.vn/res/g74/737094/prof/s640x400/foody-upload-api-foody-mobile-phu-yen-jpg-180503093800.jpg","MobilePicturePath":"https://images.foody.vn/res/g74/737094/prof/s640x400/foody-upload-api-foody-mobile-phu-yen-jpg-180503093800.jpg","DetailUrl":"/ha-noi/tuyet-nhung-com-ga-phu-yen","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"25 Nguyễn Phong Sắc, P. Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":32,"TotalView":16155,"TotalFavourite":25,"TotalCheckins":8,"AvgRating":"7.0","AvgRatingOriginal":6.962000,"ReviewUrl":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/binh-luan","AlbumUrl":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/album-anh","Latitude":21.0368480000000,"Longitude":105.7897550000000,"MainCategoryId":3,"PictureCount":153,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/che-dua-thai-lan-nguyen-phong-sac","BranchUrl":"/thuong-hieu/che-dua-thai-lan-nguyen-phong-sac?c=ha-noi","BranchName":"Hệ thống Chè Dừa Thái Lan - Nguyễn Phong Sắc","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"32","TotalPictures":153,"TotalPicturesFormat":"153","TotalSaves":0,"Reviews":[{"Id":2921035,"RestaurantID":0,"RestaurantStatus":0,"UserID":616780,"Title":"Qu\u0026#225; ch\u0026#225;n ng\u0026#224;y thất tịch","Comment":"Hôm nay gấu bảo ngày ngưu lang chức nữ gặp nhau nên ăn chè đỗ đỏ, mình mới đặt chè đỗ đỏ với 1 số loại chè khác. Grab đến quán bảo đợi 10p vì phải nấu, uh thì mình đợi. Xong grab gọi lại bảo hết tất c...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":1.000000,"OwnerUserName":"thang0208","OwnerFirstName":"Thang","OwnerLastName":"Ngoc","OwnerFullName":"Thang Ngoc","OwnerAvatar":"https://images.foody.vn/usr/g62/616780/avt/c50x50/beauty-upload-api-foody-avatar-69fb5139-a52b-40d4-95d7-efa8a0cd871b-191020213924.jpg","OwnerGender":"male","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/thang0208","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/binh-luan-2921035"},{"Id":2790695,"RestaurantID":0,"RestaurantStatus":0,"UserID":8610623,"Title":"Ch\u0026#232; Dừa Th\u0026#225;i Lan - Nguyễn Phong Sắc","Comment":"Quán nhỏ xinh nằm ngay đầu đường nguyễn phong sắc,ngã 4 trần thái tông xuân thủy cầu giấy.\n\nMenu đa dạng với các loại chè như chè sầu,dừa dầm đến những loại chè truyền thống như chè bưởi,chè đỗ đen..v...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.600000,"OwnerUserName":"xjuzoyr","OwnerFirstName":"Linh","OwnerLastName":"Chi","OwnerFullName":"Linh Chi","OwnerAvatar":"https://images.foody.vn/usr/g862/8610623/avt/c50x50/xjuzoyr-avatar-373-636750583830011143.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/xjuzoyr","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/binh-luan-2790695"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":214084,"Name":"Chè Dừa Thái Lan - Nguyễn Phong Sắc","UrlRewriteName":"che-dua-thai-lan-nguyen-phong-sac","PicturePath":"https://images.foody.vn/res/g22/214084/prof/s180x180/foody-mobile-dua640-jpg-631-635953770711301483.jpg","PicturePathLarge":"https://images.foody.vn/res/g22/214084/prof/s640x400/foody-mobile-dua640-jpg-631-635953770711301483.jpg","MobilePicturePath":"https://images.foody.vn/res/g22/214084/prof/s640x400/foody-mobile-dua640-jpg-631-635953770711301483.jpg","DetailUrl":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"P105A C7 Nghĩa Tân, Ngõ 140 Trần Tử Bình, P. Nghĩa Tân","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":36,"TotalView":42685,"TotalFavourite":13,"TotalCheckins":8,"AvgRating":"7.3","AvgRatingOriginal":7.316000,"ReviewUrl":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/binh-luan","AlbumUrl":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/album-anh","Latitude":21.0425066000000,"Longitude":105.7910876000000,"MainCategoryId":3,"PictureCount":133,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"36","TotalPictures":133,"TotalPicturesFormat":"133","TotalSaves":0,"Reviews":[{"Id":11798200,"RestaurantID":0,"RestaurantStatus":0,"UserID":11579565,"Title":"H\u0026#249;ng B\u0026#233;o - Lẩu Cua Đồng - Trần Tử B\u0026#236;nh","Comment":"Thi thoảng đi ăn lại thì thấy chất lượng quán tốt hơn so vs lần trước mình ăn rồi.😛","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.000000,"OwnerUserName":"Chi2k","OwnerFirstName":"Quỳnhchi","OwnerLastName":"Nguyễn","OwnerFullName":"Quỳnhchi Nguyễn","OwnerAvatar":"https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Chi2k","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/binh-luan-11798200"},{"Id":10567766,"RestaurantID":0,"RestaurantStatus":0,"UserID":11579565,"Title":"H\u0026#249;ng B\u0026#233;o - Lẩu Cua Đồng - Trần Tử B\u0026#236;nh","Comment":"Quán mới đổi người  nấu hay sao ấy mà hôm mình ăn lẩu ếch lại đắt hơn mà nấu siêu nhiều mỡ, thề lần đầu tiên ăn thấy chán như thế😔","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":7.000000,"OwnerUserName":"Chi2k","OwnerFirstName":"Quỳnhchi","OwnerLastName":"Nguyễn","OwnerFullName":"Quỳnhchi Nguyễn","OwnerAvatar":"https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Chi2k","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/binh-luan-10567766"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":160574,"Name":"Hùng Béo - Lẩu Cua Đồng - Trần Tử Bình","UrlRewriteName":"hung-beo-lau-cua-dong-tran-tu-binh","PicturePath":"https://images.foody.vn/res/g17/160574/prof/s180x180/foody-mobile-960x600_hung-beo-lau-533-636147262410516048.jpg","PicturePathLarge":"https://images.foody.vn/res/g17/160574/prof/s640x400/foody-mobile-960x600_hung-beo-lau-533-636147262410516048.jpg","MobilePicturePath":"https://images.foody.vn/res/g17/160574/prof/s640x400/foody-mobile-960x600_hung-beo-lau-533-636147262410516048.jpg","DetailUrl":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"15 Trần Bình","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":23,"TotalView":37441,"TotalFavourite":37,"TotalCheckins":15,"AvgRating":"7.3","AvgRatingOriginal":7.320000,"ReviewUrl":"/ha-noi/ole-banh-truyen-thong-nhat-ban/binh-luan","AlbumUrl":"/ha-noi/ole-banh-truyen-thong-nhat-ban/album-anh","Latitude":21.0361150000000,"Longitude":105.7788790000000,"MainCategoryId":3,"PictureCount":171,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":false,"BookingUrl":"","DeliveryUrl":"","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"23","TotalPictures":171,"TotalPicturesFormat":"171","TotalSaves":0,"Reviews":[{"Id":2053668,"RestaurantID":0,"RestaurantStatus":0,"UserID":512100,"Title":"Ole - B\u0026#225;nh Truyền Thống Nhật Bản","Comment":"Ngon sạch. Vọ trí hơi nóng. Nhân viên nhanh nhẹn vui vẻ. Cần trang trí không gian quán cho phù hợp hơn đẻ tránh tình trạng nóng quá tải khách","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.600000,"OwnerUserName":"Cuongmy","OwnerFirstName":"Cường","OwnerLastName":"My","OwnerFullName":"Cường My","OwnerAvatar":"https://images.foody.vn/usr/g52/512100/avt/c50x50/beauty-upload-api-foody-avatar-5734e3fe-3efd-4703-aeec-083401b954c1-190814200612.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Cuongmy","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/ole-banh-truyen-thong-nhat-ban/binh-luan-2053668"},{"Id":2051031,"RestaurantID":0,"RestaurantStatus":0,"UserID":9123375,"Title":"Hot Dog khổng lồ","Comment":"Hot dog khổng lồ ăn mãi hết. Vỏ rất giòn, nếu bạn nào sợ ngất thì cứ vô tư ăn vì dù chiên dầu nhưng k ngấy đâu nhé. Chị chủ chiên rất khéo vỏ vàng ruộm, sốt ngon cực đỉnh lun.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.800000,"OwnerUserName":"Hien_nt","OwnerFirstName":"Hien_nt","OwnerLastName":"","OwnerFullName":"Hien_nt","OwnerAvatar":"https://images.foody.vn/usr/g913/9123375/avt/c50x50/beauty-upload-api-foody-avatar-394d790d-d30a-4769-a330-363891ecd622-191215142508.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Hien_nt","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/ole-banh-truyen-thong-nhat-ban/binh-luan-2051031"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":214740,"Name":"Ole - Bánh Truyền Thống Nhật Bản","UrlRewriteName":"ole-banh-truyen-thong-nhat-ban","PicturePath":"https://images.foody.vn/res/g22/214740/prof/s180x180/foody-mobile-ole640-jpg-850-635949570629965289.jpg","PicturePathLarge":"https://images.foody.vn/res/g22/214740/prof/s640x400/foody-mobile-ole640-jpg-850-635949570629965289.jpg","MobilePicturePath":"https://images.foody.vn/res/g22/214740/prof/s640x400/foody-mobile-ole640-jpg-850-635949570629965289.jpg","DetailUrl":"/ha-noi/ole-banh-truyen-thong-nhat-ban","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"67 Yên Hòa, P. Yên Hòa","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":35,"TotalView":2696,"TotalFavourite":20,"TotalCheckins":6,"AvgRating":"7.2","AvgRatingOriginal":7.162000,"ReviewUrl":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/binh-luan","AlbumUrl":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/album-anh","Latitude":21.0233415000000,"Longitude":105.7958695000000,"MainCategoryId":3,"PictureCount":104,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/bun-cha-nem-cua-be-yen-hoa","BranchUrl":"/thuong-hieu/bun-cha-nem-cua-be?c=ha-noi","BranchName":"Hệ thống Bún Chả \u0026 Nem Cua Bể","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"35","TotalPictures":104,"TotalPicturesFormat":"104","TotalSaves":0,"Reviews":[{"Id":14908494,"RestaurantID":0,"RestaurantStatus":0,"UserID":19869596,"Title":"Bố xin ch\u0026#250;ng m\u0026#224;y đấyyyyy","Comment":"Làm ăn bát nháo vãi l, rau đéo có, bát đéo có đũa đéo có. ĂN BỐC À.\nBÚN THÌ CHUA, DC 3 CÁI MIẾNG THỊT LÀM ANH bố m đói.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":1.000000,"OwnerUserName":"foodee_x1j5uvj3","OwnerFirstName":"Hiếu","OwnerLastName":"PCI","OwnerFullName":"Hiếu PCI","OwnerAvatar":"https://images.foody.vn/usr/g1987/19869596/avt/c50x50/foody-avatar-654-637777768251432573.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_x1j5uvj3","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/binh-luan-14908494"},{"Id":12985559,"RestaurantID":0,"RestaurantStatus":0,"UserID":11579565,"Title":"B\u0026#250;n Chả \u0026amp; Nem Cua Bể - Y\u0026#234;n H\u0026#242;a","Comment":"Mình đặt 1 bún chả đầy đủ . Bún chả ăn ngon. Nước chấm để trong hộp nắp chắc chắn.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.200000,"OwnerUserName":"Chi2k","OwnerFirstName":"Quỳnhchi","OwnerLastName":"Nguyễn","OwnerFullName":"Quỳnhchi Nguyễn","OwnerAvatar":"https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Chi2k","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/binh-luan-12985559"}],"ReviewsTest":null,"IsOpening":false,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":264770,"Name":"Bún Chả \u0026 Nem Cua Bể - Yên Hòa","UrlRewriteName":"bun-cha-nem-cua-be-yen-hoa","PicturePath":"https://images.foody.vn/res/g27/264770/prof/s180x180/foody-mobile-nem-cua-be-6831-1432-565-636064356571448314.jpg","PicturePathLarge":"https://images.foody.vn/res/g27/264770/prof/s640x400/foody-mobile-nem-cua-be-6831-1432-565-636064356571448314.jpg","MobilePicturePath":"https://images.foody.vn/res/g27/264770/prof/s640x400/foody-mobile-nem-cua-be-6831-1432-565-636064356571448314.jpg","DetailUrl":"/ha-noi/bun-cha-nem-cua-be-yen-hoa","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"2/421 Hoàng Quốc Việt, P. Nghĩa Tân","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":42,"TotalView":1701,"TotalFavourite":14,"TotalCheckins":8,"AvgRating":"7.9","AvgRatingOriginal":7.882000,"ReviewUrl":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/binh-luan","AlbumUrl":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/album-anh","Latitude":21.0458140000000,"Longitude":105.7860350000000,"MainCategoryId":3,"PictureCount":104,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"42","TotalPictures":104,"TotalPicturesFormat":"104","TotalSaves":0,"Reviews":[{"Id":6659403,"RestaurantID":0,"RestaurantStatus":0,"UserID":18306374,"Title":"Ch\u0026#225;n","Comment":"Rau sống héo úa hỏng, quất thì toàn thối, thiếu dưa chuột. Ăn bún đậu mắm tôm mà k có quất thì mất vị quá. Quán làm chán quá!","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":3.400000,"OwnerUserName":"foodee_pxcljj8i","OwnerFirstName":"Nguyễn","OwnerLastName":"Linh","OwnerFullName":"Nguyễn Linh","OwnerAvatar":"https://images.foody.vn/usr/g1831/18306374/avt/c50x50/beauty-upload-api-foody-avatar-423ea137-da03-4d9c-b025-3c1d959dd4d6-191130193559.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_pxcljj8i","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/binh-luan-6659403"},{"Id":4754815,"RestaurantID":0,"RestaurantStatus":0,"UserID":18004183,"Title":"B\u0026#250;n Đậu C\u0026#250;c***- Ho\u0026#224;ng Quốc Việt","Comment":"Ngon , vừa miệng❤️giá cả hợp lí                                                ","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":10.000000,"OwnerUserName":"foodee_9dicnbry","OwnerFirstName":"Quỳnh","OwnerLastName":null,"OwnerFullName":"Quỳnh","OwnerAvatar":"https://images.foody.vn/default/s50/user-default-female.png","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_9dicnbry","OwnerDisplayName":null,"ShortReview":true,"Url":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/binh-luan-4754815"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":762583,"Name":"Bún Đậu Cúc Cu - Hoàng Quốc Việt","UrlRewriteName":"bun-dau-met-cuc-cu-hoang-quoc-viet","PicturePath":"https://images.foody.vn/res/g77/762583/prof/s180x180/image-e3bc5f75-200910115833.jpeg","PicturePathLarge":"https://images.foody.vn/res/g77/762583/prof/s640x400/image-e3bc5f75-200910115833.jpeg","MobilePicturePath":"https://images.foody.vn/res/g77/762583/prof/s640x400/image-e3bc5f75-200910115833.jpeg","DetailUrl":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"66 Duy Tân, P. Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":31,"TotalView":13690,"TotalFavourite":38,"TotalCheckins":6,"AvgRating":"6.4","AvgRatingOriginal":6.388000,"ReviewUrl":"/ha-noi/pho-cuon-ngu-xa-duy-tan/binh-luan","AlbumUrl":"/ha-noi/pho-cuon-ngu-xa-duy-tan/album-anh","Latitude":21.0312530000000,"Longitude":105.7822150000000,"MainCategoryId":3,"PictureCount":106,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/pho-cuon-ngu-xa-duy-tan","BranchUrl":"/thuong-hieu/pho-cuon-ngu-xa?c=ha-noi","BranchName":"Hệ thống Phở Cuốn Ngũ Xã","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"31","TotalPictures":106,"TotalPicturesFormat":"106","TotalSaves":0,"Reviews":[{"Id":13742585,"RestaurantID":0,"RestaurantStatus":0,"UserID":19365772,"Title":"Đồ ăn oke - vừa gi\u0026#225;","Comment":"Ngày trước chưa dịch, buổi trưa ra đây ăn rất đông. Đợt này chỉ đc bán mang về nên chắc cũng đỡ, mình thấy ship nhanh và khá cẩn thận. Đồ ăn vẫn ổn, phù hợp giá tiền. Mình gọi phở chiên phồng và 1 cốc...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":7.600000,"OwnerUserName":"foodee_u32az83y","OwnerFirstName":"Trang Hoàng","OwnerLastName":"","OwnerFullName":"Trang Hoàng","OwnerAvatar":"https://images.foody.vn/default/s50/user-default-female.png","OwnerGender":"female","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_u32az83y","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/pho-cuon-ngu-xa-duy-tan/binh-luan-13742585"},{"Id":10262683,"RestaurantID":0,"RestaurantStatus":0,"UserID":11579565,"Title":"Phở Cuốn Ngũ X\u0026#227; - Duy T\u0026#226;n","Comment":"-phở cuốn ở đây ăn khá đầy, ăn 10 cái là no căng bụng luôn ấy. Thấy review khen chê thất thường , nhưng mình thấy ăn ở quán vẫn oke .","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.000000,"OwnerUserName":"Chi2k","OwnerFirstName":"Quỳnhchi","OwnerLastName":"Nguyễn","OwnerFullName":"Quỳnhchi Nguyễn","OwnerAvatar":"https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Chi2k","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/pho-cuon-ngu-xa-duy-tan/binh-luan-10262683"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/pho-cuon-ngu-xa-duy-tan/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":109338,"Name":"Phở Cuốn Ngũ Xã - Duy Tân","UrlRewriteName":"pho-cuon-ngu-xa-duy-tan","PicturePath":"https://images.foody.vn/res/g11/109338/prof/s180x180/foody-mobile-pho-cuon2-jpg-934-635550098425249236.jpg","PicturePathLarge":"https://images.foody.vn/res/g11/109338/prof/s640x400/foody-mobile-pho-cuon2-jpg-934-635550098425249236.jpg","MobilePicturePath":"https://images.foody.vn/res/g11/109338/prof/s640x400/foody-mobile-pho-cuon2-jpg-934-635550098425249236.jpg","DetailUrl":"/ha-noi/pho-cuon-ngu-xa-duy-tan","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"2 Hẻm 32 Ngách 5 Ngõ 204 Trần Duy Hưng, P. Trung Hòa","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":28,"TotalView":3144,"TotalFavourite":36,"TotalCheckins":7,"AvgRating":"6.4","AvgRatingOriginal":6.418000,"ReviewUrl":"/ha-noi/xoi-tam-thai-ha/binh-luan","AlbumUrl":"/ha-noi/xoi-tam-thai-ha/album-anh","Latitude":21.0089670000000,"Longitude":105.7966910000000,"MainCategoryId":3,"PictureCount":111,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/xoi-tam-thai-ha","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"28","TotalPictures":111,"TotalPicturesFormat":"111","TotalSaves":0,"Reviews":[{"Id":3732556,"RestaurantID":0,"RestaurantStatus":0,"UserID":1662701,"Title":"X\u0026#244;i T\u0026#225;m - Th\u0026#225;i H\u0026#224;","Comment":"Xôi Tám - 322 Thái Hà \n\nBạn sẽ order các topping và xôi theo ý muốn , có hai loại xôi là xôi xéo (15k) và xôi trắng(10k) xôi dẻo và ngon lắm nha. CÒn topping thì giá dao động từ 8k-15k tuỳ loại : xá x...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.600000,"OwnerUserName":"hoanganh8790","OwnerFirstName":"Trang","OwnerLastName":"Hoang","OwnerFullName":"Trang Hoang","OwnerAvatar":"https://images.foody.vn/usr/g167/1662701/avt/c50x50/beauty-upload-api-foody-avatar-62f86f2f-250c-407d-be57-92ccccc540d9-191025131450.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/hoanganh8790","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/xoi-tam-thai-ha/binh-luan-3732556"},{"Id":3713181,"RestaurantID":0,"RestaurantStatus":0,"UserID":15480563,"Title":"X\u0026#244;i T\u0026#225;m - Th\u0026#225;i H\u0026#224;","Comment":"Thật không thể tin vào mắt mình..! Xôi chưa bằng 1 nắm tay :(( sẽ không có lần t2 hic","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":1.000000,"OwnerUserName":"foodee_667zapgi","OwnerFirstName":"Anhh","OwnerLastName":"Linhh","OwnerFullName":"Anhh Linhh","OwnerAvatar":"https://images.foody.vn/usr/g1549/15480563/avt/c50x50/beauty-upload-api-foody-avatar-482e93a1-e57a-4ff9-bf2d-b6d7e3176eb0-191216001840.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_667zapgi","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/xoi-tam-thai-ha/binh-luan-3713181"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/xoi-tam-thai-ha/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":647491,"Name":"Xôi Tám - Trần Duy Hưng","UrlRewriteName":"xoi-tam-thai-ha","PicturePath":"https://images.foody.vn/res/g65/647491/prof/s180x180/foody-mobile-xoi-tam-jpg-523-636410905562883010.jpg","PicturePathLarge":"https://images.foody.vn/res/g65/647491/prof/s640x400/foody-mobile-xoi-tam-jpg-523-636410905562883010.jpg","MobilePicturePath":"https://images.foody.vn/res/g65/647491/prof/s640x400/foody-mobile-xoi-tam-jpg-523-636410905562883010.jpg","DetailUrl":"/ha-noi/xoi-tam-thai-ha","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"273 Tô Hiệu, P. Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":30,"TotalView":1281,"TotalFavourite":38,"TotalCheckins":4,"AvgRating":"8.7","AvgRatingOriginal":8.700000,"ReviewUrl":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/binh-luan","AlbumUrl":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/album-anh","Latitude":21.0415730000000,"Longitude":105.7914360000000,"MainCategoryId":3,"PictureCount":29,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/safodi-buffet-lau-hoi-lau-nuong","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"30","TotalPictures":29,"TotalPicturesFormat":"29","TotalSaves":0,"Reviews":[{"Id":9996039,"RestaurantID":0,"RestaurantStatus":0,"UserID":20049115,"Title":"Lẩu ở đ\u0026#226;y ok","Comment":"Mình đến lúc gần 8h tối, khách vãng lai may vẫn còn bàn. Phục vụ tận tình, lẩu ra nhanh, lên đồ cũng nhanh. Mình gọi suất 99k có cá viên bò viên, ba chỉ bò, thịt lợn, ngao, đậu, váng đậu, xúc xích, ra...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.400000,"OwnerUserName":"foodee_d9s9jwjp","OwnerFirstName":"Hiền","OwnerLastName":"Lê","OwnerFullName":"Hiền Lê","OwnerAvatar":"https://images.foody.vn/usr/g2005/20049115/avt/c50x50/beauty-upload-api-foody-avatar-723ab79f-3a4f-4453-a455-948d19f153fd-200504094741.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_d9s9jwjp","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/binh-luan-9996039"},{"Id":9399442,"RestaurantID":0,"RestaurantStatus":0,"UserID":22274735,"Title":"Safodi - Buffet Lẩu Hơi \u0026amp; Lẩu Nướng","Comment":"Với mình thì lẩu ở đây khá ngon , vị đậm đà . Chiều buồn buồn se mát thế này mà húp nước lẩu chua ngọt bên quán thì quá đã . Giá cũng hợp lí . Khá hài lòng .","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.000000,"OwnerUserName":"terrycjtroller","OwnerFirstName":"Huyen Hoa","OwnerLastName":"Nguyen","OwnerFullName":"Huyen Hoa Nguyen","OwnerAvatar":"https://images.foody.vn/usr/g2228/22274735/avt/c50x50/foody-avatar-445-637449429964270545.jpg","OwnerGender":"female","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/terrycjtroller","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/binh-luan-9399442"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":1042834,"Name":"Safodi - Buffet Lẩu Hơi \u0026 Lẩu Nướng","UrlRewriteName":"safodi-buffet-lau-hoi-lau-nuong","PicturePath":"https://images.foody.vn/res/g105/1042834/prof/s180x180/file_restaurant_photo_tbzf_16576-bf99d9bf-220712134254.jpg","PicturePathLarge":"https://images.foody.vn/res/g105/1042834/prof/s640x400/file_restaurant_photo_tbzf_16576-bf99d9bf-220712134254.jpg","MobilePicturePath":"https://images.foody.vn/res/g105/1042834/prof/s640x400/file_restaurant_photo_tbzf_16576-bf99d9bf-220712134254.jpg","DetailUrl":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"36 Phố Dịch Vọng Hậu, P. Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":34,"TotalView":8162,"TotalFavourite":25,"TotalCheckins":9,"AvgRating":"7.1","AvgRatingOriginal":7.078000,"ReviewUrl":"/ha-noi/pho-dinh-3-dich-vong-hau/binh-luan","AlbumUrl":"/ha-noi/pho-dinh-3-dich-vong-hau/album-anh","Latitude":21.0325152000000,"Longitude":105.7870686000000,"MainCategoryId":3,"PictureCount":98,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/pho-dinh-3-dich-vong-hau","BranchUrl":"/thuong-hieu/pho-dinh-3?c=ha-noi","BranchName":"Hệ thống Phở Định 3","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"34","TotalPictures":98,"TotalPicturesFormat":"98","TotalSaves":0,"Reviews":[{"Id":16123956,"RestaurantID":0,"RestaurantStatus":0,"UserID":14880419,"Title":"Qu\u0026#225; tệ anh em ạ !","Comment":"Phở định giờ ăn chán , thái độ từ nhân viên đến chủ lồi lõm ! \nHôm mình đi ăn 3 ngừoi là gần cuối canh , bánh phở cứng , nước mặn ko sắc đc như xưa ! \nĐang ăn thì chủ quán tắt điện đánh phụp như đuổi ...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":5.000000,"OwnerUserName":"billgates_2028","OwnerFirstName":"Khánh","OwnerLastName":"Nguyễn Gia","OwnerFullName":"Khánh Nguyễn Gia","OwnerAvatar":"https://images.foody.vn/usr/g1489/14880419/avt/c50x50/beauty-upload-api-foody-avatar-7f2bc26c-9b7d-411d-ad51-e8a66585c493-191122121319.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/billgates_2028","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/pho-dinh-3-dich-vong-hau/binh-luan-16123956"},{"Id":7099955,"RestaurantID":0,"RestaurantStatus":0,"UserID":1301649,"Title":"Phở Định 3 - Đồng B\u0026#244;ng","Comment":"sáng nay đi ăn phở nạm gầu, thấy quán vẫn tấp nập khách ra vào mặc kệ covid 😀 menu có nhiều lựa chọn, giá trung bình 50k, phở lõi thì 70k. còn có cả phở không thịt và phở cho trẻ em, quẩy 1 người và ...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":7.800000,"OwnerUserName":"rosecloud121","OwnerFirstName":"Mint","OwnerLastName":"Ng","OwnerFullName":"Mint Ng","OwnerAvatar":"https://images.foody.vn/usr/g131/1301649/avt/c50x50/ruka-avatar-711-637173934938683397.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/rosecloud121","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/pho-dinh-3-dich-vong-hau/binh-luan-7099955"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/pho-dinh-3-dich-vong-hau/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":29272,"Name":"Phở Định 3 - Dịch Vọng Hậu","UrlRewriteName":"pho-dinh-3-dich-vong-hau","PicturePath":"https://images.foody.vn/res/g3/29272/prof/s180x180/foody-mobile-pho-jpg-932-635917368774327730.jpg","PicturePathLarge":"https://images.foody.vn/res/g3/29272/prof/s640x400/foody-mobile-pho-jpg-932-635917368774327730.jpg","MobilePicturePath":"https://images.foody.vn/res/g3/29272/prof/s640x400/foody-mobile-pho-jpg-932-635917368774327730.jpg","DetailUrl":"/ha-noi/pho-dinh-3-dich-vong-hau","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"115 B7 Tô Hiệu, P. Nghĩa Tân","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":12,"Name":"Món Miền Nam","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-mien-nam"}],"SpecialDesc":null,"TotalReview":32,"TotalView":9671,"TotalFavourite":35,"TotalCheckins":3,"AvgRating":"7.0","AvgRatingOriginal":6.950000,"ReviewUrl":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/binh-luan","AlbumUrl":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/album-anh","Latitude":21.0438417000000,"Longitude":105.7965615000000,"MainCategoryId":3,"PictureCount":74,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"32","TotalPictures":74,"TotalPicturesFormat":"74","TotalSaves":0,"Reviews":[{"Id":6940305,"RestaurantID":0,"RestaurantStatus":0,"UserID":20196225,"Title":"B\u0026#225;nh X\u0026#232;o \u0026amp; Nem Lụi -***","Comment":"Quán hơi bị ngon nha. Giao hàng nhanh. Bánh xèo chuẩn vị, giòn, ít dầu so với quán khác. Ngon nhất vẫn là nem lụi","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":10.000000,"OwnerUserName":"foodee_om9w0plt","OwnerFirstName":"Duy","OwnerLastName":"","OwnerFullName":"Duy","OwnerAvatar":"https://images.foody.vn/default/s50/user-default-female.png","OwnerGender":"male","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_om9w0plt","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/binh-luan-6940305"},{"Id":4004457,"RestaurantID":0,"RestaurantStatus":0,"UserID":19046663,"Title":"B\u0026#225;nh X\u0026#232;o \u0026amp; Nem Lụi -***","Comment":"Ngày xưa đây là quán tủ của  mình, từ hồi nem còn 5k 1 cái, mà về sau tăng lên 6k vẫn ok, nhưng dạo gần đây mấy lát xoài cắt quá dày nên ăn ko đc ngon, đỉnh điểm lad hôm qua gọi đĩa nem ăn vừa nguội v...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":4.600000,"OwnerUserName":"foodee_fohig9fa","OwnerFirstName":"Dũng","OwnerLastName":"Thái Việt","OwnerFullName":"Dũng Thái Việt","OwnerAvatar":"https://images.foody.vn/usr/g1905/19046663/avt/c50x50/beauty-upload-api-foody-avatar-bee17315-9f84-4ab5-9c7a-04e0f40d6617-200207173213.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_fohig9fa","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/binh-luan-4004457"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":231953,"Name":"Song Nguyệt - Bánh Xèo \u0026 Nem Lụi - Tô Hiệu","UrlRewriteName":"song-nguyet-banh-xeo-nem-lui-to-hieu","PicturePath":"https://images.foody.vn/res/g24/231953/prof/s180x180/foody-mobile-34-jpg-265-635974352692854698.jpg","PicturePathLarge":"https://images.foody.vn/res/g24/231953/prof/s640x400/foody-mobile-34-jpg-265-635974352692854698.jpg","MobilePicturePath":"https://images.foody.vn/res/g24/231953/prof/s640x400/foody-mobile-34-jpg-265-635974352692854698.jpg","DetailUrl":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"36 ngõ 24  Phan Văn Trường, P.Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"},{"Id":21,"Name":"Món Nhật","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-nhat-ban"},{"Id":36,"Name":"Món Á","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-chau-a"}],"SpecialDesc":null,"TotalReview":172,"TotalView":561,"TotalFavourite":4,"TotalCheckins":0,"AvgRating":"9.6","AvgRatingOriginal":9.626000,"ReviewUrl":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/binh-luan","AlbumUrl":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/album-anh","Latitude":21.0410136000000,"Longitude":105.7875145000000,"MainCategoryId":3,"PictureCount":9,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"172","TotalPictures":9,"TotalPicturesFormat":"9","TotalSaves":0,"Reviews":[{"Id":16780209,"RestaurantID":0,"RestaurantStatus":0,"UserID":1001288,"Title":"Rất ngonnnn","Comment":"Mình đặt cho anh xã ăn mà anh khen nức nở                                      ","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.000000,"OwnerUserName":"giangxoan11112706","OwnerFirstName":"Nguyễn","OwnerLastName":"T.Giang","OwnerFullName":"Nguyễn T.Giang","OwnerAvatar":"https://images.foody.vn/usr/g101/1001288/avt/c50x50/beauty-upload-api-foody-avatar-e4ff95c4-6f91-4152-b32f-99773576b5ce-191025125259.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/giangxoan11112706","OwnerDisplayName":null,"ShortReview":true,"Url":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/binh-luan-16780209"},{"Id":16107545,"RestaurantID":0,"RestaurantStatus":0,"UserID":23299868,"Title":"Phong Th\u0026#224;nhh Qu\u0026#225;n - Qu\u0026#225;n Ăn - Phan Văn Trường","Comment":"Cơm rất ngon , sạch sẽ , làm nhanh , nước sốt rất chi là ưnggg nhé 🍗🍗🍗🍗    ","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.400000,"OwnerUserName":"Thanh_tam_pham_thi","OwnerFirstName":"Thanh Tâm Phạm Thị","OwnerLastName":"","OwnerFullName":"Thanh Tâm Phạm Thị","OwnerAvatar":"https://images.foody.vn/usr/g2330/23299868/avt/c50x50/thanh_tam_pham_thi-avatar-342-637506191180367188.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Thanh_tam_pham_thi","OwnerDisplayName":null,"ShortReview":true,"Url":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/binh-luan-16107545"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null},{"Id":28,"Name":"Giao cơm văn phòng","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":1000027868,"Name":"Phong Thànhh Quán - Quán Ăn - Phan Văn Trường","UrlRewriteName":"phong-thanhh-quan-quan-an-phan-van-truong.glrxgp","PicturePath":"https://images.foody.vn/res/g100003/1000027868/prof/s180x180/file_restaurant_photo_ykxn_16254-2fdda806-210705174327.jpeg","PicturePathLarge":"https://images.foody.vn/res/g100003/1000027868/prof/s640x400/file_restaurant_photo_ykxn_16254-2fdda806-210705174327.jpeg","MobilePicturePath":"https://images.foody.vn/res/g100003/1000027868/prof/s640x400/file_restaurant_photo_ykxn_16254-2fdda806-210705174327.jpeg","DetailUrl":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]}],"adItems":[],"totalResult":2455,"currentPage":4,"locationQuery":null,"maxPageToLoad":5,"brand":"","providerList":[],"book":false,"totalSubItems":59,"documentSource":"Restaurant","listResultCount":93042,"restaurantResultCount":2514,"userResultCount":7330050,"articleResultCount":4395,"pictureResultCount":20947}; 
    var jsonDataSearch = {"photoCollectionResultCount":8741,"provinceId":218,"categoryId":3,"districtId":21,"districtName":"Quận Cầu Giấy","searchUrl":"/ha-noi/quan-an","searchDefaultUrl":"/ha-noi/dia-diem","keyword":"","viewType":"row","sortType":1,"priceMin":0,"priceMax":5000000,"districts":[{"Id":20,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Ba Đình","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Ba Dinh"},{"Id":690,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Bắc Từ Liêm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Bac Tu Liem"},{"Id":21,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Cầu Giấy","UrlRewriteName":null,"ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Cau Giay"},{"Id":22,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Đống Đa","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Dong Da"},{"Id":23,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hà Đông","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Ha Dong"},{"Id":24,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hai Bà Trưng","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hai Ba Trung"},{"Id":25,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hoàn Kiếm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hoan Kiem"},{"Id":26,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hoàng Mai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hoang Mai"},{"Id":27,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Long Biên","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Long Bien"},{"Id":945,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Nam Từ Liêm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Nam Tu Liem"},{"Id":28,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Tây Hồ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Tay Ho"},{"Id":29,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Thanh Xuân","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Thanh Xuan"},{"Id":692,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Thị Xã Sơn Tây","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Thi Xa Son Tay"},{"Id":674,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Ba Vì","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Ba Vi"},{"Id":675,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Chương Mỹ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Chuong My"},{"Id":676,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Đan Phượng","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Dan Phuong"},{"Id":677,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Đông Anh","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Dong Anh"},{"Id":678,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Gia Lâm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Gia Lam"},{"Id":679,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Hoài Đức","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Hoai Duc"},{"Id":680,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Mê Linh","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Me Linh"},{"Id":681,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Mỹ Đức","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen My Duc"},{"Id":682,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Phú Xuyên","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Phu Xuyen"},{"Id":683,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Phúc Thọ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Phuc Tho"},{"Id":684,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Quốc Oai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Quoc Oai"},{"Id":685,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Sóc Sơn","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Soc Son"},{"Id":686,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thạch Thất","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thach That"},{"Id":687,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thanh Oai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thanh Oai"},{"Id":688,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thanh Trì","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thanh Tri"},{"Id":689,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thường Tín","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thuong Tin"},{"Id":691,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Ứng Hòa","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Ung Hoa"}],"allAreas":[],"allDistricts":[],"allPurposes":[],"allCategories":[],"allCuisines":[],"allDishCategories":[],"allProperties":[],"allDinings":[],"selectedAreas":[],"selectedDistricts":[{"Id":21,"Avatar":null,"ParentId":218,"ParentName":null,"Name":"Quận Cầu Giấy","UrlRewriteName":"quan-cau-giay","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":1,"AsciiName":"Quan Cau Giay"}],"selectedPurposes":[],"selectedCategories":[{"Id":3,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quán ăn","UrlRewriteName":"quan-an","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":8,"AsciiName":"Quan an"}],"selectedCuisines":[{"Id":1,"Avatar":"foody-01-vietnam-635950402447733778.png","ParentId":0,"ParentName":null,"Name":"Món Việt","UrlRewriteName":"viet-nam","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[{"Id":12,"Avatar":"foody-12-miennam-635950401085583984.png","ParentId":1,"ParentName":null,"Name":"Món Miền Nam","UrlRewriteName":"mien-nam","ResultCount":24495,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Mien Nam"},{"Id":2,"Avatar":"foody-02-mienbac-635950402329745934.png","ParentId":1,"ParentName":null,"Name":"Món Bắc","UrlRewriteName":"mien-bac","ResultCount":27554,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Bac"},{"Id":7,"Avatar":"foody-07-mientrung-635950401707280292.png","ParentId":1,"ParentName":null,"Name":"Món Miền Trung","UrlRewriteName":"mien-trung","ResultCount":24634,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Mien Trung"},{"Id":29,"Avatar":"foody-29-taynguyen-635950400755089030.png","ParentId":1,"ParentName":null,"Name":"Tây Nguyên","UrlRewriteName":"tay-nguyen","ResultCount":4555,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Tay Nguyen"}],"FilterType":4,"AsciiName":"Mon Viet"}],"selectedDishCategories":[],"selectedProperties":[],"selectedPrices":[],"selectedDinings":[],"searchItems":[{"Address":"223 Tô Hiệu, P. Nghĩa Tân","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":47,"TotalView":5964,"TotalFavourite":40,"TotalCheckins":1,"AvgRating":"7.1","AvgRatingOriginal":7.054000,"ReviewUrl":"/ha-noi/tuyet-nhung-com-ga-phu-yen/binh-luan","AlbumUrl":"/ha-noi/tuyet-nhung-com-ga-phu-yen/album-anh","Latitude":21.0415890000000,"Longitude":105.7924980000000,"MainCategoryId":3,"PictureCount":142,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/tuyet-nhung-com-ga-phu-yen","BranchUrl":"/thuong-hieu/tuyet-nhung-com-ga-phu-yen?c=ha-noi","BranchName":"Hệ thống Tuyết Nhung - Cơm Gà Phú Yên","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"47","TotalPictures":142,"TotalPicturesFormat":"142","TotalSaves":0,"Reviews":[{"Id":14924525,"RestaurantID":0,"RestaurantStatus":0,"UserID":19859387,"Title":"Đắt, chất lượng trung b\u0026#236;nh","Comment":"Quá đắt so với mức giá. Món nộm thì tốt nhất đừng gọi, toàn giá với rau, trà đá cũng thế.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":2.000000,"OwnerUserName":"foodee_kilxyjpk","OwnerFirstName":"Hồng","OwnerLastName":"","OwnerFullName":"Hồng","OwnerAvatar":"https://images.foody.vn/default/s50/user-default-female.png","OwnerGender":"male","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_kilxyjpk","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/tuyet-nhung-com-ga-phu-yen/binh-luan-14924525"},{"Id":8794725,"RestaurantID":0,"RestaurantStatus":0,"UserID":352254,"Title":"Cơm v\u0026#224; g\u0026#224; kh\u0026#244;ng n\u0026#243;ng, gi\u0026#225; cao so với chất lượng","Comment":"Mình đến ăn lúc 5h30 chiều, thấy ăn cơm nguội, gà xé cũng ít và không ngon nóng. Suất cơm gà 40k mà có quá ít cơm và gà. Đồ ăn lại không có gì đặc biệt nữa.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":4.400000,"OwnerUserName":"tungvu3196","OwnerFirstName":"Tung Vu","OwnerLastName":"","OwnerFullName":"Tung Vu","OwnerAvatar":"https://images.foody.vn/usr/g36/352254/avt/c50x50/foody-avatar-981-637145531689255321.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/tungvu3196","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/tuyet-nhung-com-ga-phu-yen/binh-luan-8794725"}],"ReviewsTest":null,"IsOpening":false,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/tuyet-nhung-com-ga-phu-yen/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":737094,"Name":"Tuyết Nhung - Cơm Gà Phú Yên - Tô Hiệu","UrlRewriteName":"tuyet-nhung-com-ga-phu-yen","PicturePath":"https://images.foody.vn/res/g74/737094/prof/s180x180/foody-upload-api-foody-mobile-phu-yen-jpg-180503093800.jpg","PicturePathLarge":"https://images.foody.vn/res/g74/737094/prof/s640x400/foody-upload-api-foody-mobile-phu-yen-jpg-180503093800.jpg","MobilePicturePath":"https://images.foody.vn/res/g74/737094/prof/s640x400/foody-upload-api-foody-mobile-phu-yen-jpg-180503093800.jpg","DetailUrl":"/ha-noi/tuyet-nhung-com-ga-phu-yen","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"25 Nguyễn Phong Sắc, P. Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":32,"TotalView":16155,"TotalFavourite":25,"TotalCheckins":8,"AvgRating":"7.0","AvgRatingOriginal":6.962000,"ReviewUrl":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/binh-luan","AlbumUrl":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/album-anh","Latitude":21.0368480000000,"Longitude":105.7897550000000,"MainCategoryId":3,"PictureCount":153,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/che-dua-thai-lan-nguyen-phong-sac","BranchUrl":"/thuong-hieu/che-dua-thai-lan-nguyen-phong-sac?c=ha-noi","BranchName":"Hệ thống Chè Dừa Thái Lan - Nguyễn Phong Sắc","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"32","TotalPictures":153,"TotalPicturesFormat":"153","TotalSaves":0,"Reviews":[{"Id":2921035,"RestaurantID":0,"RestaurantStatus":0,"UserID":616780,"Title":"Qu\u0026#225; ch\u0026#225;n ng\u0026#224;y thất tịch","Comment":"Hôm nay gấu bảo ngày ngưu lang chức nữ gặp nhau nên ăn chè đỗ đỏ, mình mới đặt chè đỗ đỏ với 1 số loại chè khác. Grab đến quán bảo đợi 10p vì phải nấu, uh thì mình đợi. Xong grab gọi lại bảo hết tất c...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":1.000000,"OwnerUserName":"thang0208","OwnerFirstName":"Thang","OwnerLastName":"Ngoc","OwnerFullName":"Thang Ngoc","OwnerAvatar":"https://images.foody.vn/usr/g62/616780/avt/c50x50/beauty-upload-api-foody-avatar-69fb5139-a52b-40d4-95d7-efa8a0cd871b-191020213924.jpg","OwnerGender":"male","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/thang0208","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/binh-luan-2921035"},{"Id":2790695,"RestaurantID":0,"RestaurantStatus":0,"UserID":8610623,"Title":"Ch\u0026#232; Dừa Th\u0026#225;i Lan - Nguyễn Phong Sắc","Comment":"Quán nhỏ xinh nằm ngay đầu đường nguyễn phong sắc,ngã 4 trần thái tông xuân thủy cầu giấy.\n\nMenu đa dạng với các loại chè như chè sầu,dừa dầm đến những loại chè truyền thống như chè bưởi,chè đỗ đen..v...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.600000,"OwnerUserName":"xjuzoyr","OwnerFirstName":"Linh","OwnerLastName":"Chi","OwnerFullName":"Linh Chi","OwnerAvatar":"https://images.foody.vn/usr/g862/8610623/avt/c50x50/xjuzoyr-avatar-373-636750583830011143.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/xjuzoyr","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/binh-luan-2790695"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":214084,"Name":"Chè Dừa Thái Lan - Nguyễn Phong Sắc","UrlRewriteName":"che-dua-thai-lan-nguyen-phong-sac","PicturePath":"https://images.foody.vn/res/g22/214084/prof/s180x180/foody-mobile-dua640-jpg-631-635953770711301483.jpg","PicturePathLarge":"https://images.foody.vn/res/g22/214084/prof/s640x400/foody-mobile-dua640-jpg-631-635953770711301483.jpg","MobilePicturePath":"https://images.foody.vn/res/g22/214084/prof/s640x400/foody-mobile-dua640-jpg-631-635953770711301483.jpg","DetailUrl":"/ha-noi/che-dua-thai-lan-nguyen-phong-sac","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"P105A C7 Nghĩa Tân, Ngõ 140 Trần Tử Bình, P. Nghĩa Tân","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":36,"TotalView":42685,"TotalFavourite":13,"TotalCheckins":8,"AvgRating":"7.3","AvgRatingOriginal":7.316000,"ReviewUrl":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/binh-luan","AlbumUrl":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/album-anh","Latitude":21.0425066000000,"Longitude":105.7910876000000,"MainCategoryId":3,"PictureCount":133,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"36","TotalPictures":133,"TotalPicturesFormat":"133","TotalSaves":0,"Reviews":[{"Id":11798200,"RestaurantID":0,"RestaurantStatus":0,"UserID":11579565,"Title":"H\u0026#249;ng B\u0026#233;o - Lẩu Cua Đồng - Trần Tử B\u0026#236;nh","Comment":"Thi thoảng đi ăn lại thì thấy chất lượng quán tốt hơn so vs lần trước mình ăn rồi.😛","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.000000,"OwnerUserName":"Chi2k","OwnerFirstName":"Quỳnhchi","OwnerLastName":"Nguyễn","OwnerFullName":"Quỳnhchi Nguyễn","OwnerAvatar":"https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Chi2k","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/binh-luan-11798200"},{"Id":10567766,"RestaurantID":0,"RestaurantStatus":0,"UserID":11579565,"Title":"H\u0026#249;ng B\u0026#233;o - Lẩu Cua Đồng - Trần Tử B\u0026#236;nh","Comment":"Quán mới đổi người  nấu hay sao ấy mà hôm mình ăn lẩu ếch lại đắt hơn mà nấu siêu nhiều mỡ, thề lần đầu tiên ăn thấy chán như thế😔","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":7.000000,"OwnerUserName":"Chi2k","OwnerFirstName":"Quỳnhchi","OwnerLastName":"Nguyễn","OwnerFullName":"Quỳnhchi Nguyễn","OwnerAvatar":"https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Chi2k","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/binh-luan-10567766"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":160574,"Name":"Hùng Béo - Lẩu Cua Đồng - Trần Tử Bình","UrlRewriteName":"hung-beo-lau-cua-dong-tran-tu-binh","PicturePath":"https://images.foody.vn/res/g17/160574/prof/s180x180/foody-mobile-960x600_hung-beo-lau-533-636147262410516048.jpg","PicturePathLarge":"https://images.foody.vn/res/g17/160574/prof/s640x400/foody-mobile-960x600_hung-beo-lau-533-636147262410516048.jpg","MobilePicturePath":"https://images.foody.vn/res/g17/160574/prof/s640x400/foody-mobile-960x600_hung-beo-lau-533-636147262410516048.jpg","DetailUrl":"/ha-noi/hung-beo-lau-cua-dong-tran-tu-binh","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"15 Trần Bình","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":23,"TotalView":37441,"TotalFavourite":37,"TotalCheckins":15,"AvgRating":"7.3","AvgRatingOriginal":7.320000,"ReviewUrl":"/ha-noi/ole-banh-truyen-thong-nhat-ban/binh-luan","AlbumUrl":"/ha-noi/ole-banh-truyen-thong-nhat-ban/album-anh","Latitude":21.0361150000000,"Longitude":105.7788790000000,"MainCategoryId":3,"PictureCount":171,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":false,"BookingUrl":"","DeliveryUrl":"","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"23","TotalPictures":171,"TotalPicturesFormat":"171","TotalSaves":0,"Reviews":[{"Id":2053668,"RestaurantID":0,"RestaurantStatus":0,"UserID":512100,"Title":"Ole - B\u0026#225;nh Truyền Thống Nhật Bản","Comment":"Ngon sạch. Vọ trí hơi nóng. Nhân viên nhanh nhẹn vui vẻ. Cần trang trí không gian quán cho phù hợp hơn đẻ tránh tình trạng nóng quá tải khách","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.600000,"OwnerUserName":"Cuongmy","OwnerFirstName":"Cường","OwnerLastName":"My","OwnerFullName":"Cường My","OwnerAvatar":"https://images.foody.vn/usr/g52/512100/avt/c50x50/beauty-upload-api-foody-avatar-5734e3fe-3efd-4703-aeec-083401b954c1-190814200612.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Cuongmy","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/ole-banh-truyen-thong-nhat-ban/binh-luan-2053668"},{"Id":2051031,"RestaurantID":0,"RestaurantStatus":0,"UserID":9123375,"Title":"Hot Dog khổng lồ","Comment":"Hot dog khổng lồ ăn mãi hết. Vỏ rất giòn, nếu bạn nào sợ ngất thì cứ vô tư ăn vì dù chiên dầu nhưng k ngấy đâu nhé. Chị chủ chiên rất khéo vỏ vàng ruộm, sốt ngon cực đỉnh lun.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.800000,"OwnerUserName":"Hien_nt","OwnerFirstName":"Hien_nt","OwnerLastName":"","OwnerFullName":"Hien_nt","OwnerAvatar":"https://images.foody.vn/usr/g913/9123375/avt/c50x50/beauty-upload-api-foody-avatar-394d790d-d30a-4769-a330-363891ecd622-191215142508.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Hien_nt","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/ole-banh-truyen-thong-nhat-ban/binh-luan-2051031"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":214740,"Name":"Ole - Bánh Truyền Thống Nhật Bản","UrlRewriteName":"ole-banh-truyen-thong-nhat-ban","PicturePath":"https://images.foody.vn/res/g22/214740/prof/s180x180/foody-mobile-ole640-jpg-850-635949570629965289.jpg","PicturePathLarge":"https://images.foody.vn/res/g22/214740/prof/s640x400/foody-mobile-ole640-jpg-850-635949570629965289.jpg","MobilePicturePath":"https://images.foody.vn/res/g22/214740/prof/s640x400/foody-mobile-ole640-jpg-850-635949570629965289.jpg","DetailUrl":"/ha-noi/ole-banh-truyen-thong-nhat-ban","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"67 Yên Hòa, P. Yên Hòa","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":35,"TotalView":2696,"TotalFavourite":20,"TotalCheckins":6,"AvgRating":"7.2","AvgRatingOriginal":7.162000,"ReviewUrl":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/binh-luan","AlbumUrl":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/album-anh","Latitude":21.0233415000000,"Longitude":105.7958695000000,"MainCategoryId":3,"PictureCount":104,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/bun-cha-nem-cua-be-yen-hoa","BranchUrl":"/thuong-hieu/bun-cha-nem-cua-be?c=ha-noi","BranchName":"Hệ thống Bún Chả \u0026 Nem Cua Bể","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"35","TotalPictures":104,"TotalPicturesFormat":"104","TotalSaves":0,"Reviews":[{"Id":14908494,"RestaurantID":0,"RestaurantStatus":0,"UserID":19869596,"Title":"Bố xin ch\u0026#250;ng m\u0026#224;y đấyyyyy","Comment":"Làm ăn bát nháo vãi l, rau đéo có, bát đéo có đũa đéo có. ĂN BỐC À.\nBÚN THÌ CHUA, DC 3 CÁI MIẾNG THỊT LÀM ANH bố m đói.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":1.000000,"OwnerUserName":"foodee_x1j5uvj3","OwnerFirstName":"Hiếu","OwnerLastName":"PCI","OwnerFullName":"Hiếu PCI","OwnerAvatar":"https://images.foody.vn/usr/g1987/19869596/avt/c50x50/foody-avatar-654-637777768251432573.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_x1j5uvj3","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/binh-luan-14908494"},{"Id":12985559,"RestaurantID":0,"RestaurantStatus":0,"UserID":11579565,"Title":"B\u0026#250;n Chả \u0026amp; Nem Cua Bể - Y\u0026#234;n H\u0026#242;a","Comment":"Mình đặt 1 bún chả đầy đủ . Bún chả ăn ngon. Nước chấm để trong hộp nắp chắc chắn.","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.200000,"OwnerUserName":"Chi2k","OwnerFirstName":"Quỳnhchi","OwnerLastName":"Nguyễn","OwnerFullName":"Quỳnhchi Nguyễn","OwnerAvatar":"https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Chi2k","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/binh-luan-12985559"}],"ReviewsTest":null,"IsOpening":false,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/bun-cha-nem-cua-be-yen-hoa/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":264770,"Name":"Bún Chả \u0026 Nem Cua Bể - Yên Hòa","UrlRewriteName":"bun-cha-nem-cua-be-yen-hoa","PicturePath":"https://images.foody.vn/res/g27/264770/prof/s180x180/foody-mobile-nem-cua-be-6831-1432-565-636064356571448314.jpg","PicturePathLarge":"https://images.foody.vn/res/g27/264770/prof/s640x400/foody-mobile-nem-cua-be-6831-1432-565-636064356571448314.jpg","MobilePicturePath":"https://images.foody.vn/res/g27/264770/prof/s640x400/foody-mobile-nem-cua-be-6831-1432-565-636064356571448314.jpg","DetailUrl":"/ha-noi/bun-cha-nem-cua-be-yen-hoa","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"2/421 Hoàng Quốc Việt, P. Nghĩa Tân","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":42,"TotalView":1701,"TotalFavourite":14,"TotalCheckins":8,"AvgRating":"7.9","AvgRatingOriginal":7.882000,"ReviewUrl":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/binh-luan","AlbumUrl":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/album-anh","Latitude":21.0458140000000,"Longitude":105.7860350000000,"MainCategoryId":3,"PictureCount":104,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"42","TotalPictures":104,"TotalPicturesFormat":"104","TotalSaves":0,"Reviews":[{"Id":6659403,"RestaurantID":0,"RestaurantStatus":0,"UserID":18306374,"Title":"Ch\u0026#225;n","Comment":"Rau sống héo úa hỏng, quất thì toàn thối, thiếu dưa chuột. Ăn bún đậu mắm tôm mà k có quất thì mất vị quá. Quán làm chán quá!","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":3.400000,"OwnerUserName":"foodee_pxcljj8i","OwnerFirstName":"Nguyễn","OwnerLastName":"Linh","OwnerFullName":"Nguyễn Linh","OwnerAvatar":"https://images.foody.vn/usr/g1831/18306374/avt/c50x50/beauty-upload-api-foody-avatar-423ea137-da03-4d9c-b025-3c1d959dd4d6-191130193559.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_pxcljj8i","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/binh-luan-6659403"},{"Id":4754815,"RestaurantID":0,"RestaurantStatus":0,"UserID":18004183,"Title":"B\u0026#250;n Đậu C\u0026#250;c***- Ho\u0026#224;ng Quốc Việt","Comment":"Ngon , vừa miệng❤️giá cả hợp lí                                                ","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":10.000000,"OwnerUserName":"foodee_9dicnbry","OwnerFirstName":"Quỳnh","OwnerLastName":null,"OwnerFullName":"Quỳnh","OwnerAvatar":"https://images.foody.vn/default/s50/user-default-female.png","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_9dicnbry","OwnerDisplayName":null,"ShortReview":true,"Url":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/binh-luan-4754815"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":762583,"Name":"Bún Đậu Cúc Cu - Hoàng Quốc Việt","UrlRewriteName":"bun-dau-met-cuc-cu-hoang-quoc-viet","PicturePath":"https://images.foody.vn/res/g77/762583/prof/s180x180/image-e3bc5f75-200910115833.jpeg","PicturePathLarge":"https://images.foody.vn/res/g77/762583/prof/s640x400/image-e3bc5f75-200910115833.jpeg","MobilePicturePath":"https://images.foody.vn/res/g77/762583/prof/s640x400/image-e3bc5f75-200910115833.jpeg","DetailUrl":"/ha-noi/bun-dau-met-cuc-cu-hoang-quoc-viet","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"66 Duy Tân, P. Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":31,"TotalView":13690,"TotalFavourite":38,"TotalCheckins":6,"AvgRating":"6.4","AvgRatingOriginal":6.388000,"ReviewUrl":"/ha-noi/pho-cuon-ngu-xa-duy-tan/binh-luan","AlbumUrl":"/ha-noi/pho-cuon-ngu-xa-duy-tan/album-anh","Latitude":21.0312530000000,"Longitude":105.7822150000000,"MainCategoryId":3,"PictureCount":106,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/pho-cuon-ngu-xa-duy-tan","BranchUrl":"/thuong-hieu/pho-cuon-ngu-xa?c=ha-noi","BranchName":"Hệ thống Phở Cuốn Ngũ Xã","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"31","TotalPictures":106,"TotalPicturesFormat":"106","TotalSaves":0,"Reviews":[{"Id":13742585,"RestaurantID":0,"RestaurantStatus":0,"UserID":19365772,"Title":"Đồ ăn oke - vừa gi\u0026#225;","Comment":"Ngày trước chưa dịch, buổi trưa ra đây ăn rất đông. Đợt này chỉ đc bán mang về nên chắc cũng đỡ, mình thấy ship nhanh và khá cẩn thận. Đồ ăn vẫn ổn, phù hợp giá tiền. Mình gọi phở chiên phồng và 1 cốc...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":7.600000,"OwnerUserName":"foodee_u32az83y","OwnerFirstName":"Trang Hoàng","OwnerLastName":"","OwnerFullName":"Trang Hoàng","OwnerAvatar":"https://images.foody.vn/default/s50/user-default-female.png","OwnerGender":"female","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_u32az83y","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/pho-cuon-ngu-xa-duy-tan/binh-luan-13742585"},{"Id":10262683,"RestaurantID":0,"RestaurantStatus":0,"UserID":11579565,"Title":"Phở Cuốn Ngũ X\u0026#227; - Duy T\u0026#226;n","Comment":"-phở cuốn ở đây ăn khá đầy, ăn 10 cái là no căng bụng luôn ấy. Thấy review khen chê thất thường , nhưng mình thấy ăn ở quán vẫn oke .","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.000000,"OwnerUserName":"Chi2k","OwnerFirstName":"Quỳnhchi","OwnerLastName":"Nguyễn","OwnerFullName":"Quỳnhchi Nguyễn","OwnerAvatar":"https://images.foody.vn/usr/g1158/11579565/avt/c50x50/chi2k-avatar-159-637309618490498502.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Chi2k","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/pho-cuon-ngu-xa-duy-tan/binh-luan-10262683"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/pho-cuon-ngu-xa-duy-tan/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":109338,"Name":"Phở Cuốn Ngũ Xã - Duy Tân","UrlRewriteName":"pho-cuon-ngu-xa-duy-tan","PicturePath":"https://images.foody.vn/res/g11/109338/prof/s180x180/foody-mobile-pho-cuon2-jpg-934-635550098425249236.jpg","PicturePathLarge":"https://images.foody.vn/res/g11/109338/prof/s640x400/foody-mobile-pho-cuon2-jpg-934-635550098425249236.jpg","MobilePicturePath":"https://images.foody.vn/res/g11/109338/prof/s640x400/foody-mobile-pho-cuon2-jpg-934-635550098425249236.jpg","DetailUrl":"/ha-noi/pho-cuon-ngu-xa-duy-tan","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"2 Hẻm 32 Ngách 5 Ngõ 204 Trần Duy Hưng, P. Trung Hòa","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":28,"TotalView":3144,"TotalFavourite":36,"TotalCheckins":7,"AvgRating":"6.4","AvgRatingOriginal":6.418000,"ReviewUrl":"/ha-noi/xoi-tam-thai-ha/binh-luan","AlbumUrl":"/ha-noi/xoi-tam-thai-ha/album-anh","Latitude":21.0089670000000,"Longitude":105.7966910000000,"MainCategoryId":3,"PictureCount":111,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/xoi-tam-thai-ha","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"28","TotalPictures":111,"TotalPicturesFormat":"111","TotalSaves":0,"Reviews":[{"Id":3732556,"RestaurantID":0,"RestaurantStatus":0,"UserID":1662701,"Title":"X\u0026#244;i T\u0026#225;m - Th\u0026#225;i H\u0026#224;","Comment":"Xôi Tám - 322 Thái Hà \n\nBạn sẽ order các topping và xôi theo ý muốn , có hai loại xôi là xôi xéo (15k) và xôi trắng(10k) xôi dẻo và ngon lắm nha. CÒn topping thì giá dao động từ 8k-15k tuỳ loại : xá x...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":8.600000,"OwnerUserName":"hoanganh8790","OwnerFirstName":"Trang","OwnerLastName":"Hoang","OwnerFullName":"Trang Hoang","OwnerAvatar":"https://images.foody.vn/usr/g167/1662701/avt/c50x50/beauty-upload-api-foody-avatar-62f86f2f-250c-407d-be57-92ccccc540d9-191025131450.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/hoanganh8790","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/xoi-tam-thai-ha/binh-luan-3732556"},{"Id":3713181,"RestaurantID":0,"RestaurantStatus":0,"UserID":15480563,"Title":"X\u0026#244;i T\u0026#225;m - Th\u0026#225;i H\u0026#224;","Comment":"Thật không thể tin vào mắt mình..! Xôi chưa bằng 1 nắm tay :(( sẽ không có lần t2 hic","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":1.000000,"OwnerUserName":"foodee_667zapgi","OwnerFirstName":"Anhh","OwnerLastName":"Linhh","OwnerFullName":"Anhh Linhh","OwnerAvatar":"https://images.foody.vn/usr/g1549/15480563/avt/c50x50/beauty-upload-api-foody-avatar-482e93a1-e57a-4ff9-bf2d-b6d7e3176eb0-191216001840.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_667zapgi","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/xoi-tam-thai-ha/binh-luan-3713181"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/xoi-tam-thai-ha/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":647491,"Name":"Xôi Tám - Trần Duy Hưng","UrlRewriteName":"xoi-tam-thai-ha","PicturePath":"https://images.foody.vn/res/g65/647491/prof/s180x180/foody-mobile-xoi-tam-jpg-523-636410905562883010.jpg","PicturePathLarge":"https://images.foody.vn/res/g65/647491/prof/s640x400/foody-mobile-xoi-tam-jpg-523-636410905562883010.jpg","MobilePicturePath":"https://images.foody.vn/res/g65/647491/prof/s640x400/foody-mobile-xoi-tam-jpg-523-636410905562883010.jpg","DetailUrl":"/ha-noi/xoi-tam-thai-ha","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"273 Tô Hiệu, P. Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":30,"TotalView":1281,"TotalFavourite":38,"TotalCheckins":4,"AvgRating":"8.7","AvgRatingOriginal":8.700000,"ReviewUrl":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/binh-luan","AlbumUrl":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/album-anh","Latitude":21.0415730000000,"Longitude":105.7914360000000,"MainCategoryId":3,"PictureCount":29,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/safodi-buffet-lau-hoi-lau-nuong","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"30","TotalPictures":29,"TotalPicturesFormat":"29","TotalSaves":0,"Reviews":[{"Id":9996039,"RestaurantID":0,"RestaurantStatus":0,"UserID":20049115,"Title":"Lẩu ở đ\u0026#226;y ok","Comment":"Mình đến lúc gần 8h tối, khách vãng lai may vẫn còn bàn. Phục vụ tận tình, lẩu ra nhanh, lên đồ cũng nhanh. Mình gọi suất 99k có cá viên bò viên, ba chỉ bò, thịt lợn, ngao, đậu, váng đậu, xúc xích, ra...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.400000,"OwnerUserName":"foodee_d9s9jwjp","OwnerFirstName":"Hiền","OwnerLastName":"Lê","OwnerFullName":"Hiền Lê","OwnerAvatar":"https://images.foody.vn/usr/g2005/20049115/avt/c50x50/beauty-upload-api-foody-avatar-723ab79f-3a4f-4453-a455-948d19f153fd-200504094741.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_d9s9jwjp","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/binh-luan-9996039"},{"Id":9399442,"RestaurantID":0,"RestaurantStatus":0,"UserID":22274735,"Title":"Safodi - Buffet Lẩu Hơi \u0026amp; Lẩu Nướng","Comment":"Với mình thì lẩu ở đây khá ngon , vị đậm đà . Chiều buồn buồn se mát thế này mà húp nước lẩu chua ngọt bên quán thì quá đã . Giá cũng hợp lí . Khá hài lòng .","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.000000,"OwnerUserName":"terrycjtroller","OwnerFirstName":"Huyen Hoa","OwnerLastName":"Nguyen","OwnerFullName":"Huyen Hoa Nguyen","OwnerAvatar":"https://images.foody.vn/usr/g2228/22274735/avt/c50x50/foody-avatar-445-637449429964270545.jpg","OwnerGender":"female","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/terrycjtroller","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/binh-luan-9399442"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":1042834,"Name":"Safodi - Buffet Lẩu Hơi \u0026 Lẩu Nướng","UrlRewriteName":"safodi-buffet-lau-hoi-lau-nuong","PicturePath":"https://images.foody.vn/res/g105/1042834/prof/s180x180/file_restaurant_photo_tbzf_16576-bf99d9bf-220712134254.jpg","PicturePathLarge":"https://images.foody.vn/res/g105/1042834/prof/s640x400/file_restaurant_photo_tbzf_16576-bf99d9bf-220712134254.jpg","MobilePicturePath":"https://images.foody.vn/res/g105/1042834/prof/s640x400/file_restaurant_photo_tbzf_16576-bf99d9bf-220712134254.jpg","DetailUrl":"/ha-noi/safodi-buffet-lau-hoi-lau-nuong","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"36 Phố Dịch Vọng Hậu, P. Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"}],"SpecialDesc":null,"TotalReview":34,"TotalView":8162,"TotalFavourite":25,"TotalCheckins":9,"AvgRating":"7.1","AvgRatingOriginal":7.078000,"ReviewUrl":"/ha-noi/pho-dinh-3-dich-vong-hau/binh-luan","AlbumUrl":"/ha-noi/pho-dinh-3-dich-vong-hau/album-anh","Latitude":21.0325152000000,"Longitude":105.7870686000000,"MainCategoryId":3,"PictureCount":98,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/pho-dinh-3-dich-vong-hau","BranchUrl":"/thuong-hieu/pho-dinh-3?c=ha-noi","BranchName":"Hệ thống Phở Định 3","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"34","TotalPictures":98,"TotalPicturesFormat":"98","TotalSaves":0,"Reviews":[{"Id":16123956,"RestaurantID":0,"RestaurantStatus":0,"UserID":14880419,"Title":"Qu\u0026#225; tệ anh em ạ !","Comment":"Phở định giờ ăn chán , thái độ từ nhân viên đến chủ lồi lõm ! \nHôm mình đi ăn 3 ngừoi là gần cuối canh , bánh phở cứng , nước mặn ko sắc đc như xưa ! \nĐang ăn thì chủ quán tắt điện đánh phụp như đuổi ...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":5.000000,"OwnerUserName":"billgates_2028","OwnerFirstName":"Khánh","OwnerLastName":"Nguyễn Gia","OwnerFullName":"Khánh Nguyễn Gia","OwnerAvatar":"https://images.foody.vn/usr/g1489/14880419/avt/c50x50/beauty-upload-api-foody-avatar-7f2bc26c-9b7d-411d-ad51-e8a66585c493-191122121319.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/billgates_2028","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/pho-dinh-3-dich-vong-hau/binh-luan-16123956"},{"Id":7099955,"RestaurantID":0,"RestaurantStatus":0,"UserID":1301649,"Title":"Phở Định 3 - Đồng B\u0026#244;ng","Comment":"sáng nay đi ăn phở nạm gầu, thấy quán vẫn tấp nập khách ra vào mặc kệ covid 😀 menu có nhiều lựa chọn, giá trung bình 50k, phở lõi thì 70k. còn có cả phở không thịt và phở cho trẻ em, quẩy 1 người và ...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":7.800000,"OwnerUserName":"rosecloud121","OwnerFirstName":"Mint","OwnerLastName":"Ng","OwnerFullName":"Mint Ng","OwnerAvatar":"https://images.foody.vn/usr/g131/1301649/avt/c50x50/ruka-avatar-711-637173934938683397.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/rosecloud121","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/pho-dinh-3-dich-vong-hau/binh-luan-7099955"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/pho-dinh-3-dich-vong-hau/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":29272,"Name":"Phở Định 3 - Dịch Vọng Hậu","UrlRewriteName":"pho-dinh-3-dich-vong-hau","PicturePath":"https://images.foody.vn/res/g3/29272/prof/s180x180/foody-mobile-pho-jpg-932-635917368774327730.jpg","PicturePathLarge":"https://images.foody.vn/res/g3/29272/prof/s640x400/foody-mobile-pho-jpg-932-635917368774327730.jpg","MobilePicturePath":"https://images.foody.vn/res/g3/29272/prof/s640x400/foody-mobile-pho-jpg-932-635917368774327730.jpg","DetailUrl":"/ha-noi/pho-dinh-3-dich-vong-hau","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"115 B7 Tô Hiệu, P. Nghĩa Tân","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":12,"Name":"Món Miền Nam","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-mien-nam"}],"SpecialDesc":null,"TotalReview":32,"TotalView":9671,"TotalFavourite":35,"TotalCheckins":3,"AvgRating":"7.0","AvgRatingOriginal":6.950000,"ReviewUrl":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/binh-luan","AlbumUrl":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/album-anh","Latitude":21.0438417000000,"Longitude":105.7965615000000,"MainCategoryId":3,"PictureCount":74,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"32","TotalPictures":74,"TotalPicturesFormat":"74","TotalSaves":0,"Reviews":[{"Id":6940305,"RestaurantID":0,"RestaurantStatus":0,"UserID":20196225,"Title":"B\u0026#225;nh X\u0026#232;o \u0026amp; Nem Lụi -***","Comment":"Quán hơi bị ngon nha. Giao hàng nhanh. Bánh xèo chuẩn vị, giòn, ít dầu so với quán khác. Ngon nhất vẫn là nem lụi","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":10.000000,"OwnerUserName":"foodee_om9w0plt","OwnerFirstName":"Duy","OwnerLastName":"","OwnerFullName":"Duy","OwnerAvatar":"https://images.foody.vn/default/s50/user-default-female.png","OwnerGender":"male","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_om9w0plt","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/binh-luan-6940305"},{"Id":4004457,"RestaurantID":0,"RestaurantStatus":0,"UserID":19046663,"Title":"B\u0026#225;nh X\u0026#232;o \u0026amp; Nem Lụi -***","Comment":"Ngày xưa đây là quán tủ của  mình, từ hồi nem còn 5k 1 cái, mà về sau tăng lên 6k vẫn ok, nhưng dạo gần đây mấy lát xoài cắt quá dày nên ăn ko đc ngon, đỉnh điểm lad hôm qua gọi đĩa nem ăn vừa nguội v...","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":4.600000,"OwnerUserName":"foodee_fohig9fa","OwnerFirstName":"Dũng","OwnerLastName":"Thái Việt","OwnerFullName":"Dũng Thái Việt","OwnerAvatar":"https://images.foody.vn/usr/g1905/19046663/avt/c50x50/beauty-upload-api-foody-avatar-bee17315-9f84-4ab5-9c7a-04e0f40d6617-200207173213.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/foodee_fohig9fa","OwnerDisplayName":null,"ShortReview":false,"Url":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/binh-luan-4004457"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":231953,"Name":"Song Nguyệt - Bánh Xèo \u0026 Nem Lụi - Tô Hiệu","UrlRewriteName":"song-nguyet-banh-xeo-nem-lui-to-hieu","PicturePath":"https://images.foody.vn/res/g24/231953/prof/s180x180/foody-mobile-34-jpg-265-635974352692854698.jpg","PicturePathLarge":"https://images.foody.vn/res/g24/231953/prof/s640x400/foody-mobile-34-jpg-265-635974352692854698.jpg","MobilePicturePath":"https://images.foody.vn/res/g24/231953/prof/s640x400/foody-mobile-34-jpg-265-635974352692854698.jpg","DetailUrl":"/ha-noi/song-nguyet-banh-xeo-nem-lui-to-hieu","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]},{"Address":"36 ngõ 24  Phan Văn Trường, P.Dịch Vọng Hậu","District":"Quận Cầu Giấy","City":"Hà Nội","Phone":null,"Promotions":[],"Cuisines":[{"Id":1,"Name":"Món Việt","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-viet-nam"},{"Id":21,"Name":"Món Nhật","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-nhat-ban"},{"Id":36,"Name":"Món Á","NameEn":null,"ASCIIName":null,"DetailUrl":"/ha-noi/dia-diem-phong-cach-chau-a"}],"SpecialDesc":null,"TotalReview":172,"TotalView":561,"TotalFavourite":4,"TotalCheckins":0,"AvgRating":"9.6","AvgRatingOriginal":9.626000,"ReviewUrl":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/binh-luan","AlbumUrl":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/album-anh","Latitude":21.0410136000000,"Longitude":105.7875145000000,"MainCategoryId":3,"PictureCount":9,"Status":2,"IconUrl":null,"FriendAction":{"TotalCount":0,"FriendActions":[]},"HasAlredyAddedToList":false,"AdsProviders":[],"DistrictId":21,"DistrictUrl":"/ha-noi/khu-vuc-quan-cau-giay","CategoryGroupKey":null,"Distance":null,"HasBooking":false,"HasDelivery":true,"BookingUrl":"","DeliveryUrl":"https://shopeefood.vn/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp","BranchUrl":"","BranchName":"Hệ thống ","BankCards":[],"Location":"ha-noi","TotalReviewsFormat":"172","TotalPictures":9,"TotalPicturesFormat":"9","TotalSaves":0,"Reviews":[{"Id":16780209,"RestaurantID":0,"RestaurantStatus":0,"UserID":1001288,"Title":"Rất ngonnnn","Comment":"Mình đặt cho anh xã ăn mà anh khen nức nở                                      ","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.000000,"OwnerUserName":"giangxoan11112706","OwnerFirstName":"Nguyễn","OwnerLastName":"T.Giang","OwnerFullName":"Nguyễn T.Giang","OwnerAvatar":"https://images.foody.vn/usr/g101/1001288/avt/c50x50/beauty-upload-api-foody-avatar-e4ff95c4-6f91-4152-b32f-99773576b5ce-191025125259.jpg","OwnerGender":"F","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/giangxoan11112706","OwnerDisplayName":null,"ShortReview":true,"Url":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/binh-luan-16780209"},{"Id":16107545,"RestaurantID":0,"RestaurantStatus":0,"UserID":23299868,"Title":"Phong Th\u0026#224;nhh Qu\u0026#225;n - Qu\u0026#225;n Ăn - Phan Văn Trường","Comment":"Cơm rất ngon , sạch sẽ , làm nhanh , nước sốt rất chi là ưnggg nhé 🍗🍗🍗🍗    ","Guest":null,"MoneySpend":null,"VisitAgain":null,"GuestId":null,"MoneySpendId":null,"VisitAgainId":null,"SelectMenu":null,"CreatedOn":"\/Date(-62135596800000)\/","AvgRating":9.400000,"OwnerUserName":"Thanh_tam_pham_thi","OwnerFirstName":"Thanh Tâm Phạm Thị","OwnerLastName":"","OwnerFullName":"Thanh Tâm Phạm Thị","OwnerAvatar":"https://images.foody.vn/usr/g2330/23299868/avt/c50x50/thanh_tam_pham_thi-avatar-342-637506191180367188.jpg","OwnerGender":"","OwnerIsVerified":false,"OwnerTrustPercent":0,"OwnerTotalPictures":0,"OwnerTotalReviews":0,"TotalPictures":0,"PostedByDevice":null,"ReviewType":0,"YoutubeCode":null,"Pictures":null,"Comments":null,"TotalComments":0,"TotalHelpfuls":0,"TotalLikes":0,"HasLiked":false,"TotalDislikes":0,"HasDisliked":false,"VerifyingPercent":0,"UserLevel":null,"PointRank":0,"Hashtags":null,"Banners":null,"ResUrlRewriteName":null,"ResLocation":null,"TranslateSource":null,"IsOld":false,"ViaSocialType":null,"IsAllowComment":false,"DisplayType":null,"IsLatestCurrentUserReview":false,"CreateOnTimeDiff":null,"UserLiekeds":null,"IsOwner":null,"TotalViews":null,"Video":null,"IsActive":false,"OwnerProfileUrl":"/thanh-vien/Thanh_tam_pham_thi","OwnerDisplayName":null,"ShortReview":true,"Url":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/binh-luan-16107545"}],"ReviewsTest":null,"IsOpening":true,"HasVideo":false,"MasterCategoryId":1,"Services":[{"Id":1,"Type":0,"Url":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp/goi-mon","Title":null,"Text":"Giao tận nơi","Avatar":null,"BackgroundColor":null,"RestaurantId":0,"Description":null}],"Floor":{"Id":0,"Code":null,"Name":null,"NameEn":null,"Avatar":"https://images.foody.vn/default/s50/no-image.png","Color":null,"Description":null,"DescriptionEn":null},"Categories":[{"Id":3,"Name":"Quán ăn","NameEn":null,"ASCIIName":null,"DetailUrl":null},{"Id":28,"Name":"Giao cơm văn phòng","NameEn":null,"ASCIIName":null,"DetailUrl":null}],"BookingMobileUrl":"","PromotionPlainTitle":null,"Id":1000027868,"Name":"Phong Thànhh Quán - Quán Ăn - Phan Văn Trường","UrlRewriteName":"phong-thanhh-quan-quan-an-phan-van-truong.glrxgp","PicturePath":"https://images.foody.vn/res/g100003/1000027868/prof/s180x180/file_restaurant_photo_ykxn_16254-2fdda806-210705174327.jpeg","PicturePathLarge":"https://images.foody.vn/res/g100003/1000027868/prof/s640x400/file_restaurant_photo_ykxn_16254-2fdda806-210705174327.jpeg","MobilePicturePath":"https://images.foody.vn/res/g100003/1000027868/prof/s640x400/file_restaurant_photo_ykxn_16254-2fdda806-210705174327.jpeg","DetailUrl":"/ha-noi/phong-thanhh-quan-quan-an-phan-van-truong.glrxgp","DocumentType":0,"ShowInSearchResult":false,"IsAd":false,"SubItems":[]}],"adItems":[],"totalResult":2455,"currentPage":4,"locationQuery":null,"maxPageToLoad":5,"brand":"","providerList":[],"book":false,"totalSubItems":59,"documentSource":"Restaurant","listResultCount":93042,"restaurantResultCount":2514,"userResultCount":7330050,"articleResultCount":4395,"pictureResultCount":20947};
    var resultExcutedCallback = function () {
        bindDeliverService();
    }

    function googleLoadMap()
    {
        if(window.initInfoBox)
            initInfoBox();

    }

				</script>





				<div id="tab-footer-top-friend-user" class="microsite-banner-edge"
					style="background-color: #fff; padding: 20px 0; float: left; clear: both; width: 100%;position:relative;z-index:11;">
					<ul class="home-tab" style="width: 1170px; margin: 0 auto;">
						<li class="active">
							<a href="#tab-footer-top-user" style="padding: 15px 0; margin-right: 60px;">Top Thành
								viên</a>
						</li>

					</ul>

					<div id="tab-footer-top-user">


					</div>


					<script type="text/javascript">
						$(function () {
            $("#tab-footer-top-friend-user").custabs();
        });
					</script>
				</div>


				<div id="addWishListPopup" style="display: none; margin: 0; padding: 0;">

					<div id="banner-ads" class="save-popup-ads">


					</div>
					<div class="fldg-left" data-bind="visible:IsLoadingRes()">
						<div class="fldg-left">
							<div class="pre-avatar animated-bg" style="height:188px;width:300px"></div>
							<div style="overflow:hidden; clear:both;">
								<div class="pre-review-points animated-bg" style="margin: 10px 0 0 0;"></div>
								<div style="float: left;width: 255px;margin-left: 10px;margin-top: 13px;">
									<div class="preload-bar long animated-bg" style="margin-bottom: 7px;"></div>
									<div class="preload-bar medium animated-bg" style="clear: both;margin-bottom: 6px;">
									</div>
								</div>
							</div>
							<div class="pre-avatar animated-bg" style="height:36px;width:300px;margin: 10px 0;"></div>
							<div class="fldr-summary" style="height:200px">
							</div>
						</div>


					</div>
					<div class="fldg-left" data-bind="visible:!IsLoadingRes()">
						<div class="fldg-left" data-bind="with:ResSummary">
							<a>
								<img class="fldr-res-avatar" src="" data-bind="attr:{src:Restaurant.Avatar}">
            </a>
								<div style="overflow:hidden; clear:both;">
									<div class="review-points green"
										data-bind="css:{'green':Restaurant.AvgRating>=6, 'grey':Restaurant.AvgRating==0||Restaurant.AvgRating==null}">
										<span data-bind="text:Restaurant.AvgRating.formatPoint()">_._</span>
									</div>

									<div style="float: left; width: 255px; margin-left: 10px;">
										<div class="fldr-res-title ng-binding" data-bind="text:Restaurant.Name">&nbsp;
										</div>
										<div class="fldr-res-address ng-binding" data-bind="text:Restaurant.Address">
											&nbsp;</div>
									</div>
								</div>

								<div><a class="btn-write fd-write-review"
										data-bind="attr:{'data-res-id':$parent.restaurantId,'resid':$parent.restaurantId}"><i class="fa fa-comment"></i>&nbsp;Viết
										bình luận</a></div>

								<div class="fldr-summary">
									<div class="fldr-res-points">
										<span data-bind="text:AvgReview.Total.formatK(0)">&nbsp;</span>&nbsp;Bình luận
									</div>
									<ul>
										<li>
											<div class="counts" data-bind="text:AvgReview.TotalPerfect.formatK(0)">
												&nbsp;</div>
											<div>Tuyệt vời</div>
										</li>
										<li>
											<div class="counts" data-bind="text:AvgReview.TotalGood.formatK(0)">&nbsp;
											</div>
											<div>Khá tốt</div>
										</li>
										<li>
											<div class="counts" data-bind="text:AvgReview.TotalAvg.formatK(0)">&nbsp;
											</div>
											<div>Trung bình</div>
										</li>
										<li>
											<div class="counts" data-bind="text:AvgReview.TotalBad.formatK(0)">&nbsp;
											</div>
											<div>Kém</div>
										</li>
									</ul>
									<div class="fldr-rating">
										<div class="title">Đánh giá:</div>
										<img class="ruler" src="/style/images/icons/ratin-rank.png">
										<ul data-bind="foreach: { data: Rating, as: 'rate' }">
											<li>
												<label data-bind="text:rate.Label">&nbsp;</label>
												<div class="range" data-bind="{attr:{'data-val':rate.Point}}"></div>
												<span data-bind="text:rate.Point">&nbsp;</span>
											</li>
										</ul>
									</div>
								</div>

						</div>
					</div>
					<ul data-bind="if:isLoading()" style="float:right; width:655px;">
						<li class="tool-custom-list">
							<div class="list-addmore-but">
								<span style="float: left; margin-right: 10px;">Chọn bộ sưu tập để lưu lại </span>
								<span data-bind="visible: isLoading" style="float: left; margin-top: 2px;">
                        <img src="/style/images/icons/ajax-loader.gif" alt="loading..." />
                    </span>
								<span style="float:right;" class="fa fa-map-marker">
                    </span>
							</div>
							<div class="custom-list-wrapper">
								<div class="search-of-collections">
									<input class="txt-search-title" type="text" value="" placeholder="T&#236;m kiếm bộ sưu tập theo t&#234;n..." />
									<span class="fa fa-search" style="position: absolute; left: 15px; top: 11px; color: #999;"></span>
									<span class="fa fa-times" style="position: absolute; right: 15px; top: 11px; cursor: pointer;"></span>
								</div>
								<ul class="list-of-collections">
									<li style="position: relative; overflow: hidden;">
										<div
											style="border-bottom: 1px solid #eee;padding: 14px 0px 0px 30px;height: 22px;">
										</div>
									</li>
									<li style="position: relative; overflow: hidden;">
										<div
											style="border-bottom: 1px solid #eee;padding: 14px 0px 0px 30px;height: 22px;">
										</div>
									</li>
									<li style="position: relative; overflow: hidden;">
										<div
											style="border-bottom: 1px solid #eee;padding: 14px 0px 0px 30px;height: 22px;">
										</div>
									</li>
									<li style="position: relative; overflow: hidden;">
										<div
											style="border-bottom: 1px solid #eee;padding: 14px 0px 0px 30px;height: 22px;">
										</div>
									</li>
									<li style="position: relative; overflow: hidden;">
										<div
											style="border-bottom: 1px solid #eee;padding: 14px 0px 0px 30px;height: 22px;">
										</div>
									</li>
									<li style="position: relative; overflow: hidden;">
										<div
											style="border-bottom: 1px solid #eee;padding: 14px 0px 0px 30px;height: 22px;">
										</div>
									</li>
								</ul>

							</div>
							<div class="place-collection-createbutton">
								<div class="pre-avatar animated-bg" style="height:38px;width:100%;margin-top:15px;">
								</div>
							</div>
						</li>


					</ul>

					<ul data-bind="visible:!isLoading()" style="float:right; width:655px;">
						<li class="tool-custom-list">
							<div class="list-addmore-but">
								<span style="float: left; margin-right: 10px;">Chọn bộ sưu tập để lưu lại </span>
								<span data-bind="visible: isLoading" style="float: left; margin-top: 2px;">
                        <img src="/style/images/icons/ajax-loader.gif" alt="loading..." />
                    </span>
								<span style="float:right;" class="fa fa-map-marker">

                    </span>
							</div>
							<div class="custom-list-wrapper">

								<div class="search-of-collections">
									<input class="txt-search-title" type="text" value="" placeholder="T&#236;m kiếm bộ sưu tập theo t&#234;n..."
                               onkeyup="addWishListPopupModel.searchTitleChange();"/>
									<span class="fa fa-search" style="position: absolute; left: 15px; top: 11px; color: #999;"></span>
									<span class="fa fa-times" style="position: absolute; right: 15px; top: 11px; cursor: pointer;" onclick="addWishListPopupModel.clearTitle()"></span>
								</div>
								<ul data-bind="foreach: lists" class="list-of-collections">
									<li style="position: relative; overflow: hidden;"
										data-bind="visible: Title.toLowerCase().indexOf($root.searchTitle().toLowerCase()) > -1">

										<a
											data-bind="attr: { 'data-name': Name }, css: { 'checked': RestaurantId() == $parent.restaurantId() }, click: $parent.toggleSelection">
											<span class="list-label" data-bind="text: Title"></span>
										</a>
										<a data-bind="attr: { href: Url }" href="#" target="_blank" title="Go to list"
											class="custom-list-viewdetail">
											<label data-bind="text:'Xem {0}'.replace('{0}',TotalItems())"></label>
											<i class="fa fa-angle-right"></i>
										</a>
									</li>
								</ul>

							</div>
							<div class="place-collection-createbutton">
								<a href="#" data-bind="click: createNewList">
									+ Tạo bộ sưu tập mới
								</a>
							</div>
						</li>
					</ul>
				</div>
				<script>
					var content = $('#banner-ads').children().length;
    if (content > 0) {
        $("#banner-ads").addClass('ads-banner');
    }
				</script>
				<div class="footer-down-app-wrap"
					style="margin-top:0;background: #eeeeee;position: relative;z-index: 11;">
					<div class="footer-down-app">
						<div class="footer-intro-app">Tìm địa điểm trên đường đi? Tải app Foody!</div>
						<div style="float:left; width:240px;margin-top:-8px;">
							<div
								style="border:#ddd 1px solid; background:#fff;text-align: center; padding: 5px 30px;width:100px;margin-bottom:40px; overflow:hidden; clear:both;">
								Thống kê
							</div>
							<div class="footer-down-stats">
								<div class="footer-down-stats-header">334,384 Địa điểm</div>
								<div class="footer-down-stats-desc">toàn quốc</div>
							</div>
							<div class="footer-down-stats">
								<div class="footer-down-stats-header">38,630,265 người sử dụng</div>
								<div class="footer-down-stats-desc">trong & ngoài nước</div>
							</div>
							<div class="footer-down-stats">
								<div class="footer-down-stats-header">1,481,841 bình luận</div>
								<div class="footer-down-stats-desc">đã chia sẻ</div>
							</div>
							<div class="footer-down-stats">
								<div class="footer-down-stats-header">608,066 check-in</div>
								<div class="footer-down-stats-desc">đã thực hiện</div>
							</div>
							<div class="footer-down-stats">
								<div class="footer-down-stats-header">10,232,333 hình ảnh</div>
								<div class="footer-down-stats-desc">được tải lên</div>
							</div>
							<div class="footer-down-stats">
								<div class="footer-down-stats-header">24,623,376 Bộ sưu tập</div>
								<div class="footer-down-stats-desc">bộ sưu tập được tạo</div>
							</div>

						</div>
						<div style="float:right; width:752px;">


							<a href="https://itunes.apple.com/app/id570435154" target="_blank"
								style="float: left; text-align: center; display: block;" rel="nofollow">
								<span style="border: #ddd 1px solid; background: #fff; padding: 5px 30px; border-radius: 2px;">iOS App</span>
								<img style="margin-top:20px;" src="/style/images/icons/ios-footer.png" alt="App Foody iOS" title="App Foody iOS" />
                </a>
								<a href="https://play.google.com/store/apps/details?id=com.foody.vn.activity"
									target="_blank" style="float: left; text-align: center; display: block;"
									rel="nofollow">
									<span style="border: #ddd 1px solid; background: #fff; padding: 5px 30px; border-radius: 2px;">Android App</span>
									<img style="margin-top:20px;" src="/style/images/icons/android-footer.png" alt="App Foody Android" title="App Foody Android" />
                </a>
									<a href="https://www.windowsphone.com/en-us/store/app/foody/0ed64e33-cff6-4211-a971-71e496ae9066"
										target="_blank" style="float: left; text-align: center; display: block;"
										rel="nofollow">
										<span style="border: #ddd 1px solid; background: #fff; padding: 5px 30px; border-radius: 2px;">Windows App</span>
										<img src="/style/images/icons/windows-footer.png" alt="App Foody WindowPhone" title="App Foody WindowPhone" />
                </a>

						</div>
					</div>
				</div>

				<footer class="footer" id="footer-in-bottom" style="position: relative;z-index: 11;">
					<div class="footer-fixed">
						<div class="footer-min">
							<div class="footer-left-box" style="display:none;">
								<div class="footer-titles">Cài đặt</div>
								<ul>
									<li style="width:100%;float:left;margin:3px 0 7px;">
										<div style="float: left;padding:3px 5px 0 0;color:#666; width:100px;">Tỉnh thành
										</div>
										<div style="float: left;">
											<dl id="f_dropdown" class="drop_seeall">
												<dt>
													<a href="javascript:void(0)"
														style="cursor:default;"><span class="text" style="cursor:default;">H&#224; Nội</span></a>
												</dt>
											</dl>
										</div>
									</li>
									<li style="width:100%;float:left;margin:3px 0 7px;">
										<div style="float: left;padding-right:5px;color:#666; width:100px;">Ngôn ngữ
										</div>
										<div class="footer-language-chooser">

											<a href="javascript:void(0)" style="cursor:default;" rel="nofollow"
												style="color: #02AAD4"
												href="/__get/common/changelanguage?code=vn&amp;returnUrl=http%3A%2F%2Fwww.foody.vn%2Fha-noi%2Fquan-an-phong-cach-viet-nam-tai-quan-cau-giay%3Fc%3Dquan-an%26categorygroup%3Dfood%26page%3D4%26append%3DTrue">
												Tiếng Việt
											</a>
										</div>
									</li>

								</ul>
							</div>
							<div class="footer-middle-box">
								<div class="footer-titles">Khám phá</div>
								<ul>

									<li><a href="/ung-dung-mobile" rel="nofollow">Ứng dụng Mobile</a></li>

									<li><a href="javascript:void(0)" class="add-new-list" rel="nofollow">Tạo bộ sưu
											tập</a></li>

									<li><a href="/bao-mat-thong-tin" rel="nofollow">Bảo mật thông tin</a></li>
									<li><a href="/dieu-khoan-su-dung" rel="nofollow">Quy định</a></li>

								</ul>
							</div>
							<div class="footer-middle-box">
								<div class="footer-titles">Công ty</div>
								<ul>
									<li><a href="/gioi-thieu" rel="nofollow">Giới thiệu</a></li>


									<li><a href="/tro-giup" rel="nofollow">Trợ giúp</a></li>
									<li><a href="/jobs" rel="nofollow">Việc làm</a></li>

									<li><a href="/regulation" rel="nofollow">Quy chế</a></li>
									<li><a href="/thoa-thuan-su-dung" rel="nofollow">Thỏa thuận sử dụng dịch vụ</a></li>
									<li><a href="/lien-he" rel="nofollow">Liên hệ</a></li>
								</ul>
							</div>
							<div class="footer-middle-box" style="padding-left: 35px; width: 200px;" id="footer-join">
								<div class="footer-titles" rel="nofollow">Tham gia trên</div>
								<ul>
									<li><a href="https://www.facebook.com/FoodyVietnam" target="_blank"
											rel="nofollow">Facebook</a></li>
									<li><a href="https://www.instagram.com/foodysaigon" target="_blank"
											rel="nofollow">Instagram</a></li>
									<li><a href="https://www.youtube.com/c/FoodyVn" target="_blank"
											rel="nofollow">Youtube</a></li>
									<li><a href="https://plus.google.com/104802868919802646307" target="_blank"
											rel="publisher">Google</a></li>
									<li style="clear: both;">
										<a href="https://shopeefood.vn" target="_blank" rel="nofollow">
											ShopeeFood.vn
										</a>
										- Giao đồ ăn tận nơi
									</li>
								</ul>
							</div>
							<div class="footer-middle-box" style="padding-left: 35px; width: 160px;">
								<div class="footer-titles">Giấy phép</div>
								<ul>
									<li><a>MXH 363/GP-BTTTT</a></li>

									<li>
										<a target="_blank" rel="nofollow"
											href="http://online.gov.vn/HomePage/WebsiteDisplay.aspx?DocId=13113">
											<img src="/style/images/gov_seals.jpg" width="160" style="margin-left: -5px;" alt="logo-da-dang-ky-bo-cong-thuong" />
                                    </a>
									</li>
								</ul>
							</div>
							<div class="footer-middle-box" style="padding-left: 35px; width: 160px;">

								<script language="JavaScript" src="https://dunsregistered.dnb.com"
									type="text/javascript"></script>
							</div>
						</div>

					</div>
					<div class="footer-country-list">
						<span style="color: #999; clear: both; display: block;">
                        Công Ty Cổ Phần Foody, Lầu G, Tòa nhà Jabes 1, 244 đường Cống Quỳnh, phường Phạm Ngũ Lão, Quận 1, TP.HCM
                    </span>

						<span id="foody-hot-line" style="color: #999; clear: both; display: block;">
                        Email: support@shopeefood.vn
                    </span>

						<span style="color: #999; clear: both; display: block;">
                        Giấy CN ĐKDN số 0311828036 do Sở Kế hoạch và Đầu tư TP.HCM cấp ngày 11/6/2012, sửa đổi lần thứ 23, ngày 10/12/2020
                    </span>
						<span style="color: #999; clear: both; display: block;">
                        Giấy phép thiết lập MXH trên mạng số 363/GP-BTTTT do Bộ Thông tin và Truyền thông cấp ngày 30/6/2016
                        Người chịu trách nhiệm: Đặng Hoàng Minh.
                    </span>



					</div>
					<script>
						function InviteFriend() {
                    
                }
					</script>
				</footer>
				<script>
					$(document).ready(function () {
                //$(window).load(function () {
                    var scrollTo = getParameterByName('scrollto');
                    if (scrollTo != '') {
                        //$('html, body').animate({ scrollTop: $(document).height() }, "fast");
                        //setTimeout(function () {
                            $("html, body").animate({
                                scrollTop: ($(document).height() + $("html, body").height()) + 800
                            }, 2000);
                        //}, 2000);
                    }
                //});
                
            });

            function getParameterByName(name) {
                name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
                var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
                    results = regex.exec(location.search);
                return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
            }
				</script>

				<style type="text/css">
					.popup-download-app {
						position: fixed;
						z-index: 610;
						display: none;
						bottom: 0;
						width: 750px;
						height: 200px;
						background: url(/style/images/popup/750x200_popupdownloadapp.png) no-repeat;
					}

					.popup-download-app .pda-btn-close {
						position: absolute;
						right: 0;
						top: 35px;
						width: 25px;
						height: 25px;
						cursor: pointer;
						z-index: 1;
					}

					.popup-download-app .pda-btn-frame {
						position: absolute;
						left: 5px;
						top: 40px;
						width: 110px;
						bottom: 0;
						z-index: 1;
					}

					.popup-download-app .pda-btn-frame a {
						display: block;
						float: none;
						width: 100%;
						height: 40px;
						margin: 10px 0 10px 0;
						cursor: pointer;
					}

					.popup-download-app .pda-content-link {
						height: 100%;
						position: relative;
					}

					.popup-download-app .pda-qcode {
						position: absolute;
						width: 60px;
						height: 60px;
						right: 40px;
						bottom: 20px;
					}

					.popup-download-app .pda-content-link .pda-content {
						position: absolute;
						left: 300px;
						width: 340px;
						top: 117px;
						color: #959595;
						font-size: 15px;
						white-space: normal;
						line-height: 1.3em;
					}

					.popup-download-app .pda-content-link .pda-content p {
						margin-bottom: 10px;
					}

					.popup-download-app .pda-content-link .pda-content b {
						font-weight: bold;
						font-size: 18px;
						color: #ffffff;
					}
				</style>

				<div class="popup-download-app">
					<div class="pda-btn-close"></div>
					<div class="pda-btn-frame">
						<a href="https://itunes.apple.com/app/id570435154" title="iOS App">
							<img src="/style/images/popup/popupdownload-appstore.png" />
            </a>
							<a href="https://play.google.com/store/apps/details?id=com.foody.vn.activity"
								title="Android App">
								<img src="/style/images/popup/popupdownload-googleplay.png" />
            </a>
								<a href="https://www.windowsphone.com/en-us/store/app/foody/0ed64e33-cff6-4211-a971-71e496ae9066"
									title="Windows App">
									<img src="/style/images/popup/popupdownload-windowstore.png" />
            </a>
					</div>
					<a href="/ung-dung-mobile">
						<div class="pda-content-link">
							<div class="pda-content">
								<p><b>Ứng Dụng tìm kiếm địa điểm ăn uống</b></p>
								<p>Nhanh & tiện lợi - với hàng ngàn địa điểm, bình luận, hình ảnh & thành viên chia sẻ
								</p>
							</div>
						</div>
					</a>
					<img class="pda-qcode" src="/style/images/popup/android-code-vn.png" />

</div>
					<script type="text/javascript">
						//popupDownloadRePosition();
    //function popupDownloadRePosition() {
    //    var popup = $('.popup-download-app');
    //    var wWidth = $(window).innerWidth();
    //    var pWidth = popup.width();
    //    var pLeft = (wWidth - pWidth) / 2;
    //    popup.css('left', pLeft);
    //}
    ////$('.popup-download-app').slideDown(function () { $('.popup-download-app').attr('style', ''); });
    //$('.popup-download-app .pda-btn-close').on('click', function () {
    //    $('.popup-download-app').slideUp();
    //    $.cookie('pda-close', '1', { path: '/' });
    //});
    //setTimeout(function () {
    //    if ($.cookie('pda-close') != '1')
    //        $('.popup-download-app').slideDown();
    //}, 2000);

    //$(window).resize(function () {
    //    popupDownloadRePosition();
    //});

					</script>



					<div id="HelperCtrl" ng-controller="HelperCtrl" style="position:absolute;z-index:10;"></div>

				</div>




				<script>
					function googleLoadMapCallback() {
        if (typeof (googleLoadMap) == "function") {
            googleLoadMap();
        }
    }
				</script>

				<script type="text/javascript"
					src="//maps.googleapis.com/maps/api/js?v=3&amp;callback=googleLoadMapCallback&amp;libraries=visualization,drawing,geometry,places&amp;key=AIzaSyA2Zb2vY8-t_9BUYqFFjc9LQiNWUZPLft4&amp;language=vn">
				</script>





				<script>
					window.dataLanguagesPc = {
        BtnCollectionSaved: 'Đã lưu bộ sưu tập',
        BtnCollectionSave: 'Lưu bộ sưu tập',
        BtnShare: 'Chia sẻ',
        BtnLike: 'Thích',
        BtnUnLike: 'Bỏ thích',
        UpdatedOn: 'Cập nhật ngày',
        Views: 'Lượt xem',
        Photos: 'Hình ảnh',
        BtnViewMoreCollection: 'Xem thêm bộ sưu tập',
        BtnViewMorePhoto: 'Xem thêm hình ảnh',
        DlgPhotoTitleSave: 'Lưu ảnh vào bộ sưu tập',
        InputCollectionName: 'Tên bộ sưu tập',
        Description: 'Mô tả bộ sưu tập',
        BtnCollectionCreate: 'Tạo mới bộ sưu tập',
        BtnCreate: 'Tạo',
        BtnCreateNew: 'Tạo mới bộ sưu tập',
        BtnEdit: 'Chỉnh sửa',
        BtnDelete: 'Xoá',
        BtnPublic: 'Công khai (Public)',
        InputCollectionNameNew: 'Nhập tên bộ sưu tập mới',
        DlgCollectionTitleEdit: 'Chỉnh sửa bộ sưu tập',
        BtnCancel: 'Huỷ',
        BtnSave: 'Lưu',
        Saved: 'Lưu lại',
        Like: 'Thích',
        DlgCollectionTitleShare: 'Chia sẻ bộ sưu tập hình ảnh',
        DlgCollectionChooseMethodShare: 'Vui lòng chọn hình thức chia sẻ',
        MsgConfirmDeletePhoto: 'Bạn có chắc muốn xoá hình này?',
        MsgConfirmDeleteCollection: 'Bạn có chắc muốn xoá bộ sưu tập này?',
        MsgCollectionNameExist: 'Tên bộ sưu tập đã tồn tại',
        MsgAddPhotoSelectRequired: 'Vui lòng chọn hình ảnh của bạn để thêm vào bộ sưu tập này!',
        MsgActionFailure: 'Có lỗi xảy ra trong quá trình xử lý.\r\nBạn vui lòng thử lại sau.',
        FilterByName: 'Tìm kiếm theo tên bộ sưu tập'
    };
				</script>
				<script>
					var PopupSavePhotoModel = function () {
        var self = this;

        var listCollectionModel = function (arg) {
            var self = this;
            var root = arg.root;
            var type = arg.type;
            this.Items = ko.observableArray([]);
            this.Total = ko.observable(0);
            this.LastId = ko.observable(null);
            this.Count = ko.observable(14);

            function createItemModel(item) {
                item.TotalItems = ko.observable(item.TotalItems);
                item.IsChecked = ko.observable(item.IsChecked);
                item.Name = ko.observable(item.Name);
                item.IconState = function (state) {
                    if (state) {
                        if (root.IsLoading() == true) {
                            if (root.Model.Filter.Id() == item.Id)
                                return 'fa fa-circle-o-notch fa-spin';
                        }
                    }
                    return item.IsChecked() == true ? 'fa fa-circle' : 'fa fa-circle-o';
                }
                return item;
            }

            function createCollectionModel(items) {
                var rs = self.Items;
                if (!items || items.length == 0)
                    return rs;
                for (var i = 0; i < items.length; i++) {
                    rs.push(createItemModel(items[i]));
                }
                return rs;
            }

            this.Reset = function () {
                self.Items([]);
                self.Total(0);
                self.LastId(null);
            };
            this.BindData = function (data) {
                createCollectionModel(data.Items);
                self.Total(data.Total);
                self.LastId(data.LastId);
            };

            this.SetCheckedItem = function (id, isChecked) {


                var items = self.Items();
                var len = items.length;

                for (var i = 0; i < len; i++) {
                    var collection = items[i];
                    if (collection.Id == id) {
                        collection.IsChecked(isChecked);
                        var count = collection.TotalItems();
                        if (type == 1)
                            collection.TotalItems(isChecked == true ? count + 1 : count - 1);
                        break;
                    }
                }
            }

            this.fnLoadMore = function () {
                root.bindListCollection({ type: type });
            };
            this.TotalRemaining = function () {
                return self.Total() - self.Items().length;
            };
        };

        var fnCallBack = null;
        var bPopup = null;
        var selector = '#ppSavePhoto';
        self.IsLoading = ko.observable(false);
        self.IsEnabledCreateInput = ko.observable(true);
        self.Model = {
            PictureId: ko.observable(null),
            Filter: {
                Id: ko.observable(null),
                Name: ko.observable(''),
                NameOther: ko.observable('')
            }
        };
        self.Model.ListColl = new listCollectionModel({ root: self, type: 1 });
        self.Model.ListCollOther = new listCollectionModel({ root: self, type: 2 });

        function callFunction(fnc, arg) {
            if (typeof fnc == 'function')
                fnc(arg);
        }

        function listCollection(arg, fnc) {
            var query = arg.type == 2 ? self.Model.Filter.NameOther() : self.Model.Filter.Name();
            var count = arg.type == 2 ? self.Model.ListCollOther.Count() : self.Model.ListColl.Count();
            var lastId = arg.type == 2 ? self.Model.ListCollOther.LastId() : self.Model.ListColl.LastId();
            $.get('/PhotoCollection/ListCollection?checkPictureId=' + self.Model.PictureId() + '&query=' + query + '&type=' + arg.type + '&lastId=' + lastId + '&count=' + count, function (res) {
                if (res)
                    callFunction(fnc, res);

            }).error(function (res) {
                console.log(res);
            });
        }






        this.bindListCollection = function (arg, fnc) {

            arg = arg ? arg : { type: 1 };

            self.IsLoading(true);
            if (arg.reset == true)
                if (arg.type === 2) {
                    self.Model.ListCollOther.Reset();
                } else {
                    self.Model.ListColl.Reset();
                }
            listCollection(arg, function (res) {
                if (arg.type === 2) {
                    self.Model.ListCollOther.BindData(res);
                } else {
                    self.Model.ListColl.BindData(res);
                }

                self.IsLoading(false);
                setTimeout(function () {
                    bPopup.reposition(200);
                }, 200);
                callFunction(fnc);
            });
        }

        self.ItemsAfterRender = function () {

        };
        self.fnFilter = function (type) {

            if (type == 2)
                self.Model.Filter.NameOther($('#ppSavePhoto #pc-other-collections .dlgcf-title input[type="text"]').val());
            else
                self.Model.Filter.Name($('#ppSavePhoto #pc-my-collections .dlgcf-title input[type="text"]').val());

            if (self.fnFilter._timeout)
                clearTimeout(self.fnFilter._timeout);
            self.fnFilter._timeout = setTimeout(function () {
                self.bindListCollection({ type: type, reset: true });
            }, 500);

            return true;
        };
        self.fnCreateCollection = function () {
            if (!window.popupEditPhotoCollection) return;
            self.Close();
            window.popupEditPhotoCollection.Show({ Name: '', Description: '', IsPublic: true, IsContribute: true }, function (res) {

                self.IsLoading(true);

                res.PictureId = self.Model.PictureId();

                $.post('/PhotoCollection/CreateCollection', res, function (res1) {
                    if (res1 && res1.data) {
                        window.popupEditPhotoCollection.Close();
                    }
                    else if (res1.error) {
                        if (res1.error.code == 2) {
                            alert('Tên bộ sưu tập đã tồn tại');
                        }
                        self.IsLoading(false);
                    }
                    else {
                        alert('Có lỗi xảy ra trong quá trình xử lý.\r\nBạn vui lòng thử lại sau.');
                        self.IsLoading(false);
                    }

                }).error(function (res1) {
                    console.log(res1);
                    alert('Có lỗi xảy ra trong quá trình xử lý.\r\nBạn vui lòng thử lại sau.');
                    self.IsLoading(false);
                });
            }, function () {
                self.Show({ PictureId: self.Model.PictureId() }, fnCallBack);
            });
        };
        self.fnSavePhotoToggle = function (type, collection) {


            self.Model.Filter.Id(collection.Id);
            var iconState = collection.IconState(true);


            if (type == 2) {
                if (collection.IsChecked() == true) {
                    return;
                }
                self.IsLoading(true);
                $('#ppSavePhoto ul li [item-id="' + collection.Id + '"] i').attr('class', iconState);
                $.post('/PhotoCollection/AddPhotoContributeToggle', { pictureId: self.Model.PictureId(), collectionId: self.Model.Filter.Id() }, function (data) {
                    console.log(data);

                    if (data.success == true) {
                        self.Model.ListCollOther.SetCheckedItem(collection.Id, data.IsChecked);
                    } else {
                        console.log(data);
                    }
                    self.IsLoading(false);
                });

            } else {
                self.IsLoading(true);
                $('#ppSavePhoto ul li [item-id="' + collection.Id + '"] i').attr('class', iconState);
                $.post('/PhotoCollection/SavePhotoToggle', {
                    CollectionId: self.Model.Filter.Id(),
                    PictureId: self.Model.PictureId()
                }, function (res) {

                    if (res) {
                        self.Model.ListColl.SetCheckedItem(collection.Id, res.IsChecked);
                    }
                    self.IsLoading(false);
                }).error(function (res) {
                    console.log(res);
                    alert('Có lỗi xảy ra trong quá trình xử lý.\r\nBạn vui lòng thử lại sau.');
                    self.IsLoading(false);
                });
            }

        };
        self.Close = function () {
            bPopup.close();
        };
        self.Show = function (arg, callback) {
            fnCallBack = callback;
            self.Model.PictureId(arg.PictureId);
            self.Model.Filter.Name('');
            self._tabUi.Reset();

            if (arg.Reset == true) {
                self.Model.ListCollOther.Reset();
                self.Model.ListColl.Reset();
            }

            bPopup = $(selector).bPopup({
                zIndex: 10000,
                closeClass: 'dlgc-btn-close',
                modalClose: true,
                followSpeed: 0,
                onOpen: function () {
                    $('#ppSavePhoto .pc-nav-add-photo>ul>li a[href="#pc-my-collections"]').parent().click();
                    // self.bindListCollection({ type: 1, reset: true });

                },
                onClose: function () {
                }
            });
        }

        self.fnOK = function () {
            callFunction(fnCallBack, { Name: self.Model.Name(), Description: self.Model.Description() });
        };
        self.fnCancel = function () {
            self.Close();
        };

        self._tabUi = $('#ppSavePhoto .pc-nav-add-photo').custabs({
            onChanged: function (sender) {
                var target = $(sender).find('a').attr('href');
                if (target == '#pc-my-collections') {
                    self.bindListCollection({ type: 1, reset: true });
                } else {
                    self.bindListCollection({ type: 2, reset: true });
                }
                //console.log(target);
            }
        });

        function _autoLoadMoreOwner() {
            if ($('#pc-my-collections:visible').length < 1 || self.Model.ListColl.TotalRemaining() < 1) return;
            var sTop = $('.pc-list-collection:visible').scrollTop();
            var tHeight = $('#pc-my-collections').height();
            var tOffset = $('#pc-my-collections').offset();
            if (sTop + tOffset.top > tHeight) {
                self.Model.ListColl.fnLoadMore();
            }
        }
        function _autoLoadMoreSaved() {
            if ($('#pc-other-collections:visible').length < 1 || self.Model.ListCollOther.TotalRemain() < 1) return;
            var sTop = $('.pc-list-collection:visible').scrollTop();
            var tHeight = $('#pc-other-collections').height();
            var tOffset = $('#pc-other-collections').offset();
            if (sTop + tOffset.top > tHeight) {
                self.Model.ListCollOther.fnLoadMore();
            }
        }
        $('.pc-list-collection').scroll(function () {
            if (window._timeOut)
                clearTimeout(window._timeOut);
            window._timeOut = setTimeout(function () {
                _autoLoadMoreOwner();
                _autoLoadMoreSaved();
            }, 100);
        });
    };

    $(function () {
        window.popupSavePhoto = new PopupSavePhotoModel(window.dataLanguagesPc);

        ko.applyBindings(popupSavePhoto, document.getElementById('ppSavePhoto'));
    });
				</script>
				<style>



				</style>
				<div id="ppSavePhoto" class="fd-popup pc-popup pp-save-photo">
					<div class="fd-popup-frame">
						<div class="dlgc-btn-close"></div>
						<div class="dlgc-title">
							Lưu ảnh vào bộ sưu tập
							<span class="fa fa-photo" style="float:right;margin-top:15px;"></span>
						</div>
						<div class="dlgc-content-frame">

							<div class="dlgcf-content">
								<div class="pc-nav-add-photo">
									<ul>
										<li>
											<a href="#pc-my-collections">
												Bộ sưu tập
											</a>
										</li>
										<li>
											<a href="#pc-other-collections">
												Bộ sưu tập khác
											</a>
										</li>
									</ul>
									<div id="pc-my-collections" class="pc-nav-content" style="display: none;">
										<div class="dlgcf-title">
											<input type="text" data-bind="event: { keyup: fnFilter.bind(null,1) },value: Model.CollectionName,enable:IsEnabledCreateInput" placeholder="Tìm kiếm theo tên bộ sưu tập" />
											<span class="fa fa-search" style="position: absolute; left: 15px; top: 11px; color: #999;"></span>
										</div>
										<ul class="pc-list-collection pc-nav-content-scroll"
											data-bind="foreach:{data:Model.ListColl.Items , afterRender: ItemsAfterRender}">
											<li>
												<div
													data-bind="click:$root.fnSavePhotoToggle.bind($data,1), attr:{'item-id':Id,class:IsChecked()==true?'pc-checked':''}">
													<i data-bind="attr:{class:IconState()}" class="fa fa-circle"></i>
													<span class="pc-list-item-name" data-bind="html:Name"></span>
													<span class="pc-list-item-summary">
                                        <!-- ko text:TotalItems()-->
                                        <!-- /ko -->
                                        Hình ảnh
                                    </span>
												</div>
												<a class="custom-list-link" data-bind="attr:{href:Url}" target="_blank"
													href="javascript:void(0)">
												</a>
											</li>
										</ul>
										<div data-bind="visible:IsLoading" class="pc-nav-content-loading"></div>

									</div>
									<div id="pc-other-collections" class="pc-nav-content" style="display: none;">
										<div class="dlgcf-title">
											<input type="text" data-bind=" event: { keyup: fnFilter.bind(null,2) },value: Model.CollectionName,enable:IsEnabledCreateInput" placeholder="Tìm kiếm theo tên bộ sưu tập" />
											<span class="fa fa-search" style="position: absolute; left: 15px; top: 11px; color: #999;"></span>
										</div>
										<ul class="pc-list-collection pc-nav-content-scroll"
											data-bind="foreach:{data: Model.ListCollOther.Items , afterRender: ItemsAfterRender}">
											<li>
												<div
													data-bind="click:$root.fnSavePhotoToggle.bind($data,2), attr:{'item-id':Id,class:IsChecked()==true?'pc-checked':''}">
													<i data-bind="attr:{class:IconState()}" class="fa fa-circle"></i>
													<span class="pc-list-item-name" data-bind="html:Name"></span>
													<span class="pc-list-item-summary">
                                        <!-- ko text:TotalItems()-->
                                        <!-- /ko -->
                                        Hình ảnh
                                    </span>
												</div>
												<a class="custom-list-link" data-bind="attr:{href:Url}" target="_blank"
													href="javascript:void(0)">
												</a>
											</li>
										</ul>
										<div data-bind="visible:IsLoading" class="pc-nav-content-loading"></div>

									</div>
								</div>

							</div>
							<div class="dlgcf-buttons clearfix">
								<button data-bind="click:fnCreateCollection" class="dlgc-btn btn-ok">
                    + Tạo mới bộ sưu tập
                </button>

							</div>
						</div>
					</div>
				</div>
				<script>
					window.dataLanguagesPc = {
        BtnCollectionSaved: 'Đã lưu bộ sưu tập',
        BtnCollectionSave: 'Lưu bộ sưu tập',
        BtnShare: 'Chia sẻ',
        BtnLike: 'Thích',
        BtnUnLike: 'Bỏ thích',
        UpdatedOn: 'Cập nhật ngày',
        Views: 'Lượt xem',
        Photos: 'Hình ảnh',
        BtnViewMoreCollection: 'Xem thêm bộ sưu tập',
        BtnViewMorePhoto: 'Xem thêm hình ảnh',
        DlgPhotoTitleSave: 'Lưu ảnh vào bộ sưu tập',
        InputCollectionName: 'Tên bộ sưu tập',
        Description: 'Mô tả bộ sưu tập',
        BtnCollectionCreate: 'Tạo mới bộ sưu tập',
        BtnCreate: 'Tạo',
        BtnCreateNew: 'Tạo mới bộ sưu tập',
        BtnEdit: 'Chỉnh sửa',
        BtnDelete: 'Xoá',
        BtnPublic: 'Công khai (Public)',
        InputCollectionNameNew: 'Nhập tên bộ sưu tập mới',
        DlgCollectionTitleEdit: 'Chỉnh sửa bộ sưu tập',
        BtnCancel: 'Huỷ',
        BtnSave: 'Lưu',
        Saved: 'Lưu lại',
        Like: 'Thích',
        DlgCollectionTitleShare: 'Chia sẻ bộ sưu tập hình ảnh',
        DlgCollectionChooseMethodShare: 'Vui lòng chọn hình thức chia sẻ',
        MsgConfirmDeletePhoto: 'Bạn có chắc muốn xoá hình này?',
        MsgConfirmDeleteCollection: 'Bạn có chắc muốn xoá bộ sưu tập này?',
        MsgCollectionNameExist: 'Tên bộ sưu tập đã tồn tại',
        MsgAddPhotoSelectRequired: 'Vui lòng chọn hình ảnh của bạn để thêm vào bộ sưu tập này!',
        MsgActionFailure: 'Có lỗi xảy ra trong quá trình xử lý.\r\nBạn vui lòng thử lại sau.',
        FilterByName: 'Tìm kiếm theo tên bộ sưu tập'
    };
				</script>
				<script>
					var PopupEditCollectionModel = function (language) {
        var self = this;
        var callBack = null;
        var fnOnClose = null;
        var bPopup = null;
        self.lang = language;
        var selector = '#ppEditCollection';

        self.Model = {
            Name: ko.observable(''),
            Description: ko.observable(''),
            IsPublic: ko.observable('true'),
            IsContribute: ko.observable(true)
        };

        function callFunction(fnc, arg) {
            if (typeof fnc == 'function')
                fnc(arg);
        }

        self.Close = function () {
            bPopup.close();
            if (typeof fnOnClose == "function")
                fnOnClose();
        };
        self.Show = function (arg, callback, onClose) {
            callBack = callback;
            fnOnClose = onClose;
            if (arg) {
                self.Model.Name(arg.Name);
                self.Model.Description(arg.Description);
                self.Model.IsPublic(arg.IsPublic + '');
                self.Model.IsContribute(arg.IsContribute);
            } else {
                self.Model.Name('');
                self.Model.Description('');
                self.Model.IsPublic('true');
                self.Model.IsContribute(true);
            }


            bPopup = $(selector).bPopup({
                zIndex: 10001,
                closeClass: 'dlgc-btn-close',
                modalClose: false,
                followSpeed: 0,
                onOpen: function () {
                    // callFunction(callBack);
                }
            });
        }

        self.fnOK = function () {
            var name = self.Model.Name();
            if (name == null || name == '') {
                alert('Vui lòng nhập tên bộ sưu tập!');
                return;
            }
            callFunction(callBack, {
                Name: self.Model.Name(),
                Description: self.Model.Description(),
                IsPublic: self.Model.IsPublic() == 'true' ? true : false,
                IsContribute: self.Model.IsContribute()
            });
        };
        self.fnCancel = function () {
            self.Close();
        };

        $('#ppEditCollection input[name="pc-setting-is-public"]').on('change', function () {
            if ($('#pc_ckb_isPublic').is(':checked'))
                self.Model.IsContribute(true);
        });
    };

    $(function () {
        window.popupEditPhotoCollection = new PopupEditCollectionModel(window.dataLanguagesPc);

        ko.applyBindings(popupEditPhotoCollection, document.getElementById('ppEditCollection'));
    });
				</script>

				<div id="ppEditCollection" class="fd-popup pc-popup">
					<div class="fd-popup-frame">
						<div class="dlgc-btn-close" data-bind="click:fnCancel"></div>
						<div class="dlgc-title">
							<span data-bind="text:lang.DlgCollectionTitleEdit"></span>
							<span style="float:right;margin-top:15px;" class="fa fa-photo"></span>
						</div>
						<div class="dlgc-content-frame">

							<div class="dlgcf-content">
								<div>
									<input style="padding-left: 15px;" type="text" data-bind="value: Model.Name,attr:{placeholder:lang.InputCollectionName}" placeholder="Tên bộ sưu tập" />
                </div>
									<div style="margin-top:-1px;">
										<textarea rows="6" style="padding-left: 15px;" placeholder="mô tả bộ sưu tập" data-bind="value: Model.Description,attr:{placeholder:lang.Description}"></textarea>
									</div>
									<div style="padding:5px 15px 20px 15px;">
										<div
											style="color: #888; padding: 0 0 5px 0; text-transform: uppercase; font-size: 11px;">
											Cấu hình bộ sưu tập
										</div>
										<ul class="dlcf-btns-radio">
											<li>
												<input data-bind="checked:Model.IsPublic" type="radio" value="false" id="pc_ckb_isPrivate" name="pc-setting-is-public" />
												<label for="pc_ckb_isPrivate">Chỉ mình tôi (Private)</label>
											</li>
											<li>
												<input data-bind="checked:Model.IsPublic" type="radio" value="true" id="pc_ckb_isPublic" name="pc-setting-is-public" />
												<label for="pc_ckb_isPublic">Công khai (Public)</label>
												<ul class="fd-p-checkbox" data-bind="visible:Model.IsPublic()=='true'">
													<li>
														<input data-bind="checked:Model.IsContribute" type="checkbox" id="ckb-ppeditc-ispublic" />
														<label for="ckb-ppeditc-ispublic">Cho phép thành viên khác gợi ý thêm hình ảnh</label>
													</li>
												</ul>
											</li>
										</ul>


									</div>
								</div>
								<div class="dlgcf-buttons clearfix">
									<button data-bind="click:fnOK,text:lang.BtnSave" class="dlgc-btn btn-ok">Lưu</button>

								</div>
							</div>
						</div>
					</div>
					<script>
						var PopupEditListModel = function (language) {
        var self = this;
        var fncallBack = null;
        var fnOnClose = null;
        var bPopup = null;
        self.lang = language;
        var selector = '#ppEditList';

        self.Model = {
            Id: ko.observable(null),
            Title: ko.observable(''),
            Description: ko.observable(''),
            IsPublic: ko.observable('true'),
            IsContribute: ko.observable('true'),
            RestaurantId: ko.observable(null)
        };

        function callFunction(fnc, arg) {
            if (typeof fnc == 'function')
                fnc(arg);
        }

        function fnReset() {
            self.Model.Title('');
            self.Model.Description('');
            self.Model.IsPublic('true');
            self.Model.IsContribute('true');
            
            fnUpdateUi();
        }

        function fnGetData(fnc) {
            var t = new Date().getTime();
            var listId = self.Model.Id()*1;
            if (!(listId > 0)) {
                //callFunction(fnc);
                return;
            }
            $.get('/__get/List/GetList?listId=' + listId
                + '&t=' + t, function (res) {

                    if (!res) {
                        alert(self.lang.MsgActionFailure);
                        return;
                    }
                    if (res.error) {
                        if (res.error.code == 3) {
                            alert('Tên bộ sưu tập đã tồn tại');
                            return;
                        }

                        alert(self.lang.MsgActionFailure);
                        return;
                    }

                    callFunction(fnc, res);

                }).error(function (res) {
                    alert(self.lang.MsgActionFailure);
                    console.log(res);
                });
        }

        function fnSaveData(data, fnc) {
            if (data.Description == null)
                data.Description = '';
            data.Title = encodeURI(data.Title);
            data.Description = encodeURI(data.Description);
            $.post('/__post/List/SaveList', data, function (res) {

                if (!res) {
                    alert(self.lang.MsgActionFailure);
                    return;
                }
                if (res.error) {
                    if (res.error.msg)
                        alert(res.error.msg);
                    else
                        alert(self.lang.MsgActionFailure);
                    return;
                }

                callFunction(fnc, res);

            }).error(function (res) {
                alert(self.lang.MsgActionFailure);
                console.log(res);
            });
        }

        function fnShow() {

            fnGetData(function (res) {
                self.Model.Title(res.Title);
                self.Model.Description(res.Description);
                self.Model.IsPublic(res.IsPublic + '');
                self.Model.IsContribute(res.IsContribute);
                fnUpdateUi();
            });
        }


        self.Close = function () {
            bPopup.close();
            if (typeof fnOnClose == "function")
                fnOnClose();
        };
        self.IsEdit = ko.computed(function () {
            return self.Model.Id() > 0;
        });

        self.Show = function (arg, callback, onClose) {
            fncallBack = callback;
            fnOnClose = onClose;
        
           
           
            fnReset();
            self.Model.Id(arg.Id);
            self.Model.RestaurantId(arg.RestaurantId);


            bPopup = $(selector).bPopup({
                zIndex: 10001,
                closeClass: 'dlgc-btn-close',
                modalClose: false,
                onOpen: function () {
                    fnShow();
                }

            });
        }

        self.fnOK = function () {
            var name = self.Model.Title();
            if (name == null || name == '') {
                alert('Vui lòng nhập tên bộ sưu tập!');
                return;
            }
            fnSaveData({
                Id: self.Model.Id(),
                Title: self.Model.Title(),
                Description: self.Model.Description(),
                IsPublic: self.Model.IsPublic() == 'true' ? true : false,
                IsContribute: self.Model.IsContribute(),
                RestaurantId: self.Model.RestaurantId()
            },
                function (res) {
                    callFunction(fncallBack, res);
                });
        };
        self.fnCancel = function () {
            self.Close();
        };

        function fnUpdateUi() {
            if ($('#lc_ckb_isPublic').is(':checked')) {
                $('#ppEditList .fd-p-checkbox').slideDown();
                self.Model.IsPublic('true');
            } else {
                //$('#ppEditList .fd-p-checkbox').slideUp();
                self.Model.IsPublic('false');
            }
        }
        $('#ppEditList input[name="lc-setting-is-public"]').on('change', function () {
            fnUpdateUi();
        });
    };

    $(function () {
        window.popupEditList = new PopupEditListModel(window.dataLanguagesPc);

        ko.applyBindings(popupEditList, document.getElementById('ppEditList'));
    });
					</script>

					<div id="ppEditList" class="fd-popup pc-popup">
						<div class="fd-popup-frame">
							<div class="dlgc-btn-close" data-bind="click:fnCancel"></div>
							<div class="dlgc-title">
								<!-- ko if: IsEdit -->
								<span>Cập nhật bộ sưu tập của bạn</span>
								<!-- /ko -->
								<!-- ko ifnot: IsEdit -->
								<span>Tạo bộ sưu tập mới</span>
								<!-- /ko -->
								<span style="float: right; margin-top: 15px;" class="fa fa-map-marker"></span>
							</div>
							<div class="dlgc-content-frame">

								<div class="dlgcf-content">
									<div>
										<input style="padding-left: 15px;" type="text" data-bind="value: Model.Title,attr:{placeholder:lang.InputCollectionName}" placeholder="Tên bộ sưu tập" />
                </div>
										<div style="margin-top:-1px;">
											<textarea rows="6" style="padding-left: 15px;" placeholder="mô tả bộ sưu tập" data-bind="value: Model.Description,attr:{placeholder:lang.Description}"></textarea>
										</div>
										<div style="padding:5px 15px 0 15px;">
											<div
												style="color: #888; padding: 0 0 5px 0; text-transform: uppercase; font-size: 11px;">
												Cấu hình bộ sưu tập
											</div>
											<ul class="dlcf-btns-radio">
												<li>
													<input data-bind="checked:Model.IsPublic" type="radio" value="false" id="lc_ckb_isPrivate" name="lc-setting-is-public" />
													<label for="lc_ckb_isPrivate">Chỉ mình tôi (Private)</label>
												</li>
												<li>
													<input data-bind="checked:Model.IsPublic" type="radio" value="true" id="lc_ckb_isPublic" name="lc-setting-is-public" />
													<label for="lc_ckb_isPublic">Công khai (Public)</label>
													<ul class="fd-p-checkbox">
														<li>
															<input data-bind="checked:Model.IsContribute" type="checkbox" id="ckb-ppeditl-ispublic" checked="checked" />
															<label for="ckb-ppeditl-ispublic">Cho phép thành viên khác gợi ý thêm địa điểm</label>
														</li>
													</ul>
												</li>
											</ul>
										</div>
									</div>
									<div class="dlgcf-buttons clearfix">
										<button data-bind="click:fnOK,text:lang.BtnSave" class="dlgc-btn btn-ok">Cập nhật bộ sưu tập</button>
									</div>
								</div>
							</div>
						</div>

						<div id="popupContaner">
							<div id="restaurant-reviews-popup" style="height: 500px; display: none;"></div>
							<div id="foodyBoxContainer"></div>
							<div id="facebookFriendsPopupContainer"></div>
							<div id="user-like-popup"></div>
							<div id="foody-login-box-cotaner"></div>
							<div id="p-micro-ecard" style="display:none;"></div>
							<div id="p-micro-bank-card" style="display:none;"></div>
						</div>






						<div class="fd-back-top" style="display:none;">
							<ul>
								<li id="btn-back-top">
									<a href="javascript:void(0)">
										<i class="fa fa-angle-up"></i>
										<label>Về đầu trang</label>
									</a>
								</li>
								<li>
									<a href="https://itunes.apple.com/app/id570435154" target="_blank"
										onclick="ga('ads.send', 'event', 'Button Download', 'Click', 'iOS');">
										<i class="fa fa-apple"></i>
										<label>Tải ứng dụng</label>
									</a>
								</li>
								<li>
									<a href="https://play.google.com/store/apps/details?id=com.foody.vn.activity"
										target="_blank"
										onclick="ga('ads.send', 'event', 'Button Download', 'Click', 'Android');">
										<i class="fa fa-android"></i>
										<label>Tải ứng dụng</label>
									</a>
								</li>
							</ul>
						</div>



						<script src="/scripts/public.search.min.js?6b6fe8" type="text/javascript"></script>
						<script>
							//<!-- Cài đặt mã Remarketing -->
        var dataLayer = window.dataLayer || [];
        dataLayer.push({
            'event': 'dynamic_remarketing',
            'dynx_itemid':'',
            'dynx_pagetype' : 'searchresults',
            'dynx_totalvalue' : 0
        });
        $(function () {
            $('#pkeywords').val(model.keyword());
            //$('#directory-search-resulttab').fixedAds({
            //    top: 50
            //});
            //$('#directory-banner-container').fixedAds({
            //    top: 50,
            //    //edgeSelector: ".footer-down-app-wrap"
            //});
        })
						</script>





</body>

</html>"""



c = r"""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:fb="http://www.facebook.com/2008/fbml">

<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>Địa điểm Quán ăn phong cách Món Việt tại Quận Cầu Giấy, Hà Nội | Foody.vn</title>

	<meta http-equiv="Content-type" content="text/html;charset=UTF-8" />
	<meta name="description"
		content="Danh sách > 2514 địa điểm Quán ăn phong cách Món Việt tại Quận Cầu Giấy, Hà Nội. Foody.vn là website #1 tại VN về tìm kiếm địa điểm, có hàng ngàn bình luận, hình ảnh" />
	<meta name="keywords"
		content="Foody.vn là nơi chia sẻ và đánh giá địa điểm, với hàng ngàn địa điểm về ẩm thực, giải trí cùng hàng ngàn bình luận. Tham gia để chia sẻ trải nghiệm với cộng đồng" />

	<meta name="apple-itunes-app" content="app-id=1218739449">
	<link rel="manifest" href="/manifest.json">



	<meta name="robots" content="index, follow" />



	<meta name="msvalidate.01" content="9F288B3B53D32225CE6A70FA2DB2BF6D" />

	<link rel="SHORTCUT ICON" href="/favicon.ico" />

	<meta property="og:title" content="Địa điểm Quán ăn phong cách Món Việt tại Quận Cầu Giấy, Hà Nội" />
	<meta property="og:description"
		content="Danh sách > 2514 địa điểm Quán ăn phong cách Món Việt tại Quận Cầu Giấy, Hà Nội. Foody.vn là website #1 tại VN về tìm kiếm địa điểm, có hàng ngàn bình luận, hình ảnh" />
	<meta property="og:type" content="foodyvn:restaurant" />
	<meta property="og:url" content="" />
	<meta property="og:site_name" content="Foody" />
	<meta property="fb:app_id" content="395614663835338" />
	<meta property="og:image" content="" />
	<meta property="og:image:url" content="" />


	<meta property="og:title" content="Địa điểm Quán ăn phong cách Món Việt tại Quận Cầu Giấy, Hà Nội | Foody.vn" />
	<meta property="og:image" content="/style/images/logofoody.jpg" />
	<meta property="fb:app_id" content="395614663835338" />
	<meta property="og:description"
		content="Danh sách > 2514 địa điểm Quán ăn phong cách Món Việt tại Quận Cầu Giấy, Hà Nội. Foody.vn là website #1 tại VN về tìm kiếm địa điểm, có hàng ngàn bình luận, hình ảnh" />
	<meta property="og:type" content="website" />
	<meta property="og:url"
		content="http://www.foody.vn/ha-noi/quan-an-phong-cach-viet-nam-tai-quan-cau-giay?c=quan-an&amp;categorygroup=food&amp;page=400&amp;append=True" />
	<meta property="og:site_name" content="Foody" />



	<link rel="canonical"
		href="https://www.foody.vn/ha-noi/quan-an-phong-cach-viet-nam-tai-quan-cau-giay?cquan-an&categorygroupfood&page400&appendtrue" />





	<link href="/style/css/public.main.new.min.css?6b6fe8" rel="stylesheet" />





	<script type="text/javascript">
		var staticPath = '/';
    var province = 'ha-noi';
    var provinceId = '218';
    var fbAppId = '395614663835338';
    var defaultLatgitude = '21.033333' * 1;
    var defaultLongitude = '105.850000' * 1;
    var logoutUrl='/dang-xuat';
    var globalLanguages = {
        Comment_User_Like_Empty: 'Chưa có thành viên nào',
        Comment_User_DisLike_Empty: 'Chưa có ai không thích'
    }

    var ssoUrl = 'https://id.foody.vn/account/login';
    var defaultUrl = '';
    var ssoEnable = true;
    var ssoDomainAuthorize = ssoUrl + 'Account/SocialAuthLogin?provider=';
    var defualtDomainAuthorize = '/Account/SocialAuthLogin?provider=';
    var CONST_MEDIA_UPLOAD_URL = "https://images.foody.vn/";
    var CountryId = '86';
    var LanguageId = '1';
    var IsIndo = CountryId == '42' ? true : false;
    var CONST_MEDIA_XUSER_TOKEN = '';

    var NowPythonSetting = {
        ApiHost:'https://gappapi.deliverynow.vn/',
        AuthenHost: 'https://gsso.deliverynow.vn/',
        SecrectKey: 'a3f713fe2494ded5c1e609db3fc9e72c59724443e410006ef224c8adcffce0e0'
    }
    var TableNowSetting = {
        Host: 'https://gappapi.tablenow.vn',
        WebHost: 'https://shopeefood.vn',
        WebHostUrl: 'table',
        ConfigUrl: '',
        Version: 1,
        AppType: 2000,
        ClientType: 1,
        ApiVersion: 1,
        ClientLanguage: 'vn'
    }
	</script>

	<script>
		var routeConfig = {};
    routeConfig.defaultCategory = 'dia-diem';
    routeConfig.microsite = {
        reviewPath: 'binh-luan',
        prPath: 'quang-cao',
        qaPath: 'hoi-dap',
        albumPath: 'album-anh',
        menuPath: 'thuc-don',
        checkinPath: 'check-in'
    };
    routeConfig.account = {
        loginUrl: '/dang-nhap',
        logoutUrl: '/dang-xuat?returnUrl=%2F',
        lookedAccount: '/khoa-tai-khoan'
    }
    window.ReviewLanguages = {
        Common_You_Have: 'Bạn có',
        Common_Points: 'điểm',
        Review_You_Lose: 'Bạn bị trừ',
        Redeem_OrderStatus_Pending: 'Chờ duyệt'
    };
    routeConfig.micrositeUrlTemplate = '/_LOCATION_/_URL_REWRITE_';
    routeConfig.micrositeReviewUrlTemplate = '/_LOCATION_/_URL_REWRITE_/binh-luan';
	</script>





	<script src="/scripts/public.resources.min.js?6b6fe8" type="text/javascript"></script>
	<script src="/scripts/public.core.new.min.js?6b6fe8" type="text/javascript"></script>
	<script src="/scripts/public.foody.min.js?6b6fe8" type="text/javascript"></script>
	<script src="/scripts/public.account.update.profile.min.js?6b6fe8" type="text/javascript"></script>
	<script src="/scripts/wishlist/public.foody.wishlist.context.min.js?6b6fe8" type="text/javascript"></script>

	<script src="/scripts/public.angular.min.js?6b6fe8" type="text/javascript"></script>

	<script src="/scripts/public.angular.core.min.js?6b6fe8" type="text/javascript"></script>




	<link href="/style/css/public.place.min.css?6b6fe8" rel="stylesheet" />
	<link href="/style/css/public.search.min.css?6b6fe8" rel="stylesheet" />
	<link href="/style/css/preload.css" rel="stylesheet" />




	<!-- Google Tag Manager -->
	<script>
		(function (w, d, s, l, i) {
            w[l] = w[l] || []; w[l].push({
                'gtm.start':
                    new Date().getTime(), event: 'gtm.js'
            }); var f = d.getElementsByTagName(s)[0],
                j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : ''; j.async = true; j.src =
                    'https://www.googletagmanager.com/gtm.js?id=' + i + dl; f.parentNode.insertBefore(j, f);
        })(window, document, 'script', 'dataLayer', 'GTM-5FMV7KK');
	</script>
	<!-- End Google Tag Manager -->



	<!-- foody 2 -->


	<script>
		(function (i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
            (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date(); a = s.createElement(o),
        m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
    })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-33292184-1', 'auto');
    ga('create', 'UA-33292184-1', { 'name': 'ads' });

    
    ga('send', 'pageview');
    //ga('sr.send', 'pageview');
	</script>



	<!-- Facebook Pixel Code -->
	<script>
		!function (f, b, e, v, n, t, s) {
            if (f.fbq) return; n = f.fbq = function () {
                n.callMethod ?
                n.callMethod.apply(n, arguments) : n.queue.push(arguments)
            }; if (!f._fbq) f._fbq = n;
            n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = []; t = b.createElement(e); t.async = !0;
            t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s)
        }(window,
        document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');

        fbq('init', '869522799763514');
        fbq('track', "PageView");
        fbq('track', "ViewContent");
	</script>
	<noscript>
		<img height="1" width="1" style="display:none"
                 src="https://www.facebook.com/tr?id=869522799763514&ev=PageView&noscript=1" />
        </noscript>
		<!-- End Facebook Pixel Code -->

</head>

<body itemscope itemtype="http://schema.org/WebPage">
	<!-- Google Tag Manager (noscript) -->
	<noscript>
		<iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5FMV7KK" height="0" width="0"
			style="display:none;visibility:hidden"></iframe>
	</noscript>
	<!-- End Google Tag Manager (noscript) -->


	<script type="application/ld+json">
		{
    "@context" : "https://schema.org",
    "@type" : "Website",
    "name" : "Foody",
    "alternateName": "Foody Vietnam",
    "url" : "https://www.foody.vn",
    "sameAs" : [ "https://www.facebook.com/FoodyVietnam","https://twitter.com/foodyvn","https://plus.google.com/+FoodyVn","https://www.instagram.com/foodysaigon"]
    
    }
	</script>
	<div id="fb-root"></div>


	<div id="FoodyApp" ng-app="FoodyApp">



		<header class="header">





			<script>
				$(function () {
            $('.rootcategory-right').width($('.rootcategory-menu').width() - $('.nearby-button').width() - $('.dropdown1').width() - 630);
            

            if ($("#pkeywords").val().length == 0) {
                $('#pkeywords').addClass('watermark');
            } else {
                $('#pkeywords').removeClass('watermark');
            }
            $("#pkeywords").watermark('Địa điểm, món ăn, loại hình...', {
                useNative: true,
                className: 'watermark'
            })
                .focus(function () {
                    if ($(this).val().length == 0)
                        $(this).addClass('watermark');
                    else
                        $(this).removeClass('watermark');
                })
                .keyup(function () {
                    if ($(this).val().length == 0)
                        $(this).addClass('watermark');
                    else
                        $(this).removeClass('watermark');
                })
                .blur(function () {
                    if ($(this).val().length == 0)
                        $(this).addClass('watermark');
                    else
                        $(this).removeClass('watermark');
                });
        })
			</script>
			<div class="container-topbar">
				<div class="topbar">
					<a href="https://www.foody.vn" class="current" rel="home">Khám Phá</a>

					<a href="https://shopeefood.vn?utm_source=FoodyWeb&utm_medium=topbar_link_click&utm_campaign=FoodyRef"
						target="_blank" rel="nofollow">Đặt Giao Hàng</a>
					<a href="https://shopeefood.vn/ha-noi/fresh?utm_source=FoodyWeb&utm_medium=topbar_link_click&utm_campaign=FoodyRef"
						style="position:relative" target="_blank" rel="nofollow">Đi chợ
						<img style="position: absolute;top: 0px;right: -5px;border-radius: 7px;" src="/style/css/strongbow/images/sb-new.gif" /></a>





				</div>
			</div>
			<div class="header-toolbar">
				<div class="foody-wapper">
					<a href="/" class="logo foody-logo" rel="home" alt="foody-logo">
						<img src="/style/images/logo/foody-vn.png" alt="Foody.vn" />
            </a>
						<div class="root-cate" id="head-province" ng-controller="LocationCtrl"
							ng-init="Init({Name:'H&#224; Nội',Id:'218'})" ng-class="{'fl-show':IsShow}">
							<div class="rn-nav-name" ng-click="Show()">
								<span style="white-space: nowrap;overflow: hidden;text-overflow: ellipsis;max-width: 85px;">H&#224; Nội</span>
								<span class="fa fa-sort-desc"></span>
							</div>
							<div id="popupLocation" class="foody-location" ng-class="{'fl-loading':IsLoading}"
								style="display:none;">
								<div class="arrow"></div>
								<ul class="fl-panel">
									<li ng-if="Model.TopCities.length>0 || Model.OtherCities.length>0">
										<div class="flp-title">
											<i class="fa fa-globe"></i>
											Tỉnh thành
										</div>
										<div class="loc-contain">
											<div class="fa fa-search loc-search"></div>
											<input type="text" class="loc-query" placeholder="Tìm tỉnh thành" ng-model="Query" ng-change="FilterLocation(Query)"/>
            </div>
											<ul class="flp-countries" ng-if="Query">
												<li>
													<ul>
														<li ng-repeat="item in Locations">
															<a data-id="{{item.Id}}" href="{{item.Url}}">
																<label>{{item.DisplayName}}</label>
																<span>{{item.RestaurantCount|formatN}}</span>
															</a>
														</li>
													</ul>
												</li>
											</ul>
											<ul class="flp-countries" ng-if="!Query">
												<li ng-if="Model.TopCities.length>0">
													<ul>
														<li ng-repeat="item in Model.TopCities">
															<a data-id="{{item.Id}}" href="{{item.Url}}">
																<label>{{item.DisplayName}}</label>
																<span>{{item.RestaurantCount|formatN}}</span>
															</a>
														</li>
													</ul>
												</li>
												<li ng-if="Model.OtherCities.length>0">
													<label>Tỉnh thành khác</label>
													<ul>
														<li ng-repeat="item in Model.OtherCities">
															<a data-id="{{item.Id}}" href="{{item.Url}}">
																<label>{{item.DisplayName}}</label>
																<span>{{item.RestaurantCount|formatN}}</span>
															</a>
														</li>
													</ul>
												</li>
												<li ng-if="Model.WorldWideCountries.length>0"
													ng-repeat="item in Model.WorldWideCountries">
													<label data-id="{{item.Id}}">{{item.Name}}</label>
													<ul>
														<li ng-repeat="c in item.Cities">
															<a data-id="{{c.Id}}" href="{{c.Url}}">
																<label>{{c.DisplayName}}</label>
																<span>{{c.RestaurantCount|formatN}}</span>
															</a>
														</li>
													</ul>
												</li>
											</ul>
									</li>
								</ul>
								<div class="fl-summary"
									ng-show="Model.TopCities.length>0 || Model.OtherCities.length>0">

									<a href="/ha-noi/o-dau" title="{{Model.FoodyStat.TotalRes|formatN}}">
										<i class="fa fa-map-marker"></i>
										<span>{{Model.FoodyStat.TotalRes|formatNK}}</span>
									</a>

									<a href="/ha-noi/quan-an/binh-luan"
										title="{{Model.FoodyStat.TotalReviews|formatN}}">
										<i class="fa fa-comment"></i>
										<span>{{Model.FoodyStat.TotalReviews|formatNK}}</span>
									</a>

									<a href="/ha-noi/hinh-anh" title="{{Model.FoodyStat.TotalPics|formatN}}">
										<i class="fa fa-camera"></i>
										<span>{{Model.FoodyStat.TotalPics|formatNK}}</span>
									</a>
									<a href="/ha-noi/bo-suu-tap" title="{{Model.FoodyStat.TotalLists|formatN}}">
										<i class="fa fa-bookmark"></i>
										<span>{{Model.FoodyStat.TotalLists|formatNK}}</span>
									</a>
								</div>
							</div>


						</div>
						<div class="root-cate" id="head-navigation">

							<div class="rn-nav-name">
								<span data-value="1">Ăn uống</span> <span class="fa fa-sort-desc"></span>
							</div>

							<script>
								$('#head-navigation').on('click', function () {
                            if ($('#head-navigation .menu-frame-category').length == 0) {
                                $('#head-navigation').load('/common/_TopCategoryGroupMenu?isUseForSearch=true', function () {
                                    $('#head-navigation .menu-frame-category').show();
                                });
                                return;
                            }
                            $('#head-navigation .menu-frame-category').toggle();
                        });
							</script>
						</div>

						<div class="search-bar-top" id="FoodySearchApp" ng-controller="DlgSearchFilterCtrl"
							ng-init="Init({CityId:'218',Url:'/ha-noi/dia-diem'})">
							<form id="searchFormTop" action="/ha-noi/quan-an" method="get">
								<div
									style="float: left;position: relative;border: 1px solid #eee;border-right:none; width: 415px;box-sizing: border-box;">
									<input ng-model="Filter.Keyword" ng-change="LoadCategory()" style="vertical-align: middle" name="q" type="text" id="pkeywords" data-autocomplete-type="keywords" data-autocomplete-url="/__get/AutoComplete/Keywords?provinceId=218" data-autocomplete-minlength="2" />


									<a href="javascript:void(0)" class="ico-nofilter" ng-click="Show()"
										ng-class="{'ico-filter':FilterCount>0}" style="padding: 6px 10px 0 0;">
										<div ng-class="{'fa-sliders':FilterCount==0,'filtercount':FilterCount>0}"
											ng-cloak class="fa">
											<div ng-if="FilterCount>0" class="count">{{FilterCount}}</div>
										</div>
										Bộ lọc
									</a>
									<input type="hidden" name="ss" value="header_search_form" />



									<script type="text/javascript">
										var searchBoxDropdown = new DropDownCategoryHelper3();

    $(function () {
        searchBoxDropdown.Init({
            btnCategory: $("#pkeywords")[0],
            category: $(".search-bar-top .suggestion-box")[0],
            clickBtnToClose: false
        });
        var keywords = $.cookie('fd.sk');
        if (keywords) {
            var buff = keywords.split('#');

            for (var i = 0; i < 2 ; i++) {
                if (buff[i]) {
                    var ele = '<li><a href="/ha-noi/quan-an?q=' + buff[i].replace('<s', '< s').replace('<S', '< S') + '" class="suggestion-box-item"><span style="float:left;padding-right:5px;color:#666" class="fa fa-search"></span>' +
                                                  buff[i].replace('<s', '< s').replace('<S', '< S') + '<span class="fa fa-angle-right" style="font-size: 14px;"></span>' +
                                            '</a></li>'
                    $('.sb-list-items').append($(ele));
                }

            }

        }
        //$("#pkeywords").on("input", function () {
        //    //$(".search-bar-top .suggestion-box").hide();
        //});

    });
									</script>
									<div class="suggestion-box">


										<!-- res ads -->

										<!-- banner -->

										<div
											style="padding: 5px 10px;font-size: 11px; color: #aaa;background: #FCFCFC;border-bottom: #eee 1px solid;">
											Từ khoá đã tìm</div>

										<ul class="sb-list-items">


											<!-- normal -->

										</ul>
									</div>

								</div>
							</form>

							<a class="ico-search" onclick="$('#searchFormTop').submit()">
								<span class="fa fa-search"></span>
							</a>
							<div bind-unsafe-html="Html">

							</div>
						</div>
						<div class="menu-header">

							<ul class="nav-place-menu">
								<li>
									<a href="javascript:void(0)">
										<span class="fa fa-bars"></span>
									</a>

									<div class="menu-frame">
										<div class="arrow"></div>
										<ul class="menu-box" style="display: block">
											<li>
												<a href="/ha-noi/o-dau" title="Ở đ&#226;u">
													<span>Ở đ&#226;u</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi#/delivery" title="Giao h&#224;ng">
													<span>Giao h&#224;ng</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/hinh-anh" title="Ăn g&#236;">
													<span>Ăn g&#236;</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/bo-suu-tap" title="Sưu tập">
													<span>Sưu tập</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/bo-suu-tap-hinh-anh" title="Bộ sưu tập h&#236;nh ảnh">
													<span>Bộ sưu tập h&#236;nh ảnh</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/coupon" title="Coupons">
													<span>Coupons</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/video" title="TV">
													<span>TV</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/binh-luan" title="B&#236;nh luận">
													<span>B&#236;nh luận</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/food/bai-viet" title="Blogs">
													<span>Blogs</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/khuyen-mai" title="Khuyến m&#227;i">
													<span>Khuyến m&#227;i</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/su-kien" title="Miễn ph&#237;">
													<span>Miễn ph&#237;</span>
												</a>

											</li>
											<li>
												<a href="/ha-noi/top-thanh-vien" title="Top th&#224;nh vi&#234;n">
													<span>Top th&#224;nh vi&#234;n</span>
												</a>

											</li>
										</ul>
									</div>
								</li>

							</ul>


						</div>
						<div class="header-apps test">
							<a href="/ung-dung-mobile" target="_blank"><span class="fa fa-mobile"></span>&nbsp;Apps</a>
						</div>
						<div class="nav-place" ng-controller="MenuLoginCtrl">
							<div class="account-manage" id="accountmanager">
								<a class="fd-btn-login-new" ng-click="Login()" ng-class="{'loading':IsLoading}">
									<span>Đăng nhập</span>
								</a>




								<div id="update-profile-popup" style="display: none">
								</div>
								<div id="update-profile-popup-loading" style="display: none">
									Loading...
								</div>
								<div id="loginPopup" style="display: none">
									<div id="loginPopupPH" style="text-align:center; line-height:30px;">
										<img style="display:inline" src="/style/images/icons/ajax-loader.gif">
    </div>
									</div>
									<div id="loginFacebookPopup" style="display: none">Loading...</div>

									<input type="hidden" id="encryptedlogin" />


                </div>
									<div id="NotificationCtrl" style="position: relative; float: left;"
										ng-controller="NotificationCtrl" ng-init="Init('')">
										<div class="" style="float: right;">
											<div class="notificationBox" ng-cloak>
												<div ng-click="Show()"
													ng-class="SummaryTotalUnread()>0?'notification-new-none notification-new-have':'notification-new-none'">
													{{SummaryTotalUnread()}}
												</div>
												<div class="notificationsFlyout" ng-show="IsShow">
													<span class="arrow"></span>
													<div style="display: block">
														<div>
															<div class="notify-header">
																<ul class="tabs">
																	<li ng-class="{'show-news':IsShowNews}">
																		<a style="border-radius: 3px 0px 0px 3px;"
																			href="javascript:void(0)"
																			ng-click="TabClick(1)"
																			ng-class="{'active':ActiveTab==1}">
																			Dịch vụ
																			<span style="color: #fff;background: #cc0000;border-radius: 10px;font-size:11px;padding: 2px 6px;text-align: center;" ng-show="SummaryOrder>0">{{SummaryOrder}}</span>
																		</a>
																	</li>
																	<li ng-class="{'show-news':IsShowNews}">
																		<a style="border-radius: 0px 3px 3px 0px; border-left: #ccc 1px solid;"
																			href="javascript:void(0)"
																			ng-click="TabClick(2)"
																			ng-class="{'active':ActiveTab==2}">
																			Của tôi
																			<span style="color: #fff;background: #cc0000;border-radius: 10px;font-size:11px;padding: 2px 6px;text-align: center;" ng-show="SummarySocial>0">{{SummarySocial}}</span>
																		</a>
																	</li>
																	<li ng-show="IsShowNews"
																		ng-class="{'show-news':IsShowNews}">
																		<a style="border-radius: 0px 3px 3px 0px; border-left: #ccc 1px solid;"
																			href="javascript:void(0)"
																			ng-click="TabClick(3)"
																			ng-class="{'active':ActiveTab==3}">
																			Tin mới
																			<span style="color: #fff;background: #cc0000;border-radius: 10px;font-size:11px;padding: 2px 6px;text-align: center;" ng-show="SummaryNews>0">{{SummaryNews}}</span>
																		</a>
																	</li>
																</ul>
															</div>
															<div class="clear"></div>
															<div class="notifications-box tab-idx-1" id="tab-order"
																ng-show="ActiveTab==1">
																<div ng-show="!IsLoginRequire">
																	<a ng-repeat="item in ListOrder.Items "
																		href="{{item.Url ? item.Url : 'javascript:void(0)' }}">
																		<div class="notification-message-item"
																			ng-class="{'new-notification': Unread}">
																			<div style="float: left; text-align: left;">
																				<div
																					class="notification-message-item-avatar">
																					<img ng-src="{{item.RepresentImg}}" style="border-radius:unset"/>
                                    </div>
																					<div
																						class="notification-message-content">
																						<div
																							ng-bind-html="item.Content">
																						</div>
																						<div>
																							<!-- Tablenow, type 20: cancel -->
																							<div ng-if="item.ObjectType==42 && item.ActionType!=20"
																								class="notification-icon tablenow-icon">
																							</div>
																							<!-- Delivery, type 20: cancel -->
																							<div ng-if="item.ObjectType==44 && item.ActionType!=20"
																								class="notification-icon delivery-icon">
																							</div>
																							<!-- follow -->
																							<span ng-if="item.ActionType==20" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-times-circle" style="color: #cc0000;font-size: 16px;"></span>
																							</span>
																							<span class="notification-posted-time" style="float:left" utime="{{item.DateStamp}}" title="{{item.DateString}}">{{item.DateDisplay}}</span>
																						</div>
																					</div>
																				</div>
																				<div class="clear"></div>
																			</div>
																	</a>
																</div>
																<div class="notification-message-item item-msg"
																	ng-show="ListOrder.Items.length==0 && IsInit && !IsLoginRequire">
																	Chưa có thông báo!
																</div>
																<div class="notification-message-item item-msg"
																	ng-show="IsLoginRequire" ng-click="Login()">
																	<span class="fa fa-lock"></span>
																	Đăng nhập để xem
																</div>
																<div style="text-align: center"
																	class="notification-message-item"
																	ng-show="ListOrder.Total - ListOrder.Items.length>0">
																	<img class="loading" src="/style/images/icons/ajax-loader.gif" ng-show="ListOrder.IsLoading" />
                        Xem thêm
                    </div>
																</div>
																<div class="notifications-box tab-idx-2" id="tab-social"
																	ng-show="ActiveTab==2">
																	<div ng-show="!IsLoginRequire">
																		<a ng-repeat="item in ListSocial.Items"
																			href="{{item.Url ? item.Url : 'javascript:void(0)' }}"
																			target="{{item.Target}}"
																			ng-show="item.Content.length > 0">
																			<div class="notification-message-item"
																				ng-class="{'new-notification': Unread}">
																				<div
																					style="float: left; text-align: left;">
																					<div
																						class="notification-message-item-avatar">
																						<img ng-src="{{item.RepresentImg}}" />
                                    </div>
																						<div
																							class="notification-message-content">
																							<div
																								ng-bind-html="item.Content">
																							</div>
																							<div>
																								<span ng-if="item.ActionType==5" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-user"></span>
																								</span>
																								<span ng-if="item.ActionType==2" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-comment" style="color: #009a59"></span>
																								</span>
																								<span ng-if="item.ActionType==1" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-thumbs-up" style="color: #3b5998"></span>
																								</span>
																								<!-- follow -->
																								<span ng-if="item.ActionType==10" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-bookmark" style="color: #cc0000"></span>
																								</span>
																								<!-- follow -->
																								<!-- follow User-->
																								<span ng-if="item.ActionType==17" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-plus" style="color: #cc0000"></span>
																								</span>
																								<!-- follow -->
																								<!-- update list -->
																								<span ng-if="item.ActionType==12" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-check-circle" style="color: #03ae03"></span>
																								</span>
																								<!-- update list -->
																								<!-- using foody -->
																								<span ng-if="item.ActionType==14" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-facebook-square" style="color: #3b5998"></span>
																								</span>
																								<!-- using foody -->
																								<span ng-if="item.ActionType==15" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-check-circle" style="color: #03ae03"></span>
																								</span>
																								<span ng-if="item.ActionType==18 || item.ActionType==27" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-list" style="color: #ce8b0d"></span>
																								</span>
																								<span ng-if="item.ActionType==33" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-tag" style="color: #1b95e0"></span>
																								</span>
																								<span ng-if="item.ActionType==34" style="float: left; padding-right: 5px;">
                                                <span class="fa fa-tag" style="color: #1b95e0"></span>
																								</span>

																								<span class="notification-posted-time" utime="{{item.DateStamp}}" title="{{item.DateString}}">{{item.DateDisplay}}</span>
																							</div>
																						</div>

																					</div>
																					<div class="clear"></div>
																				</div>
																		</a>
																	</div>

																	<div class="notification-message-item item-msg"
																		ng-show="ListSocial.Items.length==0 && IsInit && !IsLoginRequire">
																		Chưa có thông báo!
																	</div>
																	<div class="notification-message-item item-msg"
																		ng-show="IsLoginRequire" ng-click="Login()">
																		<span class="fa fa-lock"></span>
																		Đăng nhập để xem
																	</div>
																	<div style="text-align: center"
																		class="notification-message-item"
																		ng-show="ListSocial.Total>ListSocial.Items.length">
																		<img class="loading" src="/style/images/icons/ajax-loader.gif" ng-show="IsInit" />
                            Xem thêm
                        </div>
																	</div>
																	<div class="notifications-box tab-idx-3"
																		id="tab-news" ng-show="ActiveTab==3">

																		<a ng-repeat="item in ListNews.Items "
																			href="{{item.Url ? item.Url : 'javascript:void(0)' }}">
																			<div class="notification-message-item"
																				ng-class="{'new-notification': Unread}">
																				<div
																					style="float: left; text-align: left;">
																					<div
																						class="notification-message-item-avatar">
																						<img ng-src="{{item.RepresentImg}}" />
                                    </div>
																						<div
																							class="notification-message-content">
																							<div>
																								<span style="font-weight: bold; color: #333;">{{item.Title}}</span>
																							</div>
																							<div class="notification-message-text"
																								ng-bind-html="item.Message">
																							</div>
																							<div>

																								<span class="notification-posted-time" utime="{{item.DateTimestamp}}" title="{{item.DateString}}">{{item.DateDisplay}}</span>
																							</div>
																						</div>

																					</div>
																					<div class="clear"></div>
																				</div>
																		</a>
																		<div class="notification-message-item item-msg"
																			ng-show="ListNews.Items.length==0 && IsInit && !IsLoginRequire">
																			Chưa có thông báo!
																		</div>
																		<div style="text-align: center"
																			class="notification-message-item"
																			ng-show="ListNews.Total - ListNews.Items.length>0">
																			<img class="loading" src="/style/images/icons/ajax-loader.gif" ng-show="ListNews.IsLoading" />
                        Xem thêm
                    </div>
																		</div>
																		<div class="notification-message-item item-msg"
																			ng-show="!IsInit">
																			<img class="loading" src="/style/images/icons/ajax-loader.gif" />
                    Đang tải
                </div>
																		</div>

																	</div>
																</div>
															</div>


														</div>

													</div>



													<div class="nav-add-buttons">
														<a>+</a>
														<div id="add-buttons">
															<span class="arrow" style="left: 257px;"></span>
															<ul>
																<li
																	style="padding: 8px 15px 6px 15px; border-bottom: #ddd 1px solid;">
																	Bạn có thể</li>

																<li>
																	<a href="javascript:void(0)"
																		ng-click="ActionUrl('/them-dia-diem')">
																		<span class="fa fa-map-marker icons" style="font-size: 26px;"></span>
																		<span class="add-buttons-text">
                                        <span class="text-main">Tạo địa điểm</span><br />
																		<span class="text-desc">Sẽ được duyệt trong vòng 48 tiếng</span>
																		</span>
																	</a>
																</li>
																<li>
																	<a href="javascript:void(0)"
																		class="add-new-reviews">
																		<span class="fa fa-comment icons"></span>
																		<span class="add-buttons-text">
                                        <span class="text-main">Viết bình luận</span><br />
																		<span class="text-desc">Để chia sẻ trải nghiệm cho cộng đồng</span>
																		</span>
																	</a>
																</li>
																<li>
																	<a href="javascript:void(0)" class="add-new-list">
																		<span class="fa fa-bars icons"></span>
																		<span class="add-buttons-text">
                                        <span class="text-main">Tạo bộ sưu tập</span><br />
																		<span class="text-desc">Để lưu trữ địa điểm của bạn</span>
																		</span>

																	</a>
																</li>

																<li>
																	<a href="javascript:void(0)"
																		ng-click="ActionUrl('/gop-y')"
																		class="add-feedback">
																		<span class="fa fa-thumbs-down icons"></span>
																		<span class="add-buttons-text">
                                        <span class="text-main">Góp ý</span><br />
																		<span class="text-desc">Để phục vụ bạn tốt hơn</span>
																		</span>

																	</a>
																</li>
															</ul>
														</div>
													</div>
													<div class="language-dropdown-container">
														<a href="javascript:void(0);" class="language-dropdown-btn">
															<img src="/style/images/icons/lang/vn.png"  style="float:left;"/>
        </a>

															<div class="language-dropdown-list" style="display: none;">

																<a onclick="return changeLanguage('en')" rel="nofollow"
																	href="/__get/common/changelanguage?code=en&amp;returnUrl=http%3A%2F%2Fwww.foody.vn%2Fha-noi%2Fquan-an-phong-cach-viet-nam-tai-quan-cau-giay%3Fc%3Dquan-an%26categorygroup%3Dfood%26page%3D400%26append%3DTrue"
																	title="en">
																	<img src="/style/images/icons/lang/us.png" alt="en" title="en" style="float:left;"/>
																	<span style="float:left; line-height:21px; padding-left:4px;font-size:12px; font-weight:normal; text-transform:uppercase;">en</span>
																</a>
																<div class="clear"></div>
															</div>
													</div>
													<script type="text/javascript">
														function changeLanguage(code) {
            var languageUrl = '/__get/common/changelanguage';
            languageUrl = languageUrl + '?code=' + code + '&returnUrl' + location.href;
            location.href = languageUrl;

            return false;
        }

        var languageDropdown = new DropDownCategoryHelper3();

        $(function () {
            languageDropdown.Init({
                btnCategory: $(".language-dropdown-container .language-dropdown-btn")[0],
                category: $(".language-dropdown-container .language-dropdown-list")[0]
            });
        });
													</script>

												</div>

											</div>
										</div>
		</header>

		<div class="t_clear" style="display: none"></div>



		<script type="text/javascript">
			$(function () {
        // top search form
        $("#searchFormTop input[data-autocomplete-url]").foodyAutocomplete({
            offsetTop: 0,
            offsetLeft: 0,
            offsetWidth: 250,
            minLength: 1,
            showImg: true,
            showAddress: true,
            goDetailsOnSelect: true,
            viewMoreLinkText: 'Xem thêm',
            detailsLinkText: 'Chi tiết',
            allResultLinkText: 'Xem tất cả kết quả',
            closedLinkText: 'Đóng cửa',
            onItemSelected: function (data, event) {
                $('#searchFormTop').submit();
            }
        });
    });
		</script>








		<!-- Start Banner Ads -->



		<script type="text/javascript">
			$(function () {
        if ($("#catfish-banner").find("div").length > 0) {
            if ($.cookie("hideCatfishBanner")=="true") {
                $("#catfish-banner").hide();
            }
            else {
                $("#catfish-banner").css("opacity", "1");
                $("#catfish-banner").css("overflow", "inherit");
            }

            $(".catfish-banner-btn").live("click", function () {
                $("#catfish-banner").hide();
                //var date = new Date();
                //var days = 1;
                //date.setTime(date.getTime() + (days*24*60*60* 1000));
                //$.cookie("hideCatfishBanner", true, { expires: date });
                //$.cookie("hideCatfishBanner", true);
                $.cookie('hideCatfishBanner', true, { path: '/' });
            });
        }
    });
		</script>
		<!-- End Banner Ads -->



		<script src="/scripts/infobox.js"></script>
		<link href="/style/css/video.css" rel="stylesheet" />
		<link href="/style/css/micro.css" rel="stylesheet" />
		<script type="text/javascript">
			if(window.fbq)
        window.fbq('track', 'Search');
		</script>

		<!--Start of Main section -->

		<section class="search-page directory-page" id="directorypage">
			<div id="GalleryPopupApp" ng-controller="GalleryPopupController">
				<div class="fd-popup" id="search-filter-poup">
					<div class="fd-popup-frame">
						<div class="dlgc-btn-close"></div>
						<div class="dlgc-title">
							<span>Bộ lọc nâng cao</span>
						</div>
						<div class="dlgc-content-frame">
							<div class="dlgcf-content">
								<div id="float-filter-container" class="pn-filter"
									data-bind="if: true, style: { display: 'block' }" style="display: none;">
									<div id="float-filter">
										<ul class="filter-tab">
											<li>
												<a class="header-text"
													data-bind="css: { 'act': currentShownFilter() == 'category' }, click: function () { showFilter('category') }"
													href="#filter-category">
													<span class="fa fa-bars" style="padding-right:8px;padding-top:1px;"></span>
													<span>Phân loại</span>
													<span style="float: right;font-weight: normal;font-size: 16px;color: #999;padding-right: 5px;" class="fa fa-angle-right"></span>
												</a>
											</li>
											<li>
												<a class="header-text"
													data-bind="css: { 'act': currentShownFilter() == 'area' }, click: function () { showFilter('area') }"
													href="#filter-area">
													<span class="fa fa-location-arrow" style="padding-right:8px;padding-top:1px;"></span>
													<span>Khu vực</span>
													<span style="float: right;font-weight: normal;font-size: 16px;color: #999;padding-right: 5px;" class="fa fa-angle-right"></span>
												</a>
											</li>
											<li>
												<a class="header-text"
													data-bind="css: { 'act': currentShownFilter() == 'purpose' }, click: function () { showFilter('purpose') }"
													href="#filter-purpose">
													<span class="fa fa-thumbs-up" style="padding-right:8px;padding-top:1px;"></span>
													<span>Mục đích</span>
													<span style="float: right;font-weight: normal;font-size: 16px;color: #999;padding-right: 5px;" class="fa fa-angle-right"></span>
												</a>
											</li>
											<li>
												<a class="header-text"
													data-bind="css: { 'act': currentShownFilter() == 'cuisine' }, click: function () { showFilter('cuisine') }"
													href="#filter-cuisine">
													<span class="fa fa-cutlery" style="padding-right:8px;padding-top:1px;"></span>
													<span>Ẩm thực</span>
													<span style="float: right;font-weight: normal;font-size: 16px;color: #999;padding-right: 5px;" class="fa fa-angle-right"></span>
												</a>
											</li>
											<li>
												<a class="header-text"
													data-bind="css: { 'act': currentShownFilter() == 'property' }, click: function () { showFilter('property') }"
													href="#filter-property">
													<span class="fa fa-check-square" style="padding-right:8px;padding-top:1px;"></span>
													<span>Tiện nghi</span>
													<span style="float: right;font-weight: normal;font-size: 16px;color: #999;padding-right: 5px;" class="fa fa-angle-right"></span>
												</a>
											</li>
											<li>
												<a class="header-text" style="border-bottom:#e6e6e6 1px solid;"
													data-bind="css: { 'act': currentShownFilter() == 'dining' }, click: function () { showFilter('dining') }"
													href="#filter-dining">
													<span class="fa fa-certificate" style="padding-right:8px;padding-top:1px;"></span>
													<span>Thích hợp</span>
													<span style="float: right;font-weight: normal;font-size: 16px;color: #999;padding-right: 5px;" class="fa fa-angle-right"></span>
												</a>
											</li>
										</ul>
										<div data-bind="visible: currentShownFilter() == 'category'"
											class="directory-left-filter-itembox" style="display: none;">
											<div data-bind="visible: $root.isFilterLoading() == false || allCategories().length > 0"
												class="left-filters">
												<div class="list-filters">
													<!-- ko foreach: allCategories() -->
													<div class="list-filters-item"
														data-bind="click: $root.handleClickFilter">
														<div class="left" data-checkbox="checkbox">
															<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span>
															<span data-bind="text: Name"></span>
														</div>
														<div data-bind="text: ResultCount" class="right">
														</div>
													</div>
													<!-- /ko -->
												</div>
											</div>
											<div style="display: none"
												data-bind="visible: $root.isFilterLoading() && allCategories().length == 0">
												<img style="margin: 102px auto; padding: 0;"
                                     src="/style/images/icons/ajax-loader.gif" />
                            </div>

											</div>
											<div data-bind="visible: currentShownFilter() == 'area'"
												class="directory-left-filter-itembox" style="display: none;">
												<div data-bind="visible: $root.isFilterLoading() == false || allAreas().length > 0"
													class="left-filters">
													<div style="float: left; width: 100%;">
														<div class="left-filters-h1">H&#224; Nội</div>
														<input data-bind="value: districtId()" type="hidden" name="districtId" />

														<div class="district-change">
															<select style="border: #e5e5e5 1px solid; padding:7px 2px;margin:0;margin-right:10px; " data-bind="event:{change: $root.handleClickDistrict}, options: $root.districts, optionsText: 'Name', optionsValue: 'Id', value: districtId, optionsCaption: '[chọn quận]    '"></select>
														</div>
														<div data-bind="visible: allAreas().length > $root.maxItemsToShowFilterKeyword"
															class="filter-keyword-filter">
															<input data-bind="value: areaKeywordFilter, valueUpdate: 'keyup'" type="text" placeholder="Nhập từ khóa để tìm khu vực" style="border: #e5e5e5 1px solid; padding: 9px 4px 8px 4px; width: 380px; " />
                                    </div>
														</div>

														<div class="list-filters">
															<!-- ko foreach: areaGroups() -->
															<h3 style="margin: 15px 0 5px 0; clear: both; font-size: 15px;font-weight:bold; float: left; width: 100%; border-bottom: 1px #f6f6f6 solid; padding-bottom: 3px;"
																data-bind="text: name, visible: $root.areaGroups().length > 1 && !IsHidden()">
															</h3>
															<!-- ko foreach: items() -->
															<div class="list-filters-item"
																data-bind="click: $root.handleClickFilter, visible: !IsHidden()">
																<div class="left" data-checkbox="checkbox">
																	<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span>
																	<span data-bind="text: Name"></span>
																	<span class="external-links">
                                                <a rel="nofollow" data-bind="click: $root.gotoAreaLandingPage, attr: { href: getAreaLandingPageUrl(UrlRewriteName) }" href="#" target="_blank"></a>
                                            </span>
																</div>
																<div data-bind="text: ResultCount" class="right">
																</div>
															</div>
															<!-- /ko -->
															<!-- /ko -->
														</div>
													</div>
													<div style="display: none"
														data-bind="visible: $root.isFilterLoading() && allAreas().length == 0">
														<img style="margin: 102px auto; padding: 0;"
                                     src="/style/images/icons/ajax-loader.gif" />
                            </div>

													</div>
													<div data-bind="visible: currentShownFilter() == 'purpose'"
														class="directory-left-filter-itembox" style="display: none;">
														<div data-bind="visible: $root.isFilterLoading() == false || allPurposes().length > 0"
															class="left-filters">
															<div data-bind="visible: allPurposes().length > $root.maxItemsToShowFilterKeyword"
																class="filter-keyword">
																<input data-bind="value: purposeKeywordFilter, valueUpdate: 'keyup'" type="text" placeholder="Nhập từ khóa để tìm mục đích" style="border: #e5e5e5 1px solid; padding:8px 4px; width: 700px;" />
                                </div>
																<div class="list-filters" style="margin-top: 5px;">
																	<!-- ko foreach: allPurposes() -->
																	<div class="list-filters-item"
																		data-bind="click: $root.handleClickFilter, visible: !IsHidden()">
																		<div class="left" data-checkbox="checkbox">
																			<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { test: '', check: Selected() }"></span>
																			<span data-bind="text: Name"></span>
																		</div>
																		<div data-bind="text: ResultCount"
																			class="right">
																		</div>
																	</div>
																	<!-- /ko -->
																</div>
															</div>
															<div style="display: none"
																data-bind="visible: $root.isFilterLoading() && allPurposes().length == 0">
																<img style="margin: 102px auto; padding: 0;"
                                     src="/style/images/icons/ajax-loader.gif" />
                            </div>

															</div>
															<div data-bind="visible: currentShownFilter() == 'cuisine'"
																class="directory-left-filter-itembox"
																style="display: none;">
																<div data-bind="visible: $root.isFilterLoading() == false || allCuisines().length > 0"
																	data-bind="    visible: $root.isFilterLoading() == false || allCuisines().length > 0"
																	class="left-filters">
																	<div data-bind="visible: allCuisines().length > $root.maxItemsToShowFilterKeyword"
																		class="filter-keyword">
																		<input data-bind="value: cuisineKeywordFilter, valueUpdate: 'keyup'" type="text" />
                                </div>
																		<div class="list-filters">
																			<!-- ko foreach: allCuisines -->
																			<div class="list-filters-item"
																				data-bind="click: $root.handleClickCuisine, visible: !IsHidden()">
																				<div class="left"
																					data-checkbox="checkbox">
																					<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span><span data-bind="    text: Name"></span>
																				</div>
																				<div data-bind="text: ResultCount"
																					class="right">
																				</div>
																				<div data-bind="foreach: children(), visible: Selected()"
																					class="filters-item-children"
																					style="margin-left: 18px;">
																					<div style="clear: both;"
																						class="list-filters-item"
																						data-bind="click: $root.handleClickCuisine">
																						<div class="left"
																							data-checkbox="checkbox">
																							<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span><span data-bind="    text: Name"></span>
																						</div>
																					</div>
																					<div data-bind="foreach: children(), visible: Selected()"
																						class="filters-item-children"
																						style="margin-left: 18px">
																						<div class="list-filters-item"
																							data-bind="click: $root.handleClickCuisine">
																							<div class="left"
																								data-checkbox="checkbox">
																								<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span><span data-bind="    text: Name"></span>
																							</div>
																						</div>
																					</div>
																				</div>
																			</div>
																			<!-- /ko -->
																		</div>
																	</div>
																	<div style="display: none"
																		data-bind="visible: $root.isFilterLoading() && allCuisines().length == 0">
																		<img style="margin: 102px auto; padding: 0;"
                                     src="/style/images/icons/ajax-loader.gif" />
                            </div>

																	</div>
																	<div data-bind="visible: currentShownFilter() == 'dish'"
																		class="directory-left-filter-itembox"
																		style="display: none;">
																		<div data-bind="visible: $root.isFilterLoading() == false || allDishCategories().length > 0"
																			class="left-filters">
																			<div data-bind="visible: allDishCategories().length > $root.maxItemsToShowFilterKeyword"
																				class="filter-keyword">
																				<input data-bind="value: dishCategoryKeywordFilter, valueUpdate: 'keyup'" type="text" placeholder="Nhập từ khóa để tìm loại món" style="border: #e5e5e5 1px solid; padding: 8px 4px; width: 700px;" />
                                </div>
																				<div class="list-filters"
																					style="margin-top: 5px;">
																					<!-- ko foreach: allDishCategories -->
																					<div class="list-filters-item"
																						data-bind="click: $root.handleClickDishCategory, visible: !IsHidden()">
																						<div class="left"
																							data-checkbox="checkbox">
																							<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span><span data-bind="    text: Name"></span>
																						</div>
																						<div data-bind="text: ResultCount"
																							class="right">
																						</div>
																						<div data-bind="foreach: children(), visible: Selected()"
																							class="filters-item-children"
																							style="margin-left: 18px">
																							<div style="clear: both;"
																								class="list-filters-item"
																								data-bind="click: $root.handleClickDishCategory">
																								<div class="left"
																									data-checkbox="checkbox">
																									<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span><span data-bind="    text: Name"></span>
																								</div>
																							</div>
																							<div data-bind="foreach: children(), visible: Selected()"
																								class="filters-item-children"
																								style="margin-left: 18px">
																								<div class="list-filters-item"
																									data-bind="click: $root.handleClickDishCategory">
																									<div class="left"
																										data-checkbox="checkbox">
																										<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span><span data-bind="    text: Name"></span>
																									</div>
																								</div>
																							</div>
																						</div>
																					</div>
																					<!-- /ko -->
																				</div>
																			</div>
																			<div style="display: none"
																				data-bind="visible: $root.isFilterLoading() && allDishCategories().length == 0">
																				<img style="margin: 102px auto; padding: 0;"
                                     src="/style/images/icons/ajax-loader.gif" />
                            </div>

																			</div>
																			<div data-bind="visible: currentShownFilter() == 'property'"
																				class="directory-left-filter-itembox"
																				style="display: none;">
																				<div data-bind="visible: $root.isFilterLoading() == false || allProperties().length > 0"
																					class="left-filters">
																					<div data-bind="visible: allProperties().length > $root.maxItemsToShowFilterKeyword"
																						class="filter-keyword">
																						<input data-bind="value: propertyKeywordFilter, valueUpdate: 'keyup'" type="text" placeholder="Nhập từ khóa để tìm tiện nghi" style="border: #e5e5e5 1px solid; padding:8px 4px; width: 700px;" />
                                </div>
																						<div class="list-filters"
																							style="margin-top: 5px;">
																							<!-- ko foreach: allProperties -->
																							<div class="list-filters-item"
																								data-bind="click: $root.handleClickFilter, visible: !IsHidden()">
																								<div class="left"
																									data-checkbox="checkbox">
																									<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { check: Selected() }"></span>
																									<span data-bind="text: Name"></span>
																								</div>
																								<div data-bind="text: ResultCount"
																									class="right">
																								</div>
																							</div>
																							<!-- /ko -->
																						</div>
																					</div>
																					<div style="display: none"
																						data-bind="visible: $root.isFilterLoading() && allProperties().length == 0">
																						<img style="margin: 102px auto; padding: 0;"
                                     src="/style/images/icons/ajax-loader.gif" />
                            </div>

																					</div>
																					<div data-bind="visible: currentShownFilter() == 'dining'"
																						class="directory-left-filter-itembox"
																						style="border-right: #ddd 1px solid; display: none">
																						<div data-bind="visible: $root.isFilterLoading() == false || allDinings().length > 0"
																							class="left-filters">
																							<div data-bind="visible: allDinings().length > $root.maxItemsToShowFilterKeyword"
																								class="filter-keyword">
																								<input data-bind="value: diningKeywordFilter, valueUpdate: 'keyup'" type="text" />
                                </div>
																								<div
																									class="list-filters">
																									<!-- ko foreach: allDinings() -->
																									<div class="list-filters-item"
																										data-bind="click: $root.handleClickFilter, visible: !IsHidden()">
																										<div class="left"
																											data-checkbox="checkbox">
																											<span class="checkbox" data-bind="attr: { 'data-id': Id }, css: { test: '', check: Selected() }"></span>
																											<span data-bind="text: Name"></span>
																										</div>
																										<div data-bind="text: ResultCount"
																											class="right">
																										</div>
																									</div>
																									<!-- /ko -->
																								</div>
																							</div>
																							<div style="display: none"
																								data-bind="visible: $root.isFilterLoading() && allDinings().length == 0">
																								<img style="margin: 102px auto; padding: 0;"
                                     src="/style/images/icons/ajax-loader.gif" />
                            </div>

																							</div>
																						</div>
																					</div>
																				</div>

																			</div>
																		</div>
																	</div>

																	<script>
																		function getAreaLandingPageUrl(url) {
        return '/'+'ha-noi'+'/khu-vuc-' + url;
    }
																	</script>

																	<div class="directory-container">
																		<div class="directory-content">
																			<!--End of search Tool-->
																			<!--Start left filters-->
																			<div class="search-result directory-area">

																				<div class="right"
																					style="clear: both; width: 1170px;">
																					<div class="column-left">
																						<div class="directory-search-resulttab foody-toolbar"
																							id="directory-search-resulttab">
																							<div
																								style="background:none;">
																								<ul>
																									<li>
																										<a data-bind="css:{'current':documentSource()=='Restaurant'}"
																											href="/ha-noi/food/dia-diem?ds=Restaurant"
																											class="current">
																											Địa điểm
																										</a>
																									</li>
																									<li>
																										<a data-bind="visible:listResultCount()>0,css:{'current':documentSource()=='List'}"
																											href="/ha-noi/food/list?ds=List">
																											Bộ sưu tập
																										</a>
																									</li>
																									<li>
																										<a data-bind="visible:pictureResultCount()>0, css:{'current':documentSource()=='Picture'}"
																											href="/ha-noi/food/picture?ds=Picture">
																											Hình ảnh
																										</a>
																									</li>
																									<li>
																										<a data-bind="visible:photoCollectionResultCount()>0, css:{'current':documentSource()=='PhotoCollection'}"
																											href="/ha-noi/food/photo-collection?ds=PhotoCollection">
																											Bộ sưu tập
																											hình
																										</a>
																									</li>
																									<li>
																										<a data-bind="visible:articleResultCount()>0, css:{'current':documentSource()=='Article'}"
																											href="/ha-noi/food/article-list?ds=Article">
																											Blogs
																										</a>
																									</li>

																								</ul>
																								<style>
																									.directory-search-resulttab .foody-banner ul {
																										height: 400px;
																									}

																									.directory-search-resulttab .foody-banner ul li a {
																										padding: 0;
																										display: block;
																										float: left;
																									}
																								</style>




																							</div>

																						</div>
																						<div class="result-side">
																							<!--Filter Keywords-->
																							<!--End of filter keywords-->
																							<div class="directory-places-sorts foody-toolbar"
																								data-bind="visible:documentSource()=='Restaurant'"
																								style="display: none;">
																								<div
																									class="fd-clearbox">
																									<ul>
																										<li>
																											<a href="javascript:void(0)"
																												class="current"
																												data-bind="click:handleClickSortType.bind(this,1),css:{'current':sortType()==1}">Đúng
																												nhất</a>
																										</li>
																										<li>
																											<a href="javascript:void(0)"
																												data-bind="click:handleClickSortType.bind(this,7),css:{'current':sortType()==7}">Gần
																												tôi
																												nhất</a>
																										</li>
																										<li>
																											<a href="javascript:void(0)"
																												data-bind="click:handleClickSortType.bind(this,5),css:{'current':sortType()==5}">Phổ
																												biến</a>
																										</li>
																										<li>
																											<a href="javascript:void(0)"
																												data-bind="click:handleClickSortType.bind(this,2),css:{'current':sortType()==2}">Xem
																												nhiều
																												nhất</a>
																										</li>
																										<li>
																											<a href="javascript:void(0)"
																												data-bind="click:handleClickSortType.bind(this,4),css:{'current':sortType()==4}">Đánh
																												giá tốt
																												nhất</a>
																										</li>
																									</ul>

																								</div>
																								<div data-bind="visible:documentSource()=='Restaurant'"
																									class="view-types"
																									style="margin-left: 935px;position:absolute">
																									<a rel="nofollow"
																										href="https://www.foody.vn/ha-noi/quan-an-phong-cach-viet-nam-tai-quan-cau-giay?c=quan-an&amp;categorygroup=food&amp;page=400&amp;append=true&amp;vt=row"
																										class="row-view active"
																										data-bind="css: { active: viewType() == 'row' }, click: function (data, event) { changeViewType('row', data, event) }, attr: { href: rowViewUrl }"
																										title="List View"></a>

																									<a rel="nofollow"
																										href="https://www.foody.vn/ha-noi/quan-an-phong-cach-viet-nam-tai-quan-cau-giay?c=quan-an&amp;categorygroup=food&amp;page=400&amp;append=true&amp;vt=map"
																										class="map-view "
																										data-bind="css: { active: viewType() == 'map' }, click: function (data, event) { changeViewType('map', data, event) }, attr: { href: mapViewUrl }"
																										title="Map View"></a>
																								</div>
																							</div>
																							<div class="directory-places-sorts foody-toolbar"
																								data-bind="visible:false">
																								<div
																									class="fd-clearbox">
																									<ul>
																										<li>
																											<a
																												href="javascript:void(0)">Đúng
																												nhất</a>
																										</li>
																										<li>
																											<a
																												href="javascript:void(0)">Gần
																												tôi
																												nhất</a>
																										</li>
																										<li>
																											<a
																												href="javascript:void(0)">Phổ
																												biến</a>
																										</li>
																										<li>
																											<a
																												href="javascript:void(0)">Xem
																												nhiều
																												nhất</a>
																										</li>
																										<li>
																											<a
																												href="javascript:void(0)">Đánh
																												giá tốt
																												nhất</a>
																										</li>
																									</ul>
																								</div>

																							</div>
																							<div
																								class="head-result d_resultfilter">
																								<div
																									class="result-counts">
																									<div
																										class="number-msg">
																										<div
																											class="result-status-count">
																											<div
																												style="float: left;">
																												<span data-bind="text: (totalResult()).format('n0')">2.455</span>
																												Kết quả
																											</div>
																											<h1
																												data-bind="html:metaTitle">
																												Địa điểm
																												Qu&#225;n
																												ăn phong
																												c&#225;ch
																												M&#243;n
																												Việt tại
																												Quận Cầu
																												Giấy,
																												H&#224;
																												Nội
																											</h1>

																										</div>
																									</div>


																								</div>
																							</div>
																							<!--Result msg-->

																							<div class="resultnumber"
																								style="overflow:visible">


																								<div data-bind="if: true, style: { display: 'block' }"
																									style="display: none; clear: left;">

																									<!--ko foreach: filtedLists()-->
																									<div data-bind="visible: items().length > 0"
																										style="position: relative"
																										class="selectedkeyword"
																										onmouseover="$(this).children('ul, div.line').show()"
																										onmouseout="$(this).children('ul, div.line').hide()">
																										<div class="keyword"
																											data-bind="text: name">
																										</div>

																										<ul class="filter-list"
																											data-bind="foreach: items">
																											<li>
																												<span data-bind="text: Name" style="color:#333;"></span>
																												<div
																													data-bind="if: $parent.hasChildren">
																													<ul style="padding-left: 10px"
																														data-bind="foreach: children">
																														<li
																															data-bind="visible: Selected">
																															<span data-bind="text: Name" style="color:#333;"></span>
																															<ul style="padding-left: 10px"
																																data-bind="foreach: children">
																																<li data-bind="visible: Selected, text: Name"
																																	style="color:#333;">
																																</li>
																															</ul>
																														</li>
																													</ul>
																												</div>
																											</li>
																										</ul>
																										<div
																											class="closebut">
																											<a href=""
																												data-bind="click: $root.handleRemoveFilterClick">
																												<img src="/style/images/icons/keyword-close-icon.png" width="10" alt="Bỏ lọc" /></a>
																										</div>
																									</div>
																									<!--/ko-->
																								</div>
																								<div
																									data-bind="if: false">
																								</div>

																							</div>
																							<!--End of result msg-->
																							<div data-bind="if: true, style: { display: 'block' }"
																								id="result-box"
																								class="frame-result"
																								style="display: none; margin:inherit;padding-bottom:0">
																								<script>
																									var bannerAdsUrl = '/__get/Common/BannerList?bannerGroupKey=TIMKIEM&width=1000&height=90&count=1'
    var bannerAdsIndex = 0;
																								</script>
																								<div class="row-view"
																									data-bind="if: viewType() == 'row', fadeVisible: viewType() == 'row'">
																									<div
																										class="filter-results">
																										<div
																											data-bind="template: { foreach: searchItems(), name: $root.itemTemplateName() }">

																										</div>
																									</div>

																								</div>

																								<script>
																									function showDeliver(el) {
        $(el).next().toggle();
    }
																								</script>

																								<script
																									id="RestaurantItem"
																									type="text/html">
																									<div data-bind="attr:{'style':!IsAd?'':'background: #fffee2;'}"
																										class="row-item filter-result-item">
																										<div class="ri-avatar result-image">
																											<!-- ko ifnot:SubItems.length>0-->
																											<a data-bind="attr: { href: DetailUrl, title: Name }, click:$root.trackGAClick"
																												target="_blank">
																												<img data-bind="attr: { src: MobilePicturePath, alt: Name }" />
            </a>
																												<!-- /ko -->
																												<!-- ko if:SubItems.length>0-->
																												<a data-bind="attr: { href: BranchUrl, title: BranchName }, click:$root.trackGAClick"
																													target="_blank">
																													<img data-bind="attr: { src: MobilePicturePath, alt: BranchName }" onerror="this.onerror=null;this.src='/Style/images/deli-dish-no-image.png';" />
            </a>
																													<!-- /ko -->

																													<ul class="service-list" data-bind="visible:HasBooking||HasDelivery">
																														<li style="width: 100%" class="ser-type-2"
																															data-bind="visible:HasDelivery,css:{'ser-width-1': HasDelivery && !HasBooking,'ser-width-2': HasDelivery && HasBooking}">
																															<a data-bind="attr:{href:DeliveryUrl}" target="_blank">
																																<span data-bind="visible:MasterCategoryId!=2&&MasterCategoryId!=3">Đặt Giao Hàng</span>
																																<span data-bind="visible:MasterCategoryId==2||MasterCategoryId==3">Đặt Dịch Vụ</span>
																															</a>
																														</li>

																													</ul>
																													<div class="has-video" data-bind="visible:HasVideo">
																														<span class="fa fa-video-camera"></span>
																													</div>
																													<div data-bind="if: Status == 4">
																														<div class="red-label-highlight">
																															<span>Đang đóng cửa</span>
																														</div>
																													</div>
																													<div data-bind="if: Status == 6">
																														<div class="red-label-highlight">
																															<span>Cần xác thực</span>
																														</div>
																													</div>
																										</div>
																										<div class="row-view-right">
																											<div class="result-name">
																												<div class="status">
																													<div data-bind="css:{'highlight-text':AvgRating*1 >= 6,'no-point':AvgRating == '_._'},text: AvgRating, attr: { 'data-tooltip': '#ratingtooltip_' + Id, 'data-restaurantid': Id }, event: { mouseover: $root.handleRatingMouseOver, mouseout: $root.handleRatingMouseOut }"
																														class="point">
																													</div>
																												</div>
																												<div class="resname">
																													<h2>
																														<!-- ko ifnot:SubItems.length>0-->
																														<a data-bind="text: Name, attr: { href: DetailUrl, title: Name }, click:$root.trackGAClick"
																															target="_blank"></a>
																														<!-- /ko -->
																														<!-- ko if:SubItems.length>0-->
																														<a data-bind="text: BranchName, attr: { href: BranchUrl, title: BranchName }, click:$root.trackGAClick"
																															target="_blank"></a>
																														<!-- /ko -->
																													</h2>
																													<div class="result-address">
																														<div class="address">
																															<!-- ko ifnot:SubItems.length>0-->
																															<span data-bind="text: Address"></span>,
																															<a data-bind="attr:{href: DistrictUrl}">
																																<span data-bind="text: District"></span>,
																															</a>
																															<span data-bind="text: City"></span>
																															<!-- /ko -->
																															<!-- ko if:SubItems.length>0-->
																															<span class="branch-address">
                                <span class="branch-btn-ico-blue"></span>
																															<span data-bind="text:SubItems.length + 1"></span>&nbsp;chi nhánh
																															</span>
																															<!-- /ko -->
																														</div>
																														<div class="distants"
																															data-bind="text:Distance!=null?Distance.format('N1') +' KM':''">1km
																														</div>
																													</div>
																												</div>
																											</div>


																											<div data-bind="foreach:Reviews,visible:Reviews.length>0" class="row-view-reviews">
																												<div class="items">
																													<a class="avatar" data-bind="attr:{href:OwnerProfileUrl}">
																														<img data-bind="attr:{src:OwnerAvatar}" />
                    </a>
																														<div class="content block-with-text"
																															data-bind="css: { 'not-align': ShortReview }">
																															<a
																																data-bind="attr:{href:OwnerProfileUrl}"><b style="display:inherit" data-bind="text:OwnerFullName"></b></a>
																															<span data-bind="html:Comment"></span>
																														</div>
																												</div>
																											</div>
																											<div data-bind="visible:Reviews.length==0" class="row-view-reviews">
																												<div class="items">
																													<a class="avatar" href="javascript:void(0);">
																														<div class="not-review-yet"></div>
																													</a>
																													<div class="content not-review-content">
																														<a href="javascript:void(0);" style="width: 100%;display: block;">
																															<b data-bind="text:'Foody'"></b>
																															Chưa có bình luận/đánh giá về địa điểm này!&nbsp;Hãy là người đầu tiên
																															đóng góp bình luận & đánh giá về địa điểm này.
																														</a>

																													</div>
																												</div>
																											</div>
																											<div class="result-stats" style="border-bottom: 1px solid #eee;height:24px;">
																												<div data-bind="if:IsOpening" class="opentime-status">
																													<span class="online"></span>
																													Đang mở cửa
																												</div>
																												<div data-bind="if:!IsOpening" class="opentime-status" style="color: #959595">
																													<span class="offline"></span>
																													Chưa mở cửa
																												</div>

																											</div>
																											<div class="result-stats">
																												<div data-bind="attr: { 'style': !IsAd ? '' : 'background-color: #fffee2;' }"
																													class="row-view-users">
																													<div class="stats">
																														<a href="javascript:void(0)"
																															data-bind="click: function () { $root.LoadReviewPopup(Id); }">
																															<span class="fa fa-comment" style="font-weight: normal;"></span>
																															<span data-bind="text: TotalReview.formatK(1)"></span>
																														</a>
																														<a class="link"
																															data-bind="click: function () { $root.LoadGalleryPopup(Id); }">
																															<span class="fa fa-camera" style="font-weight: normal;padding-left:10px;"></span>
																															<span data-bind="text: PictureCount.formatK(1)"></span>
																														</a>
																														<a href="javascript:void(0)" data-bind="attr: { resid: Id }">
																															<span class="fa fa-bookmark" style="font-weight: normal; padding-left: 10px;"></span>
																															<span data-bind="text: TotalSaves.formatK(1)"></span>
																														</a>

																													</div>
																													<div class="row-view-right2 reviews">
																														<div class="directory-items-shortcut">
																															<div>
																																<a class="tool-custom-list-add otherlist"
																																	data-bind="attr: { 'data-id': Id }, css: { 'added': HasAlredyAddedToList }"
																																	data-core="true" style="float:right">
																																	<span class="fa fa-bookmark"></span>
																																	<!-- ko if:HasAlredyAddedToList-->
																																	<span>Đã lưu</span>
																																	<!-- /ko -->
																																	<!-- ko if:!HasAlredyAddedToList-->
																																	<span>Lưu</span>
																																	<!-- /ko -->
																																</a>
																															</div>
																														</div>
																													</div>


																												</div>
																											</div>

																										</div>





																									</div>
																								</script>


																								<div class="map-view"
																									data-bind="if: viewType()=='map', fadeVisible: viewType()=='map'">
																									<noscript>
																										<h3>
																											Trình duyệt
																											không hỗ trợ
																											javascript!
																										</h3>
																									</noscript>
																									<div id="mapLarge"
																										class="map-container">
																									</div>
																								</div>

																							</div>
																							<div data-bind="if: false"
																								class="frame-result"
																								style="margin-top:0;padding-bottom:0;">


																								<div class="row-view">

																									<div
																										class="filter-results">
																										<div class="filter-result-item"
																											style="padding:0; margin: 5px 0 20px 0;">


																										</div>

																									</div>
																								</div>
																							</div>
																							<div style="width:1025px"
																								data-bind="visible:appending()">
																								<div class="row-view">
																									<div
																										class="filter-results">
																										<div
																											class="pre-row-item filter-result-item">
																											<div
																												class="pre-avatar animated-bg-light">
																											</div>
																											<div
																												class="pre-items-content">
																												<div
																													class="pre-review-points animated-bg">
																												</div>
																												<div
																													class="preload-bar medium animated-bg">
																												</div>
																												<div
																													class="preload-bar long animated-bg">
																												</div>
																											</div>
																											<div
																												class="pre-items-content">
																												<div
																													class="pre-review-points animated-bg">
																												</div>
																												<div
																													class="preload-bar medium animated-bg">
																												</div>
																												<div
																													class="preload-bar long animated-bg">
																												</div>
																											</div>
																										</div>
																										<div
																											class="pre-row-item filter-result-item">
																											<div
																												class="pre-avatar animated-bg-light">
																											</div>
																											<div
																												class="pre-items-content">
																												<div
																													class="pre-review-points animated-bg">
																												</div>
																												<div
																													class="preload-bar medium animated-bg">
																												</div>
																												<div
																													class="preload-bar long animated-bg">
																												</div>
																											</div>
																											<div
																												class="pre-items-content">
																												<div
																													class="pre-review-points animated-bg">
																												</div>
																												<div
																													class="preload-bar medium animated-bg">
																												</div>
																												<div
																													class="preload-bar long animated-bg">
																												</div>
																											</div>
																										</div>
																										<div
																											class="pre-row-item filter-result-item">
																											<div
																												class="pre-avatar animated-bg-light">
																											</div>
																											<div
																												class="pre-items-content">
																												<div
																													class="pre-review-points animated-bg">
																												</div>
																												<div
																													class="preload-bar medium animated-bg">
																												</div>
																												<div
																													class="preload-bar long animated-bg">
																												</div>
																											</div>
																											<div
																												class="pre-items-content">
																												<div
																													class="pre-review-points animated-bg">
																												</div>
																												<div
																													class="preload-bar medium animated-bg">
																												</div>
																												<div
																													class="preload-bar long animated-bg">
																												</div>
																											</div>
																										</div>
																										<div
																											class="pre-row-item filter-result-item">
																											<div
																												class="pre-avatar animated-bg-light">
																											</div>
																											<div
																												class="pre-items-content">
																												<div
																													class="pre-review-points animated-bg">
																												</div>
																												<div
																													class="preload-bar medium animated-bg">
																												</div>
																												<div
																													class="preload-bar long animated-bg">
																												</div>
																											</div>
																											<div
																												class="pre-items-content">
																												<div
																													class="pre-review-points animated-bg">
																												</div>
																												<div
																													class="preload-bar medium animated-bg">
																												</div>
																												<div
																													class="preload-bar long animated-bg">
																												</div>
																											</div>
																										</div>
																										<div
																											class="pre-row-item filter-result-item">
																											<div
																												class="pre-avatar animated-bg-light">
																											</div>
																											<div
																												class="pre-items-content">
																												<div
																													class="pre-review-points animated-bg">
																												</div>
																												<div
																													class="preload-bar medium animated-bg">
																												</div>
																												<div
																													class="preload-bar long animated-bg">
																												</div>
																											</div>
																											<div
																												class="pre-items-content">
																												<div
																													class="pre-review-points animated-bg">
																												</div>
																												<div
																													class="preload-bar medium animated-bg">
																												</div>
																												<div
																													class="preload-bar long animated-bg">
																												</div>
																											</div>
																										</div>
																										<div
																											class="pre-row-item filter-result-item">
																											<div
																												class="pre-avatar animated-bg-light">
																											</div>
																											<div
																												class="pre-items-content">
																												<div
																													class="pre-review-points animated-bg">
																												</div>
																												<div
																													class="preload-bar medium animated-bg">
																												</div>
																												<div
																													class="preload-bar long animated-bg">
																												</div>
																											</div>
																											<div
																												class="pre-items-content">
																												<div
																													class="pre-review-points animated-bg">
																												</div>
																												<div
																													class="preload-bar medium animated-bg">
																												</div>
																												<div
																													class="preload-bar long animated-bg">
																												</div>
																											</div>
																										</div>

																									</div>
																								</div>
																							</div>
																							<div id="scrollLoadingPage"
																								class="btn-load-more full-width"
																								data-bind="click: handleClickLoadMoreResult, visible: hasMorePage() && viewType() != 'map'"
																								style="margin-bottom:10px">
																								<a href="https://www.foody.vn/ha-noi/quan-an-phong-cach-viet-nam-tai-quan-cau-giay?c=quan-an&amp;categorygroup=food&amp;page=401&amp;append=true#page401"
																									rel="next">

																									Xem tiếp kết quả ...
																									<span data-bind="text: searchItems().length+totalSubItems()">
                                                    4,800
                                                </span>/<span data-bind="text: totalResult().format('n0')">2,455</span>&nbsp;(<span data-bind="text: currentPage()">400</span>)
																								</a>
																							</div>
																							<div
																								class="add-more-places">
																								<a
																									href="/them-dia-diem"><span class="fa fa-plus-circle"></span>
																									Không tìm thấy địa
																									điểm? Tạo mới!</a>
																							</div>
																						</div>

																					</div>



																					<!-- End Banner Ads -->
																				</div>
																			</div>
																			<!--End of left filters-->
																			<!--End Ads Footer 728X90-->
																		</div>
																	</div>
																</div>
		</section>
		<div id="advanceSearchPopup" class="advanceSearchbox">
			<div id="advanceSearchDiv">
				<div data-bind="visible: isLoading"
					style="text-align:center;float:left; margin-left:400px; margin-top:220px;">
					<div style="padding-left:5px;"><img src="/style/images/icons/ajax-loader.gif" /></div>
						<div style="padding-top:5px;">Đang tải ...</div>

					</div>
					<!-- ko if: !isLoading() &&  !requestSuccess()-->
					<h3 class="oes">Tôi muốn tìm địa điểm</h3>
					<div style="float: left; width: 550px;margin-top:10px;">
						<div class="row-item-request">
							<span>Mục đích của bạn</span>
							<input data-bind="value: purpose" name="Purpose" type="text" placeholder="Ví dụ: tổ chức tiệc sinh nhật, tiệc cưới" />
							<span data-bind="visible: $.trim(purpose()) == ''" class="error">*</span>
						</div>
						<div class="row-item-request">
							<span>Khu vực</span>
							<input data-bind="value: areas" name="Areas" type="text" placeholder="Ví dụ: Quận 1, 3..." />
							<span data-bind="visible: $.trim(areas()) == ''" class="error">*</span>
						</div>
						<div class="row-item-request">
							<span>Thời gian dự tính</span>
							<input data-bind="value: time" name="Time" type="text" placeholder="Ví dụ: cuối tháng 10" />
							<span data-bind="visible: $.trim(time()) == ''" class="error">*</span>
						</div>
						<div class="row-item-request">
							<span>Số người tham gia</span>
							<input data-bind="value: people" name="People" type="text" placeholder="Ví dụ: 10 người" />
							<span data-bind="visible: $.trim(people()) == ''" class="error">*</span>
						</div>
						<div class="row-item-request">
							<span>Chi phí dự tính/người</span>
							<input data-bind="value: price" name="Price" type="text" placeholder="Ví dụ: 200 ngàn/người" />
							<span data-bind="visible: $.trim(price()) == ''" class="error">*</span>
						</div>
						<div class="row-item-request">
							<span>Yêu cầu khác</span>
							<textarea data-bind="value: more" name="More" rows="5" placeholder="Ví dụ: yêu cầu về không gian, loại món ăn, phong cách quán..."></textarea>
						</div>
						<div class="row-item-request">
							<span>Điện thoại của bạn</span>
							<input data-bind="value: phone" name="Phone" onkeypress="return isNumberKey(event)" type="text" style="background:#f8f8f8;"/>
							<span data-bind="visible: $.trim(phone())==''" class="error">*</span>
						</div>
						<div class="row-item-request">
							<span>Email của bạn</span>
							<input data-bind="value: email" name="Email" type="text" style="background:#f8f8f8;"/>
							<span data-bind="visible: !isValidEmail()" class="error">*</span>
						</div>
						<div class="row-item-request" style="display:none;">
							<span>Public</span>
							<input data-bind="checked: isPublic" name="IsPublic" type="checkbox" />
            </div>
						</div>
						<div class="advanceSearchNote">
							<h3>Ghi chú</h3>
							<ul>
								<li>Form này chỉ dùng để gửi yêu cầu khi nhu cầu của bạn rất phức tạp, và bạn không thể
									tìm thấy bằng công cụ search.</li>
								<li>Foody đang thử nghiệm tính năng này, trước mắt đội ngũ Foody sẽ giúp bạn bằng cách
									gợi ý danh sách các địa điểm phù hợp.
									Sau đó, Foody sẽ phát triển rộng hơn để cộng đồng thành viên hoặc chủ địa điểm có
									thể tham gia cùng gợi ý giúp bạn. </li>
								<li>Thời gian để xử lý yêu cầu trong vòng từ 1 - 24 tiếng hoặc lâu hơn tùy theo mức độ
									phức tạp của yêu cầu</li>
								<li>Thông tin tư vấn hoàn toàn miễn phí. Foody sẽ gửi danh sách gợi ý qua Email của bạn,
									vui lòng cập nhật đầy đủ Email liên hệ.</li>
								<li>Tính năng này hiện tại chỉ áp dụng cho tìm địa điểm tại TP. HCM</li>
							</ul>
						</div>
						<div class="bottom-buttons">
							<label>
                <span style="float: left; margin-top: 1px; padding-right: 5px;">
                    <input type="checkbox" checked="checked" disabled="disabled"/></span>
                Foody gửi danh sách các địa điểm phù hợp với yêu cầu qua <b>Email</b> của tôi</label>
							<a data-bind="click: post" href="javascript:void(0)">Gửi yêu cầu</a>
							<span data-bind="visible: isposting" style="position: absolute;right: 140px;top: 21px;"><img src="/style/images/icons/ajax-loader.gif" /></span>
						</div>
						<!-- /ko -->

						<div data-bind="visible: requestSuccess" class="request-sent-success">
							<b>Gửi yêu cầu thành công!</b> Foody sẽ phản hồi qua Email của bạn!<br />
							<a href="javascript:void(0)" data-bind="click: reset">Tiếp tục</a> gửi yêu cầu hoặc <a
								data-bind="click: close" href="javascript:void(0)">đóng lại</a></div>
						<div data-bind="visible: hasError">Đã có lỗi, vui lòng <a href="javascript:void(0)"
								data-bind="click: reset">thử lại</a></div>

					</div>
				</div>


				<script type="text/javascript">
					var loadingElement = $('<div class="search-loading"><b>Đang tải...</b></div>')
        .appendTo('body')
        .hide();
    var localize = {
        areaText: 'Khu vực',
        purposeText: 'Mục đích',
        cuisineText: 'Ẩm thực',
        dishCategoryText: 'Loại món',
        categoryText: 'Phân loại',
        propertyText: 'Tiện nghi',
        diningText: 'Thích hợp',
        metaTitleText: "Địa điểm Qu&#225;n ăn phong c&#225;ch M&#243;n Việt tại Quận Cầu Giấy, H&#224; Nội"
    };
    var jsonData = {"photoCollectionResultCount":8741,"provinceId":218,"categoryId":3,"districtId":21,"districtName":"Quận Cầu Giấy","searchUrl":"/ha-noi/quan-an","searchDefaultUrl":"/ha-noi/dia-diem","keyword":"","viewType":"row","sortType":1,"priceMin":0,"priceMax":5000000,"districts":[{"Id":20,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Ba Đình","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Ba Dinh"},{"Id":690,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Bắc Từ Liêm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Bac Tu Liem"},{"Id":21,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Cầu Giấy","UrlRewriteName":null,"ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Cau Giay"},{"Id":22,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Đống Đa","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Dong Da"},{"Id":23,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hà Đông","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Ha Dong"},{"Id":24,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hai Bà Trưng","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hai Ba Trung"},{"Id":25,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hoàn Kiếm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hoan Kiem"},{"Id":26,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hoàng Mai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hoang Mai"},{"Id":27,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Long Biên","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Long Bien"},{"Id":945,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Nam Từ Liêm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Nam Tu Liem"},{"Id":28,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Tây Hồ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Tay Ho"},{"Id":29,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Thanh Xuân","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Thanh Xuan"},{"Id":692,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Thị Xã Sơn Tây","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Thi Xa Son Tay"},{"Id":674,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Ba Vì","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Ba Vi"},{"Id":675,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Chương Mỹ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Chuong My"},{"Id":676,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Đan Phượng","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Dan Phuong"},{"Id":677,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Đông Anh","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Dong Anh"},{"Id":678,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Gia Lâm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Gia Lam"},{"Id":679,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Hoài Đức","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Hoai Duc"},{"Id":680,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Mê Linh","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Me Linh"},{"Id":681,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Mỹ Đức","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen My Duc"},{"Id":682,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Phú Xuyên","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Phu Xuyen"},{"Id":683,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Phúc Thọ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Phuc Tho"},{"Id":684,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Quốc Oai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Quoc Oai"},{"Id":685,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Sóc Sơn","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Soc Son"},{"Id":686,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thạch Thất","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thach That"},{"Id":687,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thanh Oai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thanh Oai"},{"Id":688,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thanh Trì","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thanh Tri"},{"Id":689,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thường Tín","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thuong Tin"},{"Id":691,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Ứng Hòa","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Ung Hoa"}],"allAreas":[],"allDistricts":[],"allPurposes":[],"allCategories":[],"allCuisines":[],"allDishCategories":[],"allProperties":[],"allDinings":[],"selectedAreas":[],"selectedDistricts":[{"Id":21,"Avatar":null,"ParentId":218,"ParentName":null,"Name":"Quận Cầu Giấy","UrlRewriteName":"quan-cau-giay","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":1,"AsciiName":"Quan Cau Giay"}],"selectedPurposes":[],"selectedCategories":[{"Id":3,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quán ăn","UrlRewriteName":"quan-an","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":8,"AsciiName":"Quan an"}],"selectedCuisines":[{"Id":1,"Avatar":"foody-01-vietnam-635950402447733778.png","ParentId":0,"ParentName":null,"Name":"Món Việt","UrlRewriteName":"viet-nam","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[{"Id":12,"Avatar":"foody-12-miennam-635950401085583984.png","ParentId":1,"ParentName":null,"Name":"Món Miền Nam","UrlRewriteName":"mien-nam","ResultCount":24495,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Mien Nam"},{"Id":2,"Avatar":"foody-02-mienbac-635950402329745934.png","ParentId":1,"ParentName":null,"Name":"Món Bắc","UrlRewriteName":"mien-bac","ResultCount":27554,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Bac"},{"Id":7,"Avatar":"foody-07-mientrung-635950401707280292.png","ParentId":1,"ParentName":null,"Name":"Món Miền Trung","UrlRewriteName":"mien-trung","ResultCount":24634,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Mien Trung"},{"Id":29,"Avatar":"foody-29-taynguyen-635950400755089030.png","ParentId":1,"ParentName":null,"Name":"Tây Nguyên","UrlRewriteName":"tay-nguyen","ResultCount":4555,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Tay Nguyen"}],"FilterType":4,"AsciiName":"Mon Viet"}],"selectedDishCategories":[],"selectedProperties":[],"selectedPrices":[],"selectedDinings":[],"searchItems":[],"adItems":[],"totalResult":2455,"currentPage":400,"locationQuery":null,"maxPageToLoad":400,"brand":"","providerList":[],"book":false,"totalSubItems":59,"documentSource":"Restaurant","listResultCount":93042,"restaurantResultCount":2514,"userResultCount":7330094,"articleResultCount":4395,"pictureResultCount":20947}; 
    var jsonDataSearch = {"photoCollectionResultCount":8741,"provinceId":218,"categoryId":3,"districtId":21,"districtName":"Quận Cầu Giấy","searchUrl":"/ha-noi/quan-an","searchDefaultUrl":"/ha-noi/dia-diem","keyword":"","viewType":"row","sortType":1,"priceMin":0,"priceMax":5000000,"districts":[{"Id":20,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Ba Đình","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Ba Dinh"},{"Id":690,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Bắc Từ Liêm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Bac Tu Liem"},{"Id":21,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Cầu Giấy","UrlRewriteName":null,"ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Cau Giay"},{"Id":22,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Đống Đa","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Dong Da"},{"Id":23,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hà Đông","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Ha Dong"},{"Id":24,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hai Bà Trưng","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hai Ba Trung"},{"Id":25,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hoàn Kiếm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hoan Kiem"},{"Id":26,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Hoàng Mai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Hoang Mai"},{"Id":27,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Long Biên","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Long Bien"},{"Id":945,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Nam Từ Liêm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Nam Tu Liem"},{"Id":28,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Tây Hồ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Tay Ho"},{"Id":29,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quận Thanh Xuân","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Quan Thanh Xuan"},{"Id":692,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Thị Xã Sơn Tây","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Thi Xa Son Tay"},{"Id":674,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Ba Vì","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Ba Vi"},{"Id":675,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Chương Mỹ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Chuong My"},{"Id":676,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Đan Phượng","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Dan Phuong"},{"Id":677,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Đông Anh","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Dong Anh"},{"Id":678,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Gia Lâm","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Gia Lam"},{"Id":679,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Hoài Đức","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Hoai Duc"},{"Id":680,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Mê Linh","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Me Linh"},{"Id":681,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Mỹ Đức","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen My Duc"},{"Id":682,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Phú Xuyên","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Phu Xuyen"},{"Id":683,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Phúc Thọ","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Phuc Tho"},{"Id":684,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Quốc Oai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Quoc Oai"},{"Id":685,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Sóc Sơn","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Soc Son"},{"Id":686,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thạch Thất","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thach That"},{"Id":687,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thanh Oai","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thanh Oai"},{"Id":688,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thanh Trì","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thanh Tri"},{"Id":689,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Thường Tín","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Thuong Tin"},{"Id":691,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Huyện Ứng Hòa","UrlRewriteName":null,"ResultCount":0,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":2,"AsciiName":"Huyen Ung Hoa"}],"allAreas":[],"allDistricts":[],"allPurposes":[],"allCategories":[],"allCuisines":[],"allDishCategories":[],"allProperties":[],"allDinings":[],"selectedAreas":[],"selectedDistricts":[{"Id":21,"Avatar":null,"ParentId":218,"ParentName":null,"Name":"Quận Cầu Giấy","UrlRewriteName":"quan-cau-giay","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":1,"AsciiName":"Quan Cau Giay"}],"selectedPurposes":[],"selectedCategories":[{"Id":3,"Avatar":null,"ParentId":0,"ParentName":null,"Name":"Quán ăn","UrlRewriteName":"quan-an","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[],"FilterType":8,"AsciiName":"Quan an"}],"selectedCuisines":[{"Id":1,"Avatar":"foody-01-vietnam-635950402447733778.png","ParentId":0,"ParentName":null,"Name":"Món Việt","UrlRewriteName":"viet-nam","ResultCount":0,"Selected":true,"Min":null,"Max":null,"Children":[{"Id":12,"Avatar":"foody-12-miennam-635950401085583984.png","ParentId":1,"ParentName":null,"Name":"Món Miền Nam","UrlRewriteName":"mien-nam","ResultCount":24495,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Mien Nam"},{"Id":2,"Avatar":"foody-02-mienbac-635950402329745934.png","ParentId":1,"ParentName":null,"Name":"Món Bắc","UrlRewriteName":"mien-bac","ResultCount":27554,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Bac"},{"Id":7,"Avatar":"foody-07-mientrung-635950401707280292.png","ParentId":1,"ParentName":null,"Name":"Món Miền Trung","UrlRewriteName":"mien-trung","ResultCount":24634,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Mon Mien Trung"},{"Id":29,"Avatar":"foody-29-taynguyen-635950400755089030.png","ParentId":1,"ParentName":null,"Name":"Tây Nguyên","UrlRewriteName":"tay-nguyen","ResultCount":4555,"Selected":false,"Min":null,"Max":null,"Children":[],"FilterType":4,"AsciiName":"Tay Nguyen"}],"FilterType":4,"AsciiName":"Mon Viet"}],"selectedDishCategories":[],"selectedProperties":[],"selectedPrices":[],"selectedDinings":[],"searchItems":[],"adItems":[],"totalResult":2455,"currentPage":400,"locationQuery":null,"maxPageToLoad":400,"brand":"","providerList":[],"book":false,"totalSubItems":59,"documentSource":"Restaurant","listResultCount":93042,"restaurantResultCount":2514,"userResultCount":7330094,"articleResultCount":4395,"pictureResultCount":20947};
    var resultExcutedCallback = function () {
        bindDeliverService();
    }

    function googleLoadMap()
    {
        if(window.initInfoBox)
            initInfoBox();

    }

				</script>





				<div id="tab-footer-top-friend-user" class="microsite-banner-edge"
					style="background-color: #fff; padding: 20px 0; float: left; clear: both; width: 100%;position:relative;z-index:11;">
					<ul class="home-tab" style="width: 1170px; margin: 0 auto;">
						<li class="active">
							<a href="#tab-footer-top-user" style="padding: 15px 0; margin-right: 60px;">Top Thành
								viên</a>
						</li>

					</ul>

					<div id="tab-footer-top-user">


					</div>


					<script type="text/javascript">
						$(function () {
            $("#tab-footer-top-friend-user").custabs();
        });
					</script>
				</div>


				<div id="addWishListPopup" style="display: none; margin: 0; padding: 0;">

					<div id="banner-ads" class="save-popup-ads">


					</div>
					<div class="fldg-left" data-bind="visible:IsLoadingRes()">
						<div class="fldg-left">
							<div class="pre-avatar animated-bg" style="height:188px;width:300px"></div>
							<div style="overflow:hidden; clear:both;">
								<div class="pre-review-points animated-bg" style="margin: 10px 0 0 0;"></div>
								<div style="float: left;width: 255px;margin-left: 10px;margin-top: 13px;">
									<div class="preload-bar long animated-bg" style="margin-bottom: 7px;"></div>
									<div class="preload-bar medium animated-bg" style="clear: both;margin-bottom: 6px;">
									</div>
								</div>
							</div>
							<div class="pre-avatar animated-bg" style="height:36px;width:300px;margin: 10px 0;"></div>
							<div class="fldr-summary" style="height:200px">
							</div>
						</div>


					</div>
					<div class="fldg-left" data-bind="visible:!IsLoadingRes()">
						<div class="fldg-left" data-bind="with:ResSummary">
							<a>
								<img class="fldr-res-avatar" src="" data-bind="attr:{src:Restaurant.Avatar}">
            </a>
								<div style="overflow:hidden; clear:both;">
									<div class="review-points green"
										data-bind="css:{'green':Restaurant.AvgRating>=6, 'grey':Restaurant.AvgRating==0||Restaurant.AvgRating==null}">
										<span data-bind="text:Restaurant.AvgRating.formatPoint()">_._</span>
									</div>

									<div style="float: left; width: 255px; margin-left: 10px;">
										<div class="fldr-res-title ng-binding" data-bind="text:Restaurant.Name">&nbsp;
										</div>
										<div class="fldr-res-address ng-binding" data-bind="text:Restaurant.Address">
											&nbsp;</div>
									</div>
								</div>

								<div><a class="btn-write fd-write-review"
										data-bind="attr:{'data-res-id':$parent.restaurantId,'resid':$parent.restaurantId}"><i class="fa fa-comment"></i>&nbsp;Viết
										bình luận</a></div>

								<div class="fldr-summary">
									<div class="fldr-res-points">
										<span data-bind="text:AvgReview.Total.formatK(0)">&nbsp;</span>&nbsp;Bình luận
									</div>
									<ul>
										<li>
											<div class="counts" data-bind="text:AvgReview.TotalPerfect.formatK(0)">
												&nbsp;</div>
											<div>Tuyệt vời</div>
										</li>
										<li>
											<div class="counts" data-bind="text:AvgReview.TotalGood.formatK(0)">&nbsp;
											</div>
											<div>Khá tốt</div>
										</li>
										<li>
											<div class="counts" data-bind="text:AvgReview.TotalAvg.formatK(0)">&nbsp;
											</div>
											<div>Trung bình</div>
										</li>
										<li>
											<div class="counts" data-bind="text:AvgReview.TotalBad.formatK(0)">&nbsp;
											</div>
											<div>Kém</div>
										</li>
									</ul>
									<div class="fldr-rating">
										<div class="title">Đánh giá:</div>
										<img class="ruler" src="/style/images/icons/ratin-rank.png">
										<ul data-bind="foreach: { data: Rating, as: 'rate' }">
											<li>
												<label data-bind="text:rate.Label">&nbsp;</label>
												<div class="range" data-bind="{attr:{'data-val':rate.Point}}"></div>
												<span data-bind="text:rate.Point">&nbsp;</span>
											</li>
										</ul>
									</div>
								</div>

						</div>
					</div>
					<ul data-bind="if:isLoading()" style="float:right; width:655px;">
						<li class="tool-custom-list">
							<div class="list-addmore-but">
								<span style="float: left; margin-right: 10px;">Chọn bộ sưu tập để lưu lại </span>
								<span data-bind="visible: isLoading" style="float: left; margin-top: 2px;">
                        <img src="/style/images/icons/ajax-loader.gif" alt="loading..." />
                    </span>
								<span style="float:right;" class="fa fa-map-marker">
                    </span>
							</div>
							<div class="custom-list-wrapper">
								<div class="search-of-collections">
									<input class="txt-search-title" type="text" value="" placeholder="T&#236;m kiếm bộ sưu tập theo t&#234;n..." />
									<span class="fa fa-search" style="position: absolute; left: 15px; top: 11px; color: #999;"></span>
									<span class="fa fa-times" style="position: absolute; right: 15px; top: 11px; cursor: pointer;"></span>
								</div>
								<ul class="list-of-collections">
									<li style="position: relative; overflow: hidden;">
										<div
											style="border-bottom: 1px solid #eee;padding: 14px 0px 0px 30px;height: 22px;">
										</div>
									</li>
									<li style="position: relative; overflow: hidden;">
										<div
											style="border-bottom: 1px solid #eee;padding: 14px 0px 0px 30px;height: 22px;">
										</div>
									</li>
									<li style="position: relative; overflow: hidden;">
										<div
											style="border-bottom: 1px solid #eee;padding: 14px 0px 0px 30px;height: 22px;">
										</div>
									</li>
									<li style="position: relative; overflow: hidden;">
										<div
											style="border-bottom: 1px solid #eee;padding: 14px 0px 0px 30px;height: 22px;">
										</div>
									</li>
									<li style="position: relative; overflow: hidden;">
										<div
											style="border-bottom: 1px solid #eee;padding: 14px 0px 0px 30px;height: 22px;">
										</div>
									</li>
									<li style="position: relative; overflow: hidden;">
										<div
											style="border-bottom: 1px solid #eee;padding: 14px 0px 0px 30px;height: 22px;">
										</div>
									</li>
								</ul>

							</div>
							<div class="place-collection-createbutton">
								<div class="pre-avatar animated-bg" style="height:38px;width:100%;margin-top:15px;">
								</div>
							</div>
						</li>


					</ul>

					<ul data-bind="visible:!isLoading()" style="float:right; width:655px;">
						<li class="tool-custom-list">
							<div class="list-addmore-but">
								<span style="float: left; margin-right: 10px;">Chọn bộ sưu tập để lưu lại </span>
								<span data-bind="visible: isLoading" style="float: left; margin-top: 2px;">
                        <img src="/style/images/icons/ajax-loader.gif" alt="loading..." />
                    </span>
								<span style="float:right;" class="fa fa-map-marker">

                    </span>
							</div>
							<div class="custom-list-wrapper">

								<div class="search-of-collections">
									<input class="txt-search-title" type="text" value="" placeholder="T&#236;m kiếm bộ sưu tập theo t&#234;n..."
                               onkeyup="addWishListPopupModel.searchTitleChange();"/>
									<span class="fa fa-search" style="position: absolute; left: 15px; top: 11px; color: #999;"></span>
									<span class="fa fa-times" style="position: absolute; right: 15px; top: 11px; cursor: pointer;" onclick="addWishListPopupModel.clearTitle()"></span>
								</div>
								<ul data-bind="foreach: lists" class="list-of-collections">
									<li style="position: relative; overflow: hidden;"
										data-bind="visible: Title.toLowerCase().indexOf($root.searchTitle().toLowerCase()) > -1">

										<a
											data-bind="attr: { 'data-name': Name }, css: { 'checked': RestaurantId() == $parent.restaurantId() }, click: $parent.toggleSelection">
											<span class="list-label" data-bind="text: Title"></span>
										</a>
										<a data-bind="attr: { href: Url }" href="#" target="_blank" title="Go to list"
											class="custom-list-viewdetail">
											<label data-bind="text:'Xem {0}'.replace('{0}',TotalItems())"></label>
											<i class="fa fa-angle-right"></i>
										</a>
									</li>
								</ul>

							</div>
							<div class="place-collection-createbutton">
								<a href="#" data-bind="click: createNewList">
									+ Tạo bộ sưu tập mới
								</a>
							</div>
						</li>
					</ul>
				</div>
				<script>
					var content = $('#banner-ads').children().length;
    if (content > 0) {
        $("#banner-ads").addClass('ads-banner');
    }
				</script>
				<div class="footer-down-app-wrap"
					style="margin-top:0;background: #eeeeee;position: relative;z-index: 11;">
					<div class="footer-down-app">
						<div class="footer-intro-app">Tìm địa điểm trên đường đi? Tải app Foody!</div>
						<div style="float:left; width:240px;margin-top:-8px;">
							<div
								style="border:#ddd 1px solid; background:#fff;text-align: center; padding: 5px 30px;width:100px;margin-bottom:40px; overflow:hidden; clear:both;">
								Thống kê
							</div>
							<div class="footer-down-stats">
								<div class="footer-down-stats-header">334,384 Địa điểm</div>
								<div class="footer-down-stats-desc">toàn quốc</div>
							</div>
							<div class="footer-down-stats">
								<div class="footer-down-stats-header">38,630,265 người sử dụng</div>
								<div class="footer-down-stats-desc">trong & ngoài nước</div>
							</div>
							<div class="footer-down-stats">
								<div class="footer-down-stats-header">1,481,841 bình luận</div>
								<div class="footer-down-stats-desc">đã chia sẻ</div>
							</div>
							<div class="footer-down-stats">
								<div class="footer-down-stats-header">608,066 check-in</div>
								<div class="footer-down-stats-desc">đã thực hiện</div>
							</div>
							<div class="footer-down-stats">
								<div class="footer-down-stats-header">10,232,333 hình ảnh</div>
								<div class="footer-down-stats-desc">được tải lên</div>
							</div>
							<div class="footer-down-stats">
								<div class="footer-down-stats-header">24,623,376 Bộ sưu tập</div>
								<div class="footer-down-stats-desc">bộ sưu tập được tạo</div>
							</div>

						</div>
						<div style="float:right; width:752px;">


							<a href="https://itunes.apple.com/app/id570435154" target="_blank"
								style="float: left; text-align: center; display: block;" rel="nofollow">
								<span style="border: #ddd 1px solid; background: #fff; padding: 5px 30px; border-radius: 2px;">iOS App</span>
								<img style="margin-top:20px;" src="/style/images/icons/ios-footer.png" alt="App Foody iOS" title="App Foody iOS" />
                </a>
								<a href="https://play.google.com/store/apps/details?id=com.foody.vn.activity"
									target="_blank" style="float: left; text-align: center; display: block;"
									rel="nofollow">
									<span style="border: #ddd 1px solid; background: #fff; padding: 5px 30px; border-radius: 2px;">Android App</span>
									<img style="margin-top:20px;" src="/style/images/icons/android-footer.png" alt="App Foody Android" title="App Foody Android" />
                </a>
									<a href="https://www.windowsphone.com/en-us/store/app/foody/0ed64e33-cff6-4211-a971-71e496ae9066"
										target="_blank" style="float: left; text-align: center; display: block;"
										rel="nofollow">
										<span style="border: #ddd 1px solid; background: #fff; padding: 5px 30px; border-radius: 2px;">Windows App</span>
										<img src="/style/images/icons/windows-footer.png" alt="App Foody WindowPhone" title="App Foody WindowPhone" />
                </a>

						</div>
					</div>
				</div>

				<footer class="footer" id="footer-in-bottom" style="position: relative;z-index: 11;">
					<div class="footer-fixed">
						<div class="footer-min">
							<div class="footer-left-box" style="display:none;">
								<div class="footer-titles">Cài đặt</div>
								<ul>
									<li style="width:100%;float:left;margin:3px 0 7px;">
										<div style="float: left;padding:3px 5px 0 0;color:#666; width:100px;">Tỉnh thành
										</div>
										<div style="float: left;">
											<dl id="f_dropdown" class="drop_seeall">
												<dt>
													<a href="javascript:void(0)"
														style="cursor:default;"><span class="text" style="cursor:default;">H&#224; Nội</span></a>
												</dt>
											</dl>
										</div>
									</li>
									<li style="width:100%;float:left;margin:3px 0 7px;">
										<div style="float: left;padding-right:5px;color:#666; width:100px;">Ngôn ngữ
										</div>
										<div class="footer-language-chooser">

											<a href="javascript:void(0)" style="cursor:default;" rel="nofollow"
												style="color: #02AAD4"
												href="/__get/common/changelanguage?code=vn&amp;returnUrl=http%3A%2F%2Fwww.foody.vn%2Fha-noi%2Fquan-an-phong-cach-viet-nam-tai-quan-cau-giay%3Fc%3Dquan-an%26categorygroup%3Dfood%26page%3D400%26append%3DTrue">
												Tiếng Việt
											</a>
										</div>
									</li>

								</ul>
							</div>
							<div class="footer-middle-box">
								<div class="footer-titles">Khám phá</div>
								<ul>

									<li><a href="/ung-dung-mobile" rel="nofollow">Ứng dụng Mobile</a></li>

									<li><a href="javascript:void(0)" class="add-new-list" rel="nofollow">Tạo bộ sưu
											tập</a></li>

									<li><a href="/bao-mat-thong-tin" rel="nofollow">Bảo mật thông tin</a></li>
									<li><a href="/dieu-khoan-su-dung" rel="nofollow">Quy định</a></li>

								</ul>
							</div>
							<div class="footer-middle-box">
								<div class="footer-titles">Công ty</div>
								<ul>
									<li><a href="/gioi-thieu" rel="nofollow">Giới thiệu</a></li>


									<li><a href="/tro-giup" rel="nofollow">Trợ giúp</a></li>
									<li><a href="/jobs" rel="nofollow">Việc làm</a></li>

									<li><a href="/regulation" rel="nofollow">Quy chế</a></li>
									<li><a href="/thoa-thuan-su-dung" rel="nofollow">Thỏa thuận sử dụng dịch vụ</a></li>
									<li><a href="/lien-he" rel="nofollow">Liên hệ</a></li>
								</ul>
							</div>
							<div class="footer-middle-box" style="padding-left: 35px; width: 200px;" id="footer-join">
								<div class="footer-titles" rel="nofollow">Tham gia trên</div>
								<ul>
									<li><a href="https://www.facebook.com/FoodyVietnam" target="_blank"
											rel="nofollow">Facebook</a></li>
									<li><a href="https://www.instagram.com/foodysaigon" target="_blank"
											rel="nofollow">Instagram</a></li>
									<li><a href="https://www.youtube.com/c/FoodyVn" target="_blank"
											rel="nofollow">Youtube</a></li>
									<li><a href="https://plus.google.com/104802868919802646307" target="_blank"
											rel="publisher">Google</a></li>
									<li style="clear: both;">
										<a href="https://shopeefood.vn" target="_blank" rel="nofollow">
											ShopeeFood.vn
										</a>
										- Giao đồ ăn tận nơi
									</li>
								</ul>
							</div>
							<div class="footer-middle-box" style="padding-left: 35px; width: 160px;">
								<div class="footer-titles">Giấy phép</div>
								<ul>
									<li><a>MXH 363/GP-BTTTT</a></li>

									<li>
										<a target="_blank" rel="nofollow"
											href="http://online.gov.vn/HomePage/WebsiteDisplay.aspx?DocId=13113">
											<img src="/style/images/gov_seals.jpg" width="160" style="margin-left: -5px;" alt="logo-da-dang-ky-bo-cong-thuong" />
                                    </a>
									</li>
								</ul>
							</div>
							<div class="footer-middle-box" style="padding-left: 35px; width: 160px;">

								<script language="JavaScript" src="https://dunsregistered.dnb.com"
									type="text/javascript"></script>
							</div>
						</div>

					</div>
					<div class="footer-country-list">
						<span style="color: #999; clear: both; display: block;">
                        Công Ty Cổ Phần Foody, Lầu G, Tòa nhà Jabes 1, 244 đường Cống Quỳnh, phường Phạm Ngũ Lão, Quận 1, TP.HCM
                    </span>

						<span id="foody-hot-line" style="color: #999; clear: both; display: block;">
                        Email: support@shopeefood.vn
                    </span>

						<span style="color: #999; clear: both; display: block;">
                        Giấy CN ĐKDN số 0311828036 do Sở Kế hoạch và Đầu tư TP.HCM cấp ngày 11/6/2012, sửa đổi lần thứ 23, ngày 10/12/2020
                    </span>
						<span style="color: #999; clear: both; display: block;">
                        Giấy phép thiết lập MXH trên mạng số 363/GP-BTTTT do Bộ Thông tin và Truyền thông cấp ngày 30/6/2016
                        Người chịu trách nhiệm: Đặng Hoàng Minh.
                    </span>



					</div>
					<script>
						function InviteFriend() {
                    
                }
					</script>
				</footer>
				<script>
					$(document).ready(function () {
                //$(window).load(function () {
                    var scrollTo = getParameterByName('scrollto');
                    if (scrollTo != '') {
                        //$('html, body').animate({ scrollTop: $(document).height() }, "fast");
                        //setTimeout(function () {
                            $("html, body").animate({
                                scrollTop: ($(document).height() + $("html, body").height()) + 800
                            }, 2000);
                        //}, 2000);
                    }
                //});
                
            });

            function getParameterByName(name) {
                name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
                var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
                    results = regex.exec(location.search);
                return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
            }
				</script>

				<style type="text/css">
					.popup-download-app {
						position: fixed;
						z-index: 610;
						display: none;
						bottom: 0;
						width: 750px;
						height: 200px;
						background: url(/style/images/popup/750x200_popupdownloadapp.png) no-repeat;
					}

					.popup-download-app .pda-btn-close {
						position: absolute;
						right: 0;
						top: 35px;
						width: 25px;
						height: 25px;
						cursor: pointer;
						z-index: 1;
					}

					.popup-download-app .pda-btn-frame {
						position: absolute;
						left: 5px;
						top: 40px;
						width: 110px;
						bottom: 0;
						z-index: 1;
					}

					.popup-download-app .pda-btn-frame a {
						display: block;
						float: none;
						width: 100%;
						height: 40px;
						margin: 10px 0 10px 0;
						cursor: pointer;
					}

					.popup-download-app .pda-content-link {
						height: 100%;
						position: relative;
					}

					.popup-download-app .pda-qcode {
						position: absolute;
						width: 60px;
						height: 60px;
						right: 40px;
						bottom: 20px;
					}

					.popup-download-app .pda-content-link .pda-content {
						position: absolute;
						left: 300px;
						width: 340px;
						top: 117px;
						color: #959595;
						font-size: 15px;
						white-space: normal;
						line-height: 1.3em;
					}

					.popup-download-app .pda-content-link .pda-content p {
						margin-bottom: 10px;
					}

					.popup-download-app .pda-content-link .pda-content b {
						font-weight: bold;
						font-size: 18px;
						color: #ffffff;
					}
				</style>

				<div class="popup-download-app">
					<div class="pda-btn-close"></div>
					<div class="pda-btn-frame">
						<a href="https://itunes.apple.com/app/id570435154" title="iOS App">
							<img src="/style/images/popup/popupdownload-appstore.png" />
            </a>
							<a href="https://play.google.com/store/apps/details?id=com.foody.vn.activity"
								title="Android App">
								<img src="/style/images/popup/popupdownload-googleplay.png" />
            </a>
								<a href="https://www.windowsphone.com/en-us/store/app/foody/0ed64e33-cff6-4211-a971-71e496ae9066"
									title="Windows App">
									<img src="/style/images/popup/popupdownload-windowstore.png" />
            </a>
					</div>
					<a href="/ung-dung-mobile">
						<div class="pda-content-link">
							<div class="pda-content">
								<p><b>Ứng Dụng tìm kiếm địa điểm ăn uống</b></p>
								<p>Nhanh & tiện lợi - với hàng ngàn địa điểm, bình luận, hình ảnh & thành viên chia sẻ
								</p>
							</div>
						</div>
					</a>
					<img class="pda-qcode" src="/style/images/popup/android-code-vn.png" />

</div>
					<script type="text/javascript">
						//popupDownloadRePosition();
    //function popupDownloadRePosition() {
    //    var popup = $('.popup-download-app');
    //    var wWidth = $(window).innerWidth();
    //    var pWidth = popup.width();
    //    var pLeft = (wWidth - pWidth) / 2;
    //    popup.css('left', pLeft);
    //}
    ////$('.popup-download-app').slideDown(function () { $('.popup-download-app').attr('style', ''); });
    //$('.popup-download-app .pda-btn-close').on('click', function () {
    //    $('.popup-download-app').slideUp();
    //    $.cookie('pda-close', '1', { path: '/' });
    //});
    //setTimeout(function () {
    //    if ($.cookie('pda-close') != '1')
    //        $('.popup-download-app').slideDown();
    //}, 2000);

    //$(window).resize(function () {
    //    popupDownloadRePosition();
    //});

					</script>



					<div id="HelperCtrl" ng-controller="HelperCtrl" style="position:absolute;z-index:10;"></div>

				</div>




				<script>
					function googleLoadMapCallback() {
        if (typeof (googleLoadMap) == "function") {
            googleLoadMap();
        }
    }
				</script>

				<script type="text/javascript"
					src="//maps.googleapis.com/maps/api/js?v=3&amp;callback=googleLoadMapCallback&amp;libraries=visualization,drawing,geometry,places&amp;key=AIzaSyA2Zb2vY8-t_9BUYqFFjc9LQiNWUZPLft4&amp;language=vn">
				</script>





				<script>
					window.dataLanguagesPc = {
        BtnCollectionSaved: 'Đã lưu bộ sưu tập',
        BtnCollectionSave: 'Lưu bộ sưu tập',
        BtnShare: 'Chia sẻ',
        BtnLike: 'Thích',
        BtnUnLike: 'Bỏ thích',
        UpdatedOn: 'Cập nhật ngày',
        Views: 'Lượt xem',
        Photos: 'Hình ảnh',
        BtnViewMoreCollection: 'Xem thêm bộ sưu tập',
        BtnViewMorePhoto: 'Xem thêm hình ảnh',
        DlgPhotoTitleSave: 'Lưu ảnh vào bộ sưu tập',
        InputCollectionName: 'Tên bộ sưu tập',
        Description: 'Mô tả bộ sưu tập',
        BtnCollectionCreate: 'Tạo mới bộ sưu tập',
        BtnCreate: 'Tạo',
        BtnCreateNew: 'Tạo mới bộ sưu tập',
        BtnEdit: 'Chỉnh sửa',
        BtnDelete: 'Xoá',
        BtnPublic: 'Công khai (Public)',
        InputCollectionNameNew: 'Nhập tên bộ sưu tập mới',
        DlgCollectionTitleEdit: 'Chỉnh sửa bộ sưu tập',
        BtnCancel: 'Huỷ',
        BtnSave: 'Lưu',
        Saved: 'Lưu lại',
        Like: 'Thích',
        DlgCollectionTitleShare: 'Chia sẻ bộ sưu tập hình ảnh',
        DlgCollectionChooseMethodShare: 'Vui lòng chọn hình thức chia sẻ',
        MsgConfirmDeletePhoto: 'Bạn có chắc muốn xoá hình này?',
        MsgConfirmDeleteCollection: 'Bạn có chắc muốn xoá bộ sưu tập này?',
        MsgCollectionNameExist: 'Tên bộ sưu tập đã tồn tại',
        MsgAddPhotoSelectRequired: 'Vui lòng chọn hình ảnh của bạn để thêm vào bộ sưu tập này!',
        MsgActionFailure: 'Có lỗi xảy ra trong quá trình xử lý.\r\nBạn vui lòng thử lại sau.',
        FilterByName: 'Tìm kiếm theo tên bộ sưu tập'
    };
				</script>
				<script>
					var PopupSavePhotoModel = function () {
        var self = this;

        var listCollectionModel = function (arg) {
            var self = this;
            var root = arg.root;
            var type = arg.type;
            this.Items = ko.observableArray([]);
            this.Total = ko.observable(0);
            this.LastId = ko.observable(null);
            this.Count = ko.observable(14);

            function createItemModel(item) {
                item.TotalItems = ko.observable(item.TotalItems);
                item.IsChecked = ko.observable(item.IsChecked);
                item.Name = ko.observable(item.Name);
                item.IconState = function (state) {
                    if (state) {
                        if (root.IsLoading() == true) {
                            if (root.Model.Filter.Id() == item.Id)
                                return 'fa fa-circle-o-notch fa-spin';
                        }
                    }
                    return item.IsChecked() == true ? 'fa fa-circle' : 'fa fa-circle-o';
                }
                return item;
            }

            function createCollectionModel(items) {
                var rs = self.Items;
                if (!items || items.length == 0)
                    return rs;
                for (var i = 0; i < items.length; i++) {
                    rs.push(createItemModel(items[i]));
                }
                return rs;
            }

            this.Reset = function () {
                self.Items([]);
                self.Total(0);
                self.LastId(null);
            };
            this.BindData = function (data) {
                createCollectionModel(data.Items);
                self.Total(data.Total);
                self.LastId(data.LastId);
            };

            this.SetCheckedItem = function (id, isChecked) {


                var items = self.Items();
                var len = items.length;

                for (var i = 0; i < len; i++) {
                    var collection = items[i];
                    if (collection.Id == id) {
                        collection.IsChecked(isChecked);
                        var count = collection.TotalItems();
                        if (type == 1)
                            collection.TotalItems(isChecked == true ? count + 1 : count - 1);
                        break;
                    }
                }
            }

            this.fnLoadMore = function () {
                root.bindListCollection({ type: type });
            };
            this.TotalRemaining = function () {
                return self.Total() - self.Items().length;
            };
        };

        var fnCallBack = null;
        var bPopup = null;
        var selector = '#ppSavePhoto';
        self.IsLoading = ko.observable(false);
        self.IsEnabledCreateInput = ko.observable(true);
        self.Model = {
            PictureId: ko.observable(null),
            Filter: {
                Id: ko.observable(null),
                Name: ko.observable(''),
                NameOther: ko.observable('')
            }
        };
        self.Model.ListColl = new listCollectionModel({ root: self, type: 1 });
        self.Model.ListCollOther = new listCollectionModel({ root: self, type: 2 });

        function callFunction(fnc, arg) {
            if (typeof fnc == 'function')
                fnc(arg);
        }

        function listCollection(arg, fnc) {
            var query = arg.type == 2 ? self.Model.Filter.NameOther() : self.Model.Filter.Name();
            var count = arg.type == 2 ? self.Model.ListCollOther.Count() : self.Model.ListColl.Count();
            var lastId = arg.type == 2 ? self.Model.ListCollOther.LastId() : self.Model.ListColl.LastId();
            $.get('/PhotoCollection/ListCollection?checkPictureId=' + self.Model.PictureId() + '&query=' + query + '&type=' + arg.type + '&lastId=' + lastId + '&count=' + count, function (res) {
                if (res)
                    callFunction(fnc, res);

            }).error(function (res) {
                console.log(res);
            });
        }






        this.bindListCollection = function (arg, fnc) {

            arg = arg ? arg : { type: 1 };

            self.IsLoading(true);
            if (arg.reset == true)
                if (arg.type === 2) {
                    self.Model.ListCollOther.Reset();
                } else {
                    self.Model.ListColl.Reset();
                }
            listCollection(arg, function (res) {
                if (arg.type === 2) {
                    self.Model.ListCollOther.BindData(res);
                } else {
                    self.Model.ListColl.BindData(res);
                }

                self.IsLoading(false);
                setTimeout(function () {
                    bPopup.reposition(200);
                }, 200);
                callFunction(fnc);
            });
        }

        self.ItemsAfterRender = function () {

        };
        self.fnFilter = function (type) {

            if (type == 2)
                self.Model.Filter.NameOther($('#ppSavePhoto #pc-other-collections .dlgcf-title input[type="text"]').val());
            else
                self.Model.Filter.Name($('#ppSavePhoto #pc-my-collections .dlgcf-title input[type="text"]').val());

            if (self.fnFilter._timeout)
                clearTimeout(self.fnFilter._timeout);
            self.fnFilter._timeout = setTimeout(function () {
                self.bindListCollection({ type: type, reset: true });
            }, 500);

            return true;
        };
        self.fnCreateCollection = function () {
            if (!window.popupEditPhotoCollection) return;
            self.Close();
            window.popupEditPhotoCollection.Show({ Name: '', Description: '', IsPublic: true, IsContribute: true }, function (res) {

                self.IsLoading(true);

                res.PictureId = self.Model.PictureId();

                $.post('/PhotoCollection/CreateCollection', res, function (res1) {
                    if (res1 && res1.data) {
                        window.popupEditPhotoCollection.Close();
                    }
                    else if (res1.error) {
                        if (res1.error.code == 2) {
                            alert('Tên bộ sưu tập đã tồn tại');
                        }
                        self.IsLoading(false);
                    }
                    else {
                        alert('Có lỗi xảy ra trong quá trình xử lý.\r\nBạn vui lòng thử lại sau.');
                        self.IsLoading(false);
                    }

                }).error(function (res1) {
                    console.log(res1);
                    alert('Có lỗi xảy ra trong quá trình xử lý.\r\nBạn vui lòng thử lại sau.');
                    self.IsLoading(false);
                });
            }, function () {
                self.Show({ PictureId: self.Model.PictureId() }, fnCallBack);
            });
        };
        self.fnSavePhotoToggle = function (type, collection) {


            self.Model.Filter.Id(collection.Id);
            var iconState = collection.IconState(true);


            if (type == 2) {
                if (collection.IsChecked() == true) {
                    return;
                }
                self.IsLoading(true);
                $('#ppSavePhoto ul li [item-id="' + collection.Id + '"] i').attr('class', iconState);
                $.post('/PhotoCollection/AddPhotoContributeToggle', { pictureId: self.Model.PictureId(), collectionId: self.Model.Filter.Id() }, function (data) {
                    console.log(data);

                    if (data.success == true) {
                        self.Model.ListCollOther.SetCheckedItem(collection.Id, data.IsChecked);
                    } else {
                        console.log(data);
                    }
                    self.IsLoading(false);
                });

            } else {
                self.IsLoading(true);
                $('#ppSavePhoto ul li [item-id="' + collection.Id + '"] i').attr('class', iconState);
                $.post('/PhotoCollection/SavePhotoToggle', {
                    CollectionId: self.Model.Filter.Id(),
                    PictureId: self.Model.PictureId()
                }, function (res) {

                    if (res) {
                        self.Model.ListColl.SetCheckedItem(collection.Id, res.IsChecked);
                    }
                    self.IsLoading(false);
                }).error(function (res) {
                    console.log(res);
                    alert('Có lỗi xảy ra trong quá trình xử lý.\r\nBạn vui lòng thử lại sau.');
                    self.IsLoading(false);
                });
            }

        };
        self.Close = function () {
            bPopup.close();
        };
        self.Show = function (arg, callback) {
            fnCallBack = callback;
            self.Model.PictureId(arg.PictureId);
            self.Model.Filter.Name('');
            self._tabUi.Reset();

            if (arg.Reset == true) {
                self.Model.ListCollOther.Reset();
                self.Model.ListColl.Reset();
            }

            bPopup = $(selector).bPopup({
                zIndex: 10000,
                closeClass: 'dlgc-btn-close',
                modalClose: true,
                followSpeed: 0,
                onOpen: function () {
                    $('#ppSavePhoto .pc-nav-add-photo>ul>li a[href="#pc-my-collections"]').parent().click();
                    // self.bindListCollection({ type: 1, reset: true });

                },
                onClose: function () {
                }
            });
        }

        self.fnOK = function () {
            callFunction(fnCallBack, { Name: self.Model.Name(), Description: self.Model.Description() });
        };
        self.fnCancel = function () {
            self.Close();
        };

        self._tabUi = $('#ppSavePhoto .pc-nav-add-photo').custabs({
            onChanged: function (sender) {
                var target = $(sender).find('a').attr('href');
                if (target == '#pc-my-collections') {
                    self.bindListCollection({ type: 1, reset: true });
                } else {
                    self.bindListCollection({ type: 2, reset: true });
                }
                //console.log(target);
            }
        });

        function _autoLoadMoreOwner() {
            if ($('#pc-my-collections:visible').length < 1 || self.Model.ListColl.TotalRemaining() < 1) return;
            var sTop = $('.pc-list-collection:visible').scrollTop();
            var tHeight = $('#pc-my-collections').height();
            var tOffset = $('#pc-my-collections').offset();
            if (sTop + tOffset.top > tHeight) {
                self.Model.ListColl.fnLoadMore();
            }
        }
        function _autoLoadMoreSaved() {
            if ($('#pc-other-collections:visible').length < 1 || self.Model.ListCollOther.TotalRemain() < 1) return;
            var sTop = $('.pc-list-collection:visible').scrollTop();
            var tHeight = $('#pc-other-collections').height();
            var tOffset = $('#pc-other-collections').offset();
            if (sTop + tOffset.top > tHeight) {
                self.Model.ListCollOther.fnLoadMore();
            }
        }
        $('.pc-list-collection').scroll(function () {
            if (window._timeOut)
                clearTimeout(window._timeOut);
            window._timeOut = setTimeout(function () {
                _autoLoadMoreOwner();
                _autoLoadMoreSaved();
            }, 100);
        });
    };

    $(function () {
        window.popupSavePhoto = new PopupSavePhotoModel(window.dataLanguagesPc);

        ko.applyBindings(popupSavePhoto, document.getElementById('ppSavePhoto'));
    });
				</script>
				<style>



				</style>
				<div id="ppSavePhoto" class="fd-popup pc-popup pp-save-photo">
					<div class="fd-popup-frame">
						<div class="dlgc-btn-close"></div>
						<div class="dlgc-title">
							Lưu ảnh vào bộ sưu tập
							<span class="fa fa-photo" style="float:right;margin-top:15px;"></span>
						</div>
						<div class="dlgc-content-frame">

							<div class="dlgcf-content">
								<div class="pc-nav-add-photo">
									<ul>
										<li>
											<a href="#pc-my-collections">
												Bộ sưu tập
											</a>
										</li>
										<li>
											<a href="#pc-other-collections">
												Bộ sưu tập khác
											</a>
										</li>
									</ul>
									<div id="pc-my-collections" class="pc-nav-content" style="display: none;">
										<div class="dlgcf-title">
											<input type="text" data-bind="event: { keyup: fnFilter.bind(null,1) },value: Model.CollectionName,enable:IsEnabledCreateInput" placeholder="Tìm kiếm theo tên bộ sưu tập" />
											<span class="fa fa-search" style="position: absolute; left: 15px; top: 11px; color: #999;"></span>
										</div>
										<ul class="pc-list-collection pc-nav-content-scroll"
											data-bind="foreach:{data:Model.ListColl.Items , afterRender: ItemsAfterRender}">
											<li>
												<div
													data-bind="click:$root.fnSavePhotoToggle.bind($data,1), attr:{'item-id':Id,class:IsChecked()==true?'pc-checked':''}">
													<i data-bind="attr:{class:IconState()}" class="fa fa-circle"></i>
													<span class="pc-list-item-name" data-bind="html:Name"></span>
													<span class="pc-list-item-summary">
                                        <!-- ko text:TotalItems()-->
                                        <!-- /ko -->
                                        Hình ảnh
                                    </span>
												</div>
												<a class="custom-list-link" data-bind="attr:{href:Url}" target="_blank"
													href="javascript:void(0)">
												</a>
											</li>
										</ul>
										<div data-bind="visible:IsLoading" class="pc-nav-content-loading"></div>

									</div>
									<div id="pc-other-collections" class="pc-nav-content" style="display: none;">
										<div class="dlgcf-title">
											<input type="text" data-bind=" event: { keyup: fnFilter.bind(null,2) },value: Model.CollectionName,enable:IsEnabledCreateInput" placeholder="Tìm kiếm theo tên bộ sưu tập" />
											<span class="fa fa-search" style="position: absolute; left: 15px; top: 11px; color: #999;"></span>
										</div>
										<ul class="pc-list-collection pc-nav-content-scroll"
											data-bind="foreach:{data: Model.ListCollOther.Items , afterRender: ItemsAfterRender}">
											<li>
												<div
													data-bind="click:$root.fnSavePhotoToggle.bind($data,2), attr:{'item-id':Id,class:IsChecked()==true?'pc-checked':''}">
													<i data-bind="attr:{class:IconState()}" class="fa fa-circle"></i>
													<span class="pc-list-item-name" data-bind="html:Name"></span>
													<span class="pc-list-item-summary">
                                        <!-- ko text:TotalItems()-->
                                        <!-- /ko -->
                                        Hình ảnh
                                    </span>
												</div>
												<a class="custom-list-link" data-bind="attr:{href:Url}" target="_blank"
													href="javascript:void(0)">
												</a>
											</li>
										</ul>
										<div data-bind="visible:IsLoading" class="pc-nav-content-loading"></div>

									</div>
								</div>

							</div>
							<div class="dlgcf-buttons clearfix">
								<button data-bind="click:fnCreateCollection" class="dlgc-btn btn-ok">
                    + Tạo mới bộ sưu tập
                </button>

							</div>
						</div>
					</div>
				</div>
				<script>
					window.dataLanguagesPc = {
        BtnCollectionSaved: 'Đã lưu bộ sưu tập',
        BtnCollectionSave: 'Lưu bộ sưu tập',
        BtnShare: 'Chia sẻ',
        BtnLike: 'Thích',
        BtnUnLike: 'Bỏ thích',
        UpdatedOn: 'Cập nhật ngày',
        Views: 'Lượt xem',
        Photos: 'Hình ảnh',
        BtnViewMoreCollection: 'Xem thêm bộ sưu tập',
        BtnViewMorePhoto: 'Xem thêm hình ảnh',
        DlgPhotoTitleSave: 'Lưu ảnh vào bộ sưu tập',
        InputCollectionName: 'Tên bộ sưu tập',
        Description: 'Mô tả bộ sưu tập',
        BtnCollectionCreate: 'Tạo mới bộ sưu tập',
        BtnCreate: 'Tạo',
        BtnCreateNew: 'Tạo mới bộ sưu tập',
        BtnEdit: 'Chỉnh sửa',
        BtnDelete: 'Xoá',
        BtnPublic: 'Công khai (Public)',
        InputCollectionNameNew: 'Nhập tên bộ sưu tập mới',
        DlgCollectionTitleEdit: 'Chỉnh sửa bộ sưu tập',
        BtnCancel: 'Huỷ',
        BtnSave: 'Lưu',
        Saved: 'Lưu lại',
        Like: 'Thích',
        DlgCollectionTitleShare: 'Chia sẻ bộ sưu tập hình ảnh',
        DlgCollectionChooseMethodShare: 'Vui lòng chọn hình thức chia sẻ',
        MsgConfirmDeletePhoto: 'Bạn có chắc muốn xoá hình này?',
        MsgConfirmDeleteCollection: 'Bạn có chắc muốn xoá bộ sưu tập này?',
        MsgCollectionNameExist: 'Tên bộ sưu tập đã tồn tại',
        MsgAddPhotoSelectRequired: 'Vui lòng chọn hình ảnh của bạn để thêm vào bộ sưu tập này!',
        MsgActionFailure: 'Có lỗi xảy ra trong quá trình xử lý.\r\nBạn vui lòng thử lại sau.',
        FilterByName: 'Tìm kiếm theo tên bộ sưu tập'
    };
				</script>
				<script>
					var PopupEditCollectionModel = function (language) {
        var self = this;
        var callBack = null;
        var fnOnClose = null;
        var bPopup = null;
        self.lang = language;
        var selector = '#ppEditCollection';

        self.Model = {
            Name: ko.observable(''),
            Description: ko.observable(''),
            IsPublic: ko.observable('true'),
            IsContribute: ko.observable(true)
        };

        function callFunction(fnc, arg) {
            if (typeof fnc == 'function')
                fnc(arg);
        }

        self.Close = function () {
            bPopup.close();
            if (typeof fnOnClose == "function")
                fnOnClose();
        };
        self.Show = function (arg, callback, onClose) {
            callBack = callback;
            fnOnClose = onClose;
            if (arg) {
                self.Model.Name(arg.Name);
                self.Model.Description(arg.Description);
                self.Model.IsPublic(arg.IsPublic + '');
                self.Model.IsContribute(arg.IsContribute);
            } else {
                self.Model.Name('');
                self.Model.Description('');
                self.Model.IsPublic('true');
                self.Model.IsContribute(true);
            }


            bPopup = $(selector).bPopup({
                zIndex: 10001,
                closeClass: 'dlgc-btn-close',
                modalClose: false,
                followSpeed: 0,
                onOpen: function () {
                    // callFunction(callBack);
                }
            });
        }

        self.fnOK = function () {
            var name = self.Model.Name();
            if (name == null || name == '') {
                alert('Vui lòng nhập tên bộ sưu tập!');
                return;
            }
            callFunction(callBack, {
                Name: self.Model.Name(),
                Description: self.Model.Description(),
                IsPublic: self.Model.IsPublic() == 'true' ? true : false,
                IsContribute: self.Model.IsContribute()
            });
        };
        self.fnCancel = function () {
            self.Close();
        };

        $('#ppEditCollection input[name="pc-setting-is-public"]').on('change', function () {
            if ($('#pc_ckb_isPublic').is(':checked'))
                self.Model.IsContribute(true);
        });
    };

    $(function () {
        window.popupEditPhotoCollection = new PopupEditCollectionModel(window.dataLanguagesPc);

        ko.applyBindings(popupEditPhotoCollection, document.getElementById('ppEditCollection'));
    });
				</script>

				<div id="ppEditCollection" class="fd-popup pc-popup">
					<div class="fd-popup-frame">
						<div class="dlgc-btn-close" data-bind="click:fnCancel"></div>
						<div class="dlgc-title">
							<span data-bind="text:lang.DlgCollectionTitleEdit"></span>
							<span style="float:right;margin-top:15px;" class="fa fa-photo"></span>
						</div>
						<div class="dlgc-content-frame">

							<div class="dlgcf-content">
								<div>
									<input style="padding-left: 15px;" type="text" data-bind="value: Model.Name,attr:{placeholder:lang.InputCollectionName}" placeholder="Tên bộ sưu tập" />
                </div>
									<div style="margin-top:-1px;">
										<textarea rows="6" style="padding-left: 15px;" placeholder="mô tả bộ sưu tập" data-bind="value: Model.Description,attr:{placeholder:lang.Description}"></textarea>
									</div>
									<div style="padding:5px 15px 20px 15px;">
										<div
											style="color: #888; padding: 0 0 5px 0; text-transform: uppercase; font-size: 11px;">
											Cấu hình bộ sưu tập
										</div>
										<ul class="dlcf-btns-radio">
											<li>
												<input data-bind="checked:Model.IsPublic" type="radio" value="false" id="pc_ckb_isPrivate" name="pc-setting-is-public" />
												<label for="pc_ckb_isPrivate">Chỉ mình tôi (Private)</label>
											</li>
											<li>
												<input data-bind="checked:Model.IsPublic" type="radio" value="true" id="pc_ckb_isPublic" name="pc-setting-is-public" />
												<label for="pc_ckb_isPublic">Công khai (Public)</label>
												<ul class="fd-p-checkbox" data-bind="visible:Model.IsPublic()=='true'">
													<li>
														<input data-bind="checked:Model.IsContribute" type="checkbox" id="ckb-ppeditc-ispublic" />
														<label for="ckb-ppeditc-ispublic">Cho phép thành viên khác gợi ý thêm hình ảnh</label>
													</li>
												</ul>
											</li>
										</ul>


									</div>
								</div>
								<div class="dlgcf-buttons clearfix">
									<button data-bind="click:fnOK,text:lang.BtnSave" class="dlgc-btn btn-ok">Lưu</button>

								</div>
							</div>
						</div>
					</div>
					<script>
						var PopupEditListModel = function (language) {
        var self = this;
        var fncallBack = null;
        var fnOnClose = null;
        var bPopup = null;
        self.lang = language;
        var selector = '#ppEditList';

        self.Model = {
            Id: ko.observable(null),
            Title: ko.observable(''),
            Description: ko.observable(''),
            IsPublic: ko.observable('true'),
            IsContribute: ko.observable('true'),
            RestaurantId: ko.observable(null)
        };

        function callFunction(fnc, arg) {
            if (typeof fnc == 'function')
                fnc(arg);
        }

        function fnReset() {
            self.Model.Title('');
            self.Model.Description('');
            self.Model.IsPublic('true');
            self.Model.IsContribute('true');
            
            fnUpdateUi();
        }

        function fnGetData(fnc) {
            var t = new Date().getTime();
            var listId = self.Model.Id()*1;
            if (!(listId > 0)) {
                //callFunction(fnc);
                return;
            }
            $.get('/__get/List/GetList?listId=' + listId
                + '&t=' + t, function (res) {

                    if (!res) {
                        alert(self.lang.MsgActionFailure);
                        return;
                    }
                    if (res.error) {
                        if (res.error.code == 3) {
                            alert('Tên bộ sưu tập đã tồn tại');
                            return;
                        }

                        alert(self.lang.MsgActionFailure);
                        return;
                    }

                    callFunction(fnc, res);

                }).error(function (res) {
                    alert(self.lang.MsgActionFailure);
                    console.log(res);
                });
        }

        function fnSaveData(data, fnc) {
            if (data.Description == null)
                data.Description = '';
            data.Title = encodeURI(data.Title);
            data.Description = encodeURI(data.Description);
            $.post('/__post/List/SaveList', data, function (res) {

                if (!res) {
                    alert(self.lang.MsgActionFailure);
                    return;
                }
                if (res.error) {
                    if (res.error.msg)
                        alert(res.error.msg);
                    else
                        alert(self.lang.MsgActionFailure);
                    return;
                }

                callFunction(fnc, res);

            }).error(function (res) {
                alert(self.lang.MsgActionFailure);
                console.log(res);
            });
        }

        function fnShow() {

            fnGetData(function (res) {
                self.Model.Title(res.Title);
                self.Model.Description(res.Description);
                self.Model.IsPublic(res.IsPublic + '');
                self.Model.IsContribute(res.IsContribute);
                fnUpdateUi();
            });
        }


        self.Close = function () {
            bPopup.close();
            if (typeof fnOnClose == "function")
                fnOnClose();
        };
        self.IsEdit = ko.computed(function () {
            return self.Model.Id() > 0;
        });

        self.Show = function (arg, callback, onClose) {
            fncallBack = callback;
            fnOnClose = onClose;
        
           
           
            fnReset();
            self.Model.Id(arg.Id);
            self.Model.RestaurantId(arg.RestaurantId);


            bPopup = $(selector).bPopup({
                zIndex: 10001,
                closeClass: 'dlgc-btn-close',
                modalClose: false,
                onOpen: function () {
                    fnShow();
                }

            });
        }

        self.fnOK = function () {
            var name = self.Model.Title();
            if (name == null || name == '') {
                alert('Vui lòng nhập tên bộ sưu tập!');
                return;
            }
            fnSaveData({
                Id: self.Model.Id(),
                Title: self.Model.Title(),
                Description: self.Model.Description(),
                IsPublic: self.Model.IsPublic() == 'true' ? true : false,
                IsContribute: self.Model.IsContribute(),
                RestaurantId: self.Model.RestaurantId()
            },
                function (res) {
                    callFunction(fncallBack, res);
                });
        };
        self.fnCancel = function () {
            self.Close();
        };

        function fnUpdateUi() {
            if ($('#lc_ckb_isPublic').is(':checked')) {
                $('#ppEditList .fd-p-checkbox').slideDown();
                self.Model.IsPublic('true');
            } else {
                //$('#ppEditList .fd-p-checkbox').slideUp();
                self.Model.IsPublic('false');
            }
        }
        $('#ppEditList input[name="lc-setting-is-public"]').on('change', function () {
            fnUpdateUi();
        });
    };

    $(function () {
        window.popupEditList = new PopupEditListModel(window.dataLanguagesPc);

        ko.applyBindings(popupEditList, document.getElementById('ppEditList'));
    });
					</script>

					<div id="ppEditList" class="fd-popup pc-popup">
						<div class="fd-popup-frame">
							<div class="dlgc-btn-close" data-bind="click:fnCancel"></div>
							<div class="dlgc-title">
								<!-- ko if: IsEdit -->
								<span>Cập nhật bộ sưu tập của bạn</span>
								<!-- /ko -->
								<!-- ko ifnot: IsEdit -->
								<span>Tạo bộ sưu tập mới</span>
								<!-- /ko -->
								<span style="float: right; margin-top: 15px;" class="fa fa-map-marker"></span>
							</div>
							<div class="dlgc-content-frame">

								<div class="dlgcf-content">
									<div>
										<input style="padding-left: 15px;" type="text" data-bind="value: Model.Title,attr:{placeholder:lang.InputCollectionName}" placeholder="Tên bộ sưu tập" />
                </div>
										<div style="margin-top:-1px;">
											<textarea rows="6" style="padding-left: 15px;" placeholder="mô tả bộ sưu tập" data-bind="value: Model.Description,attr:{placeholder:lang.Description}"></textarea>
										</div>
										<div style="padding:5px 15px 0 15px;">
											<div
												style="color: #888; padding: 0 0 5px 0; text-transform: uppercase; font-size: 11px;">
												Cấu hình bộ sưu tập
											</div>
											<ul class="dlcf-btns-radio">
												<li>
													<input data-bind="checked:Model.IsPublic" type="radio" value="false" id="lc_ckb_isPrivate" name="lc-setting-is-public" />
													<label for="lc_ckb_isPrivate">Chỉ mình tôi (Private)</label>
												</li>
												<li>
													<input data-bind="checked:Model.IsPublic" type="radio" value="true" id="lc_ckb_isPublic" name="lc-setting-is-public" />
													<label for="lc_ckb_isPublic">Công khai (Public)</label>
													<ul class="fd-p-checkbox">
														<li>
															<input data-bind="checked:Model.IsContribute" type="checkbox" id="ckb-ppeditl-ispublic" checked="checked" />
															<label for="ckb-ppeditl-ispublic">Cho phép thành viên khác gợi ý thêm địa điểm</label>
														</li>
													</ul>
												</li>
											</ul>
										</div>
									</div>
									<div class="dlgcf-buttons clearfix">
										<button data-bind="click:fnOK,text:lang.BtnSave" class="dlgc-btn btn-ok">Cập nhật bộ sưu tập</button>
									</div>
								</div>
							</div>
						</div>

						<div id="popupContaner">
							<div id="restaurant-reviews-popup" style="height: 500px; display: none;"></div>
							<div id="foodyBoxContainer"></div>
							<div id="facebookFriendsPopupContainer"></div>
							<div id="user-like-popup"></div>
							<div id="foody-login-box-cotaner"></div>
							<div id="p-micro-ecard" style="display:none;"></div>
							<div id="p-micro-bank-card" style="display:none;"></div>
						</div>






						<div class="fd-back-top" style="display:none;">
							<ul>
								<li id="btn-back-top">
									<a href="javascript:void(0)">
										<i class="fa fa-angle-up"></i>
										<label>Về đầu trang</label>
									</a>
								</li>
								<li>
									<a href="https://itunes.apple.com/app/id570435154" target="_blank"
										onclick="ga('ads.send', 'event', 'Button Download', 'Click', 'iOS');">
										<i class="fa fa-apple"></i>
										<label>Tải ứng dụng</label>
									</a>
								</li>
								<li>
									<a href="https://play.google.com/store/apps/details?id=com.foody.vn.activity"
										target="_blank"
										onclick="ga('ads.send', 'event', 'Button Download', 'Click', 'Android');">
										<i class="fa fa-android"></i>
										<label>Tải ứng dụng</label>
									</a>
								</li>
							</ul>
						</div>



						<script src="/scripts/public.search.min.js?6b6fe8" type="text/javascript"></script>
						<script>
							//<!-- Cài đặt mã Remarketing -->
        var dataLayer = window.dataLayer || [];
        dataLayer.push({
            'event': 'dynamic_remarketing',
            'dynx_itemid':'',
            'dynx_pagetype' : 'searchresults',
            'dynx_totalvalue' : 0
        });
        $(function () {
            $('#pkeywords').val(model.keyword());
            //$('#directory-search-resulttab').fixedAds({
            //    top: 50
            //});
            //$('#directory-banner-container').fixedAds({
            //    top: 50,
            //    //edgeSelector: ".footer-down-app-wrap"
            //});
        })
						</script>



</body>

</html>"""
b = c

b = str(b.strip())
print(len(b))


c = b.split('var jsonData = ')

d = c[1]

d = d.split('var jsonDataSearch')
a1 = d[0].strip()[:-1]
# print(a1)

print(len(a1))
print(len(a))


data = json.loads(a1)
print(data['districts'])
