import os
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ru.newchic.com/?mg_id=1'

        super().__init__(web_driver, url)

    # знак логотипа
    logo_newchic = WebElement(css_selector='div.lg.flex.justify-content-center')
    logo_newchic_link_men = WebElement(css_selector='div.justify-content-center>a[href="/?mg_id=2"]')
    logo_newchic_link_women = WebElement(css_selector='div.justify-content-center>a[href="/?mg_id=1"]')

    # кнопка товары для мужчин
    products_for_men = WebElement(xpath='//a[contains(text(),"МУЖЧИНАМ")]')

    # информация о сумме бесплатной доставки
    info_free_shipping = WebElement(css_selector='div.header-nav-free-shipping-tips>p>span')

    # иконка для регистрации
    icon_for_logo = WebElement(css_selector='div.cursor-pointer.header-right-user-icon a')

    # иконка для избранное
    icon_for_favorites = WebElement(css_selector='div.header-right-user-wishlist-icon>a')

    # иконка корзины
    shopping_basket = WebElement(css_selector='div a[href="/shopping_cart.html"]')

    # иконка выбора страны для доставки
    user_country = WebElement(css_selector='div.cursor-pointer.header-right-ship-to-country')

    # окно с полями для выбора страны и валюты
    user_country_selection = WebElement(xpath='//p[text()="Адрес получателя"]')

    # поле поиска
    search = WebElement(css_selector='#keywords')
    search_run_button = WebElement(css_selector='span.position-absolute')

    # товары на странице по результату поиска
    products_titles = ManyWebElements(xpath='//a[contains(@class,"product-item-name-js")]')

    # панель главного меню с разделами
    item_main_menu = ManyWebElements(css_selector='div>ul.flex.lg>li')

    # локатор меню НОВИНКИ, главного меню
    item_main_new_arrivals = WebElement(css_selector='div ul.header-nav-list-js>li>a[data-string1="Новинки"]')

    # локатор меню Весенняя коллекция
    item_main_women_spring = WebElement(css_selector='a.text-secondary[data-string1="Весенняя коллекция"]')

    # локатор главного меню Одежды
    item_menu_women_clothing = WebElement(css_selector='a.text-secondary[data-string1="Одежды"]')

    # локатор главного меню Топы
    item_menu_women_tops = WebElement(css_selector='a.text-secondary[data-string1="Топы"]')

    # локатор главного меню Большой размер
    item_menu_women_plus_size = WebElement(css_selector='a.text-secondary[data-string1="Большой размер"]')

    # локатор главного меню Обуви и сумки
    item_menu_women_shoes_bags = WebElement(css_selector='a.text-secondary[data-string1="Обуви и сумки"]')

    # локатор главного меню Аксессуары и красота
    item_menu_women_accessories = WebElement(css_selector='a.text-secondary[data-string1="Аксессуары и красота"]')

    # локатор главного меню Дом и сад
    item_menu_home_garden = WebElement(css_selector='a.text-secondary[data-string1="Дом и дача"]')

    # локатор главного меню Акция товары для женщин
    item_menu_stock = WebElement(css_selector='a.text-secondary[data-string1="Акция"]')

    # локатор главного меню Акция товары для мужчин
    item_menu_stock_men = WebElement(xpath='//a[contains(@href,"mens-clothing-3581")]/span')

    # локатор ссылки  Женщины на странице  распродажа в категории Акции
    products_sale_stock_women = WebElement(css_selector='li.category-nav__item--active>a')

    # локатор ссылки чекбокс "в акции" на странице распродажа
    link_checkbox_sale_stock = WebElement(css_selector='div.filter__ship >a')

    # локатор новой цены  "в акции" на странице распродажа
    new_price_sale_stock = ManyWebElements(xpath='//div[@class="flex align-items-center"]/strong')

    # локатор новой цены  "в акции" на странице распродажа и атрибут oriprice
    new_price_sale_stock_attr = ManyWebElements(xpath='//div[@class="flex align-items-center"]/strong/@oriprice')

    # локатор старой цены  "в акции" на странице распродажа
    old_price_sale_stock = ManyWebElements(xpath='//div[@class="flex align-items-center"]/del')

    # локатор знака "+" фильтр Категории-Украшения и часы
    plus_watches_filter = ManyWebElements(css_selector='div.d-flex span>i.nc-icon')

    # локатор знака ссылки часы в меню фильтра категории, Украшения и часы
    link_watches_filter = ManyWebElements(css_selector='div.px-lg-16>p')

    # локатор знака ссылки маникюр в меню фильтра категории, Украшения и часы
    link_manicure_filter = WebElement(xpath='//p/a[contains(text(),"маникюр")]')

    # локатор знака ссылки парики в меню фильтра категории, Украшения и часы
    link_hair_wigs_filter = WebElement(xpath='//p/a[contains(text(),"парики волос")]')

    # локатор  ссылки COLOR в меню ,бокового фильтра
    link_color_filter = WebElement(xpath='//span[contains(text(),"Color")]')

    # локатор  чекбокс(1)оранжевый COLOR в меню ,бокового фильтра
    link_color_orang_filter = WebElement(css_selector='div[data-filter-id="4754"]>span.mx-lg-5')

    # локатор для ссылок "посмотреть больше", бокового фильтра.
    see_more_links = ManyWebElements(
        css_selector='span.btn-cursor.text-hover-primary.cate-filter-view-more.text-capitalize.cate-filter-view-more-js')

    # локатор для активного фильтра "черный", бокового фильтра.
    active_filter_black = WebElement(css_selector='span.btn-clear-attr-js[data-value="4727"]')

    # локатор  чекбокс(1)черный COLOR в меню ,бокового фильтра
    link_color_black_filter = WebElement(css_selector='div[data-filter-id="4727"]>span.mx-lg-5')

    # локатор кнопки "under?руб" левая, с мин ценами в фильтре на странице Распродажа женские товары
    button_price_filter_m = WebElement(xpath='//a[@data-price-to="10"]')

    # локатор кнопки "under?руб" правая с макс. ценами в фильтре на странице Распродажа женские товары
    button_price_filter_xxl = WebElement(xpath='//a[@data-price-to="40"]')

    # локатор кнопки "under?руб"  для цены в фильтре на странице Распродажа
    button_float_price_filter_m = WebElement(xpath='//a[@data-price-to="10"]/span')

    # локатор кнопки "under?руб"  для цены в фильтре на странице Распродажа
    button_float_price_filter_xxl = WebElement(xpath='//a[@data-price-to="40"]/span')
