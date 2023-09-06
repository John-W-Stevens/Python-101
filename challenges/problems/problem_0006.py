import sys
import io

# FizzBuzz: Complete the function that takes a single integer n as input and 
# prints numbers from 1 to n. For multiples of 3, the function should print "Fizz" 
# instead of the number, for multiples of 5, it should print "Buzz", 
# and for multiples of both 3 and 5, it should print "FizzBuzz".

debug_mode = True # Flip this value to False in order to test your solution

def fizz_buzz(n):
    # Your code here
    return

if debug_mode:
    fizz_buzz(5)

if __name__=='__main__' and not debug_mode:
    captured_output = io.StringIO()
    sys.stdout = captured_output
    fizz_buzz(15)
    sys.stdout = sys.__stdout__

    list_of_print_statements = captured_output.getvalue().split('\n')
    assert list_of_print_statements[0] == '1'
    assert list_of_print_statements[1] == '2'
    assert list_of_print_statements[2] == 'Fizz'
    assert list_of_print_statements[3] == '4'
    assert list_of_print_statements[4] == 'Buzz'
    assert list_of_print_statements[5] == 'Fizz'
    assert list_of_print_statements[6] == '7'
    assert list_of_print_statements[7] == '8'
    assert list_of_print_statements[8] == 'Fizz'
    assert list_of_print_statements[9] == 'Buzz'
    assert list_of_print_statements[10] == '11'
    assert list_of_print_statements[11] == 'Fizz'
    assert list_of_print_statements[12] == '13'
    assert list_of_print_statements[13] == '14'
    assert list_of_print_statements[14] == 'FizzBuzz'