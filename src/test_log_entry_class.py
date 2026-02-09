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
        """Test creation of LE class and its get() function"""

        le_class_instance = le_class.LogEntry(20260101, "Source", "Category", 0.0)

        self.assertIsInstance(le_class_instance, le_class.LogEntry)
        self.assertEqual(str(le_class_instance), "20260101, Source, Category, 0.0")