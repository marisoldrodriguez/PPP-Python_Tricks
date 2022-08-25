# Write a lambda function to cube every element of a list.
# Original list: [3,6,9,2] List after lambda function: [27,216,729,8]

originalList = [3,6,9,2]
cubedList = lambda x: [i*i*i for i in x]
print(cubedList([3,6,9,2]))