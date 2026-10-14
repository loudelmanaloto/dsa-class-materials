# Python Refresher: Code Along Guide

**For:** Data Structures and Algorithms students restarting from the basics (Programming 1 and 2 review)

**How to use this guide:** Don't just read it. Open a file (or the Python shell), **type every example yourself** (no copy-paste), run it, then change something and run it again. Breaking code on purpose is how you learn what it does.

Each section has:
- **Concept**: the idea in plain words
- **Code Along**: type and run this
- **Your Turn**: try it yourself before checking the hint

---

## Part 0: Setup

1. Check Python is installed. In a terminal:
   ```
   python --version
   ```
   You want Python 3.10 or newer.
2. Create a file called `practice.py`.
3. Run it with:
   ```
   python practice.py
   ```

### Code Along
```python
print("Hello, DSA!")
```

**Explanation:** `print()` shows output on the screen. The text inside quotes is a *string*. Every time you're unsure what your code is doing, `print()` it.

---

## Part 1: Variables and Data Types

### Concept
A **variable** is a name that points to a value. Python figures out the type on its own.

| Type | Example | Meaning |
|---|---|---|
| `int` | `42` | whole number |
| `float` | `3.14` | decimal number |
| `str` | `"hello"` | text |
| `bool` | `True` / `False` | yes or no |

### Code Along
```python
name = "Ana"
age = 19
gpa = 1.75
is_enrolled = True

print(name, age, gpa, is_enrolled)
print(type(age))        # <class 'int'>
print(type(gpa))        # <class 'float'>
```

Now math:
```python
a = 17
b = 5

print(a + b)    # 22  addition
print(a - b)    # 12  subtraction
print(a * b)    # 85  multiplication
print(a / b)    # 3.4 division (always a float)
print(a // b)   # 3   floor division (drops the decimal)
print(a % b)    # 2   modulo (the remainder)
print(a ** b)   # 1419857  exponent
```

**Why this matters for DSA:** `//` and `%` show up constantly. Checking even/odd (`n % 2 == 0`), finding the middle of a list (`len(x) // 2`), wrapping around an array. Learn them well.

### Your Turn
Write a program that stores a total of `275` minutes in a variable and prints it as hours and minutes (`4 hours 35 minutes`). *Hint: use `//` and `%`.*

---

## Part 2: Input and Output

### Code Along
```python
name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"Hi {name}! Next year you will be {age + 1}.")
```

**Explanation:**
- `input()` always returns a **string**, even if the user types a number.
- `int(...)` converts it so you can do math.
- `f"...{variable}..."` is an **f-string**. It inserts values into text.

### Your Turn
Ask for two numbers and print their sum, difference, and product.

---

## Part 3: Conditionals (Making Decisions)

### Concept
The program picks a path depending on whether a condition is `True` or `False`.

### Code Along
```python
score = int(input("Enter your score: "))

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Passed")
else:
    print("Failed")
```

**Explanation:**
- Indentation (4 spaces) is **part of the syntax** in Python. It defines what belongs inside the `if`.
- Python checks top to bottom and runs **only the first** branch that is true.

Comparison operators: `==` `!=` `<` `>` `<=` `>=`
Logical operators: `and`, `or`, `not`

```python
n = 12
if n % 2 == 0 and n > 10:
    print("Even and bigger than 10")
```

> **Common mistake:** `=` assigns a value, `==` compares. `if x = 5` is an error.

### Your Turn
Write a program that takes a number and prints whether it is positive, negative, or zero.

---

## Part 4: Loops (Repeating Things)

### Concept
Loops let you repeat code. This is the backbone of almost every algorithm.

### `for` loop: when you know how many times
```python
for i in range(5):
    print(i)
```
Output: `0 1 2 3 4`. Notice it starts at 0 and **stops before 5**.

`range` variations:
```python
range(5)          # 0, 1, 2, 3, 4
range(2, 6)       # 2, 3, 4, 5
range(0, 10, 2)   # 0, 2, 4, 6, 8   (step of 2)
range(5, 0, -1)   # 5, 4, 3, 2, 1   (counting down)
```

### `while` loop: when you repeat until something changes
```python
count = 1
while count <= 5:
    print(count)
    count += 1      # without this, the loop never ends!
```

### Accumulator pattern (you'll use this forever)
```python
total = 0
for i in range(1, 101):
    total += i
print(total)   # 5050
```

### `break` and `continue`
```python
for i in range(10):
    if i == 3:
        continue    # skip 3
    if i == 6:
        break       # stop the loop entirely
    print(i)        # prints 0 1 2 4 5
```

