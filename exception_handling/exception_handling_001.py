# The following code throws a IndexError exception. This function is poorly written because eventually,
# line 9 will result in an IndexError exception. We should modify this method such that no exception is
# raised however for the purposes of this exercise, do not modify any the logic in the while loop. Instead,
# use a try/except block to catch the IndexError exception. When we do catch the exeption, this function
# should just return.

def print_all_numbers_in_list(list_of_numbers):
    index = 0
    
    while list_of_numbers[index]:
        print(list_of_numbers[index])
        index += 1

print_all_numbers_in_list([1,2,3])