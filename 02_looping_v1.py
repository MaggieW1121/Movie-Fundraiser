# main routine starts here

# set maximum number of tickets & welcome message
MAX_TICKETS = 5

# loop to sell tickets
ticket_sales = 0
print("Welcome to Maggie Cinema! ")
while ticket_sales <= MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit:")
    ticket_sales += 1
    if name == 'xxx':
        break

while ticket_sales == MAX_TICKETS:
    print("You can only buy 5 tickets at a time")
    break
