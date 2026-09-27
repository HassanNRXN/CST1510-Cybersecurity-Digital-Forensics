#Cell 1
"""
RECORD CHECK  -  my version
===========================

Name  : Syed Hassan Raza
Lane  : Cyber Security
Date  : 24/09/2026
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.

source_ip = input("Source IP: ")
failed_logins = float(input("Failed Logins: "))
total_attempts = float(input("Total Attempts: "))


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]

# Difference: Total attempts minus failed logins gives us the successful logins
successful_logins = total_attempts - failed_logins

# Percent: The failed logins as a percentage of the total
failed_percent = (failed_logins / total_attempts) * 100

# Excellent standard: One extra calculated line that is genuinely useful
# USEFUL: Success rate helps classify if an IP is running a pure brute-force script or not
success_percent = (successful_logins / total_attempts) * 100


# =================================================================== OUTPUT
# 3. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {source_ip}")
print("=" * 34)

print(f"Failed     : {failed_logins:>10.2f}")
print(f"Total      : {total_attempts:>10.2f}")
print(f"Successful : {successful_logins:>+10.2f}")
print(f"Failed %   : {failed_percent:>10.2f} %")
print(f"Success %  : {success_percent:>10.2f} %")

print("=" * 34)
