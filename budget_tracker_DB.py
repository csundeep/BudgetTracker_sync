from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, DECIMAL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()


class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    type = Column(String(250), nullable=False)
    logo = Column(Integer, nullable=False)
    color = Column(Integer, nullable=False)
    created_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    mobile = Column(Integer, nullable=True)
    initial_amount = Column(Integer, nullable=False, default=0)
    created_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)


class Budgets(Base):
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    amount = Column(DECIMAL, nullable=False, default=0)
    expenses = Column(String(250), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    isNotificationsRequired = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    restaurant = relationship(Users)
    created_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)


class Expenses(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    type = Column(String(250), nullable=False)
    amount = Column(DECIMAL, nullable=False, default=0)
    latitude = Column(DECIMAL, nullable=True)
    longitude = Column(DECIMAL, nullable=True)
    notes = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    restaurant = relationship(Users)
    created_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)


# class MenuItem(Base):
#     __tablename__ = 'menu_item'
#
#     name = Column(String(80), nullable=False)
#     id = Column(Integer, primary_key=True)
#     description = Column(String(250))
#     price = Column(String(8))
#     course = Column(String(250))
#     restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
#     restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///budgetTracker.db', echo=True)
Base.metadata.create_all(engine)
