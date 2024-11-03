import allure
import requests

class TestOrderList:

    @allure.title('Проверить, что возвращается список заказов')
    @allure.title('Проверка статуса кода и тела ответа')
    def test_order_list(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        assert response.json()['orders'] and response.status_code == 200