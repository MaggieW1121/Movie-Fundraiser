# base on the feedback, I change an error about the number of the tickets
# the number of tiket_sales will add up only when the age is valid (done)
# some special instruction is added due to both feedback and the progamming background (done)
# extend the dictionary and also a recogition program of the menu items. (done)
# In this updated code, the recognize_menu_item function uses
#the difflib.get_close_matches method to find close matches
# to the user's input from the available menu items. If a close match is found,
#it returns the matched item; otherwise, it returns None.

# I replace the "w" in the code "with open(write_to, "w") as text_file:" 
#and "with open(snack_write_to, "w") as text_file:"
# to "a" to make sure that all information purchased in the same day 
#will be stored in the same file

#Some minor errors in instruction has been fixed

from datetime import date
import pandas
import time
import difflib

MAX_TICKETS = 5
ticket_sales = 0
ticket_cost = 0
MAX_SNACK = 5

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

ticket_menu = {
    "adult": 10.5,
    "child(from 13 to 15)": 7.5,
    "senior(older than 64)": 6.5
}

menu = {
    "pizza": 15.00,
    "salad": 10.50,
    "popcorn": 8.00,
    "fries": 4.50,
    "chips": 3.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.50,
    "ginger beer": 4.50
}



# Define helper function for input with quit functionality
def get_input(prompt):
    user_input = input(prompt).strip().lower()
    if user_input == 'q':
        print("Quitting the program.")
        exit()
    return user_input


# Function to show ticket information
def show_ticket_info(ticket_sales):
    """
    :type ticket_sales: int
    """
    tickets_remaining = MAX_TICKETS - ticket_sales
    print("Kia ora!")
    print("Welcome to Dit Cinema! ")
    print("There's a fundraiser program going on."
          "We need your help to raise money for people in need")
    print(f"Movie being shown: Avatar. {tickets_remaining} tickets remain")
    print()
    print("---------- Ticket Price List ----------")
    for key, value in ticket_menu.items():
        print(f"{key:25}: ${value:.2f}")
    print("---------------------------------------")


# Function to show instructions
def show_instructions():
    print("Instructions go here. They are brief but helpful")
    print('''\n
***** Instructions *****
For each ticket, enter ...
- The person's name 
- Age
After entering all personal information for all tickets, enter...
- Snack you want to buy
- Payment method (choose cash or credit)

Due to the age limitation of the movie, we only accept people aged 13 and over.
If you enter an age over 130, it will be seen as a mistake,
please fix it and the program will continue.

The menu will be displayed once you enter 'yes' to the snack asking question
and you can enter the snack you want in the next question.
Please make sure you only choose snacks from the menu. Other snacks are not accepted.
Please make sure every term is not blank; this is compulsory information we need.

Information collected is only for registration. It is safe and private.

When you have entered all the users, press <enter> to continue.

You are welcome to quit if you want to at any time by entering 'xxx'.

At the end of the program, a summary of the details of 
snack purchases will be displayed and written in a text file.

The program will then display the ticket details
including the cost of each ticket, the total cost
and the total profit.

This information will also be automatically written to a text file.

*************************''')
    print("You have 30 seconds to read this instruction")
    time.sleep(30)  # Delay for 30 seconds.


# Function to show snack menu
def show_menu():
    print()
    print("---------- MENU ----------")
    for key, value in menu.items():
        print(f"{key:10}: ${value:.2f}")
    print("--------------------------")


# Function to validate non-blank input
def not_blank(question):
    while True:
        response = str(get_input(question))
        if response == "":
            print("Sorry, this can't be blank. Please try again.")
        elif response.isalpha():
            return response
        else:
            print("Please enter a valid name. (eg. Amy, Ben, Candy)")


def unique_name(existing_names):
    while True:
        name = not_blank("Please enter the holder's name of the ticket" 
                         "or 'q' to quit: ")

        if name in existing_names:
            print("This name has already been entered. ")
            print("Please enter a different name or add your surname.")
        else:
            return name


# Function to validate integer input
def num_check(question):
    while True:
        try:
            response = int(get_input(question))
            if response <= 0:
                raise ValueError
            else:
                return response
        except ValueError:
            print("Please enter a valid positive number. (eg. 1, 2, 3)")


