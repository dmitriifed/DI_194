"""
GenAI-ML / Week02 / Day1 / ExerciseXP

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""

class Cat:
    def __init__(self, cat_name, cat_age): 
         self.name = cat_name
         self.age  = cat_age


cat1 = Cat("bobcat", 2)
cat2 = Cat("lion", 4)
cat3 = Cat("tiger", 6)
# Step 1: Create three cat objects
# cat1 = ...
# cat2 = ...
# cat3 = ...

# Step 2: Write a function to find the oldest cat
def find_oldest_cat(cat1: Cat, cat2: Cat, cat3: Cat):
    
    if cat1.age >= cat2.age and cat1.age >= cat3.age:
        return cat1      
    if cat2.age >= cat1.age and cat2.age >= cat3.age:
        return cat2
    else:
        return cat3

   

oldest = find_oldest_cat(cat1, cat2, cat3)
print(oldest.name, oldest.age)
 

# Step 3: Print the result
oldest = find_oldest_cat(cat1, cat2, cat3)
print(...)




# 🌟 Exercise 2 — Dogs

# Step 1: Create the Dog class
class Dog:
    def __init__(self, name, height):
        self.name = name 
        self.height = height
        # add attributes here
# dog1 = Dog("bigdog", 1000)
# dog2 = Dog("smalldog", 300)
# dog3 = Dog("longdog", 450)

    def bark(self):
         print(f"{self.name}, goes Woof") # print "<name> goes woof!"

    def jump(self):
        print(f"{self.name}, jumps {self.height * 2} cm")  # print "<name> jumps <height*2> cm high!"

# Step 2: Create dog objects
davids_dog = Dog("Guido", 1000)
sarahs_dog = Dog("Bertie", 300)

sarahs_dog.bark()
sarahs_dog.jump()

davids_dog.bark()
davids_dog.jump()

# Step 3: Print details and call methods
print()
# Step 4: Compare sizes


def compare_size():
    if sarahs_dog.height > davids_dog.height:
        print("guido is smaller")
    else:
        print("bertie is smaller")

compare_size()

# 🌟 Exercise 3 — Song

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics  # store lyrics as attribute

    def sing_me_a_song(self):
          for line in self.lyrics:
              print(line)

# Create a song and call sing_me_a_song()
my_song = Song([
          "line1",
          "line2",
          "line3"])

my_song.sing_me_a_song()




animals = ['Giraffe', 'Bear', 'Baboon', 'Cat', 'Lion', 'Zebra', 'Cougar']




class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):

        groups = {}
        for animal in sorted(self.animals):
            
            letter = animal[0] #takes the first char
            if letter not in groups:
             groups[letter] = []
            groups[letter].append(animal)
        return groups

    def get_groups(self):
        groups = self.sort_animals()
        for letter, group_animals in groups.items():

            print(f"{letter}: {group_animals}")



# Create a zoo and test it
brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.get_groups()






def main():
    pass

if __name__ == "__main__":
    main()
