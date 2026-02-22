"""
GenAI-ML / Week02 / Day1 / DailyChallenge

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""

class Farm:#this class wil represent the farm and its animals
    def __init__(self, farm_name):
         self.name = farm_name
         self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        lines=[f"{self.name}'s farm"]

        for animal_type, count in self.animals.items():
            lines.append(f"{animal_type} : {count}")

        lines.append("")         
        lines.append("E-I-E-I-0!")

        print("\n".join(lines))


farm = Farm("MacDonald")

farm.add_animal("cow", 5)
farm.add_animal("sheep", 2)
 
farm.get_info()

# def main():
#     pass

# if __name__ == "__main__":
#     main()