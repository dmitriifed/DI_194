"""
GenAI-ML / Week01 / Day4 / ExerciseXP

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""

def main():
    pass

if __name__ == "__main__":
    main()

###
###

def display_message():
    print("I am learning about functions in Python.")

display_message()

###

def favorite_book():
    input("my favorite book is ")

favorite_book()

###

def describe_city(city, country="Unknown"):
    print(city + " is in " + country + ".")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")

###

import random
def compare_to_random(user_number):
    random_number = random.randint(1, 100)

    if user_number == random_number:
        print("ok")
    else: 
        print(f"miss! your number:{user_number} random number:{random_number}")

compare_to_random(50) 

###

def make_shirt(size,text):
    size_and_text = [size,text]
    print("Making a", size, "shirt with  the message", text)
    return size_and_text
print(make_shirt("L", "I love Python"))

###

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    for i in range(len(names)):
        names[i] = "the Great " + names[i]

make_great(magician_names)
show_magicians(magician_names)

###

import random

def get_random_temp():
    return random.randint(-10, 40)

def main():
    temp = get_random_temp()
    print("The temperature right now is", temp, "degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temp <= 23:
        print("Nice weather.")
    elif temp <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")

main()

###

