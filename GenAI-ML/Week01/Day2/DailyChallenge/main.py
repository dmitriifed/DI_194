"""
GenAI-ML / Week01 / Day2 / DailyChallenge

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""

def main():
    pass

if __name__ == "__main__":
    main()

###

number = int(input("Input an integer: "))
length = int(input("Input length: ") )
multiplies = []

for i in range(1, length+1):
    multiplies.append(number * i)

print(multiplies)

###

input_string = input ("enter a string: ")

the_output = ""
previous = ""

for ch in input_string:
    if ch != previous:
        the_output += ch
        previous = ch

print(the_output)

###

