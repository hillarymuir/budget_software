#!/usr/bin/env python

"""
Docstring for budget_software.src.test_budget_targets_class

Tests for functions in budget_targets_class.py.

"""

import unittest
import budget_targets_class as bt_class

class TestFunctions(unittest.TestCase):
    """Test budget_targets_class and its functions"""

    def test_bt_class_creation_empty(self):
        """Test creation of BT class with empty dict"""
        bt_class_instance = bt_class.BudgetTargets()

        with open("../private/targets/curr_target.txt", mode="r", encoding="utf-8") as f:
            file_content_str = f.read()
        
        self.assertIsInstance(bt_class_instance, bt_class.BudgetTargets)
        self.assertEqual(bt_class_instance.target_dict, {})
        self.assertEqual(file_content_str, "{}")

    def test_bt_class_creation_with_dict(self):
        """Test creation of BT class with specified dict"""
        bt_class_instance = bt_class.BudgetTargets(target_dict={"key": "value"})

        with open("../private/targets/curr_target.txt", mode="r", encoding="utf-8") as f:
            file_content_str = f.read()
        
        self.assertIsInstance(bt_class_instance, bt_class.BudgetTargets)
        self.assertEqual(bt_class_instance.target_dict, {"key":"value"})
        self.assertEqual(file_content_str, "{\"key\":\"value\"}")