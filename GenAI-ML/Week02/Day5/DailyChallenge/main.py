"""
GenAI-ML / Week02 / Day5 / DailyChallenge

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""


# Answer the following questions:

# What is a class?
# A class is a template for creating objects. 
# It defines data(attributes) and behaviors(methods) 
# that its objects(instances) will have.
# eg. class Example
#             def __init__(self, something, somethingelse):
#                          self.something=something
#                          self.somethingelse=[]
      

# What is an instance?
# An instance is an object made from a class. 
# It has its own values for the classes atributes(its state)
# and it can use classes methods.
# 
# class Dog:
#     def __init__(self, name):
#         self.name = name
# d1 = Dog("Mika")   
# d2 = Dog("Rex") 


# What is encapsulation?
# Encpsulation is a way to build and access attributes 
# and methods inside a class, so it can only be
# read/ changed controllably.

# class BankAccount:
    # def __init__(self, balance):
    #     self._balance = balance   

    # def deposit(self, amount):
    #     if amount > 0:
    #         self._balance += amount


# What is abstraction?
# Abstraction means showing a simple, 
# clear interface (what you can do) while hiding 
# the complex implementation details (how it works).

# What is inheritance?
# Inheritance is when a class (child/subclass) 
# is built from another class (parent/base class), 
# automatically getting its attributes and methods, 
# and optionally adding or overriding behavior.

# class Animal:
#     def speak(self):
#         return "..."

# class Dog(Animal):        
#     def speak(self):
#         return "woof"


# What is multiple inheritance?
# Multiple inheritance is when a class inherits 
# from more than one parent class, 
# so it can use/merge behavior from multiple sources.

# class A: ...
# class B: ...
# class C(A, B): ...


# What is polymorphism?
# is a concept in which something occurs 
# in several different forms

# class Dog:
#     def speak(self): return "woof"

# class Cat:
#     def speak(self): return "meow"

# for animal in [Dog(), Cat()]:
#     print(animal.speak())

# What is method resolution order or MRO?
# Method Resolution Order is the order Python follows 
# to search for a method/attribute in a class hierarchy, 
# especially with multiple inheritance.
import random

class Card:
    suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values =  ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"    
      

class Deck:
    def __init__(self):
        self.cards = []
        self.shuffle()

    def shuffle(self):
        self.cards = []
        for suit in Card.suit:
            for values in Card.values:
                 card_object = Card(suit,values)
                 self.cards.append(card_object)
        random.shuffle(self.cards)   

    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()







def main():
    deck = Deck()
    print(f"Deck has {len(deck.cards)} cards after shuffle")

    card1 = deck.deal()
    card2 = deck.deal()
    print(f"Dealt: {card1}")
    print(f"Dealt: {card2}")
    print(f"Deck now has {len(deck.cards)} cards")



if __name__ == "__main__":
    main()
