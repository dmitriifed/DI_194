# # GUESS RANDOM NUMBER

# # Build a fun Number Guessing Game in Python! 🐍 The program picks a random number between 1-100, 
# # and you have 7 attempts to guess it. 
# # Get hints if you’re too high 📈 or too low 📉! Perfect for practicing loops 🔄, 
# # conditionals ❓, and user input ⌨️.

# import random

# #pick range
# low= int(input("Enter the LOWER bound: "))
# high = int(input("Enter the HIGHER bound: "))
# if low >= high:
#     print("LOWER bound must be less than UPPER bound.")
#     exit()

# #pick number
# number = int(input("Enter a number between {low} and {high}: "))
# attempts = 0

# while True:
#     guess = random.randint(low, high)
#     attempts += 1

#     print("Computer guesses;", guess)

#     if guess < number:
#         print("Too low!")
#         low = guess + 1
#     elif guess > number:
#         print("Too low")
#         high = guess -1
#     else:
#         print("Correct!")
#         print("Total attepts: ", attempts)
#         break

# import random
# # pick range
# low = int(input("Enter the LOWER bound: "))
# high = int(input("Enter the UPPER bound: "))

# if low >= high:
#     print("Invalid range.")
#     exit()

# number = random.randint(low, high)

# if number < low or number > high:
#     print("Number not inside range!")
#     exit()

# attempts = 0

# while low <= high:
#     guess = (low + high) // 2   
#     attempts += 1
    
#     print("Computer guesses:", guess)
    
#     if guess < number:
#         print("Too low!")
#         low = guess + 1
        
#     elif guess > number:
#         print("Too high!")
#         high = guess - 1
        
#     else:
#         print("Correct!")
#         print("Total attempts:", attempts)
#         break


import random

# defines the maximum range - ex.100
max_range = int(input("Enter the maximum number for the range (0 to ?): "))

if max_range <= 0:
    print("Please enter a positive number.")
    exit()

low = 0
high = max_range

number = random.randint(low, high)

attempts = 0

while True:
    guess = random.randint(low, high)
    attempts += 1
    
    print("Computer guesses:", guess)
    
    if guess < number:
        print("Too low!")
        low = guess + 1
        
    elif guess > number:
        print("Too high!")
        high = guess - 1
        
    else:
        print("Correct!")
        print("The number was:", number)
        print("Total attempts:", attempts)
        break


# HOW TO FIND THE 7 ATTEMTS??

# import random

# def simulate_attempts(max_range, simulations=10000):
#     count_attempts = {}  
#     for _ in range(simulations):
#         low = 0
#         high = max_range
#         number = random.randint(low, high)
#         attempts = 0

#         while True:
#             guess = random.randint(low, high)
#             attempts += 1

#             if guess < number:
#                 low = guess + 1
#             elif guess > number:
#                 high = guess - 1
#             else:
#                 break

    
#         count_attempts[attempts] = count_attempts.get(attempts, 0) + 1

#     return count_attempts

# # Test
# for max_range in range(50, 3000, 10):
#     results = simulate_attempts(max_range)
#     total_simulations = sum(results.values())
#     prob_7 = results.get(7, 0) / total_simulations
#     print(f"Range 0-{max_range}: Probability of 7 attempts ≈ {prob_7:.2%}")


