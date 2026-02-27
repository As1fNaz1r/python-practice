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