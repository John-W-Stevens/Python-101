# Palindrome Checker: Complete the function that takes a string as input and returns true 
# if the string is a palindrome (the string reads the same backwards as forwards, 
# ignoring whitespace and capitalization), and false otherwise.

def is_palindrome(string):
    return False

if __name__=='__main__':
    assert is_palindrome('abccba') == True
    assert is_palindrome("Madam, I'm Adam") == True
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("A man, a plan, a canal—Panama") == True
    assert is_palindrome("Bathtub") == False
    assert is_palindrome("Catalitic") == False