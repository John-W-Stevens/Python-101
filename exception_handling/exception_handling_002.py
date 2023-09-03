# Suppose we have the following validation function. This function doesn't return anything. Instead,
# we want it to raise a ValueError exception in cases where the input doesn't have at least 5 values.
# In this case, raise a ValueError exception with a message that says "Illegal argument! Input must 
# have at least 5 values!"

def validate_list_of_numbers_has_more_than_five_values(list_of_numbers):
    if len(list_of_numbers) <= 5:
        # Your code here (replace this return value with your code)
        return
    return

try:
    validate_list_of_numbers_has_more_than_five_values([1,2,3,4])
    raise RuntimeError ("Your function didn't raise ValueError as expected!")
except ValueError:
    print("Function raised exception as expected")