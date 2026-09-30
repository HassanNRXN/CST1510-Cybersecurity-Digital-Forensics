"""
RECORD CHECK  -  my version
===========================

Name  : Syed Hassan Raza
Lane  : Cyber Security
Date  : 30/09/2026

Run it:   python template.py
"""

# ==================================================================== INPUT
# 1. Ask for your three values.

label = input("Enter Source IP: ")
value = float(input("Enter failed logins: "))
limit = float(input("Enter total attempts: "))


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.

difference = limit - value
percent = (value / limit) * 100

# 3. Decide a status and store it in a variable called status.

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"


# =================================================================== OUTPUT
# 4. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"  Failed     : {value:>10.2f}")
print(f"  Total      : {limit:>10.2f}")
print(f"  Difference : {difference:>10.2f}")
print(f"  Percent    : {percent:>9.2f} %")
print(f"  Status     : {status:>10}")
print("=" * 34)