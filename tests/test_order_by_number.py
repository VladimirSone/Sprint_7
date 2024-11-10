import requests
import allure
from url import Url

class TestOrderByNumber:

    @allure.title('Проверка,что система вернет ошибку, если не указать всех данных')
    @allure.title('Проверка статуса кода и тела ответа')
    def test_order_by_no_number(self):
        response=requests.get(Url.URLGETORDERBYNUMBER)
        assert response.status_code == 400 and {'message': 'Недостаточно данных для поиска'}

    @allure.title('Проверка,что система вернет ошибку, если указан несуществующий номер запроса')
    @allure.title('Проверка статуса кода и тела ответа')
    def test_order_by_incorrect_number(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=368383')
        assert response.status_code == 404 and {'message': 'Not Found'}

    @allure.title('Проверка, что заказ получен, если валидные данные')
    @allure.title('Проверка статуса кода и тела ответа')
    def test_order_by_valid_number(self):
        response=requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=376127&t?=368383')
        assert response.status_code == 200