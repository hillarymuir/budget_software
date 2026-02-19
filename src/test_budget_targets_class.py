#!/usr/bin/env python

"""
Docstring for budget_software.src.test_budget_targets_class

Tests for functions in budget_targets_class.py.

"""

import unittest
from pathlib import Path

import budget_targets_class as bt_class

# directory path hardcoded relative to project root
PROJECT_ROOT = Path(__file__).resolve().parents[1] 
TEST_DIR = PROJECT_ROOT / "test"

class TestFunctions(unittest.TestCase):
    """Test budget_targets_class and its functions"""

    def test_bt_class_creation_empty(self):
        """Test creation of BT class with empty dict"""
        bt_class_instance = bt_class.BudgetTargets(TEST_DIR)

        with open(TEST_DIR / "private" / "targets" / "curr_target.json", mode="r", encoding="utf-8") as f:
            file_content_str = f.read()
        
        self.assertIsInstance(bt_class_instance, bt_class.BudgetTargets)
        self.assertEqual(bt_class_instance.get_targets(), {})
        self.assertEqual(file_content_str, "{}")

    def test_bt_class_creation_with_dict(self):
        """Test creation of BT class with specified dict"""
        bt_class_instance = bt_class.BudgetTargets(TEST_DIR, target_dict={"key": "value"})

        with open(TEST_DIR / "private" / "targets" / "curr_target.json", mode="r", encoding="utf-8") as f:
            file_content_str = f.read()
        
        self.assertIsInstance(bt_class_instance, bt_class.BudgetTargets)
        self.assertEqual(bt_class_instance.get_targets(), {"key":"value"})
        self.assertEqual(file_content_str, "{\"key\":\"value\"}")

    def test_bt_class_get(self):
        """Test get_targets function of BT class"""
        bt_class_instance = bt_class.BudgetTargets(TEST_DIR, target_dict={"key": "value"})

        file_contents_dict = bt_class_instance.get_targets()
        
        self.assertEqual(file_contents_dict, {"key": "value"})

    def test_bt_class_delete(self):
        """Test delete_target function of BT class with a key that exists"""
        bt_class_instance = bt_class.BudgetTargets(TEST_DIR, target_dict={"key": "value"})

        bt_class_instance.delete_target("key")

        file_contents_dict = bt_class_instance.get_targets()
        
        self.assertEqual(file_contents_dict, {})

    def test_bt_class_delete_does_not_exist(self):
        """Test delete_target function of BT class with a key that does not exist"""
        bt_class_instance = bt_class.BudgetTargets(TEST_DIR, target_dict={"key": "value"})

        self.assertRaises(KeyError, bt_class_instance.delete_target, TEST_DIR, "bad_key")

    def test_bt_class_add(self):
        """Test add_or_change_target function of BT class for adding a target"""
        bt_class_instance = bt_class.BudgetTargets(TEST_DIR, target_dict={"key": "value"})

        bt_class_instance.add_or_change_target("key2", "value2")

        file_contents_dict = bt_class_instance.get_targets()
        
        self.assertEqual(file_contents_dict, {"key": "value", "key2": "value2"})

    def test_bt_class_change(self):
        """Test add_or_change_target function of BT class for changing a target"""
        bt_class_instance = bt_class.BudgetTargets(TEST_DIR, target_dict={"key": "value"})

        bt_class_instance.add_or_change_target("key", "new_value")

        file_contents_dict = bt_class_instance.get_targets()
        
        self.assertEqual(file_contents_dict, {"key": "new_value"})
        