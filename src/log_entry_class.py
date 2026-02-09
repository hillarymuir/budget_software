#!/usr/bin/env python

"""
Docstring for budget_software.src.log_class

Class for monthly log object.

"""

class LogEntry:
    """Class for a budget log entry."""
    def __init__(self, date, source, category, dollar_amt):
        self.date = date
        self.source = source
        self.category = category
        self.dollar_amt = dollar_amt

    def __str__(self):
        return f"{self.date}, {self.source}, {self.category}, {self.dollar_amt}"