# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# lists are part of the collections familiy in python.\
# Creating a list.
my_list = [1, 2, 3, 4, 5]
print(my_list) # [1, 2, 3, 4, 5]
print(len(my_list)) #5 
print(type(my_list)) #<class 'lists'>
print(my_list[0]) # 1
print(my_list [1:4]) # [2, 3, 4]
print(my_list[1:]) #[2, 3, 4, 5]
print(my_list[:-1]) #[1, 2, 3, 4]
# Reverse the list
print(my_list[::-1]) #[5, 4, 3, 2, 1]
#modify a list
my_list.append(6) 
print(my_list) # [1, 2, 3, 4, 5, 6]
#add 7 and 8 to the end of the list
my_list.extend([7, 8])
print(my_list) # [1, 2, 3, 4]
#remove the last item
my_list.pop()
print(my_list) #
#
my_list.pop(2)
print(my_list) #
# Sort the list in accending order
my_list.sort()
print(my_list) #
#remove the list
my_list.reverse()
print(my_list) #
# remove to remove a specific value
my_list.remove(4)
print(my_list) #
# Remove hte last item using negative index
my_list.remove(1)
print(my_list) #
# Add 50 more character to the end of the list
new_list = list(range(12, 120))
print(new_list)
my_list.append(new_list)
print(my_list)
print(my_list[::3])
del [my_list[ : : 3]]

# list functions
# .append() - adds an item to the end of the list
# .pop(index) - removes and returns the item at the specified index (default is the last item)
# .sort() - sorts the list in ascending order
# .reverse() - reverses the order of the list       
# .remove(value) - removes the first occurrence of the specified value
# .extend(iterable) - adds all items from the iterable to the end of the list

cakes = ['chocolate', 'vanilla', 'red velvet', 'carrot']
print(cakes)
#access the first item
print(cakes[0]) # chocolate
#access the last item
print(cakes[-1]) # carrot
# want to chocolate cake instead of vanilla
cakes[0] = 'strawberry'
print(cakes) # ['strawberry', 'vanilla', 'red velvet', 'carrot']
# add a new cake to the end of the list
cakes.append('lemon')
print(cakes) # ['strawberry', 'vanilla', 'red velvet', 'carrot', 'lemon']
cakes[1] = 'chocolate'
print(cakes) # ['strawberry', 'chocolate', 'red velvet', 'carrot', 'lemon']
# remove the last cake
cakes.pop()
print(cakes) # ['strawberry', 'chocolate', 'red velvet', 'carrot']
# insert a new cake at index 2
cakes.insert(2, 'funfetti')
print(cakes) # ['strawberry', 'chocolate', 'funfetti', 'red velvet', 'carrot']

# Examples:

my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

my_list.pop(1)
print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# # Practice Problems:

# # Create a list with 5 of your favorite foods.
favorite_foods = ['pizza', 'sushi', 'tacos', 'ice cream', 'pasta']
# # Print the second and last item.
print(favorite_foods[1])
print(favorite_foods[-1])
# # Add a new item using .append().
favorite_foods.append("french fries")
print(favorite_foods)
# # Remove the first item using .pop(0).
favorite_foods.pop(0)
print(favorite_foods)
# # Reverse your list using .reverse().
favorite_foods.reverse()
print(favorite_foods)

my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

my_set.add(6)

my_set.remove(3)
print(my_set)

print(4 in my_set)
print(3 in my_set)

my_tuple = {1, 2, 3, 4 , 5}
print(my_tuple)
print(type(my_tuple))
print(my_tuple{0:})
print(my_tuple[1:4])