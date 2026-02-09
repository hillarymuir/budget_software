#!/usr/bin/env python

"""
Docstring for budget_software.src.log_class

Class for monthly log object.

"""

class LogEntry:
    """Class for a budget log entry."""
    def __init__(self, date, source, category, dollar_amt):
        self._date = date
        self._source = source
        self._category = category
        self._dollar_amt = dollar_amt

    def __str__(self):
        return f"{self.get("date")}, {self.get("source")}, {self.get("category")}, {self.get("dollar_amt")}"
    
    def get(self, characteristic):
        """Get a log entry class variable"""
        match characteristic:
            case "date":
                return self._date
            case "source":
                return self._source
            case "category":
                return self._category
            case "dollar_amt":
                return self._dollar_amt
            case _:
                raise NameError("Error: Characteristic not found")