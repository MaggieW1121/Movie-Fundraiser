import random
from datetime import date
import pandas
import time


# Define helper function for input with quit functionality
def get_input(prompt):
    user_input = input(prompt).strip().lower()
    if user_input == 'q':
        print("Quitting the program.")
        exit()
    return user_input


# Function to show ticket information
def ticket_num():
    print()
    print("Welcome to Dit Cinema! ")
    print("{} tickets remain".format(ticket_total))


# Function to show instructions
def show_instructions():
    print("Instructions go here. They are brief but helpful")
    print('''\n
***** Instructions *****
For each ticket, enter ...
- The person's name 
- Age
- Snack you want to buy
- Payment method (choose cash or credit)

Due to the age limitation of the movie, we only accept people aged 12 and over.
If you enter an age over 130, it will be seen as a mistake,
please fix it and the program will continue.

The menu will be displayed once you enter 'yes' to the menu question 
and you can enter the snack you want in the next question.
Please make sure you only choose snacks from the menu. Other snacks are not accepted.
Please make sure every term is not blank; this is compulsory information we need.

Information collected is only for registration. It is safe and private.

When you have entered all the users, press <enter> to continue.

You are welcome to quit if you want to at any time by entering 'q'.

At the end of the program, a summary of the details of 
snack purchases will be displayed and written in a text file.

The program will then display the ticket details
including the cost of each ticket, the total cost
and the total profit.

This information will also be automatically written to a text file.

*************************''')
    print("You have 30 seconds to read this instrction")
    time.sleep(30)  # Delay for 30 seconds.


# Function to show snack menu
def show_menu():
    print("---------- MENU ----------")
    for key, value in menu.items():
        print(f"{key:10}: ${value:.2f}")
    print("--------------------------")


# Function to validate non-blank input
def not_blank(question):
    while True:
        response = get_input(question)
        if response == "":
            print("Sorry, this can't be blank. Please try again.")
        else:
            return response


# Function to validate integer input
def num_check(question):
    while True:
        try:
            response = int(get_input(question))
            return response
        except ValueError:
            print("Please enter a number.")


# Function to calculate ticket price based on age
def ticket_price(age):
    if age < 16:
        price = 7.5
    elif age < 65:
        price = 10.5
    else:
        price = 6.5
    return price


# Function to validate yes/no or cash/credit input
def string_check(question, num_letters, valid_responses):
    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:
        response = get_input(question).lower()  # change input to get_input

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)


# Function to format currency
def currency(x):
    return "${:.2f}".format(x)


# Main routine starts here

MAX_TICKETS = 5
ticket_total = 5
MAX_SNACK = 5
ticket_remain = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

menu = {
    "pizza": 3.00,
    "salad": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.50
}

