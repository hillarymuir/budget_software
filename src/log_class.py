#!/usr/bin/env python

"""
Docstring for budget_software.src.log_class

Class for monthly log object.

"""

import csv
from pathlib import Path
import log_entry_class as le_class

# file path hardcoded relative to project root
PROJECT_ROOT = Path(__file__).resolve().parents[1] 
ENTRIES_DIR = PROJECT_ROOT / "private" / "entries"

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
        ENTRIES_DIR.mkdir(parents=True, exist_ok=True)
        self.entries_file = ENTRIES_DIR / f"{self._month_str}.csv"

        # if that monthly log exists, print notice that it is being overwritten
        # TODO: prompt user to confirm overwrite
        if self.entries_file.exists():
            print(f"Overwriting existing {self._month_str} log...")

        self.save_log()

    def get_log_entry_list(self):
        """Get log entry list attribute"""
        return self._log_entries
    
    # TODO: get log (from file)
    def get_log(self):
        """Update self._log_entires with contents of a particular log file and return"""
        with open(self.entries_file, mode="r", encoding="utf-8") as csvfile:
            log_reader = csv.reader(csvfile)
            for row in log_reader:
                if len(row) != 4:
                    raise IndexError(f"Error: one or more rows has improper length such as {row}. Avoid using commas.")
                new_entry = le_class.LogEntry(row[0], row[1], row[2], row[3])
                self._log_entries.append(new_entry)

        return self._log_entries
        
    def save_log(self):
        """Save log entries to file"""
        with open(self.entries_file, "w", encoding="utf-8", newline="") as csvfile:
            log_writer = csv.writer(csvfile)
            for entry in self._log_entries:
                log_writer.writerow(entry)

