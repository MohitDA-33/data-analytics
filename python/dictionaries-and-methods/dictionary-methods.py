# Dictionary Methods, by using methods we can access the key-value pairs, change, add or remove them.

student = {
    "Name": "Mohit",
    "City": "Delhi",
    "Company": "Meta"
}

print(student)
print(student["City"])   # Using indexing to find the value of the key.
print(student["Company"])

print(student.get("Name"))   
print(student.get("namee"))   # If the value you are trying to find through the key does not exist, it will show an error so if you dont want an error we use .get function.

student["City"] = "Lucknow"   # Updating the existing value.
student["Email"] = "Example@gmail.com"   #  Adding a new key-value pair.
print(student)

company = student.pop("Company")   # .pop, removes the key-value pair and returns the value of it.
print(company)

student["Age"] = 22
last_e = student.popitem()   # .popitem, removes a random element from the dictionary and returns it value.
print(last_e)

del student["City"]   # del, deletes a key-value pair.
print(student)

student.clear()   # .clear, clears or empties the whole dictionary.
print(student)

# Dictionary Keys, Values, and Items

names = {"Name1": "Mohit", "Name2": "Harry", "Name3": "Larry"}
key = names.keys()   # print/returns all the keys in the dictionary.
print(key)
value = names.values()   # print/returns all the values in the dictionary.
print(value)
item = names.items()   # # print/returns all the keys-value pair in the form of tuples.
print(item)

# Looping Through a Dictionary: You can also create a loop to access key-value pairs.

for key in names:   # Here creating a loop to access all the keys in the dictionary.
    print(key)

for value in names.values():   # Here creating a loop to access all the values in the dictionary.
    print(value)

for key, value in names.items():   # And here creating a loop to access all the key-value pairs.
    print(key, value)

print("Name1" in names)   # Using membership operator to check is the key exists in the dictionary or not.

new_names = names.copy()   # .copy, creates a copy of the dictionary.
print(new_names)

new_names.update({   
    "Name4": "Parry",   # .update, updates the dictionary by adding new key-value pairs in them.
    "Name5": "Rohit"
})

print(new_names)

# You can also create a nesting dictionary (one inside another).

user = {   # Here user is a parent directory.
    "id": 1,
    "profile": {   # And inside parent directory (user) is (profile) as a nesting directory. 
        "Name": "Mohit",   
        "Class": "12th",
    }
}

print(user["profile"])   # To access nested directory we use indexing.
print(user["profile"] ["Name"])
