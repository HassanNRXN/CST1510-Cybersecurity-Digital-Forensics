"""
RECORD CHECK  -  my version
============================

Name  : Syed Hassan Raza
Lane  : Cyber Security
Date  : 07/10/2026

Run it: python template.py
"""

# ========================================================= FUNCTIONS

def status_of(percent, warning_at=90):
    """Return 'OVER LIMIT', 'WARNING', or 'OK' based on percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculate and return difference (limit - value) and percentage"""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


# ========================================================= INPUT

label = input("Enter source IP: ")
value = float(input("Enter failed logins: "))
limit = float(input("Enter total attempts: "))


# ========================================================= PROCESS

difference, percent = check(value, limit)
status = status_of(percent)


# ========================================================= OUTPUT

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