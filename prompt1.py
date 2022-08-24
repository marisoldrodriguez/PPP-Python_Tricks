# Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.
# Unsorted list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] Sorted list of tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

unsortedTuple = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sortedTuple = sorted(unsortedTuple, key = lambda x: x[1])
print("Sorted Tuple: ", sortedTuple)