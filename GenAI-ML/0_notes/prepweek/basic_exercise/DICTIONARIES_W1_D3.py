## DICTIONARIES_W1_D3

# access the value of key history

sample_dict = {
    "class":{
        "student":{
            "name":"mike",
            "marks":{
                "physics": 70,
                "history": 80
            }
        }
    }
}



print(sample_dict["class"]["student"]["marks"]["history"])

sample_dict["class"]["student"]["marks"]["history"] = 100

history = sample_dict["class"]["student"]["marks"]["history"]
print(history)


sample_dict = {
    "name": "kelly",
    "age":25,
    "salary": 8000,
    "city": "New York"
}

key_to_remove = ["name", "salary"]
for item in key_to_remove:
    sample_dict.pop(item, None)

print(sample_dict)
                                                                  




my_books = {
    "title": "harry Potter",
    "author": "JK Rowling",
}

print(list(my_books.values())[1])

