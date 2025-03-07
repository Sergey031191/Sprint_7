import pytest
import requests
import allure
from data.urls import APILinks
from data.test_data import CourierCredentials, ErrorMessage


class TestCourierLogin:

    @allure.description("Проверка логина созданного курьера")
    @allure.title("Успешный вход по логину и паролю")
    def test_courier_login_success(self, create_new_courier):
        courier_login = requests.post(APILinks.MAIN_URL + APILinks.LOGIN_URL, data=create_new_courier)
        assert courier_login.status_code == 200
        assert courier_login.json()['id'] > 0

    @allure.description("Попытка логина с неправильно введенными или отсутствующими логином или паролем")
    @allure.title("Не удается залогиниться в систему")
    @pytest.mark.parametrize("wrong_creds, status_code, error_message",
                             [[CourierCredentials.test_courier_wrong_password, 404, ErrorMessage.wrong_login_pass_message],
                              [CourierCredentials.test_courier_wrong_login, 404, ErrorMessage.wrong_login_pass_message],
                              [CourierCredentials.test_courier_no_login, 400, ErrorMessage.no_login_or_pass_message],
                              [CourierCredentials.test_courier_no_password, 400, ErrorMessage.no_login_or_pass_message]])
    def test_courier_wrong_password_or_login_fail(self, wrong_creds, status_code, error_message):
        requests.post(APILinks.MAIN_URL + APILinks.COURIER_URL, data=CourierCredentials.test_courier)
        login_fail = requests.post(APILinks.MAIN_URL + APILinks.LOGIN_URL, data=wrong_creds)
        login_success = requests.post(APILinks.MAIN_URL + APILinks.LOGIN_URL, data=CourierCredentials.test_courier)
        requests.delete(APILinks.MAIN_URL + APILinks.COURIER_URL + str(login_success.json()["id"]))
        assert login_fail.status_code == status_code
        assert login_fail.json()["message"] == error_message

