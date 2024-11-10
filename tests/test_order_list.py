import allure
import requests
from url import Url

class TestOrderList:

    @allure.title('Проверить, что возвращается список заказов')
    @allure.title('Проверка статуса кода и тела ответа')
    def test_order_list(self):
        response = requests.get(Url.URLGETORDERS)
        assert response.json()['orders'] and response.status_code == 200