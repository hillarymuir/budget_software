#!/usr/bin/env python

"""
Docstring for budget_software.src.budget_targets_class

Class that holds budget target information and its class functions.

"""

import os
import ast

class BudgetTargets:
    """
    Class that holds budget target information.
    """
    def __init__(self, target_dict=None):
        if target_dict is None:
            self.target_dict = {}
        else:
            self.target_dict = target_dict

        # make sure there is a private/targets
        os.makedirs(os.path.dirname("../private/targets"), exist_ok=True)
        
        # write the new class to file
        with open("../private/targets/curr_target.txt", mode="w+", encoding="utf-8") as f:
            f.write(str(self.target_dict))

    def read_targets(self):
        pass

    def edit_targets(self):
        pass
    
    def add_category(self):
        pass