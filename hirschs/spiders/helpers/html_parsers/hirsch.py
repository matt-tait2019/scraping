import re
from .page import Page
import logging

class MainPage(Page):

	def get_category_urls(self):
		return self.body.xpath('//li[contains(@class, "menu-full-width")]/a/text()').extract(), self.body.xpath('//li[contains(@class, "menu-full-width")]/a/@href').extract()

	def get_sub_category_urls(self):
		return self.body.xpath('//ul[contains(@class, "category-list")]/li/a/@href').extract(), self.body.xpath('//ul[contains(@class, "category-list")]/li/a/text()').extract()

class ListingsPage(Page):

	def get_item_urls(self):
		return self.body.xpath('//div[contains(@class, "product-image-area")]/@product_url').extract()

class ItemPage(Page):

	def get_data_table(self):
		data_table_headers = self.body.xpath('//table[contains(@class, "data-table")]//th/text()').extract()
		data_table_columns = self.body.xpath('//table[contains(@class, "data-table")]//td/text()').extract()
		data_table_dictionary = dict(zip(data_table_headers, data_table_columns))
		return data_table_dictionary

	def get_name(self):
		name = self.body.xpath('//meta[@name=\'keywords\']/@content')[0].extract()
		return name

	def get_image_url(self):
		image_url = self.body.xpath('//img[contains(@class, "etalage_thumb_image")]/@src')[0].extract()
		return image_url 

	def get_price(self):
		price = self.body.xpath('//span[@class="price"]/text()')[0].extract().replace('\n', '')
		return price

	#todo render descriptions properly
	#some descriptions are technical and some aren't
	#some slightly more involved method needed
	def get_description(self):
		description = self.body.xpath('//div[contains(@id, "tab_description_tabbed_contents")]/div[contains(@class, "std")]/p').extract()
		return ""