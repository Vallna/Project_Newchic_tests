import time
import pytest
import config
from pages.auth_page import AuthPage


def test_positive_sing_in(web_browser):
    """Проверяем вход зарегистрированного пользователя с корректными данными"""
    page = AuthPage(web_browser)
    page.input_email_sing_in = config.positive_email
    page.input_password_sing_in = config.positive_password
    page.button_sing_in.click()
    time.sleep(1)
    page.wait_page_loaded()
    path = page.get_relative_link()
    assert path == config.path_base


def test_negativ_email_sing_in(web_browser):
    """Проверяем вход зарегистрированного пользователя по неверному email"""
    page = AuthPage(web_browser)
    email = config.negativ_email
    password = config.positive_password
    page.input_email_sing_in = email
    page.input_password_sing_in = password
    page.button_sing_in.click()
    time.sleep(1)
    page.wait_page_loaded()

    path = page.get_relative_link()
    assert path == config.path_url_reg

    error_element = page.warning_whoops_negativ_email
    assert error_element.is_visible()





#python -m pytest --driver Chrome --driver-path C:\ChromeDriver\chromedriver.exe tests/test_auth_customer.py
