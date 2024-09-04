import allure
from api_steps.courier.courier import Courier


class TestCourierCreation:
    @allure.title('Создание курьера')
    def test_create_courier_courier_created(self):
        response = Courier.create_courier(self)
        assert response.status_code == 201 and response.json().get('ok') is True
    @allure.title('Неуспешное создание курьера повторно')
    def test_create_two_same_couriers_second_courier_not_created(self):
        response = Courier.create_courier_couple_times(self)
        assert response.status_code == 409 and response.json().get('message') == "Этот логин уже используется. Попробуйте другой."
    @allure.title('Создание курьера без пароля')
    def test_create_courier_without_password_courier_not_created(self):
        response = Courier.create_courier_without_password(self)
        assert response.status_code == 400 and response.json().get('message') == "Недостаточно данных для создания учетной записи"
    @allure.title('Создание курьера без необязательных полей')
    def test_create_courier_without_not_required_field(self):
        response = Courier.create_courier_without_firstname(self)
        assert response.status_code == 201 and response.json().get('ok') is True
