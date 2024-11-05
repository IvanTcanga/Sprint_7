import allure
from methods.order_methods import OrderMethods


class TestOrdersList:
	@allure.title('Проверка ,что в тело ответа возвращается список заказов.')
	@allure.description('Проверяются код и тело ответа.')
	def test_orders_list_get_success(self):
		order_methods = OrderMethods()
		response = order_methods.get_list_orders()
		assert type(response.json()['orders']) == list and 'id' in response.json()['orders'][0]
