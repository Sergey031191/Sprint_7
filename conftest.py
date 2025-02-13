import pytest
import requests
from data.urls import APILinks
from helpers import register_new_courier_and_return_login_password


@pytest.fixture
def create_new_courier():
    data = register_new_courier_and_return_login_password()
    new_courier_creds = {"login": data[0], "password": data[1]}
    return new_courier_creds

@pytest.fixture
def create_test_courier():
    data = register_new_courier_and_return_login_password()
    sign_in = {"login": data[0], "password": data[1], "firstName": data[2]}

    yield sign_in

    courier_signin = requests.post(APILinks.MAIN_URL + APILinks.LOGIN_URL, data=sign_in)
    courier_id = courier_signin.json()["id"]
    requests.delete(APILinks.MAIN_URL + APILinks.COURIER_URL + str(courier_id))



