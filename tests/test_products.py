import pytest

from mock import Mock

from api.auth import Auth
from api.outbound import Outbound
from api.products import Products


# testing set credentials
def test_set_credentials():
	expected = "Foo"
	Outbound.make_get_request = Mock(return_value=expected)
	username = "dummy_user"
	secret = "secret"
	url = "url"
	Auth.set_credentials(username, secret, url)
	expected_url = "url/marketplace/v1/products"

	p = Products()
	result = p.get_products()
	assert result == expected
	assert Outbound.make_get_request.call_args_list[0][0][0] == expected_url
	
