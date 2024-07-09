# next steps
# add currency formatting and Heading
# integrate this component with the bas component
# show students that they can use comments
# at the top of a component at the end of a period
# so that they know what they got and what they need to do next
# add this idea to the last discussion

# PS. In base component remember to calculate the surcharge
# once payment method has been chosen.

# this version get rid of the very first column and replace with the name
import pandas

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 10.50, 6.50, 6.50, 10.50]
surcharge = [0, 0.53, 0, 0, 0.53]

movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

movie_frame = pandas.DataFrame(movie_dict)
#movie_frame = movie_frame.rename(columns={"Name": "Movie"})
movie_frame = movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
movie_frame['Total'] = movie_frame['Surcharge'] \
                       + movie_frame['Ticket Price']

# calculate the profit for each ticket
movie_frame['Profit'] = movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = movie_frame['Total'].sum()
profit = movie_frame['Profit'].sum()

# Currency .Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    movie_frame[var_item] = movie_frame[var_item].apply(currency)

# output table with ticket details
print(movie_frame)

# output total ticjet sales and profit
print("Total Ticket Sales: ${:.2f}".format(total))
print("Total Profit: ${:.2f}".format(profit))
