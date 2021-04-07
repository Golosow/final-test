#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  pytest -v --driver Remote --capability browserName chrome tests/*
#

import pytest
from pages.yandex import MainPage
from pages.settings import url_auth, valid_login, invalid_login, valid_password, invalid_password, without_login, \
    without_password

def test_auth_page_valid_login_and_password(web_browser):
    """ Make sure auth page valid login and password works fine. """
    page = MainPage(web_browser)
    page.get(url_auth)
    page.search_login_field = valid_login
    page.search_run_button_enter.click()
    page.search_password_field = valid_password
    page.search_run_button_enter.click()
    assert page.get_current_url != url_auth

def test_auth_page_valid_login_and_invalid_password(web_browser):
    """ Make sure auth page valid login and invalid password not works fine. """
    page = MainPage(web_browser)
    page.get(url_auth)
    page.search_login_field = valid_login
    page.search_run_button_enter.click()
    page.search_password_field = invalid_password
    page.search_run_button_enter.click()
    page.wait_page_loaded()
    assert page.get_current_url == url_auth, 'Неверный пароль'

def test_auth_page_invalid_login_and_invalid_password(web_browser):
    """ Make sure auth page invalid login and invalid password not works fine. """
    page = MainPage(web_browser)
    page.get(url_auth)
    page.search_login_field = invalid_login
    page.search_run_button_enter.click()
    page.search_password_field = invalid_password
    page.search_run_button_enter.click()
    page.wait_page_loaded()
    assert page.get_current_url == url_auth, 'Такой логин не подойдет'

def test_auth_page_valid_login_and_withot_password(web_browser):
    """ Make sure auth page invalid login and without password not works fine. """
    page = MainPage(web_browser)
    page.get(url_auth)
    page.search_login_field = valid_login
    page.search_run_button_enter.click()
    page.search_password_field = without_password
    page.search_run_button_enter.click()
    page.wait_page_loaded()
    assert page.get_current_url == url_auth, 'Пароль не указан'

def test_auth_page_without_login(web_browser):
    """ Make sure auth page without login not works fine. """
    page = MainPage(web_browser)
    page.get(url_auth)
    page.search_login_field = without_login
    assert page.get_current_url == url_auth, 'Логин не указан'

def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)
    page.search = 'iPhone 12'
    page.search_run_button.click()
    # Verify that user can see the list of products:
    assert page.products_titles.count() > 0
    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'iphone' in title.lower(), msg


def test_check_wrong_input_in_search(web_browser):
    """ Make sure that wrong keyboard layout input works fine. """

    page = MainPage(web_browser)
    # Try to enter "смартфон" with English keyboard:
    page.search = 'cvfhnajy'
    page.search_run_button.click()
    # Verify that user can see the list of products:
    assert page.products_titles.count() > 0
    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'смартфон' in title.lower(), msg


def test_check_sort_by_price(web_browser):
    """ Make sure that sort by price works fine."""

    page = MainPage(web_browser)
    page.search = 'чайник'
    page.search_run_button.click()
    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    assert page.products_titles.count() > 0


def test_check_sort_products_by_rating(web_browser):
    """ Make sure that sort by rating works fine."""

    page = MainPage(web_browser)
    page.search = 'чайник'
    page.search_run_button.click()
    page.sort_products_by_rating.scroll_to_element()
    page.sort_products_by_rating.click()
    page.wait_page_loaded()
    assert page.products_titles.count() > 0


def test_check_sort_products_by_feedback(web_browser):
    """ Make sure that sort by feedback works fine."""

    page = MainPage(web_browser)
    page.search = 'чайник'
    page.search_run_button.click()
    page.sort_products_by_feedback.scroll_to_element()
    page.sort_products_by_feedback.click()
    page.wait_page_loaded()
    assert page.products_titles.count() > 0


def test_check_sort_products_by_discount(web_browser):
    """ Make sure that sort by discount works fine."""

    page = MainPage(web_browser)
    page.search = 'чайник'
    page.search_run_button.click()
    page.sort_products_by_discount.scroll_to_element()
    page.sort_products_by_discount.click()
    page.wait_page_loaded()
    assert page.products_titles.count() > 0


