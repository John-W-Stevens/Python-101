# Modify the following method to return a dictionary of names to ages given an input list of names and another
# list of ages. Assume that the lists of names and ages are the same length and the names and ages in corresponding
# index positions go together (i.e., the first name in the names list should map to the first name in the ages list)
# Hint: Consider using Python's 'zip' function.

def get_names_and_ages_dict(list_of_names, list_of_ages):
    # Your code here
    return

names = ["John", "LeeAnn", "Caleb", "Madeleine", "Grace", "Ezra"]
ages = [35, 36, 12, 6, 5, 4]

names_and_ages_dict = get_names_and_ages_dict(names, ages)
assert names_and_ages_dict.get("John") == 35
assert names_and_ages_dict.get("LeeAnn") == 36
assert names_and_ages_dict.get("Caleb") == 12
assert names_and_ages_dict.get("Madeleine") == 6
assert names_and_ages_dict.get("Grace") == 5
assert names_and_ages_dict.get("Ezra") == 4
