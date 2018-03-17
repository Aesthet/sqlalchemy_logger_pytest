"""Module creates table market in in-memory-only SQLite database
"""
import logging
import pytest

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
# Session = sessionmaker() # In case app does'nt yet have Engine when defining module-level objects
# Session.configure(bind=engine)  # once engine is available
session = Session()


class OpencartMarketplace(Base):
    """orm class which map to table market"""
    # def __init__(self, product_id=None, product_name='', product_price=0, product_desc=''):

    __tablename__ = 'market'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    product_price = Column(Float)
    product_desc = Column(String)

    def __repr__(self):
        return f"<OpencartMarketplace(product_name='{self.product_name}', " \
               f"product_price='{self.product_price}', " \
               f"product_desc='{self.product_desc}')>"


Base.metadata.create_all(engine)
product_iphone_x = OpencartMarketplace(product_name='iPhone X', product_price=987.99,
                                       product_desc='iPhone featuring a 5.8-inch OLED display, '
                                                    'facial recognition and 3D camera '
                                                    'functionality, a glass body, and an A11 '
                                                    'Bionic processor')
session.add(product_iphone_x)
session.add_all([
    OpencartMarketplace(product_name='Xiaomi Mi7 Plus', product_price=455,
                        product_desc='6.01-inch  display 18:9, eight-core processor Snapdragon 845,'
                                     ' RAM - 6 GB, dual camera: main 12-megapixel module based on '
                                     'the Sony IMX380 sensor and the second 20-megapixel module, '
                                     'like the OnePlus 5'),
    OpencartMarketplace(product_name='Samsung Galaxy S8+', product_price=875.55,
                        product_desc='6.20-inch touchscreen display 1440:2960, 1.9GHz octa-core '
                                     'Samsung Exynos 8895 processor and it comes with 4GB of RAM, '
                                     '64GB storage')])
session.commit()

# session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
# session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()
# for instance in session.query(User).order_by(User.id):
#     print(instance.name, instance.fullname)
# for name, fullname in session.query(User.name, User.fullname):
#     print(name, fullname)
# for row in session.query(User, User.name).all():
# ...    print(row.User, row.name)
# <User(name='ed', fullname='Ed Jones', password='f8s7ccs')> ed
#
# >>> session.query(User).filter(User.name.like('%ed')).count()
# 2
# >>> from sqlalchemy.sql import exists
# >>> stmt = exists().where(Address.user_id==User.id)
# SQL>>> for name, in session.query(User.name).filter(stmt):
# ...     print(na  me)
# jack
#
# >>> session.delete(jack)
# SQL>>> session.query(User).filter_by(name='jack').count()
# 0
# >>> session.query(Address).filter(
# ...     Address.email_address.in_(['jack@google.com', 'j25@yahoo.com'])
# ...  ).count()
# 2

# # create logger
# module_logger = logging.getLogger('spam_application.auxiliary')
#
#
# class Auxiliary:
#     def __init__(self):
#         self.logger = logging.getLogger('spam_application.auxiliary.Auxiliary')
#         self.logger.info('creating an instance of Auxiliary')
#
#     def do_something(self):
#         self.logger.info('doing something')
#         a = 1 + 1
#         self.logger.info('done doing something')
#
# def some_function():
#     module_logger.info('received a call to "some_function"')