# checks that users enter a valid response
# (e.g. yes/no/cash/credit) based on a list of options
# this version uses a "if""else"statement to make the "Ca"and "Cr" can also accept
# this version has a custom error message
def string_check(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    # unnecessary code
    #if num_letters == 1:
        #short_version = 1
    #else:
        #short_version = 2

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                              #short_version
                return item

        print(error)


# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

for case in range(0, 5):
    want_instructions = string_check(
        "Do you want to read the instructions? (y/n)", 1, yes_no_list)
    print("You chose {}".format(want_instructions))

for case in range(0, 5):
    payment_method = string_check("Choose a payment method (cash or credit):",
                                  2, payment_list)
    print("You chose {}".format(payment_method))
