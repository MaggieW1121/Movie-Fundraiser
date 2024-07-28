snack_sales = 0
MAX_SNACK = 5
snack_cost = 0
cart = []

# dictionary {key:value}
menu = {
    "pizza": 3.00,
    "salad": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

yes_no_list = ["yes", "no"]


# Function to validate yes/no input
def string_check(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)


# Function to show snack menu
def show_menu():
    print("---------- MENU ----------")
    for key, value in menu.items():
        print(f"{key:10}: ${value:.2f}")
    print("--------------------------")


# main routine goes here
# ask user if they want to order snacks
want_snack = string_check("Do you want to buy a snack? (y/n)", 1, yes_no_list)

if want_snack == "yes":
    show_menu()
    print()
    # loop to sell snacks
    while snack_sales < MAX_SNACK:
        food = input("Select an item (q to quit): ").lower()
        if food == "q":
            break
        elif menu.get(food) is not None:
            cart.append(food)

        snack_sales += 1

# sinple export for ordered snacks
print("---------- Your ORDER ----------")
for food in cart:
    snack_cost += menu.get(food)
    print(food, end="  ")

print()
print(f"Total is: ${snack_cost:.2f}")
