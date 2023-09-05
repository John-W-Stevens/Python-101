# This file contains 2x print statements.
# The first will execute when this script is run AND whenever this file (module) is imported into another file (checkout example_002)
# All the code inside the "if __name__=='__main__'" block will only execute when this file is run directly

# Run this script.
# Observe that both print statements execute.
# Open example_002 and run that script.
# Observe that only the first print statement in example_001 executes.

print('Hello from importing_files_example_001.py')

if __name__=='__main__':
    print("Shh, I don't execute when I'm imported.")