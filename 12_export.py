import pandas
import random
from datetime import date

# lists to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 10.50, 6.50, 6.50, 10.50]
surcharge = [0, 0.53, 0, 0, 0.53]

movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

# create frame
movie_frame = pandas.DataFrame(movie_dict)

# calculate the total ticket cost (ticket + surcharge)
movie_frame['Total'] = movie_frame['Surcharge']\
                      + movie_frame['Ticket Price']

# calculate the profit for each ticket
movie_frame['Profit'] = movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = movie_frame['Total'].sum()
profit = movie_frame['Profit'].sum()

# choose winner and look up totlal win
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = movie_frame.at[win_index, 'Total']

# set index at end (before printing)
movie_frame = movie_frame.set_index('Name')

# **** Get current date for heading and filename ****
# get today's date
today = date.today()

# get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "---- Movie Fundraiser Ticket Data ({}/{}/{}) ----".format(
    year, month, day)
filename = "MF_{}_{}_{}".format(year, month, day)

# change frame to a string so that we can export it to file
movie_string = pandas.DataFrame.to_string(movie_frame)

# create strings for printing....
ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = "Total Ticket Sales: ${}".format(total)
total_profit = "Total Profit: ${}".format(profit)

# edit text below! It needs to work if we have unsold tickets
sales_status = "\n*** All the tickets have been sold! ***"

winner_heading = "\n---- Raffle Winner ----"
winner_text = "The winner is {} with a total of ${:.2f}".format(
    winner_name, total_won)

# list holding content to print / write to file
to_write = [
    heading, movie_string, ticket_cost_heading, total_ticket_sales,
    total_profit, sales_status, winner_heading, winner_text
]

# print output
for item in to_write:
    print(item)

# write output to file
# create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
