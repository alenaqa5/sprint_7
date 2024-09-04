import requests
import allure
from urls import base_url, order


class Orders:
    @allure.step('Отправить запрос на создание заказа')
    def create_order(self, payload):
        response = requests.post(f'{base_url}{order}', data=payload)
        return response
    @allure.step('Запросить список заказов')
    def get_order(self):
        response = requests.get(f'{base_url}{order}')
        return response