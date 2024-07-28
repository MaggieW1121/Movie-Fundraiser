
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

# create an empty listcart[]# declear a varible name
total = 0
cart = []  # Initialize the cart list

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------- Your ORDER ----------")
for food in cart:
    total += menu.get(food)
    print(food, end="  ")

print()
print(f"Total is: ${total:.2f}")
