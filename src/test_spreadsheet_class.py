#!/usr/bin/env python

"""
Docstring for budget_software.src.test_spreadsheet_class

Tests for functions in spreadsheet_class.py.

"""

import unittest
from pathlib import Path

import budget_targets_class as bt_class
import log_entry_class as le_class
import log_class
import spreadsheet_class as sheet_class

# directory path hardcoded relative to project root
PROJECT_ROOT = Path(__file__).resolve().parents[1] 
TEST_DIR = PROJECT_ROOT / "test"

class TestFunctions(unittest.TestCase):
    """Spreadsheet class unit tests"""

    def test_spreadsheet_creation(self):
        """Test creation of spreadsheet class"""
        bt_class_instance = bt_class.BudgetTargets(TEST_DIR, {"Category": 50.0})
        le_class_instance = le_class.LogEntry(20260101, "Source", "Category", 1.11)
        log_class_instance = log_class.Log(TEST_DIR, [le_class_instance])

        spreadsheet = sheet_class.Spreadsheet(log_class_instance, bt_class_instance, 0.0)
        
        self.assertIsInstance(spreadsheet, sheet_class.Spreadsheet)
        self.assertIs(spreadsheet.log, log_class_instance)
        self.assertIs(spreadsheet.targets, bt_class_instance)
        self.assertEqual(spreadsheet.month, int(log_class_instance.name))
        self.assertEqual(spreadsheet.money_remaining, 1.11)
        self.assertEqual(spreadsheet.cat_dict, {"Category": 1.11})
