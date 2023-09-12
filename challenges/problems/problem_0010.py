from collections import deque
# Backspace string compare. Complete the following function compare() that takes two strings
# as an argument and returns True if they are equal, after removing backspaced characters,
# False otherwise.

# The strings can only contain lowercase characters and '#'. Backspaced characters are any characters
# followed by a '#'. For example, 'abc#d' -> 'abd', 'xyz##' -> 'x'.
# The following strings are equal: 'abcd#' ''axc##bq#cc#d'.

def backspace_string_compare(string_1, string_2):
    strings_to_compare = []
    
    for string in [string_1, string_2]:
        stack = deque()
        for char in string:
            if char != '#':
                stack.append(char)
            elif len(stack) > 0:
                stack.pop()
        strings_to_compare.append("".join(stack))

    return strings_to_compare[0] == strings_to_compare[1]

backspace_string_compare('abc', 'abc')

if __name__=='__main__':
    class bcolors:
        OKGREEN = '\033[92m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'

    test_cases = [
        ('abc', 'abc', True),
        ('a#b#c#', '', True),
        ('', '', True),
        ('#####', '############', True),
        ('abc###', 'ab###', True),
        ('abc', 'abcd##', False),
    ]
    
    print()
    print('-----------------------Testing Solution-----------------------')
    for index, test in enumerate(test_cases):
        string_1 = test[0]
        string_2 = test[1]
        expected = test[2]

        result = backspace_string_compare(string_1, string_2)

        if result == expected:
            print(bcolors.OKGREEN + '  PASSED' + bcolors.ENDC + ' - Test {} - verified input of ("{}", "{}") returned expected: {}'.format(index + 1, string_1, string_2, expected))
        else:
            print(bcolors.FAIL + '  FAILED' + bcolors.ENDC + ' - Test {} - given input of ("{}", "{}"), expected: {}, but got {}'.format(index + 1, string_1, string_2, expected, result))