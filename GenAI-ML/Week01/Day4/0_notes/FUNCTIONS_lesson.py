####
# def say_hello(username, location="Ramat Gan"):
#     """A function that says hello"""
#     print(f'Hello, {username.capitalize()}! you are from {location.capitalize()}')

# def logout(username):
#     print(f"user {username} logged out!")

# user = input("what is the username? ")
# loc = input("where are you from? ")

# say_hello(location=loc, username=user)
# logout(user)
####
####
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# print(get_formatted_name('xiao', 'hendrix'))
###


# def add_three(num):
#     return num +3

# def square(num):
#     return num **2

# def divide_2(num):
#     return num /2

# step1 = 10

# step2 = add_three(step1)
# step3 = square(step2)
# step4 = divide_2(step3)

# print(step4)
####
####
# def add_three(num):
#     return num + 3

# def square(num):
#     return num ** 2

# def divide_2(num):
#     return num / 2

# steps = [add_three, square, divide_2]

# value = 10
# for fn in steps:
#     value = fn(value)

# print(value)
####
####
# def get_coords(location):
#     print(f"I know where{location} is.")
#     return (33.1234, 100.745)
# lat, lon = get_coords("Ramat Gan")

# print(lat)

# a,b = ("Hello", "goodbye")
# print(b)
####
####
# def say_cheese():
#     return "Cheese"
# print(say_cheese)

# func_dict = {
#     "my_function": say_cheese
# }

# print(func_dict["my_function"]())
####
####
# def say_hello(*args):
#     print("The greetings are: ", args)

# say_hello("ahoy", "hello", "hi")
# ####
# ####
# def say_hello(**kwargs):
#     print("The greetings are: ", kwargs)

# say_hello(greeting1="ahoy", greeting2="hello", greeting3="hi")
# ####
# ####
# def make_sandwich(type, *args, **kwargs):
#     print(f"making a {type} sandwich")
#     if args:
#         for arg in args:
#             print(f"adding {arg}")
#     if kwargs:
#         for arg in args:
#             print(f"adding {arg}")

# # make_sandwich(input("type of sandwich"), "letuce", "tomato", breadtype="brown pita")

# ingredients_list = []

# sandwich_type = "cheese"

# while True:
#     ing = input("what to add to sandwich")
#     if ing == "q":
#         break
#     if ing:
#         ingredients_list.append(ing)

# def create_sandwich(sandwich_kind, ingredients):
#     print(f"Making a {type} sandwich")
#     if not ingredients:
#         print("No extra ingredients added.")
#         return
#     for ingredient in ingredients:
#         print(f"adding {ingredient}")

# create_sandwich((sandwich_type, ingredients_list))

# ###

def main():
    temp = get_random_temp()
    print(f"The current temperature is{temp}")
main()