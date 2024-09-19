from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

# Define sqlite database
engine = create_engine("sqlite:///personal_finance.db")
Base = declarative_base()


# Define Expense model
class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    category = Column(String)
    date = Column(Date, default=date.today())


# Define Income Model
class Income(Base):
    __tablename__ = "income"
    id = Column(Integer, primary_key=True)
    source = Column(String)
    amount = Column(Float)
    date = Column(Date, default=date.today())


# Create tables
Base.metadata.create_all(engine)

# Setup session
Session = sessionmaker(bind=engine)
session = Session()


# Function to add expense
def add_expense(name: str, amount: float, category: str, dt: date):
    expense = Expense(name=name, amount=amount, category=category, date=dt)
    session.add(expense)
    session.commit()


# Function to add income
def add_income(source: str, amount: float, dt: date):
    income = Income(source=source, amount=amount, date=dt)
    session.add(income)
    session.commit()


# Function to fetch all expenses
def get_expenses():
    return session.query(Expense).all()


# Function to fetch all income
def get_income():
    return session.query(Income).all()
