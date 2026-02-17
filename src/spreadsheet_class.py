#!/usr/bin/env python

"""
Docstring for budget_software.src.spreadsheet_class

Class for spreadsheet (which contains budget targets alongside budget expenditures.)

"""

import log_class
import budget_targets_class

class Spreadsheet:
    """Class that holds a budget spreadsheet for one month."""
    def __init__(self, log_obj, targets_obj, starting_money):
        self.log = log_obj
        self.targets = targets_obj
        self.month = int(self.log.name)

        # calculate money remaining
        self.money_remaining = starting_money
        for entry in self.log.get_log_entry_list():
            self.money_remaining += entry.dollar_amt

        # sum each category
        self.cat_dict = {}
        for cat in self.targets.get_targets():
            self.cat_dict[cat] = 0.0
        for entry in self.log.get_log_entry_list():
            self.cat_dict[entry.category] += entry.dollar_amt