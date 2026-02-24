person = {"name":"Alice", "age":25, "city":"NYC"}
scores = {"math": 95, "science": 88, "english": 92}
empty_dict = {}

#Accessing values
print(person["name"])
print(person.get("age"))
print(person.get("email", "Not found"))  # Not found (default)

# Modifying dictionaries
person["email"] = "alice@email.com"  # Add new key
person["age"] = 26                   # Update existing
del person["city"]                   # Remove key
removed = person.pop("age")          # Remove and return value


print(len(person))
print(person.keys())
print(list(person.keys()))
print(person.values())
print(list(person.items()))

# Looping through dictionaries
print("------")
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}--{value}")


# output
# Alice
# 25
# Not found
# 2
# dict_keys(['name', 'email'])
# ['name', 'email']
# dict_values(['Alice', 'alice@email.com'])
# [('name', 'Alice'), ('email', 'alice@email.com')]
# ------
# name Alice
# email alice@email.com
# name--Alice
# email--alice@email.com


# Dictionary methods cheat sheet:

# get(key, default) - Get value, return default if missing
# keys() - Get all keys
# values() - Get all values
# items() - Get all key-value pairs
# pop(key) - Remove key and return value
# update(other_dict) - Merge dictionaries