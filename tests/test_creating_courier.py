import pytest
import requests
import allure
from data import UserData
from url import Url
from helpers import random_courier_login, random_courier_password, random_courier_firstname
class TestCreatingCourier:
    @allure.title('Проверка создания курьера по валидным данным')
    @allure.title('Проверка статуса кода и тела ответа')
    def test_creating_courier(self):
        payload = {'login': random_courier_login(), 'password': random_courier_password(), 'firstName': random_courier_firstname()}
        response = requests.post(Url.URLPOSTCOURIER, data=payload)
        assert response.status_code == 201 and response.json() == {'ok': True}

    @allure.title('Проверка, что возвращается ошибка, если создать двух одинаковых курьеров')
    @allure.title('Проверка статуса кода и тела ответа')
    def test_re_creation_courier(self):
        payload = {'login': UserData.LOGIN, 'password': random_courier_password(), 'firstName': random_courier_firstname()}
        response = requests.post(Url.URLPOSTCOURIER, data=payload)
        assert response.status_code == 409 or response.json() == {"message": "Этот логин уже используется. Попробуйте другой."}

    @allure.title('Проверка, что запрос возвращает ошибку, если нет всех данных: логин или пароль ')
    @allure.title('Проверка статуса кода и тела ответа')
    @pytest.mark.parametrize('user_data', [UserData.COURIER_NO_LOGIN, UserData.COURIER_NO_PASSWORD])
    def test_field_empy_courier(self, user_data):
        response = requests.post(Url.URLPOSTCOURIER, data=user_data)
        assert response.status_code == 400 or response.json() == {"message": "Недостаточно данных для создания учетной записи"}