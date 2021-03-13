import time

import pytest
from selenium.webdriver import ActionChains

import config
from pages.main_newchic import MainPage


def test_categories_list_box_is_presented(web_browser):
    """Проверяем, что знак логотипа присутствует на странице и виден пользователю"""
    page = MainPage(web_browser)
    assert page.logo_newchic.is_presented()


def test_clicking_logo(web_browser):
    """Проверяем переход на главную страницу по клику на логотип"""
    page = MainPage(web_browser)
    page.logo_newchic_link_women.click()
    path = page.get_relative_link()
    assert path == config.path_logo, 'ERROR clicking logo'


def test_icon_for_logo_is_presented(web_browser):
    """Проверяем, что иконка для регистрации  присутствует на странице и видна пользователю"""
    page = MainPage(web_browser)
    assert page.icon_for_logo.is_presented()


def test_clicking_icon_logo(web_browser):
    """Проверяем переход на страницу регистрации по клику на иконку для регистрации"""
    page = MainPage(web_browser)
    page.icon_for_logo.click()
    path = page.get_relative_link()
    assert path == config.path_url_reg, 'ERROR clicking logo'


def test_clicking_icon_for_favorites(web_browser):
    """Проверяем , что незарегистрированный пользователь при клике на иконку  для избранного
    попадает на страницу регистрации"""
    page = MainPage(web_browser)
    page.icon_for_favorites.click()
    path = page.get_relative_link()
    assert path == config.path_url_reg, 'ERROR clicking page'


def test_icon_shopping_basket_is_presented(web_browser):
    """Проверяем, что иконка корзины  присутствует на странице и видна пользователю"""
    page = MainPage(web_browser)
    assert page.shopping_basket.is_presented()


def test_clicking_icon_shopping_basket(web_browser):
    """Проверяем , что при клике на иконку корзины пользователь попадает на страницу корзины"""
    page = MainPage(web_browser)
    page.shopping_basket.click()
    path = page.get_relative_link()
    assert path == config.path_url_shopping_basket, 'ERROR clicking page'


def test_icon_user_country_is_presented(web_browser):
    """Проверяем, что иконка для выбора страны   присутствует на странице и видна пользователю"""
    page = MainPage(web_browser)
    assert page.user_country.is_presented()


def test_clicking_icon_user_country(web_browser):
    """Проверяем, что при клике на иконку для выбора страны и валюты открывается окно с полями для выбора"""
    page = MainPage(web_browser)
    page.user_country.click()
    assert page.user_country_selection.get_text() == "Адрес получателя"


def test_search_is_presented(web_browser):
    """Проверяем, что поле поиска представлено на странице"""
    page = MainPage(web_browser)
    assert page.search.is_presented()


def test_use_search(web_browser):
    """ Проверяем, что поле поиска работает при корректном запросе и пользователь видит продукты"""

    page = MainPage(web_browser)
    page.search = 'платье'
    page.search_run_button.click()
    assert page.products_titles.count() == 59
    found = False
    for title in page.products_titles.get_text():
        if 'платье' in title.lower():
            found = True

    message = 'В результатах ни разу не встречено искомое ключевое слово "платье"'
    assert found, message


@pytest.mark.xfail  # БАГ  или особенность сайта, этот тест не проходит, поле поиска не понимает такой запрос
def test_wrong_input_in_search(web_browser):
    """ Проверяем, что поле поиска работает, если использовать неправильную раскладку клавиатуры,
     вводим "gkfnmt" (платье)"""

    page = MainPage(web_browser)
    page.search = 'gkfnmt'
    page.search_run_button.click()
    assert page.products_titles.count() == 59, "Мы не смогли найти то, что искали"


def test_wrong_input_in_search_eng(web_browser):
    """ Проверяем, что поле поиска работает, если запрос пользователя на английском языке,
     вводим "dress" (платье)"""

    page = MainPage(web_browser)
    page.search = 'dress'
    page.search_run_button.click()
    assert page.products_titles.count() == 59, "Мы не смогли найти то, что искали"


def test_item_main_menu_is_visible(web_browser):
    """ Проверяем, что все разделы главного меню видимы на странице"""

    page = MainPage(web_browser)
    assert page.item_main_menu.is_presented()
    assert page.item_main_menu.count() == 9


