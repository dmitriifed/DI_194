#1
a= [1,2,3,4,5]
b= [3,4,5,6,7]
def difference(a, b):
    return sum(a) - sum(b)

print(difference(a, b))

print(difference([1,2,3], [1,2,3]))

print(difference([a[1]], [b[1]]))


# 2
day_toprint = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

def print_day(day_number):
    print(day_toprint.get(day_number, None))

print(day_toprint.get(4, "example") + " is the day of the week when I wrote my first Python function")


# 3

# this function takes in one parameter (a list) and returns the last value in the list. 
# It should return None if the list is empty.

def last_element(lst):
    if not lst:
        return None
    return lst[-3]

print(last_element([1,"unexpected element",3,4])) 
print(last_element([]))

# 4
# this function takes in two parameters (both numbers). 
# If the first is greater than the second, this function returns “First is greater.” 
# If the second number is greater than the first, the function returns “Second is greater.” 
# Otherwise the function returns “Numbers are equal.”


def number_compare(a, b):
    if a > b :
        return "First is greater"
    elif b > a :
        return "Second is greater"  
    else:
        return "Numbers are equal"

print(number_compare(difference([a[1]], [b[1]]), difference([b[1]], [a[1]])))


# this function takes in two parameters (two strings). 
# The first parameter should be a word and the second should be a letter. 
# The function returns the number of times that letter appears in the word. 
# The function should be case insensitive (does not matter if the input is lowercase or uppercase). 
# If the letter is not found in the word, the function should return 0.


def single_letter_count(word, letter):
    return word.lower().count(letter.lower())

print(single_letter_count("amazing", "A"))



# this function takes in one parameter (a string) and returns a 
# dictionary with the keys being the letters and the values being the count of the letter.

 # {h:1, e: 1, l: 2, o:1} "hello"
 # {p:1, e: 1, r: 1, s:1, o:1, n:1}  "person" 


def multiple_letter_count(s):
    letter_count = {}
    for letter in s:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

print(multiple_letter_count("hello"))   # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(multiple_letter_count("person"))  # {'p': 1, 'e': 1, 'r': 1, 's': 1, 'o': 1, 'n': 1}


# list_manipulation

# this function should take in three parameters (a list, command, location and value).

# If the command is “remove” and the location is “end”, 
# the function should remove the last value in the list and return the value removed

# If the command is “remove” and the location is “beginning”, 
# the function should remove the first value in the list and return the value removed

# If the command is “add” and the location is “beginning”, 
# the function should add the value (fourth parameter) to the beginning of the 
# list and return the list

# If the command is “add” and the location is “end”, 
# the function should add the value (fourth parameter) to the end of the list and return the list


def list_manipulation(lst, command, location, value=None):
    if command == 'remove' and location == 'end':
        return lst.pop()
    if command == 'remove' and location == 'beginning':
        return lst.pop(0)
    if command == 'add' and location == 'beginning':
        lst.insert(0, value)
        return lst
    if command == 'add' and location == 'end':
        lst.append(value)
        return lst
        
print(list_manipulation([1,2,3], "remove", "end"))     

print(list_manipulation([1,2,3], "add", "end", 30))     

# is_palindrome

# A Palindrome is a word, phrase, number, or other sequence of characters which reads 
# the same backward or forward. This function should take in one parameter and 
# returns True or False depending on whether it is a palindrome. 
# As a bonus, allow your function to ignore whitespace and 
# capitalization so that is_palindrome('a man a plan a canal Panama') returns True.

def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome('testing')) 
print(is_palindrome('tacocat')) 
print(is_palindrome('hannah')) 
print(is_palindrome('robert')) 

# frequency
# This function accepts a list and a search_term (this will always be a primitive value)
# and returns the number of times the search_term appears in the list.

def frequency(lst, search_term):
    return lst.count(search_term)     

print(frequency([1,2,3,4,4,4], 4))
print(frequency([True, False, True, True], False))

#flip_case
# This function accepts a string and a letter and reverses the case of all occurances of 
# the letter in the string.

# def flip_case(s, letter):
#     target = letter.lower()
#     result = []
#     for ch in s:
#         if ch.lower() == target:
#             result.append(ch.swapcase())
#         else:
#             result.append(ch)
#     return "".join(result)

# print(flip_case('hello world', 'o'))



# This function accepts a list of numbers and returns the product of all even numbers in the list.
# multiply_even_numbers([2,3,4,5,6])

def multiply_even_numbers(lst):
    product = 1
    for num in lst:
        if num % 2 == 0:
            product *= num
    return product
print(multiply_even_numbers([2,3,4,5,6]))



# This function accepts a list of numbers
# and returns the most frequent number in the list of numbers.
# You can assume that the mode will be unique.

def mode(lst):
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get)

