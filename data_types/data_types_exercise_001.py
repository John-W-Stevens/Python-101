# Complete the following function to return the type of the input variable (all test cases should pass)

def get_type_of_input(input):
    # Your code here
    return

assert get_type_of_input("28") == str
assert get_type_of_input(28) == int
assert get_type_of_input(28.00) == float
assert get_type_of_input(['a', 'b', 'c']) == list
assert get_type_of_input(('bob', 'sally')) == tuple
assert get_type_of_input({'John': '35', 'LeeAnn': '36'}) == dict
assert get_type_of_input({1, 2, 3}) == set
assert get_type_of_input(True) == bool