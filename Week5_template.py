"""
RECORD CHECK - Cyber Security Lane
==============================================
Name : Syed Hassan Raza
Lane : Cyber Security
Date : 21/10/2026
"""

# ===================================================================== CLASS
class Record:

    def __init__(self, label, value, limit):
        """Starts the Record with a source IP label, failed logins value, and total attempts limit"""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Evaluates and returns the security statuses based on the failed logins compared/re;ative to the total attempt limits"""
        if self.value >= self.limit:
            return "OVER LIMIT"
        elif self.value >= 0.9 * self.limit:
            return "WARNING"
        else:
            return "OK"


# ===================================================================== RECORDS
def load_records(path):
    """Reads the new text file line by line and returns a list of Record objects"""
    records = []
    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3:
                label = parts[0]
                value = float(parts[1])
                limit = float(parts[2])
                records.append(Record(label, value, limit))
    return records
records = load_records("week5_records.txt")


# ===================================================================== OUTPUT
# This keeps a running count of how many records come back OVER LIMIT across the entire dataset
over_limit_count = 0

for record in records:
    print()
    print("=" * 30)
    print(f"RECORD CHECK - {record.label}")
    print("=" * 30)
    
    # Evaluate status and track over-limit instances
    current_status = record.status()
    if current_status == "OVER LIMIT":
        over_limit_count += 1
        
    print(f"Failed     : {record.value:>10.2f}")
    print(f"Total      : {record.limit:>10.2f}")
    print(f"Status     : {current_status:>10}")
    print("=" * 30)

# Prints the final running summary once after the loop completes
print()
print(f"Total records OVER LIMIT: {over_limit_count}")


# ===================================================================== BEFORE YOU FINISH
# [] Run it and check every record's numbers by hand
# [] Check every method only reads/changes its OWN object (self) - nothing reaches outside itself
# [] Check every method and __init__ has a one-line docstring