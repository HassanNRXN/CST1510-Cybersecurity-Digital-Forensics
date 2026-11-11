"""
RECORD CHECK - my version
==============================

Name : Syed Hassan Raza
Lane : IT
Date : 11/11/2026

Run it:  python template.py

Work through the numbered sections in order. Each one tells you what it must do.
"""

# ====================================================================== FUNCTIONS
def parse_line(raw_line):
    """Parse a raw IT log line into a clean dictionary with hostname, used, and total."""
    line = raw_line.strip().lower()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip()
    
    result = {"hostname": hostname}
    
    for piece in rest.split(","):
        k, v = piece.split("=")
        result[k.strip()] = float(v.strip())
        
    return result

def status_of(record):
    """Determines the health status based on used versus total capacity percentage."""
    percent = (record["used"] / record["total"]) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

# ====================================================================== INPUT
raw_records = [
    "   SRV-01 , USED=87 , TOTAL=100   ",
    "srv-02,used=95,total=100",
    "  SRV-03  ,  used=120  ,  total=100  ",
    "srv-04 , used=50 , total=200",
    "   SRV-05 , USED=91 , TOTAL=100 "
]

# ====================================================================== PROCESS + OUTPUT
for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)
    print(record, status)

# ======================================================================