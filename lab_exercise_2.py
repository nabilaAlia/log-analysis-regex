### Exercise 2: Sorting Log Data
After extracting error counts using regex, you'll have a dictionary. Use the following steps to sort that data for a final report.

# 1. Create a dictionary representing extracted log counts (e.g., error types and their frequency).
fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}

# 2. Convert dictionary to a list of tuples and sort by the default (the key/index 0).
# fruit.items() is used because dictionaries themselves cannot be sorted directly.
sorted(fruit.items())
# Output: [('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

# 3. Use the 'operator' module for more precise control over sorting.
import operator
# Use itemgetter(0) to explicitly sort by the first element of the tuple (the fruit names).
# This results in an alphabetical sort.
sorted(fruit.items(), key=operator.itemgetter(0))
# Output: [('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

# 4. Use itemgetter(1) to sort by the second element of the tuple (the numeric values).
# This is useful for seeing which log entries appear the least or most.
sorted(fruit.items(), key=operator.itemgetter(1))
# Output: [('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]

# 5. Add 'reverse=True' to sort in descending order.
# In log analysis, this is the most common sort as it highlights the most frequent errors first.
sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)
# Output: [('bananas', 7), ('apples', 5), ('oranges', 3), ('pears', 2)]
