# Replace the if/else block in the following function with a ternary operator that does the same thing

def contains_odd_number_of_characters(input):
    if len(input) % 2 != 0:
        return True
    else:
        return False
    
assert contains_odd_number_of_characters("Hello") == True
assert contains_odd_number_of_characters("World!") == False