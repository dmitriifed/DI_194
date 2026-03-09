# """
# GenAI-ML / Week02 / Day2 / ExerciseXP

# Instructions:
# - Write your solution below.
# - Add tests in a __main__ block.
# """

# # LIVE DEMO — Inheritance with Vehicles
# # Parent: Vehicle | Child: Car | Grandchild: ElectricCar
# # Let's try it
# # Your code here

# class Vehicle:
#   def __init__(self, make, speed):
#     self.make = make
#     self.speed = speed

#   def describe(self):
#     print(f"{self.make} - top speed: {self.speed} km/h")

#   def move(self):
#     print(f"The {self.make} is moving.")

# class Car(Vehicle):
#   def __init__(self, make, speed, doors):
#     super().__init__(make, speed)
#     self.doors = doors

#   def honk(self):
#     print(f"The {self.make} goes: Beep beep!")

# class ElectricCar(Car):
#   def __init__(self, make, speed, doors, battery_kw):
#     super().__init__(make, speed, doors)
#     self.battery_kw = battery_kw

#   def charge(self):
#     print(f"Charging {self.make} - battery: {self.battery_kw} kW")


# tesla = ElectricCar("Tesla Model 3", 250, 4, 75)
# tesla.describe()
# tesla.honk()
# tesla.charge()
# print(tesla.doors)
  

# ### 


# class Pet:
#    is_lazy = False

#    def __init__(self, name: str, age: int):
#     self.name = name
#     self.age = age

#    def description(self):
#      print(f"{self.name} is {self.age} years old")

#    def make_sound(self):
#      print("...")  

# class Cat(Pet):
#   is_lazy = True

#   def __init__(self, name: str, age: int, indoor: bool):
#     super().__init__(name,age)
#     self.indoor = indoor
    
#   def make_sound(self):
#     print(f"{self.name} says: Meow!")


# class Dog(Pet):
#   is_lazy = True

#   def __init__(self, name: str, age: int, indoor: bool, breed: str):
#     super().__init__(name,age)
#     self.indoor = indoor
#     self.breed = breed
    
#   def make_sound(self):
#     print(f"{self.name} says: Woof!")

#   def fetch(self, item: str):
#     print(f"{self.name} fetches the {item}!")



# #TEST
# cat = Cat("Whiskers", 4, indoor=True)
# dog = Dog("Buddy", 2, "Beagle")

# cat.description()
# cat.make_sound


###   


# class Dog: 
#   def __init__(self, name: str, age: int, weight: float, breed: str):
#     self.name=name
#     self.age=age
#     self.weight=weight
#     self.breed=breed

#   def run_speed(self, weight: float, age: int):
#         if self. age <= 0
#             return 0.0
#         return (weight / age * 10)
  
#   def fight(self, other_dog: "Dog"):
#       my_speed = self.run_speed()
#       their_speed = other_dog.run_speed()
#       if my_speed > their_speed:
#           print(f"{self.name} wins")
#       elif their_speed > my_speed:
#           print(f"{other_dog.name} wins")
#       else:
#           print("it's a draw!")

# class Dogs:
#     def __init__(self):
#         self.pack = []
    
#     def add_dog(self, dog: "Dog"):
#         self.pack.append(dog)

#     def fight_all(self):
#         for i in range(len(self.pack)):
#             for j in range(i + 1,(len.self)):


###CATS          


class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

    def sing(self):
        for animal in self.animals:
            print(animal.sing())


class Cat:
    is_lazy = True

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def walk(self):
        return f'{self.name} is just walking around'
    
    def sing(self, sound=[1]):
        return f'{self.name} is singing {self.sound}'



class Bengal(Cat):
    pass
class Chartreux(Cat):
    pass

class Siamese(Cat):
    pass  


bengal_obj = Bengal("Benny", "Meow")
chartreux_obj = Chartreux("Chloe", "Mrrr")
siamese_obj = Siamese("Sia", "Shsh")

all_cats = [bengal_obj, chartreux_obj, siamese_obj]
sara_pets = Pets(all_cats)

sara_pets.walk()
sara_pets.sing()

###

#SHORTER CATS

class Pets:
    def __init__(s, animals): s.animals = animals
    def walk(s): [print(a.walk()) for a in s.animals]
    def sing(s): [print(a.sing()) for a in s.animals]

class Cat:
    def __init__(s, name, age, sound): s.name, s.age, s.sound = name, age, sound
    def walk(s): return f"{s.name} is just walking around"
    def sing(s): return f"{s.name} is singing {s.sound}"

class Bengal(Cat): pass
class Chartreux(Cat): pass
class Siamese(Cat): pass

sara_pets = Pets([Bengal("Benny",3,"Meow"), Chartreux("Chloe",5,"Mrrr"), Siamese("Sia",2,"Shsh")])
sara_pets.walk(); sara_pets.sing()

###

#DOGS

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
       return f"{self.name} goes Woof"

    def run_speed(self):
        return f"{self.weight/self.age * 10}"
    
    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} wins"
        elif my_power < other_power:
            return f"{other_dog.name} wins"
        else:
            return "tie"


dog1 = Dog("Rex", 4, 20)
dog2 = Dog("Buddy", 5, 25)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))


###
# Train dog 

from dog_import import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names = [self.name] + [dog.name for dog in args]
        print(", ".join(names) +" all play together")

    def do_a_trick(self):
        tricks = [
            "does a barrel roll",
            "stands on his back legs",
            "shakes your hand",
            "plays dead"
            ]
        if self.trained:
            index = random.randint(0, len(tricks)-1)
            print(f"{self.name} {tricks[index]}")


d1 = PetDog("Doodel-Shtroodel", 2, 10)
d2 = PetDog("Schnitzel-Witzel", 3, 12)
d3 = PetDog("Collie-Ravioli", 1, 8)

d1.train()
d1.play(d2, d3)
d1.do_a_trick()
d2.do_a_trick()


###

class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)   # age now goes to age
        new_person.last_name = self.last_name  # assign family last name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print(f"{first_name} are under 18")
                else:
                    print(f"{first_name} are over 18")
                return
        print("Not found")


fam = Family("Unkle Sam's Family")
fam.born("Johny", 15)
fam.born("Donny", 19)

fam.check_majority("Johny")
fam.check_majority("Donny")

# def main():
#     pass

# if __name__ == "__main__":
#     main()
