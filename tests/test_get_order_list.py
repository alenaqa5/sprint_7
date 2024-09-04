from api_steps.orders.orders import Orders
import allure


class TestOrderList:
    @allure.title('Получение списка заказов')
    def test_get_order(self):
        orders = Orders()
        response = orders.get_order()
        assert response.status_code == 200 and type(response.json().get('orders')) is list
