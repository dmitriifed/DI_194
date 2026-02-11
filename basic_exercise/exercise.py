first= "1st:"

a = 1
b = 2
c = 4
nums = [1, 2, 4, 9, 16, 25, 36, 49, 64, 81]
nope = "FAIL" 
num = 100
nonum = int("1000")
cool = 3 * "cool"


my_scope = 3
i_am_shouting = "a" * num

total = sum(nums[:my_scope])
increasing = all(nums[i] < nums[i + 1] for i in range(my_scope - 1))



#user puts name= "any name"
#user puts level= ">0"
#user puts fruit= "apple"
#user puts instrument = "guitar"
#user puts strings = "goat"

#test the program with the following values:

#human_years = 10
#human_years = 1
#human_years = 2
#cat and dog years = 1

#human_level = 10
#output: [10, 56, 64]
#human_level = 1
#output: [2, 15, 15]
#human_level = 2
#output [3, 24, 24]

name= input("What is your name? ")
your_level = int(input("what is your level: "))
fruit= input("What is an inferior brand of phone? ")
instrument= input("What is Eric Claptons favorite instrument? ")
strings= input("What strings did you bring? ")

human_was_level= int(input("what level were you when you got your cat and dog? "))
cat_was_level = int(input("what level was the cat when you got it? "))
dog_was_level = int(input("what level was the dog when you got it? "))


# cats and dogs have the same level, and they level up at the same rate.
levels_passed = your_level - human_was_level
cat_level = cat_was_level + 4 * levels_passed
dog_level = dog_was_level + 5 * levels_passed
 

levels_passed = your_level - human_was_level
levels_passed = your_level - human_was_level

if your_level > human_was_level > 0 and cat_was_level > 0 and dog_was_level > 0:
    cat_level = cat_was_level + 4 * levels_passed
    dog_level = dog_was_level + 5 * levels_passed
    nope = None   # PASS (inputs make sense)
else:
    cat_level = 0
    dog_level = 0
    nope = "FAIL" # FAIL (inputs not consistent)

print([your_level, cat_level, dog_level])
    


print("Your cat is level " + str(cat_level) + " and your dog is level " + str(dog_level) + ".") #BUT WHY?

# Write a comment that says "This is a comment."
# Declare a variable called first and assign it to the value "Hello World".
# Write a comment that says "This is a comment."
# Log a message to the terminal that says "I AM A COMPUTER!"

print(name)

print(first)
print("I am a computer")

# Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2. If it is, show the message "Math is fun."


if a < b < c:
    print("2nd: " \
     "math is working")
else: 
    print ("ERROR: math is out of scope")


# Use the language’s “and” boolean operator to combine the language’s “true” value with its “false” value

if a < b < c and (a==b==c) is False:

    print("3rd: math is still working")
else: 
    print ("ERROR: math is out of scope")

# Assign a variable called nope to an absence of value.

if a < b < c and (a==b==c) is False and nope is None:
    print("4th: math is still working")
else: 
    print ("Warning: math is out of scope")

# Calculate the length of the string "What's my length?"

if a < b < c and not (a==b==c) and nope is None:
    print("5th: math is still working" + ' ' +str(len("what is my length?"))) 
else: 
    print ("Warning: math is out of scope")


# Convert the string "i am shouting" to uppercase.
# Convert the string "1000" to the number 1000.
# Combine the number 4 with the string "real" to produce "4real".
# Record the output of the expression 3 * "cool".

if a < b < c and not (a==b==c) and nope is None:
    print("6th: math is still working" + '  ' + i_am_shouting.upper() + '! ' + "4" + "real" + ' '  + str(len(i_am_shouting)) + ' ' + "characters long")
else: 
    print("Warning: math is out of scope")

# Determine the type of [].
# Ask the user for their name, and store it in a variable called name.
# Ask the user for a number. If the number is negative, show a message that says "That number is less than 0!" 
# If the number is positive, show a message that says "That number is greater than 0!" Otherwise, 
# show a message that says "You picked 0!.
# Find the index of "l" in "apple".
# Check whether "y" is in "xylophone".
# Check whether a string called my_string is all in lowercase.



#if (increasing and nope is None and total < 8 and your_level > 0 
  #  and fruit.find("l") == 3 
   # and instrument.find("ar") != -1
   # and strings.islower()):
   # print("7th: " + cool + '  ' + i_am_shouting.upper() + '! ' + "4" + "real" + ' ' 
         # + str(len(i_am_shouting)) + ' ' + "characters long." + ' ' 
         # + 'Now, your name is' + ' ' + name + ' and ' + str(your_level) + " is your level." 
         # + " Please, feel free to grab the " + fruit + " and listen to my " +  strings + " " + instrument + ".")     
#else: 
   # print("Warning: math is out of scope 3, please try again with a higher level, and a goat guitar.")


# if the user put the right answer, it will show the message with all the variables, if not, it will show a warning message.

if (increasing and nope is None and total < 8 and your_level > 0 
    and fruit == "apple" and fruit.find("l") == 3
    and instrument == "guitar" and instrument.find("ar") != -1
    and strings == "goat" and strings.islower()):
    print("8th: " + cool + '  ' + i_am_shouting.upper() + '! ' + "4" + "real" + ' ' 
          + str(len(i_am_shouting)) + ' ' + "characters long." + ' ' 
          + 'Now, your name is' + ' ' + name + ' and ' + str(your_level) + " is your level." 
          + " Please, grab an " + fruit + " and listen to the the " +  strings + " " + instrument + ".")     
else: 
    print("Warning: math is out of scope 3, please try again with a higher level, an inferior brand of phone, and a goat guitar.")


# cats and dogs

if (increasing and nope is None and total < 8 and your_level > human_was_level > 0 
    and fruit == "apple" and fruit.find("l") == 3
    and instrument == "guitar" and instrument.find("ar") != -1
    and strings == "goat" and strings.islower()):
       print("9th: " + cool + '  ' + i_am_shouting.upper() + '! ' + "4" + "real" + ' ' 
          + str(len(i_am_shouting)) + ' ' + "characters long." + ' ' 
          + 'Now, your name is' + ' ' + name + ' and ' + str(your_level) + " is your level." 
          + " Your cat is level " + str(cat_level) + " and your dog is level " + str(dog_level) + "."
          + " Please, grab an " + fruit + ", listen to the " +  strings + " " + instrument + ", "
          + "and pet your cat and dog, they are very happy to see you.")
else: 
    print("BUT WHY!: math needs work, ask the pets when they got you, your level is low, you mentioned a superior brand of phone, and need to listen to the goat guitar")

# if the user put the right answer, it will show the message with all the variables, if not, it will show a warning message.


# 1
# name
# your_level = 2
# fruit = apple
# instrument = guitar
# strings = goat
# human_was_level = 1
# cat_was_level = 11
# dog_was_level = 10
# levels_passed = 1
# cat_level = 11 + 4*1 = 15
# dog_level = 10 + 5*1 = 15
# output: [2, 15, 15]

# 2
# name
# your_level = 3
# fruit = apple
# instrument = guitar
# strings = goat
# human_was_level = 2
# cat_was_level = 20
# dog_was_level = 19
# levels_passed = 1
# cat_level = 20 + 4*1 = 24
# dog_level = 19 + 5*1 = 24
# output: [3, 24, 24]

# 3
# name
# your_level = 10
# fruit = apple
# instrument = guitar
# strings = goat
# human_was_level = 2
# cat_was_level = 24
# dog_was_level = 24
# levels_passed = 8
# cat_level = 24 + 4*8 = 56
# dog_level = 24 + 5*8 = 64
# output: [10, 56, 64]