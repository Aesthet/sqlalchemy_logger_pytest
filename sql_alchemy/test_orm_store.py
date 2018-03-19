import os
import pytest

from sql_alchemy.orm_store import OpencartMarketplace
from sql_alchemy.database import init_db
from sql_alchemy.database import db_session

init_db()


def test_create_user(pre_create_product):
    result_set = pre_create_product.query(OpencartMarketplace).filter(OpencartMarketplace.product_name.in_(['iPhoneX', 'iPhone X'])).all()
    assert str(result_set) == "[<OpencartMarketplace(product_name='iPhone X', product_price='987.99', product_desc='iPhone featuring a 5.8-inch OLED display, facial recognition and 3D camera functionality, a glass body, and an A11 Bionic processor')>]"


def test_create_user_static():
    OpencartMarketplace.create_new_product('Nokia', 10, 'unbreakable nokia 3310')
    result_set = db_session.query(OpencartMarketplace).filter(OpencartMarketplace.product_name.in_(['Nokia', 'Nok ia'])).all()
    assert str(result_set) == "[<OpencartMarketplace(product_name='Nokia', product_price='10.0', product_desc='unbreakable nokia 3310')>]"


def test_add_three_products():
    OpencartMarketplace.add_three_products()
    assert OpencartMarketplace.get_products_count() == 4
