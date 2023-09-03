# Make the following function return true in all cases where the input is a string (and false otherwise)

def is_input_a_string(input):
    # your code here
    return False

assert (is_input_a_string("")) == True
assert (is_input_a_string("Hello World!")) == True
assert (is_input_a_string(28)) == False
assert (is_input_a_string(["Hello World!"])) == False