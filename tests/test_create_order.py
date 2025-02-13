import allure
import requests
import pytest
import json

from data.urls import APILinks
from data.test_data import ScooterOrderData


class TestCreateOrder:

    @allure.description("Проверка создания заказа с несколькими вариантами цветов самоката")
    @pytest.mark.parametrize('color', [["BLACK"], ["GRAY"], ["BLACK", "GRAY"], []])
    def test_create_order_different_colors_success(self, color):
        ScooterOrderData.scooter_order["color"] = color
        payload = json.dumps(ScooterOrderData.scooter_order)
        response = requests.post(APILinks.MAIN_URL + APILinks.MAIN_ORDERS_URL, data=payload)
        assert response.status_code == 201 and response.json()["track"] is not None