print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))

# This function accepts a string and returns the same string with the first letter capitalized.

def capitalize_first_letter(s):
    return s.capitalize()

print(capitalize_first_letter("hello world"))

# This function accepts a list 
# and a callback function (which you can assume returns True or False). 
# The function should iterate over each element in the list and invoke the callback 
# function at each iteration. If the result of the callback function is True, 
# the element should go into one list if it’s False, the element should go into another list.
# When it’s finished, partition should return both lists inside of one larger list.


def partition_even_odd(nums):
    evens = []
    odds = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)
    return [evens, odds]

print(partition_even_odd(list(range(50))))


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))  

print(intersection([1,2,3], [2,3,4]))

# This function accepts a function and returns a new function that can only be invoked once. 
# If the function is invoked more than once, it should return None. 
# Hint you will need to define a new function inside of your once function and return that function. 
# You can add properties to your inner function to see if it has run already.

# def add(a,b):
#     return a + b
# def once(func):
   



# one_addition = once(add)

# one_addition(2,2) # 4
# one_addition(2,2) # undefined
# one_addition(12,200) # undefined

#Complete the solution so that it reverses the string passed into it.

def reverse_string(s):
    return s[::-1]
print(reverse_string("hello world"))


# The accounts of the "Fat to Fit Club (FFC)" association are supervised by John as a 
# volunteered accountant. The association is funded through financial donations 
# from generous benefactors. John has a list of the first n donations: 
# [14, 30, 5, 7, 9, 11, 15] He wants to know how much the next benefactor 
# should give to the association so that the average of the first n + 1 donations should reach 
# an average of 30. After doing the math he found 149. 
# He thinks that he could have made a mistake.

# Could you help him?

def next_donation(donations, target_average):
    total_donations = sum(donations)
    n = len(donations)
    required_total = target_average * (n + 1)
    return required_total - total_donations
print(next_donation([14, 30, 5, 7, 9, 11, 15], 30))


# Your task is to write a function which returns the sum of a sequence of integers.

# The sequence is defined by 3 non-negative values: begin, end, step.

# If begin value is greater than the end, your function should return 0. 
# If end is not the result of an integer number of steps, 
# then don't add it to the sum. See the 4th example below.


def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    return sum(range(begin, end + 1, step))

print(sequence_sum(2, 6, 2)) 

# You must implement a function that returns the difference between the 
# largest and the smallest value 
# in a given list / array (lst) received as the parameter.

def inbetween(lst):
    return max(lst) - min(lst)
  
print(inbetween([1,2,3,4,5]))

#Given an array (arr) as an argument 
# complete the function countSmileys that should return the total number of smiling faces.

def count_smileys(arr): 
    valid = {":)", ":D", ";)", ";D", ":-)", ":~)", ";-)", ";~)", ":-D", ":~D", ";-D", ";~D"}
    return sum(1 for face in arr if face in valid)

print(count_smileys([":)", ":D", ";-D", ":~)", ";(", ":>", ":}"]))



# Create a function that will tell how many sentences are in a paragraph, 
# based on the number of periods ".", question marks "?" and "!" exclamation 
# points that an input string contains.


paragraph = """Wind moves through the late street like a quiet friend, 
brushing the leaves and carrying the smell of rain. 
I watch the city lights shimmer in puddles, 
and I wonder what stories they hide? Somewhere a train sighs and fades into distance, 
and a dog barks once, then thinks better of it. The night feels wide, but my room feels small, 
filled with the soft ticking of time. I write a line, cross it out, and write it again, 
as if words can turn back a moment. Do you ever feel the past tapping at the window, 
asking to be let in? I answer with silence, then with a smile, then with another sentence. 
The moon looks like a pale coin spent on a wish, and the clouds keep its secret moving. 
I listen for my own heartbeat, steady as a drum under blankets, and I remember to breathe. 
Tomorrow will arrive whether I am ready or not, but tonight I can hold still. 
And in this stillness, I can almost hear hope whisper—softly, stubbornly, bright!"""

def count_sentences(paragraph):
    return sum(paragraph.count(p) for p in ".?!")

print(count_sentences(paragraph))


# tortoises raceing


time= 3600


def tortoise_racing(v1, v2, g):
    if v1 >= v2:
        return None
    time = g / (v2 - v1)
    hours = int(time)
    minutes = int((time - hours) * 60)
    seconds = int(((time - hours) * 60 - minutes) * 60)
    return [hours, minutes, seconds]

print(tortoise_racing(720, 850, 70))


# Calculate string shift

def shifted_diff(first, second):
    if len(first) != len(second):
        return -1
    for i in range(len(first)):
        if first == second:
            return i
        second = second[1:] + second[0]
    return -1   

print(shifted_diff("hello world", "orldhello w"))