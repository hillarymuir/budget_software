#!/usr/bin/env python

"""
Docstring for budget_software.src.category_handling.py

Functions related to handling budget category lists

"""

import csv
from pathlib import Path

# file paths hardcoded relative to project root (may change to be args later)
PROJECT_ROOT = Path(__file__).resolve().parents[1] 
CATS_DIR = PROJECT_ROOT / "private" / "targets"
CATS_FILE = CATS_DIR / "categories.csv"

def load_categories():
    """Load categories from file"""
    cat_list = []

    with open(CATS_FILE, mode="r", encoding="utf-8") as csvfile:
        cat_reader = csv.reader(csvfile)
        for row in cat_reader:
            cat_list.extend(row)

    return cat_list

def save_categories(cat_list):
    """Save categories to file"""
    with open(CATS_FILE, "w", encoding="utf-8", newline="") as csvfile:
        cats_writer = csv.writer(csvfile)
        cats_writer.writerow(cat_list)

def clear_categories():
    """Clear categories to help testing"""
    with open(CATS_FILE, "w", encoding="utf-8", newline="") as f:
        f.write("")

def add_category(category):
    """Add category to list"""

    # make sure there is a ../private/targets/categories.csv
    CATS_DIR.mkdir(parents=True, exist_ok=True)
    if not CATS_FILE.exists():
        with open(CATS_FILE, "w", encoding="utf-8") as csvfile:
            csvfile.write("")

    cat_list = load_categories()
    if category in cat_list:
        print(f"{category} not added; already exists")

    cat_list.append(category)

    save_categories(cat_list)

def del_category(category):
    """Delete category in list"""

    # make sure file exists and category exists
    if not CATS_FILE.exists():
        raise FileNotFoundError(f"File not found to delete {category}")
    cat_list = load_categories()
    if category not in cat_list:
        raise ValueError(f"{category} not found in file, so cannot delete")

    # delete category and save
    cat_list.remove(category)
    save_categories(cat_list)

    # TODO: prompt user whether they want to delete all entries with that category, and if so, do it

def edit_category(old_cat, new_cat):
    """Edit category in list"""

    # make sure file exists and category exists
    if not CATS_FILE.exists():
        raise FileNotFoundError(f"File not found to edit {old_cat}")
    cat_list = load_categories()
    if old_cat not in cat_list:
        raise ValueError(f"{old_cat} not found in file, so cannot edit")

    # delete old_cat, add new_cat, and save
    cat_list.remove(old_cat)
    cat_list.append(new_cat)
    save_categories(cat_list)

    # TODO: automatically change all log entries that use the old category
