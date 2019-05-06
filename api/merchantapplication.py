from auth import Auth
from outbound import Outbound

class MerchantApplication(object):
	def __init__(self):
		self.url = Auth.url
		self.headers = Auth.get_headers()

	'''
	The API allows the developer to submit merchant application & credit decision. 
	This is an enhanced API to combine 2 APIs credit decision and single outlet.
	'''
	def post_merchant_app_single_outlet(self, data):
		endpoint = self.url + "/marketplace/v1/merchantapplication/singleoutletwithcreditdecision"

		return Outbound.make_post_request(endpoint, data, self.headers)


	'''
	This endpoint allows developers to create a request for credit decision 
	without submitting the complete order details.
	The service is set up to request the minimum required information a credit decision. 
	'''
	def post_merchant_app_credit_decision(self, data):
		endpoint = self.url + "/marketplace/v1/merchantapplication/creditdecision"

		return Outbound.make_post_request(endpoint, data, self.headers)



	'''
	Single outlet API which takes in an orderId
	'''
	def post_merchant_app_single_outlet_for_id(self, order_id, data):
		endpoint = self.url + "/marketplace/v1/merchantapplication/{}/singleoutlet"
		endpoint = endpoint.format(order_id)
		return Outbound.make_post_request(endpoint, data, self.headers)