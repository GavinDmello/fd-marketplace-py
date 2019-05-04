import requests
from auth import Auth

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
		return self.make_post_request(endpoint, data, self.headers)
		

	'''
	This endpoint can be used for validation of the items in the Shopping Cart, 
	such as products or product types required to be bought together, etc.
	API version 2
	'''
	def validate_v2(self):
		endpoint = "/marketplace/v2/cart/validate"
		return self.make_post_request(endpoint, data, self.headers)


	def make_post_request(self, url, data, headers):
		r = requests.post(url, json=data, headers=headers)
		if r.status_code == 200:
			return r.content
		else:
			raise Exception("Exception, API returned " + str(r.status_code))
