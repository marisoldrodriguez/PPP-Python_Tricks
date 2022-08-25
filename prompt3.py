# Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False.
# Input list: [3,6,9,2] List after lambda function and list comprehension: [False, True, False, True]

List = [3,6,9,2]
even_odd = lambda x: True if x%2 == 0 else False
print("Input list: ", List)
print("List comprehension: ", [even_odd(x) for x in [3,6,9,2]])
