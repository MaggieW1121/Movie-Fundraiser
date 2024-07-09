# Calculate the ticket price based on the age
def ticket_price(var_age):

  # ticket is $7.50 for users under 16
  if var_age < 16:
    price = 7.5

  # ticket is $10.50 for users between 16 and 64
  elif var_age < 65:
    price = 10.5

  # ticket is $6.50 for seniors that are 65 years or older
  else:
    price = 6.5

  return price


# loop for testing...
while True:

  # Get age (assum users input a valid integer)
  age = int(input("Age: "))

  # calculate ticket cost
  ticket_cost = ticket_price(age)
  print("Age: {}, Ticket Price : ${:.2f}".format(age, ticket_cost))
