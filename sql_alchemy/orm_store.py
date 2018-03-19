"""Module creates table market in in-memory-only SQLite database"""
import logging

from sqlalchemy import Column, Integer, String, Float
from sql_alchemy.database import db_session, Base


class OpencartMarketplace(Base):
    """orm class which map to table market"""

    __tablename__ = 'market'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    product_price = Column(Float)
    product_desc = Column(String)

    def __repr__(self):
        logging.debug('Representation method called')
        return f"<OpencartMarketplace(product_name='{self.product_name}', " \
               f"product_price='{self.product_price}', " \
               f"product_desc='{self.product_desc}')>"

    @staticmethod
    def find_product_by_name(name):
        logging.info(f'Search for product "{name}" performed')
        for product in db_session.query(OpencartMarketplace). \
                filter(OpencartMarketplace.product_name == name):
            logging.info(f'Product "{name}" found')
            return product
        logging.info(f'Product "{name}" is missing')

    @staticmethod
    def create_new_product(name, price, description):
        logging.info(f'Adding new product: "{name}" to database')
        new_product = OpencartMarketplace(product_name=str(name), product_price=float(price),
                                          product_desc=str(description))
        db_session.add(new_product)
        logging.info(f'Product "{name}" added to database')

    @staticmethod
    def update_product_by_name(name, price=None, description=None):
        logging.info(f'Trying to update product: "{name}"')
        update_product = db_session.query(OpencartMarketplace).filter_by(product_name=name).first()
        if price is None and description is None:
            logging.info(f'No new info for product: "{name}" provided, so no changes made')
        elif price is None:
            update_product.product_description = description
            logging.info(f'Updated product description: "{description}" for product: "{name}"')
        elif description is None:
            logging.info(f'Updated product price: "{price}" for product: "{name}"')
            update_product.product_price = price
        else:
            update_product.product_description = description
            update_product.product_price = price
            logging.info(f'Updated product description: "{description}" and product price: '
                         f'"{price}"for product: "{name}"')

    @staticmethod
    def delete_product_by_name(name):
        logging.info(f'Deleting product: "{name}" from database')
        delete_product = db_session.query(OpencartMarketplace).filter_by(product_name=name).first()
        db_session.delete(delete_product)
        logging.info(f'Product: "{name}" deleted')

    @staticmethod
    def get_products_count():
        logging.info('Getting count of all products in database')
        count_ = db_session.query(OpencartMarketplace).count()
        logging.info(f'There are "{count_}" all products in database')
        return count_

    @staticmethod
    def add_three_products():
        logging.info('Adding 3 products (smart phones) to database')
        db_session.add_all([
            OpencartMarketplace(product_name='iPhone X', product_price=987.99,
                                product_desc='iPhone featuring a 5.8-inch OLED display, '
                                             'facial recognition and 3D camera functionality, '
                                             'a glass body, and an A11 Bionic processor'),
            OpencartMarketplace(product_name='Xiaomi Mi7 Plus', product_price=455,
                                product_desc='6.01-inch  display 18:9, eight-core processor Snapdragon 845,'
                                             ' RAM - 6 GB, dual camera: main 12-megapixel module based on '
                                             'the Sony IMX380 sensor and the second 20-megapixel module, '
                                             'like the OnePlus 5'),
            OpencartMarketplace(product_name='Samsung Galaxy S8+', product_price=875.55,
                                product_desc='6.20-inch touchscreen display 1440:2960, 1.9GHz octa-core '
                                             'Samsung Exynos 8895 processor and it comes with 4GB of RAM, '
                                             '64GB storage')])
        logging.info('Commiting')
