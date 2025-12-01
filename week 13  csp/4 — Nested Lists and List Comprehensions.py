# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# fruits =    ["apple", "orange", "banana", "coconut"] # row 0
# vegtables = ["celary", "carrots", "potatoes"] 
# meats =     ["chicken", "fish", "turkey"]

# grocieries = [fruits, vegtables, meats]
# print(grocieries[1][2]) # first is down, next is verticle

# grocieries = [["apple", "orange", "banana", "coconut"], 
#               ["celary", "carrots", "potatoes"], 
#               ["chicken", "fish", "turkey"]]

# for collection in grocieries:
#     for food in collection:
#         print(food)

# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9),
#            ("*", 0, "#"))

# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
# Examples:

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[1][2])    # 6

# # List comprehension
# first_col = [row[0] for row in matrix]
# print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

# Print the first list.

# Print the second item from the third list.

# Use a list comprehension to extract the last item from each sub-list.

# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matrix[0])
print(matrix[2][1])

last_item =[row[-1] for row in matrix]
print(last_item)

squares = [x**2 for x in range(1, 11)]
for x in range(1, 11):
    print(x**2)

print(squares)