from api_steps.courier.courier import Courier
import allure

class TestLoginCourier:
    @allure.title('Авторизация курьером')
    def test_login_courier(self):
        response = Courier.login_courier(self)
        assert response.status_code == 200 and response.json().get('id') == 378157
    @allure.title('Авторизация курьером без обязательных полей')
    def test_login_courier_without_required_field(self):
        response = Courier.login_courier_without_required_field(self)
        assert response.status_code == 400 and response.json().get('message') == "Недостаточно данных для входа"
    @allure.title('Авторизация курьером, который не существует')
    def test_login_courier_user_not_exist(self):
        response = Courier.login_courier_with_not_existed_user_data(self)
        assert response.status_code == 404 and response.json().get('message') == "Учетная запись не найдена"
    @allure.title('Авторизация курьером с некорректными данными')
    def test_login_courier_incorrect_data(self):
        response = Courier.login_courier_incorrect_password(self)
        assert response.status_code == 404 and response.json().get('message') == "Учетная запись не найдена"
