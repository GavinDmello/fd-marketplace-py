from auth import Auth
from outbound import Outbound

class MerchantOrders(object):
	def __init__(self):
		self.url = Auth.url
		self.headers = Auth.get_headers()

	'''
	This endpoint retrieves a unique orderId once the shopping cart checkout process is completed. 
	This numeric identifier is then used in the merchant boarding process as input to reference the order.
	It is used for purposes of collecting information about shipping the product(s) to the merchant after the merchant boarding process is completed and approved.
	'''
	def post_merchant_orders_v1(self, orders):
		endpoint = self.url + "/marketplace/v1/merchantorders"
		return Outbound.make_post_request(endpoint, orders, self.headers)

	'''
	This endpoint collects merchant and owner information for merchant boarding purposes.
	'''
	def post_merchant_business_info(self, order_id, orders):
		endpoint = self.url +"/marketplace/v1/merchantorders/{}/businessinformation"
		endpoint = endpoint.format(order_id)
 		return Outbound.make_post_request(endpoint, orders, self.headers)


 	'''
	This endpoint collects information about each location of the business for merchant boarding purposes.
 	'''
 	def post_merchant_locations(self, order_id, orders):
 		endpoint = self.url + "/marketplace/v1/merchantorders/{}/locations"
 		endpoint = endpoint.format(order_id)
 		return Outbound.make_post_request(endpoint, orders, self.headers)

 	'''
	This endpoint collects advanced setup and account preferences for the merchant order.
 	'''
 	def post_merchant_locations(self, order_id, orders):
 		endpoint = self.url + "/marketplace/v1/merchantorders/{}/accountpreferences"
 		endpoint = endpoint.format(order_id)
 		return Outbound.make_post_request(endpoint, orders, self.headers)

 	'''
	This endpoint retrieves information about the status of the order based on its unique identifier. 
	Depending on the status it also provides additional details, such as shipment tracking and merchant identifiers.
 	'''
 	def get_order_status_v1(self, order_id):
 		endpoint = self.url + "/marketplace/v1/merchantorders/{}/status"
 		endpoint = endpoint.format(order_id)
 		return Outbound.make_get_request(endpoint, self.headers)