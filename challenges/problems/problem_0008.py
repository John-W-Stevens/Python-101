# Duplicate Character Remover: Write a function that takes a string as input and returns a 
# new string with all of the duplicate characters removed. The resulting string should maintain 
# the original order of the characters.

def remove_duplicate_characters(string):
    return ''

if __name__=='__main__':
    assert remove_duplicate_characters('abcdaefgb') == 'bcdefg'
    assert remove_duplicate_characters('abcdefghijklmnopqrstuvwxyz') == 'abcdefghijklmnopqrstuvwxyz'
    assert remove_duplicate_characters('11111') == ''