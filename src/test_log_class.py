#!/usr/bin/env python

"""
Docstring for budget_software.src.log_class

Tests for functions in log_class.py.

"""

import unittest
import log_class
import log_entry_class as le_class

class TestFunctions(unittest.TestCase):
    """Test log class and its functions"""

    def test_log_creation_with_entry(self):
        """Test log class with one entry and ability to get_log that log"""

        le_class_instance = le_class.LogEntry(20260101, "Source", "Category", 0.0)
        log_class_instance = log_class.Log([le_class_instance])

        self.assertIsInstance(log_class_instance, log_class.Log)
        self.assertIsInstance(log_class_instance.get_log_entry_list(), list)
        for entry in log_class_instance.get_log_entry_list():
            self.assertIsInstance(entry, le_class.LogEntry)

        # check file-writing
        with open(f"private/entries/{log_class_instance.name}.csv", mode="r", encoding="utf-8") as f:
            file_content_str = f.read()

        self.assertEqual(file_content_str, "20260101,Source,Category,0.0\n")

        # test get_log() using the new log created above
        log_from_file = log_class.get_log(f"private/entries/{log_class_instance.name}.csv")
        self.assertIsInstance(log_from_file, log_class.Log)
        self.assertIsInstance(log_from_file.get_log_entry_list(), list)
        for entry in log_from_file.get_log_entry_list():
            self.assertIsInstance(entry, le_class.LogEntry)

    def test_log_creation_with_bad_entry(self):
        """Test creation of log class with non-list entry"""

        le_class_instance = le_class.LogEntry(20260101, "Source", "Category", 0.0)

        self.assertRaises(TypeError, log_class.Log, le_class_instance)

    def test_log_creation_empty(self):
        """Test creation of empty log class"""

        log_class_instance = log_class.Log()

        self.assertIsInstance(log_class_instance, log_class.Log)
        self.assertEqual(log_class_instance.get_log_entry_list(), [])

        # check file-writing
        with open(f"private/entries/{log_class_instance.name}.csv", mode="r", encoding="utf-8") as f:
            file_content_str = f.read()

        self.assertEqual(file_content_str, "")

    def test_log_creation_with_mixed_entry_types(self):
        """Test creation of log class where not all arguments are entries"""

        le_class_instance = le_class.LogEntry(20260101, "Source", "Category", 0.0)

        self.assertRaises(TypeError, log_class.Log, [le_class_instance, 0])

    def test_log_creation_with_mixed_months(self):
        """Test creation of log class with different months"""

        le_class_instance1 = le_class.LogEntry(20260101, "Source", "Category", 0.0)
        le_class_instance2 = le_class.LogEntry(20260201, "Source", "Category", 0.0)
        
        self.assertRaises(ValueError, log_class.Log, [le_class_instance1, le_class_instance2])

    def test_log_entry_parent(self):
        """Test LE parent-setting"""

        le_class_instance = le_class.LogEntry(20260101, "Source", "Category", 0.0)
        log_class_instance = log_class.Log([le_class_instance])

        self.assertIs(le_class_instance.parent, log_class_instance)