# Function to calculate ticket price based on age
def ticket_price(buyer_age):
    if buyer_age < 16:
        price = 7.5
    elif buyer_age < 65:
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

        for valid_error in valid_responses:
            if response == valid_error[:
                                       short_version] or response == valid_error:
                return valid_error
        print(error)

# Function to recognize menu item
def recognize_menu_item(item):
    close_matches = difflib.get_close_matches(item, menu.keys(), n=1, cutoff=0.8)
    return close_matches[0] if close_matches else None

# Function to format currency
def currency(x):
    return "${:.2f}".format(x)


# Function to handle selling snacks
def sell_snacks():
    global snack_sales, snack_cost, cart, read_menu
    read_menu = False  # Initialize as False

    if not read_menu:
        want_snack = string_check(
            "Please confirm again, do you wish to purchase a snack? (y/n) ", 1,
            yes_no_list)
        if want_snack == "yes":
            snack_sales = 0
            show_menu()
            print("You can buy 5 snacks")
            read_menu = True  # Set to True after showing menu

            while snack_sales < MAX_SNACK:
                print("")
                snack = input("Select an item or enter 'q' to quit: ").lower()
                if snack == "q":
                    break
                recognized_snack = recognize_menu_item(snack)
                if recognized_snack:
                    cart.append(recognized_snack)
                    snack_cost += menu[recognized_snack]
                    snack_sales += 1
                    print(f"You have purchased {snack_sales} snacks.")
                else:
                    print("Invalid item. Please choose from the menu.")
                    
                #elif snack in menu:
                    #cart.append(snack)
                    #snack_cost += menu[snack]
                    #snack_sales += 1
                    #print(f"You have purchased {snack_sales} snacks.")
                #else:
                    #print("Invalid item. Please choose from the menu.")

    all_snack_items.append(", ".join(cart))
    all_snack_costs.append(snack_cost)


# ticket_cost = 0

# Function to handle payment method chosen


def choose_payment(ticket_cost):
    global payment_method
    payment_method = string_check(
        "Choose a payment method (cash for no charge "
        "or credit for a 5% charge): ", 2, payment_list)
    for item in all_ticket_costs:
        surcharge = item * 0.05 if payment_method == "credit" else 0
        all_surcharge.append(surcharge)

    snack_surcharge = snack_cost * 0.05 if payment_method == "credit" else 0
    all_snack_surcharge.append(snack_surcharge)


# Function to sell tickets
def sell_tickets():
    global ticket_sales  # Still needed if you modify global variable

    # Update the global variable if necessary

    global ticket_cost
    try:
        show_ticket_info(ticket_sales)
        num_tickets: int = num_check("How many tickets do you want to buy? ")
        if num_tickets + ticket_sales > MAX_TICKETS:
            print(
                f"Sorry, you can only buy {MAX_TICKETS - ticket_sales} tickets."
            )
            print()
            return sell_tickets()
        #else:
            #ticket_sales += num_tickets

        read_instructions = False  # Initialize as False

        if not read_instructions:
            want_instructions = string_check(
                "Do you want to read the instructions?"
                "(y/n) ", 1, yes_no_list)
            if want_instructions == "yes":
                show_instructions()
                # read_instructions = True  # Set to True after showing instructions

    except ValueError:  # was line 205 moved to 196
        print("Please enter a valid number of tickets.")

    # Process the specified number of tickets
    for _ in range(num_tickets):
        name = unique_name(all_names)

        buyer_age = int(num_check("Age: "))

        if (13 <= buyer_age <= 130):
            ticket_sales += 1
        # Perform age validation
        if not (12 <= buyer_age <= 130):
            print("Sorry, you are not within the age limit for this movie.")
            print("If you want to buy ticket, " 
                  "please go to the help desk for clarification.")
            continue


        ticket_cost = ticket_price(buyer_age)
        all_names.append(name)
        all_ticket_costs.append(ticket_cost)

    return ticket_sales


