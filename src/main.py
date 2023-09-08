from src.expense import Expense


if __name__ == '__main__':
    expense1 = Expense(25.50, "Food", "2023-09-01", "Dinner at a restaurant")
    expense2 = Expense(12.99, "Transportation", "2023-09-02", "Bus fare")
    expense3 = Expense(40.00, "Entertainment", "2023-09-03", "Movie night")
    expense4 = Expense(300.00, "Rent", "2023-09-04", "Monthly rent payment")
    expense5 = Expense(8.95, "Food", "2023-09-05", "Lunch at work")
    expense6 = Expense(50.00, "Shopping", "2023-09-06", "New clothes")
    expense7 = Expense(20.00, "Transportation", "2023-09-07", "Taxi ride")
    expense8 = Expense(15.00, "Food", "2023-09-08", "Groceries")

    # List of expenses
    expenses = [expense1, expense2, expense3, expense4, expense5, expense6, expense7, expense8]
    Expense.save_data_to_file(expenses)