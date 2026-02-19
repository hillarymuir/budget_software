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

# directory path hardcoded relative to project root
PROJECT_ROOT = Path(__file__).resolve().parents[1] 
TEST_DIR = PROJECT_ROOT / "test"
CATS_DIR = TEST_DIR / "private" / "targets"
CATS_FILE = CATS_DIR / "categories.csv"

class TestFunctions(unittest.TestCase):
    """Tests for functions in category_handling.py."""

    def test_add_category(self):
        """Test category addition"""

        test_cat = "Test category, with comma"
        cats.add_category(TEST_DIR, test_cat)

        cat_list = cats.load_categories(TEST_DIR)

        self.assertIn(test_cat, cat_list)

        cats.clear_categories(TEST_DIR)
        cat_list = cats.load_categories(TEST_DIR)
        self.assertEqual(cat_list, [])

    def test_delete_category(self):
        """Test category deletion"""

        test_cat = "Test category"
        cats.add_category(TEST_DIR, test_cat)

        cats.del_category(TEST_DIR, test_cat)

        cat_list = cats.load_categories(TEST_DIR)

        self.assertNotIn(test_cat, cat_list)

        cats.clear_categories(TEST_DIR)
        cat_list = cats.load_categories(TEST_DIR)
        self.assertEqual(cat_list, [])

    def test_edit_category(self):
        """Test category editing"""

        test_cat = "Test category (original)"
        cats.add_category(TEST_DIR, test_cat)

        revised_cat = "Test category (revised)"

        cats.edit_category(TEST_DIR, test_cat, revised_cat)

        cat_list = cats.load_categories(TEST_DIR)

        self.assertNotIn(test_cat, cat_list)
        self.assertIn(revised_cat, cat_list)

        cats.clear_categories(TEST_DIR)
        cat_list = cats.load_categories(TEST_DIR)
        self.assertEqual(cat_list, [])

    def test_budget_targets_category_creation(self):
        """Test budget targets class's automatic category addition"""
        bt_class.BudgetTargets(TEST_DIR, target_dict={"key": "value"})

        cat_list = cats.load_categories(TEST_DIR)
        self.assertIn("key", cat_list)

        cats.clear_categories(TEST_DIR)
        cat_list = cats.load_categories(TEST_DIR)
        self.assertEqual(cat_list, [])

    def test_log_class_category_creation(self):
        """Test log class's automatic category addition"""
        le_class_instance = le_class.LogEntry(20260101, "Source", "Category", 0.0)
        log_class.Log([le_class_instance])

        cat_list = cats.load_categories(TEST_DIR)
        self.assertIn("Category", cat_list)

        cats.clear_categories(TEST_DIR)
        cat_list = cats.load_categories(TEST_DIR)
        self.assertEqual(cat_list, [])

    def test_delete_category_no_file(self):
        """Test category deletion when there is no categories.csv"""

        test_cat = "Test category"
        CATS_FILE.unlink()

        self.assertRaises(FileNotFoundError, cats.del_category, TEST_DIR, test_cat)

    def test_delete_category_not_in_file(self):
        """Test category deletion when category isn't in file"""

        test_cat = "Test category"
        cats.clear_categories(TEST_DIR)

        self.assertRaises(ValueError, cats.del_category, TEST_DIR, test_cat)
