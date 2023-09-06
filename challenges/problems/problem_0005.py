# Array Manipulation: Given an array of integers, complete the function that takes the array as 
# input and returns a new array with all the odd numbers at the beginning and all the even 
# numbers at the end, preserving the original order of the number.

def get_organized_numbers(numbers):
    return []

if __name__=='__main__':
    assert get_organized_numbers([1,2,3,4,5,6,7,8,9,10]) == [1,3,5,7,9,2,4,6,8,10]
    assert get_organized_numbers([2,4,6,8,10]) == [2,4,6,8,10]
    assert get_organized_numbers([1,2]) == [1,2]
    assert get_organized_numbers([1,3,5,7,9]) == [1,3,5,7,9]

