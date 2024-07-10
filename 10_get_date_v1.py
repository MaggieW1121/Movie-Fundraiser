# Code adapted from
# https://www.programiz.com/python-programming/datetime/current-datetime

from datetime import date

# get today's date
today = date.today()

# Set up date for heading
heading_date = today.strftime("%d/%m/%Y")
print("d1 =", heading_date)

# set up date for filename...
