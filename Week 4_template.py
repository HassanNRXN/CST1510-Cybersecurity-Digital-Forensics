"""
RECORD CHECK  -  my version
============================

Name  : Syed Hassan Raza
Lane  : Cyber Security
Date  : 14/10/2026

Run it: python template.py
"""

# ========================================================= FUNCTIONS

def status_of(percent, warning_at=90):
    """Return 'OVER LIMIT', 'WARNING', or 'OK' depending on failure percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"


def check_record(value, limit):
    """Calculate remaining login capacity, failure percentage, and status"""
    difference = limit - value
    percent = (value / limit) * 100
    status = status_of(percent)
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Prints a right-aligned status report inside a box"""
    print()
    print("=" * 34)
    print(f"RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Failed      : {value:>10.2f}")
    print(f"Total       : {limit:>10.2f}")
    print(f"Remaining   : {difference:>10.2f}")
    print(f"Percent     : {percent:>10.2f} %")
    print(f"Status      : {status:>10}")
    print("=" * 34)


import os

def load_records(path):
    """Reads the source IP failed logins and total attempts from the file into the list of dicts"""
    records = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, path)
    
    with open(full_path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })
    return records


# ========================================================= STORE

# Loads the log records from the external cybersecurity data file i created
records = load_records("cyber_records.txt")


# ========================================================= PROCESS + OUTPUT

# Loops through each log entry, and then prints the report
for rec in records:
    difference, percent, status = check_record(rec["value"], rec["limit"])
    print_report(rec["label"], rec["value"], rec["limit"], difference, percent, status)


# =========================================================
# 4. Before you finish:
#
# [ x ] Run it and check every record's numbers are correct by hand
# [ x ] If you are loading from a file, check what happens when the file does not exist - write the error down
# [ x ] Check every function still does one job