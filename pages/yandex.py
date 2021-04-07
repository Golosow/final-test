#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://market.yandex.ru/'

        super().__init__(web_driver, url)


    # Search login field
    search_login_field = WebElement(id='passp-field-login')
    # Search button enter
    search_run_button_enter = WebElement(xpath='//button[@type="submit"]')
    # Search password field
    search_password_field = WebElement(id='passp-field-passwd')

    # Main search field
    search = WebElement(id='header-search')

    # Search button
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Button to sort products by price
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')
    # Button to sort products by rating
    sort_products_by_rating = WebElement(css_selector='button[data-autotest-id="quality"]')
    # Button to sort products by feedback
    sort_products_by_feedback = WebElement(css_selector='button[data-autotest-id="opinions"]')
    # Button to sort products by discount
    sort_products_by_discount = WebElement(css_selector='button[data-autotest-id="discount_p"]')
    # Button to sort products by novelty
    sort_products_by_novelty = WebElement(css_selector='button[data-autotest-id="ddate"]')

    # Search button electronics
    search_button_electronics = WebElement(xpath='//a[contains(@href, "/catalog--elektronika/")]')
    # Search button computers
    search_button_computers = WebElement(xpath='//a[contains(@href, "/catalog--kompiuternaia-tekhnika/")]')
    # Search button home appliances
    search_button_home_appliances = WebElement(xpath='//a[contains(@href, "/catalog--bytovaia-tekhnika/")]')
    # Search button for children
    search_button_for_children = WebElement(xpath='//a[contains(@href, "/catalog--detskie-tovary/")]')
    # Search button dacha
    search_button_dacha = WebElement(xpath='//a[contains(@href, "/catalog--dacha-sad-i-ogorod/")]')
    # Search button products
    search_button_products = WebElement(xpath='//a[contains(@href, "/catalog--produkty-napitki/")]')
    # Search button broadcasts
    search_button_broadcasts = WebElement(xpath='//a[contains(@href, "/live")]')
    # Search button start selling on yandex. market
    search_button_start_selling_on_yandex_market = WebElement(xpath='//span[contains(text(),"Начать продавать на Маркете")]')

    # Search catalog button
    search_catalog_button = WebElement(xpath='//button[@type="button"]')

    # Search tab purchases
    search_tab_purchases = WebElement(id='93758785-tab')
    # Search tab electronics
    search_tab_electronics = WebElement(id='91539921-tab')
    # Search tab computers
    search_tab_computers = WebElement(id='91540057-tab')
    # Search tab home appliances
    search_tab_home_appliances = WebElement(id='91539990-tab')
    # Search tab for children
    search_tab_for_children = WebElement(id='91540125-tab')
    # Search tab Dacha, garden and vegetable garden
    search_tab_dacha_garden_and_vegetable_garden = WebElement(id='91541973-tab')
    # Search tab products
    search_tab_products = WebElement(id='91540658-tab')
    # Search tab beauty
    search_tab_beauty = WebElement(id='91540461-tab')
    # Search tab hygiene
    search_tab_hygiene = WebElement(id='91540589-tab')
    # Search tab pet supplies
    search_tab_pet_supplies = WebElement(id='91540721-tab')
    # Search tab sports and outdoor activities
    search_tab_sports_and_outdoor_activities = WebElement(id='91541780-tab')
    # Search tab auto
    search_tab_auto = WebElement(id='91540397-tab')
    # Search tab construction and repair
    search_tab_construction_and_repair = WebElement(id='91540195-tab')
    # Search tab household goods
    search_tab_household_goods = WebElement(id='91540260-tab')
    # Search tab furniture
    search_tab_furniture = WebElement(id='91540328-tab')
    # Search tab clothing and shoes
    search_tab_clothing_and_shoes = WebElement(id='91542039-tab')
    # Search tab bags and suitcases
    search_tab_bags_and_suitcases = WebElement(id='91542104-tab')
    # Search tab jewelry
    search_tab_jewelry = WebElement(id='91542173-tab')
    # Search tab health
    search_tab_health = WebElement(id='91540525-tab')
    # Search tab adult products
    search_tab_adult_products = WebElement(id='91542242-tab')
    # Search tab hobbies and entertainment
    search_tab_hobbies_and_entertainment = WebElement(id='91541844-tab')
    # Search tab books
    search_tab_books = WebElement(id='91541904-tab')
    # Search tab equipment
    search_tab_equipment = WebElement(id='91542311-tab')
    # Search tab digital goods
    search_tab_digital_goods = WebElement(id='91542419-tab')
    # Search tab school and office supplies
    search_tab_school_and_office_supplies = WebElement(id='91542364-tab')
    # Search tab discounted items
    search_tab_discounted_items = WebElement(id='91542488-tab')
    # Search tab discounts and promotions
    search_tab_discounts_and_promotions = WebElement(id='91542546-tab')

    # Search tab view all products coffee
    search_tab_view_all_products_coffee = WebElement(xpath='//a[contains(@href, "/pokupki.market.yandex.ru/catalog/kofe/")]')
    # Search checkbox by manufacturer of coffee
    search_checkbox_by_manufacturer_of_coffee = WebElement(xpath='//span[contains(text(),"Unity Coffee")]')
    # Search choice product of coffee
    search_choice_product_of_coffee = WebElement(xpath='//span[contains(text(),"Кофе в зернах Unity Coffee Эфиопия Yirgacheffe, 1 кг")]')

