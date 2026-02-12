#!/usr/bin/env python

"""
Docstring for budget_software.src.log_entry_class

Tests for functions in log_entry_class.py.

"""

import unittest
import log_entry_class as le_class

class TestFunctions(unittest.TestCase):
    """Test log entry class and its functions"""

    def test_log_entry_creation(self):
        """Test creation of LE class"""

        le_class_instance = le_class.LogEntry(20260101, "Source", "Category", 0.0)

        self.assertIsInstance(le_class_instance, le_class.LogEntry)
        self.assertEqual(str(le_class_instance), "20260101,Source,Category,0.0")

    def test_log_entry_date_str(self):
        """Test creation of LE class with a string for a date"""

        self.assertRaises(TypeError, le_class.LogEntry, "Jan 1, 2026", "Source", "Category", 0.0)

    def test_log_entry_date_low(self):
        """Test creation of LE class with too-early date"""

        self.assertRaises(ValueError, le_class.LogEntry, 20190101, "Source", "Category", 0.0)
    
    def test_log_entry_date_high(self):
        """Test creation of LE class with too-late date"""

        self.assertRaises(ValueError, le_class.LogEntry, 23000101, "Source", "Category", 0.0)

    def test_log_entry_date_bad_month(self):
        """Test creation of LE class with bad month"""

        self.assertRaises(ValueError, le_class.LogEntry, 20260001, "Source", "Category", 0.0)

    def test_log_entry_date_bad_day(self):
        """Test creation of LE class with bad month"""

        self.assertRaises(ValueError, le_class.LogEntry, 20260230, "Source", "Category", 0.0)

    def test_log_entry_date_bad_leapday(self):
        """Test creation of LE class with bad month"""

        self.assertRaises(ValueError, le_class.LogEntry, 20260229, "Source", "Category", 0.0)

    def test_log_entry_date_int_dollar_amt(self):
        """Test creation of LE class with integer dollar amount"""

        le_class_instance = le_class.LogEntry(20260101, "Source", "Category", 1)

        self.assertIsInstance(le_class_instance, le_class.LogEntry)
        self.assertEqual(str(le_class_instance), "20260101,Source,Category,1.0")

    def test_log_entry_date_bad_dollar_amt(self):
        """Test creation of LE class with bad dollar amount"""

        self.assertRaises(TypeError, le_class.LogEntry, 20260101, "Source", "Category", "ten dollars")
