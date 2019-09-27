# # # -*- coding: utf-8 -*-
# import scrapy
# from .helpers.html_parsers import hirsch

# ## limts == all - for viewing all items at once...
# class HirschspiderSpider(scrapy.Spider):
#     name = "hirschspider"
#     allowed_domains = ["hirschs.co.za"]
#     start_url = 'https://www.hirschs.co.za/tv-audio'
    	
#     def start_requests(self):
#         yield scrapy.Request(url=self.start_url, callback=self.parse_main_page)

#     def parse_main_page(self, response):

#     	parser = hirsch.MainPage(response)
#     	sub_category_urls, sub_categories = parser.get_sub_category_urls()

#     	for  i,sub_category_url in enumerate(sub_category_urls):
#     		yield {"sub_cat_url":sub_category_url}
#     		request = scrapy.Request(url=sub_category_url, callback = self.parse_sub_category_page, cb_kwargs={'sub_category': sub_categories})
#     		yield request

#     def parse_sub_category_page(self, response, sub_category):
#     	parser = hirsch.MainPage(response)
#     	sub_category_urls, sub_categories = parser.get_sub_category_urls()
#     	if len(sub_category_urls)==0:
#     		yield {"ON LIST":response.url}
#     	else:
#     		for  i,sub_category_url in enumerate(sub_category_urls):
# 	    		yield {"sub_cat_url":sub_category_url}
# 	    		request = scrapy.Request(url=sub_category_url, callback = self.parse_sub_category_page, cb_kwargs={'sub_category': sub_categories})
# 	    		yield request

#     	# if len(sub_category_urls)==0:
#     		# yield "ON LISTING PAGE"
#     	# else:
# 	    	# for  i,sub_category_url in enumerate(sub_category_urls):
# 	    		# yield {"sub_cat_url":sub_category_url}
        

#     def parse_listings_page(self, response, sub_category):

#     	parser = hirsch.ListingsPage(response)
#     	item_urls = parser.get_item_urls()

#     	for item_url in item_urls:
# 	    	yield scrapy.Request(url=item_url, callback = self.parse_item_page, cb_kwargs={'sub_category':sub_category})


#     def parse_item_page(self, response, sub_category):
#     	parser = hirsch.ItemPage(response)

#     	name = parser.get_name()
#     	# item_data_table = parser.get_data_table() #on item p
#     	# image_url = parser.get_image_url()
#     	# price = parser.get_price()
#     	# description = parser.get_description()
    	
#     	# item = {
#     	# 	'brand': item_data_table['Brand'],
#     	# 	'name': name,
#     	# 	'url': response.url,
#     	# 	'image_url': image_url,
#     	# 	'SKU': item_data_table['SKU'],
#     	# 	'Categories': ["TV", sub_category],
#     	# 	'Description': description,
#     	# 	'price': price
#     	# }

#     	yield {"name": name}

       
