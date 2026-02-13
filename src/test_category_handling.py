#!/usr/bin/env python

"""
Docstring for budget_software.src.category_handling

Tests for functions in category_handling.py.

"""

import unittest
from pathlib import Path

import log_class
import log_entry_class as le_class
import budget_targets_class as bt_class
import category_handling as cats

# TODO: change tests so running them won't overwrite actual user data,
# maybe by adding file to access as an arg instead of hard-coding

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

        cat_list = cats.load_categories()

        self.assertIn(test_cat, cat_list)

        cats.clear_categories()
        cat_list = cats.load_categories()
        self.assertEqual(cat_list, [])

    def test_delete_category(self):
        """Test category deletion"""

        test_cat = "Test category"
        cats.add_category(test_cat)

        cats.del_category(test_cat)

        cat_list = cats.load_categories()

        self.assertNotIn(test_cat, cat_list)

        cats.clear_categories()
        cat_list = cats.load_categories()
        self.assertEqual(cat_list, [])

    def test_edit_category(self):
        """Test category editing"""

        test_cat = "Test category (original)"
        cats.add_category(test_cat)

        revised_cat = "Test category (revised)"

        cats.edit_category(test_cat, revised_cat)

        cat_list = cats.load_categories()

        self.assertNotIn(test_cat, cat_list)
        self.assertIn(revised_cat, cat_list)

        cats.clear_categories()
        cat_list = cats.load_categories()
        self.assertEqual(cat_list, [])

    def test_budget_targets_category_creation(self):
        """Test budget targets class's automatic category addition"""
        bt_class.BudgetTargets(target_dict={"key": "value"})

        cat_list = cats.load_categories()
        self.assertIn("key", cat_list)

        cats.clear_categories()
        cat_list = cats.load_categories()
        self.assertEqual(cat_list, [])

    def test_log_class_category_creation(self):
        """Test log class's automatic category addition"""
        le_class_instance = le_class.LogEntry(20260101, "Source", "Category", 0.0)
        log_class.Log([le_class_instance])

        cat_list = cats.load_categories()
        self.assertIn("Category", cat_list)

        cats.clear_categories()
        cat_list = cats.load_categories()
        self.assertEqual(cat_list, [])

    def test_delete_category_no_file(self):
        """Test category deletion when there is no categories.csv"""

        test_cat = "Test category"
        CATS_FILE.unlink()

        self.assertRaises(FileNotFoundError, cats.del_category, test_cat)

    def test_delete_category_not_in_file(self):
        """Test category deletion when category isn't in file"""

        test_cat = "Test category"
        cats.clear_categories()

        self.assertRaises(ValueError, cats.del_category, test_cat)
