import config
from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver):
        url = config.url_base + config.path_url_reg
        super().__init__(web_driver, url)

    icon_for_logo = WebElement(css_selector='div.cursor-pointer.header-right-user-icon a')
    input_email = WebElement(css_selector='input.sign-up-email-input-js')
    input_password = WebElement(css_selector='input.sign-up-password-input-js')
    button_registration = WebElement(css_selector='div.btn-sign-up>span')
    message_after_registr =WebElement (xpath='//div/h2[contains(text(),"Регистрация прошла успешно")]')
    input_email_sing_in = WebElement(css_selector='input#loginName')
    input_password_sing_in = WebElement(css_selector='input#loginPassword')
    button_sing_in = WebElement(xpath='//span[@class="d-block py-lg-2"]')
    warning_whoops_negativ_email = WebElement(xpath='//div[contains(@class,"login-error-text-js")][@data-msg="Пожалуйста, введите код"]')


