from auth import Auth
from outbound import Outbound

class Pricing(object):
	def __init__(self):
		self.url = Auth.url
		self.headers = Auth.get_headers()

	'''
	This endpoint can be used to retrieve “pricing” 
	for any given product (or collection of products) 
	such as the product’s own pricing, pricing for products included, 
	and any associated fees - each considered a “Pricing Product.”
	'''
	def post_pricing_equipment_v1(self, data):
		endpoint = self.url + "/marketplace/v1/pricing/equipment"

		return Outbound.make_post_request(endpoint, data, self.headers)

	'''
	This endpoint can be used to retrieve “pricing” 
	for any given product (or collection of products) 
	such as the product’s own pricing, pricing for products included, 
	and any associated fees - each considered a “Pricing Product.”
	'''
	def post_pricing_equipment_v2(self, data):
		endpoint = self.url + "/marketplace/v2/pricing/equipment"

		return Outbound.make_post_request(endpoint, data, self.headers)

	'''
	The POST Pricing/Acquiring API can be used to retrieve “pricing” for the credit card 
	processing transaction fees and rates as well as any associated flat charges - each considered a “Pricing Product.”
	'''
	def post_pricing_aquiring_v1(self, data):
		endpoint = self.url + "/marketplace/v1/pricing/acquiring"

		return Outbound.make_post_request(endpoint, data, self.headers)


	'''
	The POST Pricing/Acquiring API can be used to retrieve “pricing” for the credit card 
	processing transaction fees and rates as well as any associated flat charges - each considered a “Pricing Product.”
	'''
	def post_pricing_aquiring_v2(self, data):
		endpoint = self.url + "/marketplace/v2/pricing/acquiring"

		return Outbound.make_post_request(endpoint, data, self.headers)


	'''
	The POST Pricing/Equipment API can be used to retrieve “pricing” that applies to every merchant 
	regardless of equipment purchased or qualifying criteria - 
	each object returned is considered a “Pricing Product.”
	'''
	def post_pricing_global(self, data):
		endpoint = self.url + "/marketplace/v1/pricing/global"

		return Outbound.make_post_request(endpoint, data, self.headers)