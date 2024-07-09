# checks that users enter a valid response
# (eg yes/no/cash/credit) based on a list of options
def string_check(question, num_letters, valid_responses):

  while True:
    response = input(question).lower()

    for item in valid_responses:
      if response == item[0] or response == item:
        return item

    print("Please enter a valid answer")


# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

for case in range(0, 5):
  want_instructions = string_check(
      "Do you want to read the instructions? (y/n)", 1, yes_no_list)
  print("You chose {}".format(want_instructions))

for case in range(0, 5):
  payment_method = string_check("Choose a payment method (cash or credit):", 2,
                                payment_list)
  print("You chose {}".format(payment_method))