def test_click_item_main_menu_new_arrivals(web_browser):
    """ Проверяем, что клик на пункт меню НОвинки, открывает нужную страницу"""

    page = MainPage(web_browser)
    page.item_main_new_arrivals.click()
    path = page.get_relative_link()
    assert path == config.path_menu_new_arrivals, 'ERROR clicking page'


def test_click_item_main_menu_women_spring(web_browser):
    """ Проверяем, что клик на пункт меню Весенняя коллекция, открывает соответствующую страницу"""

    page = MainPage(web_browser)
    page.item_main_women_spring.click()
    path = page.get_relative_link()
    assert path == config.path_menu_women_spring, 'ERROR clicking page'


def test_click_item_main_menu_women_clothing(web_browser):
    """ Проверяем, что клик на пункт меню Одежды, открывает соответствующую страницу"""

    page = MainPage(web_browser)
    page.item_menu_women_clothing.click()
    path = page.get_relative_link()
    assert path == config.path_menu_womens_clothing, 'ERROR clicking page'


def test_click_item_main_menu_womens_tops(web_browser):
    """ Проверяем, что клик на пункт меню Топы, открывает соответствующую страницу"""

    page = MainPage(web_browser)
    page.item_menu_women_tops.click()
    path = page.get_relative_link()
    assert path == config.path_menu_womens_tops, 'ERROR clicking page'


def test_click_item_main_menu_plus_size(web_browser):
    """ Проверяем, что клик на пункт меню Большой размер, открывает соответствующую страницу"""

    page = MainPage(web_browser)
    page.item_menu_women_plus_size.click()
    path = page.get_relative_link()
    assert path == config.path_menu_plus_size, 'ERROR clicking page'


@pytest.mark.xfail
def test_click_item_main_menu_women_shoes_bags(web_browser):  # БАГ -ссылка ведет на главную страницу
    """ Проверяем, что клик на пункт меню Обуви и Сумки, открывает соответствующую страницу"""

    page = MainPage(web_browser)
    page.item_menu_women_shoes_bags.click()
    path = page.get_relative_link()
    assert path == config.path_womens_shoes, 'ERROR clicking page'


def test_click_item_main_menu_women_accessories(web_browser):
    """ Проверяем, что клик на пункт меню Аксессуары и красота  открывает соответствующую страницу"""

    page = MainPage(web_browser)
    page.item_menu_women_accessories.click()
    path = page.get_relative_link()
    assert path == config.path_accessories, 'ERROR clicking page'


def test_click_item_main_menu_home_garden(web_browser):
    """ Проверяем, что клик на пункт меню Дом и дача  открывает соответствующую страницу"""

    page = MainPage(web_browser)
    page.item_menu_home_garden.click()
    path = page.get_relative_link()
    assert path == config.path_home_garden, 'ERROR clicking page'


@pytest.mark.xfail
def test_click_item_main_menu_stock(web_browser):  # БАГ, открывается главная страница
    """ Проверяем, что клик на пункт меню Акции открывает соответствующую страницу"""

    page = MainPage(web_browser)
    page.item_menu_stock.click()
    path = page.get_relative_link()
    assert path == config.path_stock, 'ERROR clicking page'

def test_click_item_main_menu_stock_in_men_product(web_browser):
    """ Проверяем, что клик на пункт меню Акции в разделе для мужчин открывает страницу распродажи"""

    page = MainPage(web_browser)
    page.products_for_men.click()
    page.item_menu_stock_men.click()
    path = page.get_relative_link()
    assert path == config.path_stock_men, 'ERROR clicking page'


def test_page_clearance_stock_filter(web_browser):
    """Проверяем, что в категории Акции-распродажа на странице загружаются только товары со скидкой"""
    url = config.url_stock
    page = MainPage(web_browser, url)
    page.link_checkbox_sale_stock.click()
    old_price = page.old_price_sale_stock.count()
    new_price = page.new_price_sale_stock.count()

    assert old_price == new_price


def test_stock_filter_wom_left_button(web_browser):
    """Проверяем, что в категории Акции-распродажа если клик на кнопке фильтра минимальных цен"under?руб"
     на странице Женщины загружаются только товары с ценами не выше указанной (левая кнопка)"""
    url = config.url_stock_wom
    page = MainPage(web_browser, url)
    page.button_price_filter_m.click()
    page.link_checkbox_sale_stock.click()
    attr_name = "oriprice"
    price_list = page.new_price_sale_stock.get_attribute(attr_name)
    price_list_as_float = [float(x) for x in price_list]
    max_price_str = page.button_float_price_filter_m.get_attribute(attr_name)

    assert max(price_list_as_float) <= float(max_price_str)

