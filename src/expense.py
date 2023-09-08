from src.fileIO import json_read, json_write


class Expense:
    def __init__(self, amount, category, date, description=""):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __str__(self):
        return f"Expense: {self.amount}, {self.category}, {self.date}, {self.description}"

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["amount"], data["category"], data["date"],  data["description"])

    @classmethod
    def load_data_to_list(cls, path):
        data = json_read(path)
        expenses = []
        for expense in data:
            expenses.append(cls.from_dict(expense))
        return expenses

    @classmethod
    def save_data_to_file(cls, expenses, path):
        data = []
        for expense in expenses:
            data.append(expense.to_dict())
        json_write(data, path)
