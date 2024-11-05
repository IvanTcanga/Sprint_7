import pytest
from helpers import *


@pytest.fixture(scope='function')
def create_courier():
    login_pass = register_new_courier_and_return_login_password()
    yield login_pass

# @pytest.fixture()
# def create_courier(courier_methods):
#     response = courier_methods.create_courier(COURIER_NAME)
#     yield response.json()['id']
#     courier_methods.delete_courier(response.json()['id'])
