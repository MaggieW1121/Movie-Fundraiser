import pandas
import random

# lists to hold tickets details
all_names = ["a", "b", "c", "d", "e"]
all_tickets_costs = [7.50, 10.50, 6.50, 6.50, 10.50]
surcharge = [0, 0.53, 0, 0, 0.53]

movie_dict = {
    "Name": all_names,
    "Ticket Price": all_tickets_costs,
    "Surcharge": surcharge
}

movie_frame = pandas.DataFrame(movie_dict)
#movie_frame = movie_frame.set_index('Name')

# calculate the total ticket cost (ticket + surcharge)
movie_frame['Total'] = movie_frame['Surcharge']\
                       + movie_frame['Ticket Price']

# calculate the profit for each ticket
movie_frame['Profit'] = movie_frame['Ticket Price'] - 5

# choose a winner from our name list
winner_name = random.choice(all_names)

# get positio  of winner name in list
win_index = all_names.index(winner_name)

# look up total amount won (ie: ticket price + surcharge)
total_won = movie_frame.at[win_index, 'Total']

# set index at end (before printing)
movie_frame = movie_frame.set_index('Name')
print(movie_frame)

print()
print('---- Raffle Winner ----')
print("Congratulations {}! You have won ${} ie: your "
      "ticket is free!".format(winner_name, total_won))
