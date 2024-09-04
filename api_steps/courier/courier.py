import requests
import allure
from urls import base_url, courier_registration, login
from api_steps.courier.courier_payload import CourierPayloads as Payloads


class Courier:
    @allure.step('Создать курьера')
    def create_courier(self):
        response = requests.post(f'{base_url}{courier_registration}', data=Payloads.registration_data)
        return response
    @allure.step('Создать курьера повторно')
    def create_courier_couple_times(self):
        register_data = Payloads.registration_data
        requests.post(f'{base_url}{courier_registration}', data=register_data)
        second_courier_creation = requests.post(f'{base_url}{courier_registration}', data=register_data)
        return second_courier_creation
    @allure.step('Создать курьера без пароля')
    def create_courier_without_password(self):
        response = requests.post(f'{base_url}{courier_registration}', data=Payloads.registration_data_without_password)
        return response
    @allure.step('Создать курьера без имени')
    def create_courier_without_firstname(self):
        response = requests.post(f'{base_url}{courier_registration}', data=Payloads.registration_data_without_firstName)
        return response
    @allure.step('Авторизоваться курьером')
    def login_courier(self):
        response = requests.post(f'{base_url}{login}', data=Payloads.login)
        return response
    @allure.step('Авторизоваться курьером без обязательного поля')
    def login_courier_without_required_field(self):
        response = requests.post(f'{base_url}{login}', data=Payloads.login_without_password)
        return response
    @allure.step('Авторизоваться курьером с несуществующими данными')
    def login_courier_with_not_existed_user_data(self):
        response = requests.post(f'{base_url}{login}', data=Payloads.login_with_not_existed_user)
        return response
    @allure.step('Авторизоваться курьером с некорректными данными')
    def login_courier_incorrect_password(self):
        response = requests.post(f'{base_url}{login}', data=Payloads.login_incorrect_password)
        return response