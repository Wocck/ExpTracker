import pytest
from src.expense import Expense


def test_expense_constructor():
    expense1 = Expense(25.50, "Food", "2023-09-01", "Dinner at a restaurant")
    assert expense1.amount == 25.50
    assert expense1.category == "Food"
    assert expense1.date == "2023-09-01"
    assert expense1.description == "Dinner at a restaurant"


def test_expense_str():
    expense1 = Expense(25.50, "Food", "2023-09-01", "Dinner at a restaurant")
    assert str(expense1) == "Expense: 25.5, Food, 2023-09-01, Dinner at a restaurant"


def test_expense_to_dict():
    expense1 = Expense(25.50, "Food", "2023-09-01", "Dinner at a restaurant")
    assert expense1.to_dict() == {
        "amount": 25.50,
        "category": "Food",
        "date": "2023-09-01",
        "description": "Dinner at a restaurant"
    }


def test_expense_from_dict():
    data = {
        "amount": 25.50,
        "category": "Food",
        "date": "2023-09-01",
        "description": "Dinner at a restaurant"
    }
    expense1 = Expense.from_dict(data)
    assert expense1.amount == 25.50
    assert expense1.category == "Food"
    assert expense1.date == "2023-09-01"
    assert expense1.description == "Dinner at a restaurant"


def test_expense_load_data_to_list():
    expenses = Expense.load_data_to_list("../tests/test_data/test_expense_read_data.json")
    assert len(expenses) == 3
    assert expenses[0].amount == 25.50
    assert expenses[0].category == "Food"
    assert expenses[2].description == "Movie night"
    assert expenses[2].date == "2023-09-03"


def test_expense_save_to_file():
    read_path = "../tests/test_data/test_expense_read_data.json"
    write_path = "../tests/test_data/test_expense_write_data.json"
    # Clear the file
    with open(write_path, "w"):
        pass

    # Load data from read_path and save it to write_path
    expenses = Expense.load_data_to_list(read_path)

    # Save data to file
    Expense.save_data_to_file(expenses, write_path)

    # Read data from file
    read_expenses = Expense.load_data_to_list(write_path)
    assert len(read_expenses) == 3
    assert expenses[0].amount == 25.50
    assert expenses[0].category == "Food"
    assert expenses[2].description == "Movie night"
    assert expenses[2].date == "2023-09-03"

