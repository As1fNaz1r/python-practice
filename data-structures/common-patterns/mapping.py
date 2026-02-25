numbers = [1,2,3,4,5]
doubled = [n*2 for n in numbers]
print(doubled) 
#[2, 4, 6, 8, 10]

doubled_map = list(map(lambda x: x*2, numbers))
print(doubled_map)
# [2, 4, 6, 8, 10]

