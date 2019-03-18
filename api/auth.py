from hashlib import sha1
import email.utils
import hmac

class Auth(object):
	url = None
	secret = None
	username = None
	
	@staticmethod
	def set_credentials(username, secret, url):
		Auth.username = username
		Auth.secret = secret
		Auth.url = url

	@staticmethod
	def get_headers():
		if Auth.username == None or Auth.secret == None :
			raise "Credentials not set"
		
		dt = email.utils.formatdate(usegmt=True)
		stringToSign = 'date: ' + dt;

		encodedSignature = hmac.new(Auth.secret, stringToSign, sha1).digest().encode("base64").rstrip('\n')

		hmacAuth = 'hmac username="' + Auth.username + '",algorithm="hmac-sha1",headers="date",signature="' + encodedSignature + '"';

		headers = {
    		'date': dt,
    		'Authorization': hmacAuth
		}

		return headers