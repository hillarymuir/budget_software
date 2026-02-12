#!/usr/bin/env python

"""
Docstring for budget_software.src.category_handling

Tests for functions in category_handling.py.

"""

import unittest
import csv
from pathlib import Path

import log_class
import log_entry_class as le_class
import budget_targets_class as bt_class
import category_handling as cats



# file paths hardcoded relative to project root
PROJECT_ROOT = Path(__file__).resolve().parents[1] 
CATS_DIR = PROJECT_ROOT / "private" / "targets"
CATS_FILE = CATS_DIR / "categories.csv"

class TestFunctions(unittest.TestCase):
    """Tests for functions in category_handling.py."""

    def test_add_category(self):
        """Test category addition"""

        test_cat = "Test category, with comma"
        cats.add_category(test_cat)

        with open(CATS_FILE, mode="r", encoding="utf-8") as csvfile:
            cat_list = csv.reader(csvfile)[0]
        
        self.assertIn(test_cat, cat_list)

    def test_delete_category(self):
        """Test category deletion"""
        pass

    def test_edit_category(self):
        """Test category editing"""
        pass

    def test_budget_targets_category_creation(self):
        """Test budget targets class's automatic category addition"""
        pass

    def test_log_class_category_creation(self):
        """Test log class's automatic category addition"""
        pass