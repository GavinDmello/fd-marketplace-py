import requests
from auth import Auth
from outbound import Outbound

class Industry(object):
	def __init__(self):
		self.url = Auth.url
		self.headers = Auth.get_headers()

	'''
	This endpoint retrieves the broad industry description (industryDescription) 
	labels for a given business category. Result values returned by this endpoint 
	can be used in the request of the GET MCC/Industry endpoint.
	'''
	def get_industry(self, category_name):
		endpoint = url + "/marketplace/v1/categories/{}/industries"
		endpoint = endpoint.format(category_name)

		return Outbound.make_get_request(endpoint, self.headers)

	'''
	This endpoint retrieves the MCC - Merchant Category Code(s) - for a given industry.

	'''
	def get_mcc_indusrty(self, category_name, industry_description):
		endpoint = url + "/marketplace/v1/categories/{}/industries/{}/merchantcategorycodes"
		endpoint = endpoint.format(category_name, industry_description)

		return Outbound.make_get_request(endpoint, self.headers)

	def make_get_request(self, url, headers):
		r = requests.get(url, headers=headers)
		if r.status_code == 200:
			return r.content
		else:
			raise Exception("Exception, API returned " + str(r.status_code))
