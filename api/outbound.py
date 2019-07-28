import requests

class Outbound(object):
	
	@staticmethod
	def make_get_request(endpoint, headers):
		r = requests.get(endpoint, headers=headers)
		if r.status_code == 200:
			return r.content
		else:
			raise Exception("Exception, API returned " + str(r.status_code))


	@staticmethod
	def make_post_request(url, data, headers):
		r = requests.post(url, json=data, headers=headers)
		if r.status_code == 200:
			return r.content
		else:
			raise Exception("Exception, API returned " + str(r.status_code))
