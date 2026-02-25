pairs = [(x,y) for x in range(3) for y in range(3)]
print(pairs)


# output
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

matrix = [[1,2,3], [4,5,6],[7,8,9]]
flat = [nums for rows in matrix for nums in rows]
print(flat)

# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]