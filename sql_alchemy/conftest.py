
import pytest

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sql_alchemy.orm_store import OpencartMarketplace


# @pytest.fixture(scope='session')
# def db_prepare():
#     """an Engine, which the Session will use for connection resources"""
#     engine = create_engine('sqlite:///:memory:', echo=True)
#     # create a configured "Session" class
#     Session = sessionmaker(bind=engine)
#     Base = declarative_base()
#     OpencartMarketplace.metadata.create_all(engine)
#     session = Session()
#     return session

@pytest.fixture(scope='session')
def engine_prepare():
    return create_engine('sqlite:///:memory:')


@pytest.yield_fixture(scope='session')
def prepare_table(engine_prepare):
    OpencartMarketplace.metadata.create_all(engine_prepare)

    yield

    OpencartMarketplace.metadata.drop_all(engine_prepare)


@pytest.yield_fixture
def db_session(engine_prepare, prepare_table):
    """Returns a  session, and after test run tears down everything"""
    connection = engine_prepare.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.yield_fixture
def pre_create_product(db_session):
    product_iphone_x = OpencartMarketplace.create_new_product('iPhone X', 987.99,
                                                              'iPhone featuring a 5.8-inch OLED display, '
                                                              'facial recognition and 3D camera '
                                                              'functionality, a glass body, and an A11 '
                                                              'Bionic processor')
    db_session.add(product_iphone_x)

    yield db_session

    db_session.delete(product_iphone_x)


