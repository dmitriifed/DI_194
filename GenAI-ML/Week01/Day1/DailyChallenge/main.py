"""
GenAI-ML / Week01 / Day1 / DailyChallenge

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""

def main():
    pass

if __name__ == "__main__":
    main()

###
"""0123456789"""


while True:
    the_string = input("The string must be exactly 10 characters long: ")

    if len(the_string) < 10:
        print("String not long enough")
    elif len(the_string) > 10:
        print("String is too long")
    else:
        print("Perfect String")
        valid_string = the_string
        print(valid_string[0], valid_string[-1])
        break

built = ""
for ch in valid_string:
    built += ch
    print(built)

# import random

# chars = list(built)
# random.shuffle(chars)
# shuffled = ''.join(chars)
# print("Shuffled: ", Shuffled)

