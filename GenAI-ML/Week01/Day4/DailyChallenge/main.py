"""
GenAI-ML / Week01 / Day4 / DailyChallenge

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""

def main():
    pass

if __name__ == "__main__":
    main()

###

# Coffee Shop Menu Manager

# Initial data
# menu = {
#     "espresso": 7.0,
#     "latte": 12.0,
#     "cappuccino": 10.0
# }

# def show_menu(menu_dict):
#     if len(menu_dict) == 0:
#         print("The menu is empty.")
#         return

#     print("Current menu:")
#     for drink, price in menu_dict.items():
#         print(drink, "-", str(price) + "₪")

# def add_item(menu_dict):
#     drink = input("Enter new drink name: ").strip()
#     if drink in menu_dict:
#         print("Item already exists!")
#         return

#     price = float(input("Enter price: ").strip())
#     menu_dict[drink] = price
#     print('"' + drink + '" added!')

# def update_price(menu_dict):
#     drink = input("Which drink do you want to update? ").strip()
#     if drink not in menu_dict:
#         print("Item not found.")
#         return

#     new_price = float(input("Enter new price: ").strip())
#     menu_dict[drink] = new_price
#     print("Price updated!")

# def delete_item(menu_dict):
#     drink = input("Which drink do you want to remove? ").strip()
#     if drink in menu_dict:
#         menu_dict.pop(drink)
#         print("Item deleted.")
#     else:
#         print("Item not found.")

# def show_options():
#     print("What would you like to do?")
#     print("1. Show menu")
#     print("2. Add item")
#     print("3. Update price")
#     print("4. Delete item")
#     print("5. Exit")

# def run_coffee_shop():
#     while True:
#         show_options()
#         choice = input("Choose (1-5): ").strip()

#         if choice == "1":
#             show_menu(menu)
#         elif choice == "2":
#             add_item(menu)
#         elif choice == "3":
#             update_price(menu)
#         elif choice == "4":
#             delete_item(menu)
#         elif choice == "5":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice, try again.")

# if __name__ == "__main__":
#     run_coffee_shop()


# Coffee Shop Menu Manager

# Initial data
menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu_dict):
    """Print all drinks and prices."""
    for item, price in menu_dict:
        print(f"{item}-> {price}")



def add_item(menu_dict):
    """Add a new drink to the menu."""
    item = input("add item to menu")
    if item in menu_dict:
        print("item already in menu")
        return
    price = int(input)


def update_price(menu_dict):
    """Change the price of an existing drink."""
    pass


def delete_item(menu_dict):
    """Remove a drink from the menu."""
    pass


def show_options():
    """Print the available actions."""
    pass


def run_coffee_shop():
    """Main loop of the program."""
    # TODO
    # while True:
    #   1. show_options()
    #   2. get user choice
    #   3. if 1 -> show_menu(menu)
    #      if 2 -> add_item(menu)
    #      if 3 -> update_price(menu)
    #      if 4 -> delete_item(menu)
    #      if 5 -> print("Goodbye!") and break
    #      else -> "Invalid choice, try again."
    pass


# Start the program
run_coffee_shop()