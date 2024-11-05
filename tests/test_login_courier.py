import allure
from methods.courier_methods import CourierMethods
from data import *
import pytest


class TestCourierLogin:
    @allure.title('Проверка успешного логина в систему')
    @allure.description('Проверяем код ответа и тело')
    def test_create_courier_success(self, create_courier):
        courier_methods = CourierMethods()
        login_pass, _ = create_courier
        r = courier_methods.post_login_courier(login_pass)
        assert r.status_code == 200 and r.json()['id'] == courier_methods.get_courier_id(login_pass)
        courier_methods.delete_courier(login_pass)
