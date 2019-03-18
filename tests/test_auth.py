import pytest
from api.auth import Auth 


# test get headers without details
def test_get_headers_without_all_details():
	try:
		Auth.get_headers()
		pytest.fail("Should throw")
	except:
		pass

# testing set credentials
def test_set_credentials():
	username = "dummy_user"
	secret = "secret"
	url = "url"
	Auth.set_credentials(username, secret, url)

	assert Auth.username == username
	assert Auth.secret == secret
	assert Auth.url == url

# test get headers with details
def test_get_headers_with_all_details():
	username = "dummy_user"
	secret = "secret"
	url = "url"
	Auth.set_credentials(username, secret, url)

	try:
		Auth.get_headers()
	except:
		pytest.fail("Should not throw")