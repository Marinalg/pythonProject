import pytest
from requests import post

@pytest.mark.orders
def test_check_order_for_varus():
    url = "https://stage.partner.api.vanongo.com/orders"
    response = post(url=url)
    assert {"massage", "Authorization"} == response.json()

"Negative test"
@pytest.mark.acceptance
def test_check_code_of_login():
    url = "https://stage.partner.api.vanongo.com/firebase/login"
    response = post(url=url)
    assert 400 == response.status_code