### Your Turn
1. Print the multiplication table of a number the user enters (1 to 10).
2. Print a right triangle of stars:
   ```
   *
   **
   ***
   ****
   ```
   *Hint: `print("*" * i)`.*

---

## Part 5: Functions

### Concept
A function is a named, reusable block of code. It takes **parameters** (inputs) and can **return** a value (output).

### Code Along
```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)   # 7
```

```python
def is_even(n):
    return n % 2 == 0

print(is_even(10))  # True
print(is_even(7))   # False
```

**`print` vs `return`:** `print` shows something on screen. `return` hands a value back to the caller so you can use it. Beginners mix these up constantly. A function that only prints can't be used inside other calculations.

Default parameters:
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ben"))             # Hello, Ben!
print(greet("Ben", "Good day")) # Good day, Ben!
```

### Your Turn
Write `maximum(a, b, c)` that returns the largest of three numbers **without** using Python's built-in `max()`.

---

## Part 6: Strings

### Concept
A string is a sequence of characters. You can index into it, slice it, and loop over it.

### Code Along
```python
word = "algorithm"

print(len(word))      # 9
print(word[0])        # 'a'   first character
print(word[-1])       # 'm'   last character
print(word[0:4])      # 'algo' slice: start included, end excluded
print(word[::-1])     # 'mhtirogla' reversed
print(word.upper())   # 'ALGORITHM'
```

Looping over a string:
```python
vowels = 0
for ch in "programming":
    if ch in "aeiou":
        vowels += 1
print(vowels)   # 3
```

Useful methods: `.lower()`, `.upper()`, `.strip()`, `.split()`, `.replace(a, b)`, `.startswith()`, `.find()`.

```python
sentence = "the quick brown fox"
words = sentence.split()      # ['the', 'quick', 'brown', 'fox']
print(len(words))             # 4
print(" ".join(words))        # joins them back with spaces
```

> **Important:** strings are **immutable**. You cannot change a character in place (`word[0] = "A"` is an error). You create a new string instead. This idea comes back in DSA.

### Your Turn
Write `is_palindrome(text)` that returns `True` if the text reads the same forwards and backwards (e.g. `"madam"`).

---

## Part 7: Lists

### Concept
A list is an **ordered, changeable** collection. This is Python's version of an array, and it's the most important structure to master before DSA.

### Code Along
```python
nums = [10, 20, 30, 40]

print(nums[0])       # 10
print(nums[-1])      # 40
print(len(nums))     # 4

nums.append(50)      # add to end      -> [10, 20, 30, 40, 50]
nums.insert(1, 15)   # insert at index -> [10, 15, 20, 30, 40, 50]
nums.remove(30)      # remove a value  -> [10, 15, 20, 40, 50]
last = nums.pop()    # remove & return last item
print(nums, last)
```

Looping:
```python
for n in nums:
    print(n)

for i in range(len(nums)):
    print(i, nums[i])

for i, n in enumerate(nums):   # index AND value together
    print(i, n)
```

Slicing (same rules as strings):
```python
data = [5, 3, 8, 1, 9, 2]
print(data[1:4])    # [3, 8, 1]
print(data[:3])     # [5, 3, 8]
print(data[3:])     # [1, 9, 2]
```

### Finding the largest number manually (a real algorithm!)
```python
def find_max(items):
    biggest = items[0]
    for x in items:
        if x > biggest:
            biggest = x
    return biggest

print(find_max([5, 3, 8, 1, 9, 2]))   # 9
```

**Explanation:** Assume the first item is the biggest. Walk through every item; whenever you find a bigger one, update. That's a complete algorithm in 5 lines. It looks at each item once, so with *n* items it takes about *n* steps. Remember this idea; we'll call it **O(n)** later.

### List comprehension (shortcut, optional for now)
```python
squares = [x * x for x in range(1, 6)]    # [1, 4, 9, 16, 25]
evens   = [x for x in range(10) if x % 2 == 0]
```

### Your Turn
1. Write `find_min(items)` without using `min()`.
2. Write `average(items)` that returns the average of a list of numbers.
3. Write `count_occurrences(items, target)` that counts how many times `target` appears.

---

## Part 8: Tuples, Sets, and Dictionaries

### Tuple: ordered, **unchangeable**
```python
point = (3, 4)
x, y = point        # unpacking
print(x, y)
```

### Set: **unique** items, no order
```python
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)
print(unique)           # {1, 2, 3}
print(2 in unique)      # True (very fast lookup)
```

### Dictionary: key → value pairs
```python
student = {"name": "Ana", "age": 19, "course": "BSCS"}

