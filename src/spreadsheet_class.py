#!/usr/bin/env python

"""
Docstring for budget_software.src.spreadsheet_class

Class for spreadsheet (which contains budget targets alongside budget expenditures.)

"""

import log_class
import budget_targets_class

class Spreadsheet:
    """Class that holds a budget spreadsheet for one month."""
    def __init__(self, log_obj, targets_obj):
        self.log = log_obj
        self.targets = targets_obj
        self.month = int(self.log.name)

        # calculate money remaining
        self.money_remaining = 0.0
        for entry in self.log.get_log_entry_list():
            self.money_remaining += entry.dollar_amt

    def update_spreadsheet(self):
        """Updates targets and totals based on log."""
        pass