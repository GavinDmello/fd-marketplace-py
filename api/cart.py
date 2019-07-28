from auth import Auth
from outbound import Outbound

class Cart(object):
	def __init__(self):
		self.url = Auth.url
		self.headers = Auth.get_headers()

	'''
	This endpoint can be used for validation of the items in the Shopping Cart, 
	such as products or product types required to be bought together, etc.
	API version 1
	'''
	def validate_v1(self, data):
		endpoint = self.url + "/marketplace/v1/cart/validate"
		return Outbound.make_post_request(endpoint, data, self.headers)
		

	'''
	This endpoint can be used for validation of the items in the Shopping Cart, 
	such as products or product types required to be bought together, etc.
	API version 2
	'''
	def validate_v2(self, data):
		endpoint = self.url + "/marketplace/v2/cart/validate"
		return Outbound.make_post_request(endpoint, data, self.headers)
