# The following code is incorrect (it throws an exception). Debug and fix it such that it produces the correct result.

def get_count_of_all_odd_numbers(list_of_numbers):
    # Input validation
    if type(list_of_numbers) != list:
        # If the input isn't a list, return 0
        return 0;

    if list_of_numbers == []:
        # If the input is an empty list, return 0
        return 0
    
    count = 0;
    index = 0;
    length_of_list = len(list_of_numbers)

    while index <= length_of_list:
        number = list_of_numbers[index]

        if number % 2 != 0:
            count += 1
        index += 1

    return count

# Expect this function to return 5.
assert get_count_of_all_odd_numbers([1,2,3,4,5,6,7,8,9,10]) == 5
