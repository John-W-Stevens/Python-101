# The following code raises an exception. Debug and fix it such that the test cases pass.

def get_filtered_animals(list_of_animals, starting_charachter):

    animals_that_start_with_w = []

    for index in range(len(list_of_animals) - 1):
        animal = list_of_animals[index]
        if animal.startswith(starting_charachter):
            animals_that_start_with_w.append(animal)

    return animals_that_start_with_w

animals = ['cat', 'dog', 'wallaby', 'hamster', 'walrus']

result = get_filtered_animals(animals, 'w')

assert 'wallaby' in result
assert 'walrus' in result