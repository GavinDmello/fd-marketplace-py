from auth import Auth
from outbound import Outbound

class Identity(object):
	def __init__(self):
		self.url = Auth.url
		self.headers = Auth.get_headers()

	'''
	This endpoint returns the multiple-choice questions and the list of possible answers for each of them. 
	These can be presented to the user to verify their identity. 
	The user’s answers are then submitted using the POST Identity/Answers endpoint.
	'''
	def post_identity_questions(self, data):
		endpoint = self.url + "/marketplace/v1/identity/questions"

		return Outbound.make_post_request(endpoint, data, self.headers)


	'''
	This endpoint returns the results of the identity verification.
	It uses the input from the user as they answer the questions presented to them 
	from the POST Identity/Questions endpoint.
	'''
	def post_identity_answers(self, data):
		endpoint = self.url + "/marketplace/v1/identity/answers"

		return Outbound.make_post_request(endpoint, data, self.headers)

	'''
	This endpoint returns a list of multiple-choice questions and the list of possible answers for each of them. 
	These can be presented to the user to verify their identity.
	'''
	def post_merchant_identity_questions(self, data):
		endpoint = self.url + "/marketplace/v1/merchant/identity/questions"

		return Outbound.make_post_request(endpoint, data, self.headers)
