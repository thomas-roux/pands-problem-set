# Thomas Roux
# Solution to Problem 2 - outputs whether today is a weekday starting with a T
# Begun: 03/03/2019; 16h00

# Imports the necessary datetime module as dt
import datetime as dt

# Determines today's date in YYYY-MM-DD format
today = dt.date.today()

# Determines if today is Tuesday (1) or Thursday (3) and prints response
if dt.date.weekday(today) == 1 or dt.date.weekday(today) == 3:
    print("Yes - today begins with a T.")
else:
    print("No - today does not begin with a T.")