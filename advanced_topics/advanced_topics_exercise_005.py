# A deeper look at comparisons.
# Run the following code, examine the output in console and explain the differences in output between 
# certain types of objects. HINT: Notice that 'is' comparison returns true for int, float, and str but
# false for list, dict, and set. Why is that?

values_for_comparison = {
    'int': [20, 20],
    'float': [1.23, 1.23],
    'string': ['foo', 'foo'],
    'list': [['foo', 'bar'], ['foo', 'bar']],
    'dict': [{'john': 28}, {'john': 28}],
    'set': [{1,2,3}, {1,2,3}]
}

def double_equals_comparison(a, b):
    return a == b

def is_comparison(a, b):
    return a is b

def dunder_comparison(a, b):
    # 'dunder' means 'double underscore'
    return a.__eq__(b)

def generate_console_data(value_1, value_2, valueType):
    print('-------------Testing {} Comparisons--------------'.format(valueType))
    print()
    print('    a. Double equals comparsion for {}, {}, output: {}'.format(value_1, value_2, double_equals_comparison(value_1, value_2)))
    print('    b. is comparsion for {}, {}, output: {}'.format(value_1, value_2, is_comparison(value_1, value_2)))
    print('    c. dunder comparsion for {}, {}, output: {}'.format(value_1, value_2, dunder_comparison(value_1, value_2)))
    print()

def test_equalities():
    for value_type, values_list in values_for_comparison.items():
        generate_console_data(values_list[0], values_list[1], value_type)

test_equalities()
