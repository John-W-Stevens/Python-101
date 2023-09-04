# Use a while loop to count all the 'a' characters in a string. 'a' can be either upper or lower case. 

def count_all_A_in_string(someString):

    # Use this variable to keep track of all A/a's counted
    count = 0

    # your code here

    return count

# Expect this function to return 11 in the following case (11 a/A are in this string)
assert count_all_A_in_string("An agitated aardvark attacked an alligator") == 11

# Expect this function to return 0 in the following case (no a/A in string)
assert count_all_A_in_string("Bob broke the world record.") == 0