def test_stock_filter_wom_right_button(web_browser):
    """Проверяем, что в категории Акции-распродажа если клик на кнопке максимальных цен"under?руб"
     на странице Женщины загружаются только товары с ценами не выше указанной (правая кнопка)"""
    url = config.url_stock_wom
    page = MainPage(web_browser, url)
    page.button_price_filter_xxl.click()
    page.link_checkbox_sale_stock.click()
    attr_name = "oriprice"
    price_list = page.new_price_sale_stock.get_attribute(attr_name)
    price_list_as_float = [float(x) for x in price_list]
    max_price_str = page.button_float_price_filter_xxl.get_attribute(attr_name)

    assert max(price_list_as_float) <= float(max_price_str)


def test_check_filter_watch_open_list(web_browser):
    """Проверяем, что на странице Аксессуары и красота в фильтре Украшения и часы "+" раскрывает
    список категорий"""
    url = config.url_accessories
    page = MainPage(web_browser, url)
    element = page.plus_watches_filter[1]
    element.click()
    list_titles = page.link_watches_filter
    assert list_titles.is_presented()

def test_check_filter_beauty_open_list(web_browser):
    """Проверяем, что на странице Аксессуары и красота в фильтре Красота "+" раскрывает
    список категорий"""
    url = config.url_accessories
    page = MainPage(web_browser, url)
    element = page.plus_watches_filter[2]
    element.click()
    list_titles = page.link_manicure_filter
    assert list_titles.is_presented()


def test_check_filter_beauty_close_list(web_browser):
    """Проверяем, что на странице Аксессуары и красота в фильтре Красота "-" закрывает
    список категорий"""
    url = config.url_accessories
    page = MainPage(web_browser, url)
    element = page.plus_watches_filter[2]
    element.click()

    time.sleep(5)
    element.click()
    list_titles = page.link_manicure_filter
    assert list_titles.is_clickable


def test_check_filter_color_visible(web_browser):
    """Проверяем, что на странице Аксессуары и красота виден фильтр выбора товара по цвету COLOR """
    url = config.url_accessories
    page = MainPage(web_browser, url)

    assert page.link_color_filter.is_presented()

def test_check_filter_color_clickab(web_browser):
    """Проверяем, что на странице Аксессуары и красота в фильтре Color можно выбрать цвет товара """
    url = config.url_accessories
    page = MainPage(web_browser, url)

    assert page.link_color_filter.is_clickable

def test_check_filter_color_list(web_browser):
    """Проверяем, что на странице Аксессуары и красота в фильтре Color раскрывается список для выбора цвета товара """
    url = config.url_accessories
    page = MainPage(web_browser, url)
    page.link_color_filter.click()
    assert page.link_color_orang_filter.is_presented()

def test_check_filter_color(web_browser):
    """Проверяем, фильтр Color на странице Аксессуары и красота, при клике на чекбокс "оранжевый"
       на странице отображаются товары с указанным цветом, чтобы убедиться делаем фото страницы"""
    url = config.url_accessories
    page = MainPage(web_browser, url)
    page.link_color_orang_filter.click()
    page.refresh()
    page._web_driver.save_screenshot('orange_products_screenshot.png')



def test_check_filter_color_by_text_in_title(web_browser):
    """Проверяем фильтр Color на странице Аксессуары и красота-парики. При клике на чекбокс "черный",
       фильтр становится активным и отображается в блоке выбранных фмильтров."""

    url = config.url_accessories
    page = MainPage(web_browser, url)

    element = page.plus_watches_filter[2]
    element.click()

    page.link_hair_wigs_filter.click()
    page.see_more_links[1].click()
    page.link_color_black_filter.click()

    page.wait_page_loaded()
    assert page.active_filter_black.is_presented()






# python -m pytest --driver Chrome --driver-path C:\ChromeDriver\chromedriver.exe tests/test_main_page.py
# python -m pytest -v --driver Chrome --driver-path C:\ChromeDriver\chromedriver.exe tests/test_main_page.py
