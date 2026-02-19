#!/usr/bin/env python

"""
Docstring for budget_software.src.category_handling.py

Functions related to handling budget category lists

"""

import csv

def load_categories(dir_path):
    """Load categories from file"""
    cat_list = []

    with open(dir_path / "private" / "targets" / "curr_target.json", mode="r", encoding="utf-8") as csvfile:
        cat_reader = csv.reader(csvfile)
        for row in cat_reader:
            cat_list.extend(row)

    return cat_list

def save_categories(dir_path, cat_list):
    """Save categories to file"""
    with open(dir_path / "private" / "targets" / "curr_target.json", "w", encoding="utf-8", newline="") as csvfile:
        cats_writer = csv.writer(csvfile)
        cats_writer.writerow(cat_list)

def clear_categories(dir_path):
    """Clear categories to help testing"""
    with open(dir_path / "private" / "targets" / "curr_target.json", "w", encoding="utf-8", newline="") as f:
        f.write("")

def add_category(dir_path, category):
    """Add category to list"""

    cats_dir = dir_path / "private" / "targets"
    cats_file = cats_dir / "curr_target.json"

    # make sure there is a ../private/targets/categories.csv
    cats_dir.mkdir(parents=True, exist_ok=True)
    if not cats_file.exists():
        with open(cats_file, "w", encoding="utf-8") as csvfile:
            csvfile.write("")

    cat_list = load_categories(dir_path)
    if category in cat_list:
        print(f"{category} not added; already exists")

    cat_list.append(category)

    save_categories(dir_path, cat_list)

def del_category(dir_path, category):
    """Delete category in list"""

    cats_file = dir_path / "private" / "targets" / "curr_target.json"

    # make sure file exists and category exists
    if not cats_file.exists():
        raise FileNotFoundError(f"File not found to delete {category}")
    cat_list = load_categories(dir_path)
    if category not in cat_list:
        raise ValueError(f"{category} not found in file, so cannot delete")

    # delete category and save
    cat_list.remove(category)
    save_categories(dir_path, cat_list)

    # TODO: prompt user whether they want to delete all entries with that category, and if so, do it

def edit_category(dir_path, old_cat, new_cat):
    """Edit category in list"""

    cats_file = dir_path / "private" / "targets" / "curr_target.json"

    # make sure file exists and category exists
    if not cats_file.exists():
        raise FileNotFoundError(f"File not found to edit {old_cat}")
    cat_list = load_categories(dir_path)
    if old_cat not in cat_list:
        raise ValueError(f"{old_cat} not found in file, so cannot edit")

    # delete old_cat, add new_cat, and save
    cat_list.remove(old_cat)
    cat_list.append(new_cat)
    save_categories(dir_path, cat_list)

    # TODO: automatically change all log entries that use the old category
