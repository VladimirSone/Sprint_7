import allure
import pytest
import requests
from data import UserData
from url import Url
from helpers import random_courier_login, random_courier_password

class TestLoginCourier:

    @allure.title('Проверка авторизации курьера с валидными данными')
    @allure.description('Проверка статуса кода и тела ответа')
    def test_login_courier_valid(self):
        payload = {"login": UserData.LOGIN, "password": UserData.PASSWORD}
        response = requests.post(Url.URLPOSTLOGIN, data=payload)
        assert response.status_code == 200 and response.json() == {"id": 414493}

    @allure.title('Проверка, что система вернет ошибку, если неверно указан логин или пароль')
    @allure.description('Проверка статуса кода и тело ответа')
    @pytest.mark.parametrize('payload', [{'login': random_courier_login(), 'password': UserData.PASSWORD}, {'login': UserData.LOGIN, 'password': random_courier_password()}])
    def test_login_courier_failed(self, payload):
        response = requests.post(Url.URLPOSTLOGIN, data=payload)
        assert response.status_code == 404 and {"message": "Учетная запись не найдена"}

    @allure.title('Проверка, что система вернет ошибку, если не заполнено одно из полей')
    @pytest.mark.parametrize('user_data', [{'login': UserData.LOGIN, 'password': ""}, {'login': "", 'password': UserData.PASSWORD}])
    def test_login_courier_no_field(self, user_data):
        response = requests.post(Url.URLPOSTLOGIN, data=user_data)
        assert response.status_code == 400 and {'message': "Недостаточно данных для входа"}
