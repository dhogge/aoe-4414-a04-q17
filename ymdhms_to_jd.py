# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#
# This script converts a given date and time (year, month, day, hour, minute, second) to fractional Julian date.
#
# Parameters:
#   year   - an integer representing the year (e.g., 1970)
#   month  - an integer representing the month (1 to 12)
#   day    - an integer representing the day of the month
#   hour   - an integer representing the hour (0 to 23)
#   minute - an integer representing the minutes (0 to 59)
#   second - a float representing the seconds (can include a decimal fraction)
#
# Output:
#   Fractional Julian date
#
# Written by Dylan Hogge
# Other contributors: None
#
import sys 
import math  

# Ensure correct number of command-line arguments
if len(sys.argv) == 7:
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])
    hour = int(sys.argv[4])
    minute = int(sys.argv[5])
    second = float(sys.argv[6])
else:
    print('Usage: python3 ymdhms_to_jd.py year month day hour minute second')
    exit()

JD = day - 32075+1461*(year+4800-(14-month)//12)//4+367*(month-2+(14-month)//12*12)//12-3*((year+4900-(14-month)//12)//100)//4
JD_MN = JD-0.5
D_fract = (second+60*(minute+60*hour))/86400
JD_fract = JD_MN+D_fract

print(JD_fract)

