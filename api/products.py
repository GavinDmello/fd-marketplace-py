import requests
from auth import Auth

class Products(object):
	def __init__(self):
		
		if Auth.username == None or Auth.secret == None :
			raise "Credentials not set"

		self.url = Auth.url
		self.headers = Auth.get_headers()


	'''
	Retrieves a list of products for your Marketplace.
	'''
	def get_products(self):
		endpoint = self.url + "/marketplace/v1/products"	
		return self.make_get_request(endpoint, self.headers)

	def get_product_details(self, product_id):
		if product_id == None:
			raise "product_id is not provided"

		endpoint = self.url + "/marketplace/v1/products/{}/details"
		endpoint = endpoint.format(product_id)
		return self.make_get_request(endpoint, self.headers)

	def get_product_features(self, product_id):
		if product_id == None:
			raise "product_id is not provided"

		endpoint = self.url + "/marketplace/v1/products/{}/features"
		endpoint = endpoint.format(product_id)
		return self.make_get_request(endpoint, self.headers)

	def get_product_includes(self, product_id):
		if product_id == None:
			raise "product_id not provided"

		endpoint = self.url + "/marketplace/v1/products/{}/includes"
		endpoint = endpoint.format(product_id)
		return self.make_get_request(endpoint, self.headers)

	def get_product_specs(self, product_id):
		if product_id == None:
			raise "product_id not provided"
		
		endpoint = self.url + "/marketplace/v1/products/{}/specs"
		endpoint = endpoint.format(product_id)
		return self.make_get_request(endpoint, self.headers)

	def get_product_recommended(self, product_id):
		if product_id == None:
			raise "product_id not provided"
		
		endpoint = self.url + "/marketplace/v1/products/{}/recommended"
		endpoint = endpoint.format(product_id)
		return self.make_get_request(endpoint, self.headers)

	def get_product_faq(self, product_id):
		if product_id == None:
			raise "product_id not provided"
		
		endpoint = self.url + "/marketplace/v1/products/{}/faq"
		endpoint = endpoint.format(product_id)
		return self.make_get_request(endpoint, self.headers)

	def make_get_request(self, endpoint, headers):
		r = requests.get(endpoint, headers=headers)
		return r.content