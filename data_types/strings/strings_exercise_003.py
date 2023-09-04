# Complete the function below to convert a list of words into a string, delimited by a single space.
# If the last value in the list is a period, question mark, or exclamation point - it shouldn't have a space before it.

def convert_list_to_string(list_of_words):
    return ""

assert convert_list_to_string(['What','are','you','doing','?']) == "What are you doing?"
assert convert_list_to_string(['Hello', 'there', '!']) == "Hello there!"
assert convert_list_to_string(['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill', '.']) == "Jack and Jill went up the hill."

