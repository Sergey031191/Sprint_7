import allure
import requests

from data.urls import APILinks


class TestGetOrdersList:

    @allure.description("Получение списка заказов")
    @allure.title("Успешное получение списка заказов")
    def test_get_orders_list_success(self):
        response = requests.get(APILinks.MAIN_URL + APILinks.MAIN_ORDERS_URL)
        orders_list = response.json()["orders"]
        assert response.status_code == 200 and isinstance(orders_list, list) is True
