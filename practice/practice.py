"""
PRACTICE SET - fill in each function below.

How to check your work:
    python test_practice.py

Rules:
  * Edit ONLY this file (practice.py).
  * Functions should RETURN their answer, not print it.
  * Some problems ban certain shortcuts. The test will tell you.
  * Work on one problem at a time. Failing tests for problems you haven't
    started yet are normal.
"""


# 1. FizzBuzz
# Return a list of strings for the numbers 1 to n (inclusive):
#   "Fizz" if divisible by 3, "Buzz" if divisible by 5,
#   "FizzBuzz" if divisible by both, otherwise the number as a string.
# Example: fizzbuzz(5) -> ["1", "2", "Fizz", "4", "Buzz"]
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if int(i) % 3 == 0 and int(i) % 5 == 0:
            result.append("FizzBuzz")
        elif int(i) % 5 == 0:
            result.append("Buzz")
        elif int(i) % 3 == 0:
            result.append("Fizz")
        else:
            result.append(str(i))
    return result


# 2. Reverse a list
# Return a NEW list with the items in reverse order.
# Do not change the original list.
# Not allowed: .reverse(), reversed(), or slicing with a step like [::-1]
# Example: reverse_list([1, 2, 3]) -> [3, 2, 1]
def reverse_list(items):
    result = []
    for item in items:
        result.insert(0, item)
    return result


# 3. Second largest
# Return the second largest DISTINCT number in the list.
# If there is no second largest (fewer than 2 distinct values), return None.
# Not allowed: sorted(), .sort()
# Example: second_largest([5, 3, 8, 8, 1]) -> 5
def second_largest(items):
    pass


# 4. Remove duplicates
# Return a new list with duplicates removed, keeping the original order
# (the first time each item appears).
# Example: remove_duplicates([3, 1, 3, 2, 1]) -> [3, 1, 2]
def remove_duplicates(items):
    pass


# 5. Anagram check
# Return True if the two words use exactly the same letters
# (same counts), ignoring upper/lower case. Otherwise False.
# Example: is_anagram("Listen", "Silent") -> True
def is_anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())


# 6. Two sum
# Return a list [i, j] of two DIFFERENT indices (i < j) whose values add up
# to target. If no pair exists, return None.
# Example: two_sum([2, 7, 11, 15], 9) -> [0, 1]
def two_sum(nums, target):
    pass


# 7. Count vowels
# Return a dictionary of how many times each vowel (a, e, i, o, u) appears
# in the sentence, ignoring case. Only include vowels that actually appear.
# Example: count_vowels("Banana Bread") -> {"a": 4, "e": 1}
def count_vowels(sentence):
    pass


# 8. Power (recursion)
# Return base raised to exp, where exp is a whole number >= 0.
# You MUST solve it recursively (the function calls itself).
# Not allowed: the ** operator or pow()
# Example: power(2, 5) -> 32
def power(base, exp):
    pass
