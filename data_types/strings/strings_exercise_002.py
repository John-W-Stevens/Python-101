# Complete the following function to return True if the input is a string that contains the word 'what' or 'What'

def does_string_contain_what(a_string):
    return False

assert does_string_contain_what("What are you doing?") == True
assert does_string_contain_what("Where are you going?") == False

# Tricky case =)
assert does_string_contain_what("Whatever do you mean?") == False