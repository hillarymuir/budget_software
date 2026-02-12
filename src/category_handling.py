#!/usr/bin/env python

"""
Docstring for budget_software.src.category_handling.py

Functions related to handling budget category lists

"""

import csv
from pathlib import Path

# file paths hardcoded relative to project root
PROJECT_ROOT = Path(__file__).resolve().parents[1] 
CATS_DIR = PROJECT_ROOT / "private" / "targets"
CATS_FILE = CATS_DIR / "categories.csv"

def add_category(category):
    """Add category to list"""
    pass

def del_category(category):
    """Delete category in list"""
    # TODO: prompt user instead of just deleting all entries with that category
    pass

def edit_category(old_cat, new_cat):
    """Edit category in list"""
    # TODO: automatically change all entries that use the old category
    pass