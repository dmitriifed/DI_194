# Write the following Python code to do the following (Complete ALL of the following using dictionary comprehension)




# Given a list [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this 
# {'job': 'Instructor', 'name': 'Elie'} (the order does not matter).

[("name", "Elie"), ("job", "Instructor")]
Instructor_dict = {key: value for key, value in [("name", "Elie"), ("job", "Instructor")]}
print(Instructor_dict)

another_dictionary = dict([("name", "Elie"), ("job", "Instructor")])
print(another_dictionary)

d= dict([("name", "Elie"), ("job", "Instructor")])
yet_another_dictionary = {key: value for key, value in d.items()}
print(yet_another_dictionary)

print(d)


# Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] return a dictionary that looks like this 
# {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}. You can research the zip method to help you.
d2=dict(zip(["CA", "NJ", "RI"], ["California", "New Jersey", "Rhode Island"]))
print(d2)

# Create a dictionary with the key as a vowel in the alphabet and the value as 0. Your dictionary should look like this 
# {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).
vowels = "aeiou"
keys_and_values = ({v: 0 for v in vowels})
print(keys_and_values)

# Create a dictionary starting with the key of the position of the letter and the value as the letter in the alphabet. 
# You should return something like this (Hint - use chr(65) to get the first letter):
alphabet_dictionary = {i: chr(64 + i) for i in range(1, 27)}
another_alphabet_dictionary = chr(65) 
print(alphabet_dictionary)







# {1: 'A',
#  2: 'B',
#  3: 'C',
#  4: 'D',
#  5: 'E',
#  6: 'F',
#  7: 'G',
#  8: 'H',
#  9: 'I',
#  10: 'J',
#  11: 'K',
#  12: 'L',
#  13: 'M',
#  14: 'N',
#  15: 'O',
#  16: 'P',
#  17: 'Q',
#  18: 'R',
#  19: 'S',
#  20: 'T',
#  21: 'U',
#  22: 'V',
#  23: 'W',
#  24: 'X',
#  25: 'Y',
#  26: 'Z'}


# Super Bonus

# Given the string “awesome sauce” return a dictionary with the keys as vowels and the values as the count of vowels.

# Your dictionary should look like {‘a’: 2, ‘e’: 3, ‘i’: 0, ‘o’: 1, ‘u’: 1}

string= "awesome sauce"
vowels = "aeiou"
vowel_count = {v: string.count(v) for v in vowels}
print(vowel_count)