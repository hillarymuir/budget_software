#!/usr/bin/env python

"""
Docstring for budget_software.src.log_class

Class for monthly log object.

"""

from pathlib import Path
import log_entry_class as le_class

# file path hardcoded relative to project root
PROJECT_ROOT = Path(__file__).resolve().parents[1] 
TARGETS_DIR = PROJECT_ROOT / "private" / "entries"

class Log:
    """Class that holds monthly log of entries."""
    def __init__(self, log_entries=None):

        # confirm that parameter is a list of log entry class instances or else empty
        if log_entries is None:
            self._log_entries = []
        elif isinstance(log_entries, list):
            if all(isinstance(entry, le_class.LogEntry) for entry in log_entries):
                # confirm that all log entries are for the same month
                same_month = True
                self._month_str = str(log_entries[0].date)[:6]
                for entry in log_entries:
                    if str(entry.date)[:6] != self._month_str:
                        same_month = False
                if same_month:
                    self._log_entries = log_entries
                else:
                    raise ValueError("Error: every log entry in a log must be from the same month")
            else:
                raise TypeError("Error: every log entry must be a log entry class instance")
        else:
            raise TypeError("Error: Log argument must be a list (of log entry objects)")

        # handle creating/saving to file
        # make sure there is a ../private/entries
        TARGETS_DIR.mkdir(parents=True, exist_ok=True)
        
    def get_log_entry_list(self):
        """Get log entry list attribute"""
        return self._log_entries
        
