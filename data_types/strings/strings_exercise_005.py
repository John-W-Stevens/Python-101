# Complete the following functions to do the following:
  # If the string contains the word 'cat' -> return the entire string in upper case
  # If the string contains the word 'DOG' -> return the entire string in lower case
  # If the string does not contains only whitespace characters -> return 'ALL WHITESPACE'
  # If this string doesn't match any of those conditions, return 'NONE MATCH'


def process_string(a_string):
    if contains_cat(a_string):
        # Your code here
        return
    
    if contains_DOG(a_string):
        # Your code here
        return

    if contains_only_whitespace(a_string):
        # Your code here
        return

    return "NONE MATCH"

def contains_cat(a_string):
    # Your code here
    return False

def contains_DOG(a_string):
    # Your code here
    return False;

def contains_only_whitespace(a_string):
    # Your code here
    return False;

assert process_string("A cat jumped on me!") == "A CAT JUMPED ON ME!"
assert process_string("A DOG ATE MY MUFFIN!") == "a dog ate my muffin!"
assert process_string("     ") == "ALL WHITESPACE"
assert process_string("A wallaby suprised me!") == "NONE MATCH"