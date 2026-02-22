"""
GenAI-ML / Week01 / Day1 / ExerciseXP

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""


print("hello world")

print((99^3)*8)

15<8 #False
5 < 3 #False
3 == 3 #True
# 3 == "3" #Error
# "3" > 3 #Error
"Hello" == "hello" #False



name = "Dima"
age = "33"
hihgt = 178
info = f"My name is {name}. I am {age} years old. My hight is {hihgt}. And this the exercise."
print(info)


a=2
b=1
if a>b:
    print("hello world")


test_number = int(input("give a number"))
print((test_number / 2).is_integer())
   

test_name = input("what is your name")
if test_name == name:
    print ("Dima-KaDima!")
else: print("You need to be Dima")

test_hight = int(input("what is your hight?"))
if test_hight >= 145: 
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride")