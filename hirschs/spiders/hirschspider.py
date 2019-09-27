# -*- coding: utf-8 -*-
import scrapy
from .helpers.html_parsers import hirsch
from .helpers import file_handler

## limts == all - for viewing all items at once...
class HirschspiderSpider(scrapy.Spider):



    name = "hirschspider"

    custom_settings = {
        'FEED_URI': file_handler.allocate_output_path(spider_name=name),
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
    }

    allowed_domains = ["hirschs.co.za"]
    start_url = 'https://www.hirschs.co.za' # - should scrape all categories and sub categories from here
    	
    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse_main_page)

    def parse_main_page(self, response):

    	parser = hirsch.MainPage(response)

    	category_names, category_urls = parser.get_category_urls()

    	# yield {"cat_urls": category_urls}

    	for i,category_url in enumerate(category_urls):
    		request = scrapy.Request(url=category_url, callback = self.parse_category_page, cb_kwargs={'category': category_names[i]})
    		yield request


    	# sub_category_urls, sub_categories = parser.get_sub_category_urls()

    	# for  i,sub_category_url in enumerate(sub_category_urls):
    	# 	yield {"sub_cat_url":sub_category_url}
    	# 	request = scrapy.Request(url=sub_category_url, callback = self.parse_listings_page, cb_kwargs={'sub_category': sub_categories[i]})
    	# 	yield request

    def parse_category_page(self, response, category):
    	parser = hirsch.MainPage(response)

    	sub_category_urls, sub_categories = parser.get_sub_category_urls()

    	for  i,sub_category_url in enumerate(sub_category_urls):
    		yield {"sub_cat_url - debugging ignore me...":sub_category_url}
    		#append limit=all to url to display all listings - no point for testing too slow - switch comments to run full scrape
    		# request = scrapy.Request(url=sub_category_url+'?limit=all', callback = self.parse_listings_page, cb_kwargs={'category': category,'sub_category': sub_categories[i]})
    		request = scrapy.Request(url=sub_category_url, callback = self.parse_listings_page, cb_kwargs={'category': category,'sub_category': sub_categories[i]})
    		yield request


    def parse_listings_page(self, response, category, sub_category):

    	parser = hirsch.ListingsPage(response)
    	item_urls = parser.get_item_urls()

    	for item_url in item_urls:
	    	# yield scrapy.Request(url=item_url+'?limit=all', callback = self.parse_item_page, cb_kwargs={'category': category, 'sub_category':sub_category})
	    	yield scrapy.Request(url=item_url, callback = self.parse_item_page, cb_kwargs={'category': category, 'sub_category':sub_category})


    def parse_item_page(self, response,category, sub_category):
    	parser = hirsch.ItemPage(response)

    	name = parser.get_name()
    	item_data_table = parser.get_data_table()
    	image_url = parser.get_image_url()
    	price = parser.get_price()
    	description = parser.get_description()
    	
    	item = {
    		'brand': item_data_table['Brand'],
    		'name': name,
    		'url': response.url,
    		'image_url': image_url,
    		'SKU': item_data_table['SKU'],
    		'Categories': [category, sub_category],
    		'Description': description,
    		'price': price
    	}

    	yield item

       
