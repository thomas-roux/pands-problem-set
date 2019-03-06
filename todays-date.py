# Thomas Roux
# Solution to Problem 8 - outputs today's date in format "Weekday, Month Day Year at HH:MM am/pm"
# Begun: 03/03/2019; 16h00

# Imports datetime module
import datetime as dt

# Prints today's date in specified format
# dash (-) in %-d and %-I removes zero - https://stackoverflow.com/questions/904928/python-strftime-date-without-leading-0
print(dt.datetime.strftime(dt.datetime.now(), "%A, %B %-d %Y at %-I:%M %p"))



# need to come back to work out how to put -st, -rd and -th into day