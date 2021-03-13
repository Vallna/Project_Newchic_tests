import time
from termcolor import colored

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class WebElement(object):
    _locator = ('', '')
    _web_driver = None
    _page = None
    _timeout = 10
    _wait_after_click = False  # TODO: how we can wait after click?

    def __init__(self, timeout=10, wait_after_click=False,
                 **kwargs) -> object:

        self._timeout = timeout
        self._wait_after_click = wait_after_click

        for attr in kwargs:
            self._locator = (str(attr).replace('_', ' '), str(kwargs.get(attr)))

    def find(self, timeout=10):  # можно находить элемент
        """ Find element on the page. """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.presence_of_element_located(self._locator)
            )
        except:
            print(colored('Element not found on the page!', 'red'))

        return element

    def wait_to_be_clickable(self, timeout=10,
                             check_visibility=True):  # можно ждать пока элемент будет доступен для клика
        """ Wait until the element will be ready for click. """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.element_to_be_clickable(self._locator)
            )
        except:
            print(colored('Element not clickable!', 'red'))

        if check_visibility:
            self.wait_until_not_visible()

        return element

    def is_clickable(self):  # проверить доступен ли элемент для клика
        """ Check is element ready for click or not. """

        element = self.wait_to_be_clickable(timeout=0.1)
        return element is not None

    def is_presented(self):
        """ Check that element is presented on the page. """  # Убедитесь, что элемент представлен на странице

        element = self.find(timeout=0.1)
        return element is not None

    def is_visible(self):
        """ Check is the element visible or not. """  # Проверить, виден ли элемент

        element = self.find(timeout=0.1)

        if element:
            return element.is_displayed()

        return False

    def wait_until_not_visible(self, timeout=10):  # можно ожидать пока элемент не буден виден на странице

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.visibility_of_element_located(self._locator)
            )
        except:
            print(colored('Element not visible!', 'red'))

        if element:
            js = ('return (!(arguments[0].offsetParent === null) && '
                  '!(window.getComputedStyle(arguments[0]) === "none") &&'
                  'arguments[0].offsetWidth > 0 && arguments[0].offsetHeight > 0'
                  ');')
            visibility = self._web_driver.execute_script(js, element)
            iteration = 0

            while not visibility and iteration < 10:
                time.sleep(0.5)

                iteration += 1

                visibility = self._web_driver.execute_script(js, element)
                print('Element {0} visibility: {1}'.format(self._locator, visibility))

        return element

    def send_keys(self, keys, wait=2):  # можно передать какое то сочетание клавишь или текст, если это текстовое поле
        """ Send keys to the element. """

        keys = keys.replace('\n', '\ue007')

        element = self.find()

        if element:
            element.click()
            element.clear()
            element.send_keys(keys)
            time.sleep(wait)
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def get_text(self):  # можно получить текст текущего вебэлемента
        """ Get text of the element. """

        element = self.find()
        text = ''

        try:
            text = str(element.text)
        except Exception as e:
            print('Error: {0}'.format(e))

        return text

    def get_attribute(self, attr_name):  # можно получить какой то атрибут элемента
        """ Get attribute of the element. """

        element = self.find()

        if element:
            return element.get_attribute(attr_name)

    def _set_value(self, web_driver, value,
                   clear=True):  # это абстрактный метод и нужен для того, чтобы мы работали с текстовыми полями
        """ Set value to the input element. """

        element = self.find()

        if clear:
            element.clear()

        element.send_keys(value)

    def click(self, hold_seconds=0, x_offset=1,
              y_offset=1):  # не только кликает на элемент но и устанавливает правильно мышку на элементе и дожидается пока можно кликнуть
        """ Wait and click the element. """

        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset). \
                pause(hold_seconds).click(on_element=element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

        if self._wait_after_click:
            self._page.wait_page_loaded()

    def right_mouse_click(self, x_offset=0, y_offset=0, hold_seconds=0):
        """ Click right mouse button on the element. """  # Щелкните правой кнопкой мыши на элементе

        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset). \
                pause(hold_seconds).context_click(on_element=element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def highlight_and_make_screenshot(self, file_name='element.png'):
        """ Highlight element and make the screen-shot of all page. """  # Выделите элемент и сделайте снимок экрана всей страницы
        # этот метод позволяет скриншитить все элементы на которые мы не смогли нажать и увидим, почему не получилось, может элемент невидим
        element = self.find()

        # Scroll page to the element:
        self._web_driver.execute_script("arguments[0].scrollIntoView();", element)

        # Add red border to the style:
        self._web_driver.execute_script("arguments[0].style.border='3px solid red'", element)

        # Make screen-shot of the page:
        self._web_driver.save_screenshot(file_name)

    def scroll_to_element(
            self):  # здесь два способа доскролить до нужного элемента, черезjavaskript и просто прокрутить вниз
        """ Scroll page to the element. """

        element = self.find()

        # Scroll page to the element:
        # Option #1 to scroll to element: # этот способ невсегда срабатывает
        # self._web_driver.execute_script("arguments[0].scrollIntoView();", element)

        # Option #2 to scroll to element: этот надежнее
        try:
            element.send_keys(Keys.DOWN)
        except Exception as e:
            pass  # Just ignore the error if we can't send the keys to the element

    def delete(self):  # удалять может нужно какие то баннеры или всплывающие окна, которые закрывают элемент
        """ Deletes element from the page. """

        element = self.find()

        # Delete element:
        self._web_driver.execute_script("arguments[0].remove();", element)


class ManyWebElements(WebElement):

    def __getitem__(self, item):
        """ Get list of elements and try to return required element. """  # Получить список элементов и попытаться вернуть требуемый элемент

        elements = self.find()
        return elements[item]

    def find(self, timeout=10):
        """ Find elements on the page. """  # Найдите элементы на странице

        elements = []

        try:
            elements = WebDriverWait(self._web_driver, timeout).until(
                EC.presence_of_all_elements_located(self._locator)
            )
        except:
            print(colored('Elements not found on the page!', 'red'))

        return elements

    def _set_value(self, web_driver, value):
        """ Note: this action is not applicable for the list of elements. """  # Примечание: это действие не применимо для списка элементов
        raise NotImplemented('This action is not applicable for the list of elements')

    def click(self, hold_seconds=0, x_offset=0, y_offset=0):
        """ Note: this action is not applicable for the list of elements. """  # Примечание: это действие не применимо для списка элементов
        raise NotImplemented('This action is not applicable for the list of elements')

    def count(self):
        """ Get count of elements. """  # Получите количество элементов

        elements = self.find()
        return len(elements)

    def get_text(self):  # можно получить текст элементов, функция вернет массив
        """ Get text of elements. """

        elements = self.find()
        result = []

        for element in elements:
            text = ''

            try:
                text = str(element.text)
            except Exception as e:
                print('Error: {0}'.format(e))

            result.append(text)

        return result

    def get_attribute(self, attr_name):  # получим массив каких то атрибутов
        """ Get attribute of all elements. """

        results = []
        elements = self.find()

        for element in elements:
            results.append(element.get_attribute(attr_name))

        return results

    def highlight_and_make_screenshot(self, file_name='element.png'):
        """ Highlight elements and make the screen-shot of all page. """

        elements = self.find()

        for element in elements:
            # Scroll page to the element:
            self._web_driver.execute_script("arguments[0].scrollIntoView();", element)

            # Add red border to the style:
            self._web_driver.execute_script("arguments[0].style.border='3px solid red'", element)

        # Make screen-shot of the page:
        self._web_driver.save_screenshot(file_name)
