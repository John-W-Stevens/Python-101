import random
import time
import signal
from contextlib import contextmanager
# Complete the function two_sum that takes a list of intergers and a target integer
# and returns a list of the index positions of the two numbers in the list that add up to the target.

# Example long solution
def two_sum_long(numbers, target):
   
    # Get a map of numbers and their indexes
    numbers_dict = {number:index for (index, number) in enumerate(numbers)}

    # Iterate numbers in map
    for number in numbers_dict.keys():
      # Track the index position of the 'compliment's' index
      compliment_value_index = None

      if number == target:
         # Edge case, number and target are the same. Check if map has a zero
         compliment_value_index = numbers_dict.get(0)
      elif number < target:
         # If number is less than target, find a positive compliment
         compliment_value_index = numbers_dict.get(abs(number - target))
      elif number > target:
         # If number is greater than target, find a negative compliment
         compliment_value_index = numbers_dict.get(-abs(number - target))

      if compliment_value_index == None:
         # If no compliment is found, continue the search
         continue
      elif compliment_value_index == numbers_dict.get(number):
         # Edge case - the compliment cannot be the same number, continue the search
         continue
      else:
         # We have a match, return a list of both indecies
         return [numbers_dict.get(number), compliment_value_index]
   
    return None

# Example short solution
def two_sum_short(numbers, target):
    numbers_dict = {number: index for (index, number) in enumerate(numbers)}

    for number, index in numbers_dict.items():
        compliment = target - number
        if compliment in numbers_dict and numbers_dict[compliment] != index:
            return [index, numbers_dict[compliment]]

    return None

# Example naive solution 1
def two_sum_bad(numbers, target):
    for i in range(len(numbers)):
      number_1 = numbers[i]
      for j in range(len(numbers)):
         if i == j:
            continue

         number_2 = numbers[j]        

         if number_1 + number_2 == target:
            return [i,j]
    return None

# Example naive solution 2
def two_sum_better_but_still_bad(numbers, target):
    for i in range(len(numbers) - 1):
      number_1 = numbers[i]
      for j in range(i + 1, len(numbers)):
         if i == j:
            continue

         number_2 = numbers[j]        

         if number_1 + number_2 == target:
            return [i,j]
    return None

################################################### TEST CASES ###################################################

class bcolors:
   OKGREEN = '\033[92m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'

def run_stress_tests(name, two_sum):
   class TimeoutException(Exception): pass

   @contextmanager
   def time_limit(seconds):
      def signal_handler(signum, frame):
         raise TimeoutException("Timed out!")
      signal.signal(signal.SIGALRM, signal_handler)
      signal.alarm(seconds)
      try:
         yield
      finally:
         signal.alarm(0)

   test_cases = [50000, 500000, 5000000]

   print()
   print("Stress Test Cases for two_sum solution: {}".format(name))

   total_passed = 0
   
   for index, test_case in enumerate(test_cases):
      try:
         with time_limit(5):
            passed = stress_test(index + 1, test_case, two_sum)
            if passed:
               total_passed += 1
      except TimeoutException as e:
         print(bcolors.FAIL + "  FAILED" + bcolors.ENDC + " - Test case {} timed out with an input of {}!".format(index + 1, test_case))

   return len(test_cases) == total_passed   

def stress_test(number, input_size, two_sum):
    numbers = list(range(1, input_size))

    target = numbers[-2] + numbers[-1]

    random.shuffle(numbers)

    start = time.time()
    solution = two_sum(numbers, target)
    elapsed = time.time() - start

    number_1 = numbers[solution[0]]
    number_2 = numbers[solution[1]]

    print("  Case {} - Testing an input of {} numbers".format(number, input_size))
    if number_1 + number_2 == target:
       print(bcolors.OKGREEN + "     PASSED" + bcolors.ENDC + " - Solution found in {} seconds. \n              Found first number: {} at index position: {} and second number: {} at index position: {}. \n              {} + {} = {}".format(elapsed, number_1, solution[0], number_2, solution[1], number_1, number_2, target))
    else:
       print(bcolors.FAIL + "     FAILED" + bcolors.ENDC + " - Solution found in {} seconds. \n              Found first number: {} at index position: {} and second number: {} at index position: {}. \n              {} + {} != {}".format(elapsed, number_1, solution[0], number_2, solution[1], number_1, number_2, target))

    return number_1 + number_2 == target

def run_basic_tests(name, two_sum):

   def basic_test(two_sum, input, target, expected):
    result = two_sum(input, target)
    if result == expected:
       print(bcolors.OKGREEN + "  PASSED" + bcolors.ENDC + " - Basic test case. Verified two_sum({}, {}) returned expected: {}".format(input, target, expected))
    else:
       print(bcolors.FAIL + "  FAILED" + bcolors.ENDC + " - Basic test case. Expected two_sum({}, {}) to return {} but got: {}".format(input, target, expected, result))
       
    return result == expected

   test_cases = [
      # input, target, expected
      ([2, 7, 11, 15], 9, [0, 1]),
      ([3, 1, -2, 5], 3, [2, 3]),
      ([1, 5, 3, 2], 8, [1, 2]),
      ([0, 2, 6, -1], -1, [0, 3]),
      ([-3, 4, 3, 90], 0, [0, 2]),
      ([8, -5, 12, -7], 7, [1, 2]),
      ([2, 8, 3, 7, 10], 9, [0, 3]),
      ([10, -3, 4, 1, -1], 9, [0, 4]),
      ([-4, -10, 2, -6, 9], -14, [0, 1]),
      ([3, 2, 1, 5, 9], 18, None)
   ]

   print()
   print("BASIC Test Cases for two_sum solution: {}".format(name))

   total_passed = 0
   total_failed = 0
   total = len(test_cases)

   for input, target, expected in test_cases:
      result = basic_test(two_sum, input, target, expected)

      if result:
         total_passed += 1
      else:
         total_failed += 1

   print("Completed {} basic test cases. PASSED: {}, FAILED: {}".format(total, total_passed, total_failed))
   print()

   return len(test_cases) == total_passed

if __name__=='__main__':

   solutions = {
      "two_sum_long": two_sum_long,
      "two_sum_short": two_sum_short,
      "two_sum_bad": two_sum_bad,
      "two_sum_better_but_still_bad": two_sum_better_but_still_bad,
   }

   for name, solution in solutions.items():
      print()
      print("------------------------------------------------ Testing {} ------------------------------------------------".format(name))
      basic_passed = run_basic_tests(name, solution)
      stress_passed = run_stress_tests(name, solution)
      print()

      if basic_passed and stress_passed:
         print("All test cases passed for: {}!".format(name))
      else:
         print("Test failures for {}!".format(name))