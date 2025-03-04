import pytest
import requests
import allure
from data.urls import APILinks
from data.test_data import CourierCredentials


class TestCreateCourier:
    @allure.description("Проверка успешного создания нового курьера")
    @allure.title("Курьер успешно создан")
    def test_create_new_courier_success(self):
        new_courier_data = {
            "login": "gazzkull_trakka",
            "password": "waaaaagh1234",
            "firstName": "mag"
        }
        new_courier = requests.post(APILinks.MAIN_URL + APILinks.COURIER_URL, data=new_courier_data)
        courier_login = requests.post(APILinks.MAIN_URL + APILinks.LOGIN_URL, data=new_courier_data)
        courier_id = courier_login.json()['id']
        requests.delete(APILinks.MAIN_URL + APILinks.COURIER_URL + str(courier_id))

        assert new_courier.status_code == 201 and new_courier.text == '{"ok":true}'

    @allure.description("Проверка создания курьера без обязательных полей")
    @allure.title("Курьер не создается")
    @pytest.mark.parametrize("courier_data", [CourierCredentials.empty_login_courier,
                                              CourierCredentials.no_login_courier,
                                              CourierCredentials.no_password_courier,
                                              CourierCredentials.empty_password_courier])
    def test_create_courier_with_one_empty_field_fail(self, courier_data):
        response = requests.post(APILinks.MAIN_URL + APILinks.COURIER_URL, data=courier_data)
        assert response.status_code == 400

    @allure.description("Проверка создания одинаковых курьеров")
    @allure.title("Дубль курьера не создается")
    def test_create_two_couriers_with_same_login_fail(self, create_test_courier):
        response = requests.post(APILinks.MAIN_URL + APILinks.COURIER_URL, data=create_test_courier)
        assert response.status_code == 409
