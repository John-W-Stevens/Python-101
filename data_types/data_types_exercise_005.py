# Consider the following code:
    # x = "1" + 1

# This throws a 'TypeError' exception because we can't concatonate an int type with a string type.
# Implement logic in the function below return the concatonated value of the str and int arguments.
# Hint, consider how we might 'cast' the int to a str.

def concatonate_int_to_string(string, number):
    if type(number) != int:
        raise TypeError("Number must be int type!")
    
    # Your code here
    return

assert concatonate_int_to_string("1", 1) == "11"