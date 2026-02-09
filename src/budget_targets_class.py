#!/usr/bin/env python

"""
Docstring for budget_software.src.budget_targets_class

Class that holds budget target information and its class functions.

"""

import json
from pathlib import Path

# file paths hardcoded relative to project root
PROJECT_ROOT = Path(__file__).resolve().parents[1] 
TARGETS_DIR = PROJECT_ROOT / "private" / "targets"
TARGETS_FILE = TARGETS_DIR / "curr_target.json"

class BudgetTargets:
    """Class that holds budget target information."""
    def __init__(self, target_dict=None):
        if target_dict is None:
            self.target_dict = {}
        else:
            self.target_dict = target_dict

        # make sure there is a ../private/targets
        TARGETS_DIR.mkdir(parents=True, exist_ok=True)

        # if bt file exists, print notice that it is being overwritten 
        # eventually: either prompt user to confirm overwrite or add support for multiple possible target sets
        if TARGETS_FILE.exists():
            print("Overwriting current budget targets...")
        
        # write the new class to file
        with TARGETS_FILE.open(mode="w", encoding="utf-8") as f:
            json.dump(self.target_dict, f, separators=(",", ":"))

    def read_targets(self):
        with open("private/targets/curr_target.json", mode="r", encoding="utf-8") as f:
            file_contents = json.loads(f.read())
        return file_contents

    def edit_targets(self):
        pass
    
    def add_category(self):
        pass