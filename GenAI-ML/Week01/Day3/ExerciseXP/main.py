"""
GenAI-ML / Week01 / Day3 / ExerciseXP

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""

def main():
    pass

if __name__ == "__main__":
    main()

###

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(dict(zip(keys, values)))

###

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    total_cost += price
    print(name, "pays", price)

print("Total cost:", total_cost)

###

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}



brand["number_stores"] = 2
print("Zara's clients are:", ", ".join(brand["type_of_clothes"]))
brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
brand.pop("creation_date")



print("Last competitor:", brand["international_competitors"][-1])
print("US colors:", brand["major_color"]["US"])
print("Number of keys:", len(brand))
print("Keys:", list(brand.keys()))

more_on_zara = {"creation_date": 1975, "number_stores": 7000}
brand.update(more_on_zara)



print("Merged brand:", brand)


###

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

char_to_index = {}
for i in range(len(users)):
    char_to_index[users[i]] = i
print(char_to_index)

index_to_char = {}
for i in range(len(users)):
    index_to_char[i] = users[i]
print(index_to_char)

sorted_users = sorted(users)
sorted_char_to_index = {}
for i in range(len(sorted_users)):
    sorted_char_to_index[sorted_users[i]] = i
print(sorted_char_to_index)

###

