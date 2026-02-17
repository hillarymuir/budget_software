#!/usr/bin/env python

"""
Docstring for budget_software.src.test_spreadsheet_class

Tests for functions in spreadsheet_class.py.

"""

import unittest

import budget_targets_class as bt_class
import log_entry_class as le_class
import log_class
import spreadsheet_class as sheet_class

class TestFunctions(unittest.TestCase):

    def test_spreadsheet_creation(self):
        """Test creation of spreadsheet class"""
        bt_class_instance = bt_class.BudgetTargets()
        le_class_instance = le_class.LogEntry(20260101, "Source", "Category", 1.11)
        log_class_instance = log_class.Log([le_class_instance])

        spreadsheet = sheet_class.Spreadsheet(log_class_instance, bt_class_instance)
        
        self.assertIsInstance(spreadsheet, sheet_class.Spreadsheet)
        self.assertIs(spreadsheet.log, log_class_instance)
        self.assertIs(spreadsheet.targets, bt_class_instance)
        self.assertEqual(spreadsheet.month, int(log_class_instance.name))
        self.assertEqual(1.11, spreadsheet.money_remaining)