def test_check_sort_products_by_novelty(web_browser):
    """ Make sure that sort by novelty works fine."""

    page = MainPage(web_browser)
    page.search = 'чайник'
    page.search_run_button.click()
    page.sort_products_by_novelty.scroll_to_element()
    page.sort_products_by_novelty.click()
    page.wait_page_loaded()
    assert page.products_titles.count() > 0


def test_check_button_electronics(web_browser):
    """ Make sure that check button electronics works fine."""

    page = MainPage(web_browser)
    page.search_button_electronics.click()
    page.search_button_electronics.scroll_to_element()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_button_computers(web_browser):
    """ Make sure that check button computers works fine."""

    page = MainPage(web_browser)
    page.search_button_computers.click()
    page.search_button_computers.scroll_to_element()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_button_home_appliances(web_browser):
    """ Make sure that check button home appliances works fine."""

    page = MainPage(web_browser)
    page.search_button_home_appliances.click()
    page.search_button_home_appliances.scroll_to_element()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_button_for_children(web_browser):
    """ Make sure that check button for children works fine."""

    page = MainPage(web_browser)
    page.search_button_for_children.click()
    page.search_button_for_children.scroll_to_element()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_button_dacha(web_browser):
    """ Make sure that check button dacha works fine."""

    page = MainPage(web_browser)
    page.search_button_dacha.click()
    page.search_button_dacha.scroll_to_element()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_button_products(web_browser):
    """ Make sure that check button products works fine."""

    page = MainPage(web_browser)
    page.search_button_products.click()
    page.search_button_products.scroll_to_element()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_button_broadcasts(web_browser):
    """ Make sure that check button broadcasts works fine."""

    page = MainPage(web_browser)
    page.search_button_broadcasts.click()
    page.search_button_broadcasts.scroll_to_element()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_button_start_selling_on_yandex_market(web_browser):
    """ Make sure that check button start selling on yandex market works fine."""

    page = MainPage(web_browser)
    page.search_button_start_selling_on_yandex_market.click()
    page.search_button_start_selling_on_yandex_market.scroll_to_element()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_purchases(web_browser):
    """ Make sure that check tab purchases works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_purchases.scroll_to_element()
    page.search_tab_purchases.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_electronics(web_browser):
    """ Make sure that check tab electronics works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_electronics.scroll_to_element()
    page.search_tab_electronics.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_computers(web_browser):
    """ Make sure that check tab computers works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_computers.scroll_to_element()
    page.search_tab_computers.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_home_appliances(web_browser):
    """ Make sure that check tab home appliances works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_home_appliances.scroll_to_element()
    page.search_tab_home_appliances.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_for_children(web_browser):
    """ Make sure that check tab for children works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_for_children.scroll_to_element()
    page.search_tab_for_children.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_dacha_garden_and_vegetable_garden(web_browser):
    """ Make sure that check tab dacha garden and vegetable garden works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_dacha_garden_and_vegetable_garden.scroll_to_element()
    page.search_tab_dacha_garden_and_vegetable_garden.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_products(web_browser):
    """ Make sure that check tab products works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_products.scroll_to_element()
    page.search_tab_products.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_beauty(web_browser):
    """ Make sure that check tab beauty works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_beauty.scroll_to_element()
    page.search_tab_beauty.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_hygiene(web_browser):
    """ Make sure that check tab hygiene works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_hygiene.scroll_to_element()
    page.search_tab_hygiene.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_pet_supplies(web_browser):
    """ Make sure that check tab pet supplies works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_pet_supplies.scroll_to_element()
    page.search_tab_pet_supplies.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_sports_and_outdoor_activities(web_browser):
    """ Make sure that check tab sports and outdoor activities works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_sports_and_outdoor_activities.scroll_to_element()
    page.search_tab_sports_and_outdoor_activities.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_auto(web_browser):
    """ Make sure that check tab auto works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_auto.scroll_to_element()
    page.search_tab_auto.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_construction_and_repair(web_browser):
    """ Make sure that check tab construction and repair works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_construction_and_repair.scroll_to_element()
    page.search_tab_construction_and_repair.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_household_goods(web_browser):
    """ Make sure that check tab household goods works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_household_goods.scroll_to_element()
    page.search_tab_household_goods.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_furniture(web_browser):
    """ Make sure that check tab furniture works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_furniture.scroll_to_element()
    page.search_tab_furniture.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_clothing_and_shoes(web_browser):
    """ Make sure that check tab clothing and shoes works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_clothing_and_shoes.scroll_to_element()
    page.search_tab_clothing_and_shoes.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_bags_and_suitcases(web_browser):
    """ Make sure that check tab bags and suitcases works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_bags_and_suitcases.scroll_to_element()
    page.search_tab_bags_and_suitcases.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_jewelry(web_browser):
    """ Make sure that check tab jewelry works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_jewelry.scroll_to_element()
    page.search_tab_jewelry.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_health(web_browser):
    """ Make sure that check tab health works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_health.scroll_to_element()
    page.search_tab_health.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_adult_products(web_browser):
    """ Make sure that check tab adult products works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_adult_products.scroll_to_element()
    page.search_tab_adult_products.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_hobbies_and_entertainment(web_browser):
    """ Make sure that check tab hobbies and entertainment works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_hobbies_and_entertainment.scroll_to_element()
    page.search_tab_hobbies_and_entertainment.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_books(web_browser):
    """ Make sure that check tab books works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_books.scroll_to_element()
    page.search_tab_books.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_equipment(web_browser):
    """ Make sure that check tab equipment works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_equipment.scroll_to_element()
    page.search_tab_equipment.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_digital_goods(web_browser):
    """ Make sure that check tab digital goods works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_digital_goods.scroll_to_element()
    page.search_tab_digital_goods.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_school_and_office_supplies(web_browser):
    """ Make sure that check tab school and office supplies works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_school_and_office_supplies.scroll_to_element()
    page.search_tab_school_and_office_supplies.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_discounted_items(web_browser):
    """ Make sure that check tab discounted items works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_discounted_items.scroll_to_element()
    page.search_tab_discounted_items.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_discounts_and_promotions(web_browser):
    """ Make sure that check tab discounts and promotions works fine."""

    page = MainPage(web_browser)
    page.search_catalog_button.click()
    page.wait_page_loaded()
    page.search_tab_discounts_and_promotions.scroll_to_element()
    page.search_tab_discounts_and_promotions.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_tab_view_all_products_coffee(web_browser):
    """ Make sure that check tab view all products coffee works fine."""

    page = MainPage(web_browser)
    page.search_banner_on_main_screen_purchases.click()
    page.search_tab_view_all_products_coffee.scroll_to_element()
    page.search_tab_view_all_products_coffee.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_checkbox_by_manufacturer_of_coffee(web_browser):
    """ Make sure that check checkbox by manufacturer of coffee works fine."""

    page = MainPage(web_browser)
    page.search_banner_on_main_screen_purchases.click()
    page.search_tab_view_all_products_coffee.scroll_to_element()
    page.search_tab_view_all_products_coffee.click()
    page.search_checkbox_by_manufacturer_of_coffee.scroll_to_element()
    page.search_checkbox_by_manufacturer_of_coffee.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_choice_product_of_coffee(web_browser):
    """ Make sure that check choice product of coffee works fine."""

    page = MainPage(web_browser)
    page.search_banner_on_main_screen_purchases.click()
    page.search_tab_view_all_products_coffee.scroll_to_element()
    page.search_tab_view_all_products_coffee.click()
    page.search_checkbox_by_manufacturer_of_coffee.scroll_to_element()
    page.search_checkbox_by_manufacturer_of_coffee.click()
    page.search_choice_product_of_coffee.click()
    page.wait_page_loaded()
    assert page.get_current_url != 'https://market.yandex.ru/'


def test_check_button_by_add_to_cart(web_browser):
    """ Make sure that check button by add to cart works fine."""

    page = MainPage(web_browser)
    page.search_banner_on_main_screen_purchases.click()
    page.search_tab_view_all_products_coffee.scroll_to_element()
    page.search_tab_view_all_products_coffee.click()
    page.search_checkbox_by_manufacturer_of_coffee.scroll_to_element()
    page.search_checkbox_by_manufacturer_of_coffee.click()
    page.search_choice_product_of_coffee.scroll_to_element()
    page.search_choice_product_of_coffee.click()
    page.wait_page_loaded()
    assert page.get_current_url() != 'https://market.yandex.ru/'



