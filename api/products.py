import requests
from auth import Auth

class Products(object):
	def __init__(self):
		self.url = Auth.url
		self.headers = Auth.get_headers()

	'''
	Retrieves a list of products for your Marketplace.
	'''
	def get_products(self):
		endpoint = self.url + "/marketplace/v1/products"	
		return self.make_get_request(endpoint, self.headers)

	'''
	Retrieves the product details for any given product.
	'''
	def get_product_details(self, product_id):
		if product_id == None:
			raise "product_id is not provided"

		endpoint = self.url + "/marketplace/v1/products/{}/details"
		endpoint = endpoint.format(product_id)
		return self.make_get_request(endpoint, self.headers)

	'''
	Retrieves a list of features for any given product.
	'''
	def get_product_features(self, product_id):
		if product_id == None:
			raise "product_id is not provided"

		endpoint = self.url + "/marketplace/v1/products/{}/features"
		endpoint = endpoint.format(product_id)
		return self.make_get_request(endpoint, self.headers)

	'''
	Retrieves a list of “included products” that come with any given product.
	This may include things such as built-in hardware and accessories and/or 
	software that comes with it.
	'''
	def get_product_includes(self, product_id):
		if product_id == None:
			raise "product_id not provided"

		endpoint = self.url + "/marketplace/v1/products/{}/includes"
		endpoint = endpoint.format(product_id)
		return self.make_get_request(endpoint, self.headers)

	'''
	Retrieves a list of technical specifications for any given product. 
	This may include information such as height and weight as well as the 
	materials the product is made of in the case of a hardware type product.
	'''
	def get_product_specs(self, product_id):
		if product_id == None:
			raise "product_id not provided"
		
		endpoint = self.url + "/marketplace/v1/products/{}/specs"
		endpoint = endpoint.format(product_id)
		return self.make_get_request(endpoint, self.headers)

	'''
	Retrieves all Recommended Products for any given product. 
	For example, a terminal system may have items like a weight scale 
	and kitchen printer as its Recommended Products.
	'''
	def get_product_recommended(self, product_id):
		if product_id == None:
			raise "product_id not provided"
		
		endpoint = self.url + "/marketplace/v1/products/{}/recommended"
		endpoint = endpoint.format(product_id)
		return self.make_get_request(endpoint, self.headers)

	'''
	Retrieves a list of frequently asked questions for any given product.
	'''
	def get_product_faq(self, product_id):
		if product_id == None:
			raise "product_id not provided"
		
		endpoint = self.url + "/marketplace/v1/products/{}/faq"
		endpoint = endpoint.format(product_id)
		return self.make_get_request(endpoint, self.headers)

	def make_get_request(self, endpoint, headers):
		r = requests.get(endpoint, headers=headers)
		if r.status_code == 200:
			return r.content
		else:
			raise Exception("Exception, API returned " + str(r.status_code))