#!/usr/bin/env python

"""
Docstring for budget_software.src.log_class

Class for monthly log object.

"""

from datetime import date

class LogEntry:
    """Class for a budget log entry."""
    def __init__(self, date_, source, category, dollar_amt):

        # check for invalid data types
        if not isinstance(date_, int):
            raise TypeError("Error: date must be int")
        if isinstance(dollar_amt, int):
            dollar_amt = float(dollar_amt)
        if not isinstance(dollar_amt, float):
            raise TypeError("Error: dollar amount must be a number")
        
        # check for invalid dates
        if date_ < 20200000 or date_ > 22000000:
            raise ValueError("Error: year must be between 2020 and 2200")
        try:
            date(int(str(date_)[:3]), int(str(date_)[4:6]), int(str(date_)[6:]))
        except ValueError as e:
            raise ValueError("Error: invalid date") from e
        
        # set attributes
        self.date = date_
        self.source = source
        self.category = category
        self.dollar_amt = dollar_amt

        self.parent = None

        # TODO: add new category if self.category is not in category.csv, and add that category to budget targets

    def __str__(self):
        return f"{self.date},{self.source},{self.category},{self.dollar_amt}"
    
    # edit entry