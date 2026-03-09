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


