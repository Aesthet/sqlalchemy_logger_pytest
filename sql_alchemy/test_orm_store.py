import os
import pytest

from sql_alchemy.orm_store import OpencartMarketplace


def test_create_user(pre_create_product):
    result_set = pre_create_product.query(OpencartMarketplace).filter(OpencartMarketplace.product_name.in_(['iPhoneX', 'iPhone X'])).all()
    assert str(result_set) == "[<OpencartMarketplace(product_name='iPhone X', product_price='987.99', product_desc='iPhone featuring a 5.8-inch OLED display, facial recognition and 3D camera functionality, a glass body, and an A11 Bionic processor')>]"


def test_add_three_products(db_session):
    session = db_session
    OpencartMarketplace.add_three_products()
    assert OpencartMarketplace.get_products_count() == 3
