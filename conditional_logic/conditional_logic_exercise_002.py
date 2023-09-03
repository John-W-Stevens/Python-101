# Implement an if/elif/else block in the following function to do the following:
    # if length_of_characters == 6 return a list containing SUNDAY, MONDAY, and FRIDAY
    # if length_of_characters == 7 return a list containing TUESDAY
    # if length_or_characters == 8 return a list containing THURSDAY and SATURDAY
    # if length_of_characters == 9 return a list containing WEDNESDAY

def get_days_based_on_length_of_characters(length_of_characters):
    if length_of_characters not in [6,7,8,9]:
        raise ValueError("Invalid input! 6, 7, 8, or 9 are the only accepted values!")

    # Your code here
    return

assert "SUNDAY" in get_days_based_on_length_of_characters(6)
assert "MONDAY" in get_days_based_on_length_of_characters(6)
assert "TUESDAY" in get_days_based_on_length_of_characters(7)
assert "WEDNESDAY" in get_days_based_on_length_of_characters(9)
assert "THURSDAY" in get_days_based_on_length_of_characters(8)
assert "FRIDAY" in get_days_based_on_length_of_characters(6)
assert "SATURDAY" in get_days_based_on_length_of_characters(8)
assert "SUNDAY" in get_days_based_on_length_of_characters(6)