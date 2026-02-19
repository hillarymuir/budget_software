#!/usr/bin/env python

"""
Docstring for budget_software.src.budget_targets_class

Class that holds budget target information and its class functions.

"""

import json
from pathlib import Path

import category_handling as cats

class BudgetTargets:
    """Class that holds budget target information."""
    def __init__(self, dir_path, target_dict=None):
        if target_dict is None:
            self._target_dict = {}
        else:
            self._target_dict = target_dict

        self.dir_path = dir_path
        self.targets_dir = self.dir_path / "private" / "targets"
        self.targets_file = self.targets_dir / "curr_target.json"

        # add keys to category list
        for key in self._target_dict:
            cats.add_category(dir_path, key)

        # make sure there is a ../private/targets
        self.targets_dir.mkdir(parents=True, exist_ok=True)

        # if bt file exists, print notice that it is being overwritten 
        # TODO: either prompt user to confirm overwrite or add support for multiple possible target sets
        if self.targets_file.exists():
            print("Overwriting current budget targets...")
        
        # write the new class to file
        self.save_targets()

    def get_targets(self):
        """Update self.target_dict with contents of curr_target.json and return"""
        with open(self.targets_file, mode="r", encoding="utf-8") as f:
            self._target_dict = json.loads(f.read())
        return self._target_dict
    
    def save_targets(self):
        """Save self.target_dict to file"""
        with self.targets_file.open(mode="w", encoding="utf-8") as f:
            json.dump(self._target_dict, f, separators=(",", ":"))

    def delete_target(self, to_delete_key):
        """Delete a target and resave"""
        if to_delete_key not in self._target_dict:
            raise KeyError("Deletion target does not exist in target dictionary")

        del self._target_dict[to_delete_key]
        self.save_targets()

    def add_or_change_target(self, to_add_key, to_add_value=0.0):
        """Add or change a target and resave"""
        self._target_dict[to_add_key] = to_add_value
        self.save_targets()

        # add key of added target to categories
        cat_list = cats.load_categories(self.dir_path)
        if to_add_key not in cat_list:
            cats.add_category(self.dir_path, to_add_key)