while ticket_remain < MAX_TICKETS:
    # Reset variables for each ticket sale
    all_names = []
    all_ticket_costs = []
    all_surcharge = []
    all_snack_items = []
    all_snack_costs = []
    all_snack_surcharge = []
    cart = []
    snack_sales = 0
    snack_cost = 0

    # dictionary used to create data frame ie: column_name:list
    movie_dict = {
        "Name": all_names,
        "Ticket Price": all_ticket_costs,
        "Surcharge": all_surcharge
    }

    snack_dict = {
        "Name": all_names,
        "Snack": all_snack_items,
        "Snack Price": all_snack_costs,
        "Surcharge": all_snack_surcharge
    }

    ticket_num()
    ticket_sales = num_check("How many tickets do you want? ")

    read_instructions = False  # Initialize as False

    if not read_instructions:
        want_instructions = string_check(
            "Do you want to read the instructions? (y/n) ", 1, yes_no_list)
        if want_instructions == "yes":
            show_instructions()
            read_instructions = True  # Set to True after showing instructions

    #want_instructions = string_check("Do you want to read the instructions? (y/n) ", 1, yes_no_list)
    #if want_instructions == "yes":
    #show_instructions()

    while len(all_names) < ticket_sales:
        name = not_blank("Please enter your name or 'q' to quit: ")

        age = float(num_check("Age: "))
        # Perform age validation
        if not (12 <= age <= 120):
            print("Sorry, you are not within the age limit for this movie.")
            continue

        ticket_cost = ticket_price(age)

        payment_method = string_check("Choose a payment method (cash or credit): ",
                                      2, payment_list)
        surcharge = ticket_cost * 0.05 if payment_method == "credit" else 0

        read_menu = False  # Initialize as False

        if not read_menu:
            want_snack = string_check("Do you want to buy a snack? (y/n) ", 1,
                                      yes_no_list)
            if want_snack == "yes":
                show_menu()
                read_menu = True  # Set to True after showing instructions
                while snack_sales < MAX_SNACK:
                    snack = input("Select an item (q to quit): ").lower()
                    if snack == "q":
                        break
                    elif snack in menu:
                        cart.append(snack)
                    else:
                        print("Invalid item. Please choose from the menu.")

                for snack in cart:
                    if snack in menu:
                        snack_cost += menu[snack]

        all_names.append(name)
        all_ticket_costs.append(ticket_cost)
        all_surcharge.append(surcharge)
        all_snack_items.append(", ".join(cart))
        all_snack_costs.append(snack_cost)
        all_snack_surcharge.append(snack_cost *
                                   0.05 if payment_method == "credit" else 0)

        ticket_remain += 1
        ticket_total -= 1

    # create data frame from dictionary to organise information
    movie_frame = pandas.DataFrame(movie_dict)
    snack_frame = pandas.DataFrame(snack_dict)
    # comment the code below
    # movie_frame = movie_frame.set_index('Name')

    # calculate the total ticket cost (ticket + surcharge)
    movie_frame['Total'] = movie_frame['Surcharge'] \
                           + movie_frame['Ticket Price']

    # calculate the profit for each ticket
    movie_frame['Profit'] = movie_frame['Ticket Price'] - 5

    # calculate ticket cost and profit totals
    total = movie_frame['Total'].sum()
    profit = movie_frame['Profit'].sum()

    # choose winner and look up total won
    winner_name = random.choice(all_names)
    win_index = all_names.index(winner_name)
    total_won = movie_frame.at[win_index, 'Total']

    # calculate currency formatting (uses currency function)
    add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
    for var_item in add_dollars:
        movie_frame[var_item] = movie_frame[var_item].apply(currency)

    # set index at end(before printing)
    movie_frame = movie_frame.set_index('Name')

    # calculate the total ticket cost (ticket + surcharge)
    snack_frame['Total'] = snack_frame['Surcharge']\
                          + snack_frame['Snack Price']

    # calculate the profit for each ticket
    snack_frame['Profit'] = snack_frame['Snack Price'] * 0.1

    # calculate ticket and profit totals
    snack_total = snack_frame['Total'].sum()
    snack_profit = snack_frame['Profit'].sum()

    # set index at end (before printing)
    snack_frame = snack_frame.set_index('Name')
    snack_item_frame = snack_frame.set_index('Snack')

    # Get current date for heading and filename
    # get today's date
    today = date.today()

    # get day, month and year as individual strings
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    heading = "---- Movie Fundraiser Ticket Data ({}/{}/{}) ----".format(
        year, month, day)
    filename = "MF_{}_{}_{}".format(year, month, day)

    snack_heading = "---- Movie Fundraiser Snack Data ({}/{}/{}) ----".format(
        year, month, day)
    snack_filename = "MSF_{}_{}_{}".format(year, month, day)

    # change frame to a string so that we can export it to file
    movie_string = pandas.DataFrame.to_string(movie_frame)

    # create strings for printing....
    ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
    total_ticket_sales = "Total Ticket Sales: ${:.2f}".format(total)
    total_profit = "Total Profit: ${:.2f}".format(profit)

    # edit text below. It needs to work if we have unsold tickets
    if ticket_sales == MAX_TICKETS:
        sales_status = "\n*** All the tickets have been sold! ***"
    else:
        sales_status = "\n **** You have sold {} out of {}. " \
                       "tickets ****".format(ticket_sales, MAX_TICKETS)

    # change frame to a string so that we can export it to file
    snack_string = pandas.DataFrame.to_string(snack_frame)
    # snack_item_string = pandas.DataFrame.to_string(snack_item_frame)

    # create strings for printing....
    snack_cost_heading = "\n----- Snack Cost / Profit -----"
    total_snack_sales = "Total Snack Sales: ${:.2f}".format(snack_total)
    total_profit = "Total Snack Profit: ${:.2f}".format(snack_profit)

    winner_heading = "\n---- Raffle Winner ----"
    winner_text = "The winner is {} with a total of ${:.2f}".format(
        winner_name, total_won)

    # list holding content to print / write to file
    to_write = [
        heading, movie_string, ticket_cost_heading, total_ticket_sales,
        total_profit, sales_status, winner_heading, winner_text
    ]

    # list holding content to print / write to file
    snack_to_write = [
        snack_heading, snack_string, snack_cost_heading, total_snack_sales,
        total_profit
    ]

    # print output
    for item in to_write:
        print()
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

    # print output
    for item in snack_to_write:
        print()
        print(item)

    # write output to file
    # create file to hold data (add .txt extension)
    snack_write_to = "{}.txt".format(snack_filename)
    text_file = open(snack_write_to, "w+")

    for item in snack_to_write:
        text_file.write(item)
        text_file.write("\n")

    # close file
    text_file.close()
    
    # Code below are some discard codes used to help me recognise the changes in my program
    # print("---- Ticket Details ----")
    # print()

    # output table with ticket data
    # print(movie_frame)

    # print()
    # print("---- Ticket Cost & Profit ----")

    # output total ticket sales and profit
    # print("Total Ticket Sales: ${:2f}".format(total))
    # print("Total Profit : ${:2f}".format(profit))

    # print()
    # print('---- Raffle Winner ----')
    # print("Congratulations {}! You have won ${} ie: your"
    # "ticket is free!".format(winner_name, total_won))

    # Main function where the program execution starts


print("All tickets have been sold! Exiting program.")
