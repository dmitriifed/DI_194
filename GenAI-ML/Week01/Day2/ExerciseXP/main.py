"""
GenAI-ML / Week01 / Day2 / ExerciseXP

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""

def main():
    pass

if __name__ == "__main__":
    main()

###

my_favorite_numbers = {12, 21, 33, 1991, 0}
add_81 = 81
add_121 = 121



my_favorite_numbers.add(add_81)
my_favorite_numbers.add(add_121)
my_favorite_numbers.remove(add_121)


friend_fav_numbers = {9, 45, 14, 0, 7, 99}
our_favorite_numbers = my_favorite_numbers.union(friend_fav_numbers)

print(my_favorite_numbers)
print(friend_fav_numbers)
print(our_favorite_numbers)

###

tuples = (1, 2, 3)
tuples = tuples + (4, 5)
print(tuples)

###

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print("apples count: ", basket.count("Apples"))
basket.clear()
print("empty basket: ", basket)

###
sequence = []
integers = []
floats = []

for i in range(3,11):
    sequence.append(i/2)

for num in sequence:
    if num == int(num):
        integers.append(int(num))
    else: 
        floats.append(num)

print(sequence)
print(integers)
print(floats)

###

numbers = list(range(1, 21))
for num in numbers:
    print(num)

for i in range(1, len(numbers), 2):
    print(numbers[i])

for i in range(0, len(numbers), 2):
    print(numbers[i])


### If bob could talk

propper_dog = ("1234", "bob", "bobby", "bobster", "bobik", "bobz", "bobstein", "bigbob", "goodbob", "bobman")

while True:
    dog = input("who is the propper dog? ").strip()

    if len(dog)<4 or dog.isdigit() or dog.lower() not in propper_dog:
        print("this dog is not propper!")
    else:
        print("propper dog!")
        break

###

fruits_they_sell = input("what fruits have you (separated by spaces)? ").lower().split()
i_bye_that_fruit = input("pineapple: ").lower().strip()

if i_bye_that_fruit in fruits_they_sell: 
    print("sakit?")
else :
    print("you chose a wrong fruit")

###

toppings = []
base_price = 10
toppings_price = 2.50
menu = ["pepper", "mushroom", "cheese", "tomato"]

while True:
    choice = input(f"we have{menu} type enough ").strip().lower()
    if choice.lower() == "enough":
        break

    if choice in menu:
        toppings.append(choice)
        print(f"Adding{choice} to your pizza.")
    else:
         print("not on the menu")

total_cost = base_price + len(toppings) * toppings_price
print()

print("Your toppings:")
for t in toppings:
    print("-", t)

print("Total cost:", total_cost)

###

starting_cost=10

while True:
    age_input = input("type age or done").strip()
    if age_input.lower() == "done":
        break
    age = int(age_input)

    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15

total_cost += cost

print("Total cost:", total_cost)