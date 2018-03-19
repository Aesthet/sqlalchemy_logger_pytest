import logging

from sql_alchemy.orm_store import OpencartMarketplace
from sql_alchemy.database import init_db


init_db()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='parts/orm_store.log',
                    filemode='w')
OpencartMarketplace.add_three_products()
OpencartMarketplace.get_products_count()
OpencartMarketplace.update_product_by_name('iPhone X', price=899.9, description='Some new description')
OpencartMarketplace.update_product_by_name('iPhone X', description='Other new description')
OpencartMarketplace.find_product_by_name('no such item')
OpencartMarketplace.create_new_product('Nokia', 10, 'unbreakable nokia 3310')
OpencartMarketplace.get_products_count()