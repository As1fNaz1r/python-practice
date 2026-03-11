names = ["Alice","Bob","Charlie"]
ages = [25,30,35]
cities = ["NYC","LA","Chicoga"]
for name,age,city in zip(names,ages,cities):
    print(f"{name} is {age} years old frrom {city}")

name_age_dict = dict(zip(names,ages))

people = []
for name,age,city in zip(names,ages,cities):
    people.append({"name":name, "age":age, "city":city})
print(people)

# Alice is 25 years old frrom NYC
# Bob is 30 years old frrom LA
# Charlie is 35 years old frrom Chicoga
# [{'name': 'Alice', 'age': 25, 'city': 'NYC'}, {'name': 'Bob', 'age': 30, 'city': 'LA'}, {'name': 'Charlie', 'age': 35, 'city': 'Chicoga'}]