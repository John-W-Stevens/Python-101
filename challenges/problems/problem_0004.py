# Anagram Finder: Complete the function that takes two strings as input and returns true if 
# the two strings are anagrams (both have the same letters with the same occurrence count, 
# but in a different order), and false if they are not.

def is_anagram(string_1, string_2):
    return False

if __name__=='__main__':
    assert is_anagram('night', 'thing') == True
    assert is_anagram('best', 'bets') == True
    assert is_anagram('slip', 'lips') == True
    assert is_anagram('education', 'cautioned') == True
    assert is_anagram("bat", "cat") == False
    assert is_anagram("education", "caution") == False