print(student["name"])           # Ana
student["age"] = 20              # update
student["year"] = 2              # add new key
print(student.get("gpa", "N/A")) # safe lookup with default

for key, value in student.items():
    print(key, "->", value)
```

### Counting with a dictionary (extremely common pattern)
```python
text = "banana"
counts = {}
for ch in text:
    if ch in counts:
        counts[ch] += 1
    else:
        counts[ch] = 1
print(counts)   # {'b': 1, 'a': 3, 'n': 2}
```

**Why this matters for DSA:** Dictionaries and sets let you look things up almost instantly, which is how you make slow algorithms fast. We'll revisit them under hash tables.

### Your Turn
Given a list of words, build a dictionary that counts how many times each word appears.

---

## Part 9: Recursion (A Function Calling Itself)

### Concept
Recursion solves a problem by solving a smaller version of the same problem. Every recursive function needs:
1. **Base case**: when to stop
2. **Recursive case**: call itself with a smaller problem

### Code Along
```python
def factorial(n):
    if n == 0:           # base case
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(5))   # 120
```

**Trace it by hand** (do this on paper!):
```
factorial(3)
= 3 * factorial(2)
= 3 * (2 * factorial(1))
= 3 * (2 * (1 * factorial(0)))
= 3 * (2 * (1 * 1))
= 6
```

> If you forget the base case, Python raises `RecursionError`. Try it and see.

### Your Turn
1. Write a recursive `sum_to(n)` that returns `1 + 2 + ... + n`.
2. Write a recursive `fibonacci(n)` (0, 1, 1, 2, 3, 5, 8, ...).

---

## Part 10: Bridge to Data Structures and Algorithms

You now have the tools. Here's a preview of where they lead.

### Linear search
```python
def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

print(linear_search([4, 8, 15, 16, 23, 42], 16))   # 3
```

### Binary search (needs a **sorted** list; much faster)
```python
def binary_search(items, target):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([4, 8, 15, 16, 23, 42], 23))   # 4
```

**Explanation:** Look at the middle. If the target is bigger, throw away the left half; if smaller, throw away the right half. A list of 1,000,000 items needs only about 20 steps instead of up to 1,000,000.

### Big-O in one table (just the idea for now)

| Notation | Name | Example |
|---|---|---|
| O(1) | constant | `nums[0]` |
| O(log n) | logarithmic | binary search |
| O(n) | linear | linear search, `find_max` |
| O(n²) | quadratic | loop inside a loop |

The question we'll keep asking all semester: **"How does the work grow as the input grows?"**

---

## Debugging Habits

1. **Read the error message from the bottom up.** The last line says what went wrong; the line number says where.
2. **Print values** to see what the code is actually doing, not what you think it's doing.
3. **Test small.** Try an empty list, a one-item list, and a normal list.
4. **Change one thing at a time.**

Common errors:

| Error | Usually means |
|---|---|
| `SyntaxError` | typo: missing `:` or bracket |
| `IndentationError` | inconsistent spacing |
| `NameError` | variable used before it exists, or misspelled |
| `TypeError` | mixing types, like `"5" + 5` |
| `IndexError` | list index out of range |
| `KeyError` | dictionary key doesn't exist |

---

## Practice Set (Mixed Review)

Try these without looking back at the guide.

1. **FizzBuzz:** for 1 to 50, print `Fizz` if divisible by 3, `Buzz` if by 5, `FizzBuzz` if both, else the number.
2. **Reverse a list** without using `.reverse()` or `[::-1]`.
3. **Second largest:** find the second largest number in a list.
4. **Remove duplicates** from a list while keeping order.
5. **Anagram check:** are `"listen"` and `"silent"` made of the same letters?
6. **Two sum:** given a list and a target, return the indices of two numbers that add up to it.
7. **Count vowels** in a sentence using a dictionary.
8. **Recursion:** write `power(base, exp)` recursively.

---

## Self-Check Before Moving On

You're ready for the first DSA topic if you can do all of these without help:

- [ ] Write a function that takes a list and returns something computed from it
- [ ] Loop through a list using both `for item in list` and `for i in range(len(list))`
- [ ] Explain the difference between `print` and `return`
- [ ] Use a dictionary to count things
- [ ] Trace a small recursive function by hand
- [ ] Read an error message and find the line that caused it
