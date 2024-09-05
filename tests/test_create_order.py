import pytest
from api_steps.orders.order_payloads import OrderPayloads as Payloads
from api_steps.orders.orders import Orders
import json
import allure

class TestOrderCreation:
    @allure.title('Создание заказов с разными значениями параметра "color"')
    @pytest.mark.parametrize("payload, expected_status_code",
                             [(Payloads.no_color, 201),
        (Payloads.grey_color, 201),
        (Payloads.black_color, 201),
        (Payloads.both_colors, 201)])
    def test_create_order(self, payload, expected_status_code):
        orders = Orders()
        response = orders.create_order(json.dumps(payload))
        assert response.status_code == expected_status_code and 'track' in response.json()
