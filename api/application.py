from auth import Auth
from outbound import Outbound

class Application(object):
	def __init__(self):
		self.url = Auth.url
		self.headers = Auth.get_headers()

	'''
	This endpoint retrieves all information for the Merchant Agreement 
	that you can display to the applicant for their final “signature.”
	'''
	def get_contract_agreement(self, order_id):
		endpoint = self.url + "marketplace/v1/contracts/{}/agreement"
		endpoint = endpoint.format(order_id)
		return Outbound.make_get_request(endpoint, self.headers)

	'''
	This endpoint submits the Merchant Application. 
	It takes a document in Base64 format and uploads it to First Data as the “Merchant Agreement” for a specific orderId.
	This is the last step in the Merchant Application process as it submits all order data necessary for 
	First Data to determine the merchant’s eligibility for payment processing.
	'''
	def post_contract_document(self, data):
		endpoint = self.url + "/marketplace/v1/application/contractdocument"

		return Outbound.make_post_request(endpoint, data, self.headers)


	'''
	This endpoint allows us to validate merchant information and product data and submit an order at the same time. 
	It serves as a combination of POST Application/Checkout and POST Application/Update, 
	intended to be used in certain cases.
	'''
	def post_application_signup_info(self, data):
		endpoint = self.url + "/marketplace/v1/application/signup"

		return Outbound.make_post_request(endpoint, data, self.headers)

	'''
	This endpoint submits the Merchant Application form.
	'''
	def post_application_update(self, data):
		endpoint = self.url + "/marketplace/v1/application/update"

		return Outbound.make_post_request(endpoint, data, self.headers)

	'''
	This endpoint can be used to verify the abaNumber entered in the ACH information section 
	(contactsInformation) of the Merchant Application form before submission. 
	For every successful match this endpoint also retrieves additional information about the matched bank.
	'''
	def post_bank_validation_request(self, data):
		endpoint = self.url + "/marketplace/v1/banks/validate"

		return Outbound.make_post_request(endpoint, data, self.headers)

