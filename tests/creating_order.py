import json
import pytest
import allure
import requests
from url import Url
from data import OrderData

class TestCreatingOrder:
    @allure.title('Проверка создания заказа')
    @allure.title('Проверка создания заказа с цветом BLACK, GREY, с двумя цветами, отсутствием цвета')
    @pytest.mark.parametrize('order_data', [OrderData.order_data_black, OrderData.order_data_grey, OrderData.order_data_two_colors, OrderData.order_data_no_colors])
    def test_creating_order_color(self, order_data):
        order_data = json.dumps(order_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Url.URLPOSTORDERS, data=order_data, headers=headers)
        assert response.status_code == 201 and "track" in response.text