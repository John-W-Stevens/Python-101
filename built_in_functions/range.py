# range() function is used to create an iterable based on the specified criteria. range() is mainly used
# when constructing a for loop. You can call the range() function with different sets of arguments.

# Suppose I want a for loop that iterates over the index positions for the following list:
list_of_names = ["Susan", "Bob", "Charlies", "Dale", "Edward", "Chuck", "Mitch", "Donald", "Joe"]
# This list has 9 values. If I want a for loop that iterates from 0 -> 8 then I can create a range
# object for doing this. # Note in the following example that I am passing in the output of len(list_of_names)
# as the argument for the call to range() function. In this case, range() function will return an iterable
# of 0-9 which I can then use in my for loop. NOTE - By default, when iterating a range object, the final value
# is NOT included. So in this example, while I have a range object of (0, 9) - it will only iterate up through 8
# (not 9)

for index in range(len(list_of_names)):
    print(list_of_names[index])

# I can also call range with 2x arguments like this:
second_range = range(2, 10)

for n in range(2,10):
    print(n)
    # Note that this prints the numbers 2 - 9 and does not include (10)

# I can also pass a third argument to range() function. This is the step argument. For example,
# suppose I want to print all the odd numbers from 1 to 19 (inclusive). I can do this:

for n in range(1, 20, 2):
    print(n)

# In this example, range(1, 20, 2) means: give me a range object that starts at 1, goes up to 20, and increments by 2 -
# meaning the range object will cover (1, 3, 5, 7.... 19)