# Main routine starts here
while ticket_sales < MAX_TICKETS:
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

    # Create data frames from dictionaries to organize information
    movie_dict = {
        "Name": all_names,
        "Ticket Price": all_ticket_costs,
        "Surcharge": all_surcharge
    }

    snack_dict = {
        "Snack": all_snack_items,
        "Snack Price": all_snack_costs,
        "Surcharge": all_snack_surcharge
    }

    # Sell tickets and snacks
    sell_tickets()

    # New code: Ask if user wants to buy snacks
    # I change the posistion of this function from line 234 to line 268
    want_snacks = string_check(
        "Do you want snacks?Please enter 'y' or 'n' to quit ", 1, yes_no_list)
    if want_snacks != "y":
        sell_snacks()  # Call the sell_snacks function

    # Call function to sell snacks
    #sell_snacks()

    # Call function to choose payment method
    choose_payment(ticket_cost)

    movie_frame = pandas.DataFrame(movie_dict)
    snack_frame = pandas.DataFrame(snack_dict)

    # Calculate the total ticket cost (ticket + surcharge)
    movie_frame[
        'Total'] = movie_frame['Surcharge'] + movie_frame['Ticket Price']

    # Calculate the profit for each ticket
    movie_frame['Profit'] = movie_frame['Ticket Price'] - 5

    # Calculate ticket cost and profit totals
    total = movie_frame['Total'].sum()
    profit = movie_frame['Profit'].sum()

    # Calculate currency formatting (uses currency function)
    add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
    for var_item in add_dollars:
        movie_frame[var_item] = movie_frame[var_item].apply(currency)

    # Set index at end (before printing)
    movie_frame = movie_frame.set_index('Name')

    # Calculate the total snack cost (snack + surcharge)
    snack_frame[
        'Total'] = snack_frame['Surcharge'] + snack_frame['Snack Price']

    # Calculate the profit for each snack
    snack_frame['Profit'] = snack_frame['Snack Price'] * 0.1

    # Calculate snack cost and profit totals
    snack_total = snack_frame['Total'].sum()
    snack_profit = snack_frame['Profit'].sum()

    # Set index at end (before printing)
    snack_frame = snack_frame.set_index('Snack')

    # Get current date for heading and filename
    today = date.today()
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    heading = "---- Movie Fundraiser Ticket Data ({}/{}/{}) ----".format(
        year, month, day)
    filename = "MF_{}_{}_{}".format(year, month, day)

    snack_heading = "---- Movie Fundraiser Snack Data ({}/{}/{}) ----".format(
        year, month, day)
    snack_filename = "MSF_{}_{}_{}".format(year, month, day)

    # Change frame to a string so that we can export it to file
    movie_string = pandas.DataFrame.to_string(movie_frame)

    # Create strings for printing and writing to file
    ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
    total_ticket_sales = "Total Ticket Sales: ${:.2f}".format(total)
    total_profit = "Total Profit: ${:.2f}".format(profit)
    if ticket_sales == MAX_TICKETS:
        sales_status = "\n*** All the tickets have been sold! ***"
    else:
        sales_status = "\n **** This fundraiser program have sold {} out of {}. ".format(
            ticket_sales, MAX_TICKETS) + "tickets ****"

    # Change frame to a string so that we can export it to file
    snack_string = pandas.DataFrame.to_string(snack_frame)

    # Create strings for printing and writing to file
    snack_cost_heading = "\n----- Snack Cost / Profit -----"
    total_snack_sales = "Total Snack Sales: ${:.2f}".format(snack_total)
    total_snack_profit = "Total Snack Profit: ${:.2f}".format(snack_profit)

    # List holding content to print / write to file
    to_write = [
        heading, movie_string, ticket_cost_heading, total_ticket_sales,
        total_profit, sales_status
    ]

    snack_to_write = [
        snack_heading, snack_string, snack_cost_heading, total_snack_sales,
        total_snack_profit
    ]

    # Print output
    for item in to_write:
        print()
        print(item)

    # Write output to file
    write_to = "{}.txt".format(filename)
    with open(write_to, "a") as text_file:
        for item in to_write:
            text_file.write(item)
            text_file.write("\n")

    if want_snacks == "yes":
        # Print output
        for item in snack_to_write:
            print()
            print(item)
            print()
            print()  # more blank space

        # Write output to file
        snack_write_to = "{}.txt".format(snack_filename)
        with open(snack_write_to, "a") as text_file:
            for item in snack_to_write:
                text_file.write(item)
                text_file.write("\n")

print("Ngā mihi! All tickets have been sold! Exiting program.")
