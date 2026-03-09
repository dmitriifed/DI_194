"""
GenAI-ML / Week02 / Day4 / ExerciseXP

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""
import os
print(os.listdir())

def get_number():
    user_input = "hello"  # simulate bad input
    try:
        number = int(user_input)
        print(f"You entered: {number}")
    except ValueError:
        print(f"'{user_input}' is not a valid number!")


get_number()


def get_number_good():
    user_input = "42"  # simulate good input
    try:
        number = int(user_input)
        print(f"You entered: {number}")
    except ValueError:
        print(f"'{user_input}' is not a valid number!")



get_number_good()


def get_words_from_file(file_path):
    with open(file_path, "r", encoding = "utf-8") as f:
        content = f.read()
    words = content.split()
    return words

print(get_words_from_file("word.txt"))






import json

student_data = {"name": "Charlie", "grades": [85, 92, 78, 95], "graduated": False}

# WHEN TO USE:
# Use these when you're reading from or writing to a .json file on disk.

# Write Python dic -> Json file (dump = dump to file)
with open("student.json", "w") as f:
    json.dump(student_data, f, indent=2)

# Read JSON file -> Python dict (load = load from file)
with open("student.json", "r") as f:
    loaded = json.load(f)


print(f"Loaded: {loaded}")
print(f"Name: {loaded['name']}")
print(f"Average grade: {sum(loaded['grades']) / len(loaded['grades'])}")


import json

# Json string -> Python dict (loads = load from string)

# WHEN TO USE:
# Use these when you get JSON from an API response or need to send JSON in a request.

json_string = '{"name": "Alice", "age": 30, "languages": ["Python", "JavaScript"]}'
data = json.loads(json_string)

print(f"Type {type(data)}")
print(f"Name: {data['name']}")
print(f"Languages: {data['languages']}")
print()

person = {"name": "Bob", "age": 25, "active": True, "score": None}

ugly = json.dumps(person)
print(f"Ugly:   {ugly}")

pretty = json.dumps(person, indent=2)
print(f"Pretty:\n{pretty}")


import json

sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Parse the JSON string
data = jason.loads(sampleJson)
print = data(f"full dict: {data}")
# Step 2: Access and print the salary

# Step 3: Add birth_date to the employee

# Step 4: Save to employee.json

# Step 5: Read back and verify



# def main():
#     pass


# if __name__ == "__main__":
#     main()
