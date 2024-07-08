# function goes here

# checks users enter an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response
            
        except ValueError:
            print("Please enter a number")
            
# main routine goes here
ticket_sales = 0

while True:

    name = input("Please enter your name or 'xxx' to quit:")

    if name == 'xxx':
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are too young for this movie")
        print("Please enter an integer that is more than (or equal to) 14")
        continue
    else:
        print("That looks like a typo, please enter an integer that is less than (or equal to) 120")
        continue

    ticket_sales += 1
