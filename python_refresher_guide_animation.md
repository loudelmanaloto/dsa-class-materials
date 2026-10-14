# Python Refresher for Animation Students: Code Along Guide

**For:** BS Entertainment and Multimedia Computing (Digital Animation Technology) students restarting Python before Data Structures and Algorithms

**Why you're learning this:** Every animation tool you will ever use (Blender, Maya, After Effects, Unity, game engines) is built from the same few ideas: lists of frames, colors stored as numbers, loops that run once per frame, and functions that blend one pose into the next. Studios write Python scripts to automate boring work like renaming 500 files or fixing 200 layers. This guide re-teaches the basics using those things.

**How to use this guide:** Don't just read it. Open a file (or the Python shell), **type every example yourself** (no copy-paste), run it, then change a number and run it again. Breaking code on purpose is how you learn what it does.

Each section has:
- **Concept**: the idea in plain words
- **Code Along**: type and run this
- **Your Turn**: try it yourself before moving on

When you finish, test yourself with the auto-checked **Animation Practice Set** (see the end).

---

## Part 0: Setting Up Your Computer

You need two things: **Python** (the language, which runs your code) and **Visual Studio Code** (the editor, where you write it). Install them in this order. This takes about 15 minutes.

### Step 1: Check if Python is already installed

Open a terminal:
- **Windows:** press the Windows key, type `cmd`, press Enter
- **Mac:** open Spotlight (Cmd + Space), type `Terminal`, press Enter

Type:
```
python --version
```
- If you see `Python 3.10` or higher (for example `Python 3.12.4`), skip to **Step 3**.
- If you see an older version (like `Python 2.7`), or an error, or the **Microsoft Store opens**, continue to Step 2.

> On Mac, try `python3 --version` instead. Mac uses `python3` as the command name in place of `python`.

### Step 2: Install Python

1. Go to **https://www.python.org/downloads/**
2. Click the big yellow **Download Python 3.x.x** button. (Always download from python.org, not from other sites.)
3. Run the installer you downloaded.
4. **Windows only: before clicking anything else, tick the box at the bottom that says _"Add python.exe to PATH"_.** This is the most commonly missed step, and without it your terminal won't find Python.
5. Click **Install Now** and wait for it to finish. Click **Close**.
6. **Close your terminal and open a new one**, then check again:
   ```
   python --version
   ```
   You should now see the version number.

**Still not working?**

| Problem | Fix |
|---|---|
| `'python' is not recognized...` | You skipped the PATH box. Re-run the installer, choose **Modify**, then **Next**, and tick *"Add Python to environment variables"*. Or uninstall and reinstall with the box ticked. |
| Typing `python` opens the Microsoft Store | Windows has a placeholder. Open **Settings → Apps → Advanced app settings → App execution aliases** and turn **off** the two entries named *python.exe* and *python3.exe*. Then try again. |
| `python` still doesn't work, but you installed it | Try `py --version` instead. On Windows, `py` is a launcher that also runs Python. If it works, use `py` wherever this guide says `python`. |
| It still says an old version | You may have two Pythons installed. Ask your instructor. |

### Step 3: Install Visual Studio Code

1. Go to **https://code.visualstudio.com/**
2. Click **Download** and run the installer.
3. On Windows, during install, tick these options if you see them:
   - *Add "Open with Code" action to Windows Explorer file context menu*
   - *Add to PATH*
4. Open VS Code when it finishes.

### Step 4: Add the Python extension to VS Code

VS Code doesn't know Python by itself. The extension teaches it.

1. Click the **Extensions** icon on the left sidebar (it looks like four squares), or press `Ctrl + Shift + X`.
2. In the search box, type **Python**.
3. Install the one by **Microsoft** (it has millions of downloads and a blue checkmark). It also installs *Pylance* automatically, which gives you code suggestions and highlights mistakes as you type.

### Step 5: Make a folder for your work

Never write code loose on your Desktop. Keep it all in one folder.

1. Create a folder somewhere you'll find it again, for example `Documents\DSA`.
2. In VS Code, click **File → Open Folder...** and choose that folder.
3. If VS Code asks *"Do you trust the authors of the files in this folder?"*, click **Yes, I trust the authors** (it's your own folder).

### Step 6: Create and run your first file

1. In the **Explorer** panel on the left, hover over your folder name and click the **New File** icon. Name it `hello.py`. (The `.py` ending is what makes it a Python file.)
2. Type this exactly:
   ```python
   print("Action!")
   ```
3. Press `Ctrl + S` to save. **Always save before running.**
4. Click the **Run** button (a small ▶ triangle at the top right of the editor).
5. A terminal opens at the bottom, and you should see:
   ```
   Action!
   ```

If you see that, your setup is finished.

### Step 7: Select the right Python (only if something looks wrong)

If VS Code shows a warning that no Python was found, or you have more than one Python installed:

1. Press `Ctrl + Shift + P` to open the Command Palette.
2. Type **Python: Select Interpreter** and press Enter.
3. Choose the one that matches the version you installed (for example *Python 3.12.x*).

You can see the selected version at the bottom-right corner of the VS Code window.

### Running your code from the terminal

The ▶ button is convenient, but you'll also need the terminal, because your auto-checkers run from there.

1. In VS Code, open a terminal with **Terminal → New Terminal** (or press ``Ctrl + ` ``, the key above Tab).
2. Run a file by typing its name:
   ```
   python hello.py
   ```
3. To run the practice checker later, use:
   ```
   python test_practice_anim.py
   ```
   Make sure the terminal is **inside the same folder** as that file. You can check with `dir` on Windows (or `ls` on Mac) and look for your file in the list. To move into a folder, type `cd foldername`.

### Handy VS Code habits

| Shortcut | What it does |
|---|---|
| `Ctrl + S` | Save the file (do this constantly) |
| `Ctrl + /` | Comment or uncomment the selected lines |
| `Ctrl + Z` | Undo |
| `Tab` | Indent the line (Python needs correct indentation) |
| ``Ctrl + ` `` | Show or hide the terminal |
| `Ctrl + Shift + P` | Command Palette (search any command) |

> **Mac users:** use `Cmd` in place of `Ctrl` in all of these.

### Code Along (first real code)
Replace the contents of `hello.py` with:
```python
print("Action!")
```
and run it again. Now change `"Action!"` to `"Cut!"` and run it again. You've just written and edited your first program.

**Explanation:** `print()` shows output on the screen. The text inside quotes is a *string*. Whenever you're unsure what your code is doing, `print()` it. It's the same as scrubbing through a timeline to check what's on a frame.

### Setup checklist

- [ ] `python --version` shows 3.10 or higher
- [ ] VS Code opens, and the Microsoft Python extension is installed
- [ ] I opened my work **folder** in VS Code (not just a single file)
- [ ] `hello.py` runs and prints `Action!`
- [ ] I can open a terminal inside VS Code and run `python hello.py`

If all five are checked, you're ready for Part 1.

**Explanation:** `print()` shows output on the screen. The text inside quotes is a *string*. Whenever you're unsure what your code is doing, `print()` it. It's the same as scrubbing through a timeline to check what's on a frame.

---

## Part 1: Variables and Data Types

### Concept
A **variable** is a name that points to a value, like a label on a layer. Python figures out the type on its own.

| Type | Animation example | Meaning |
|---|---|---|
| `int` | `24` (frames per second) | whole number |
| `float` | `0.5` (opacity) | decimal number |
| `str` | `"hero_walk"` | text |
| `bool` | `True` / `False` | yes or no |

### Code Along
```python
character = "Mimi"
fps = 24
opacity = 0.75
is_visible = True

print(character, fps, opacity, is_visible)
print(type(fps))        # <class 'int'>
print(type(opacity))    # <class 'float'>
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

### Real use: frames to seconds
An animation has 100 frames at 24 fps. How long is it?
```python
total_frames = 100
fps = 24

seconds = total_frames // fps      # 4 whole seconds
leftover = total_frames % fps      # 4 extra frames
print(f"{seconds} seconds and {leftover} frames")   # 4 seconds and 4 frames
```

**Why this matters for DSA:** `//` and `%` show up constantly. Splitting time into minutes and seconds, finding the middle of a list (`len(x) // 2`), wrapping around an animation loop. Learn them well.

### Your Turn
A clip is 1,000 frames long at 30 fps. Print its length as `X seconds and Y frames`.

---

## Part 2: Input and Output

### Code Along
```python
name = input("Character name? ")
frames = int(input("How many frames long is the walk cycle? "))

print(f"{name}'s walk cycle is {frames} frames.")
print(f"At 24 fps that's {frames / 24} seconds.")
```

**Explanation:**
- `input()` always returns a **string**, even if the user types a number.
- `int(...)` converts it so you can do math.
- `f"...{variable}..."` is an **f-string**. It inserts values into text. You can even put math inside the braces.

Formatting trick you'll use for timecodes:
```python
print(f"{5:02d}")      # 05   (pad to 2 digits with a zero)
print(f"{0.12345:.2f}")  # 0.12 (2 decimal places)
```

### Your Turn
Ask for a width and a height, then print the aspect ratio (width / height) with 2 decimal places. Try `1920` and `1080`.

---

## Part 3: Conditionals (Making Decisions)

### Concept
The program picks a path depending on whether a condition is `True` or `False`. Games and animation tools do this every frame: *Is the character on the ground? Is health at zero? Is this a keyframe?*

### Code Along
```python
health = int(input("Enter health (0-100): "))

if health > 60:
    print("Green bar")
elif health > 25:
    print("Yellow bar")
elif health > 0:
    print("Red bar, flashing!")
else:
    print("Game over")
```

**Explanation:**
- Indentation (4 spaces) is **part of the syntax** in Python. It defines what belongs inside the `if`.
- Python checks top to bottom and runs **only the first** branch that is true.

Comparison operators: `==` `!=` `<` `>` `<=` `>=`
Logical operators: `and`, `or`, `not`

```python
frame = 48

if frame % 12 == 0 and frame > 0:
    print("This is a keyframe")
```

> **Common mistake:** `=` assigns a value, `==` compares. `if frame = 48` is an error.

### Your Turn
Ask the user for an opacity from 0 to 1. Print `"Invisible"` if it's 0, `"Fully visible"` if it's 1, `"Semi-transparent"` if it's in between.

---

## Part 4: Loops (Repeating Things)

### Concept
Loops let you repeat code. An animation *is* a loop: the same drawing code runs once per frame, 24 times per second. Loops are the backbone of almost every algorithm.

### `for` loop: when you know how many times
```python
for frame in range(5):
    print("Rendering frame", frame)
```
Output: frames `0 1 2 3 4`. Notice it starts at 0 and **stops before 5**.

`range` variations:
```python
range(5)          # 0, 1, 2, 3, 4
range(2, 6)       # 2, 3, 4, 5
range(0, 10, 2)   # 0, 2, 4, 6, 8   (step of 2, "animate on twos")
range(5, 0, -1)   # 5, 4, 3, 2, 1   (counting down)
```

### `while` loop: repeat until something changes
```python
y = 100          # ball height
while y > 0:
    print("Ball at height", y)
    y -= 20      # without this, the loop never ends!
```

### Accumulator pattern (you'll use this forever)
```python
total_frames = 0
for shot_length in [48, 72, 24, 120]:
    total_frames += shot_length
print(total_frames)   # 264
```

### `break` and `continue`
```python
for frame in range(10):
    if frame == 3:
        continue    # skip frame 3
    if frame == 6:
        break       # stop rendering entirely
    print(frame)    # prints 0 1 2 4 5
```

### Your Turn
1. Print every 4th frame from 0 to 100 (`0, 4, 8, ...`).
2. Print a staircase of frames, one more per line:
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
A function is a named, reusable block of code, like a preset or a reusable rig. It takes **parameters** (inputs) and can **return** a value (output).

### Code Along
```python
def seconds_to_frames(seconds, fps):
    return seconds * fps

print(seconds_to_frames(3, 24))   # 72
```

The most important function in animation, **linear interpolation** (lerp), used for every tween:
```python
def lerp(start, end, t):
    return start + (end - start) * t

print(lerp(0, 100, 0))      # 0.0    start
print(lerp(0, 100, 1))      # 100    end
print(lerp(0, 100, 0.5))    # 50.0   halfway
print(lerp(10, 20, 0.25))   # 12.5
```

`t` goes from 0 to 1. Slide a character from x=0 to x=100 over 5 frames:
```python
for frame in range(5):
    t = frame / 4
    print(frame, lerp(0, 100, t))   # 0, 25, 50, 75, 100
```

**`print` vs `return`:** `print` shows something on screen. `return` hands a value back so you can use it somewhere else. Beginners mix these up constantly. A function that only prints can't be used inside other calculations, so `lerp` must *return*.

Default parameters:
```python
def make_label(name, fps=24):
    return f"{name} @ {fps}fps"

print(make_label("walk"))       # walk @ 24fps
print(make_label("walk", 30))   # walk @ 30fps
```

### Your Turn
Write `fade(opacity, amount)` that lowers the opacity by `amount` but never goes below 0. Test it with `fade(0.5, 0.2)` and `fade(0.1, 0.3)`. Do **not** use `max()`.

---

## Part 6: Strings

### Concept
A string is a sequence of characters. You can index into it, slice it, and loop over it. Animators deal with strings all day: file names, layer names, and frame sequences.

### Code Along
```python
filename = "walk_cycle_042.png"

print(len(filename))        # 18
print(filename[0])          # 'w'  first character
print(filename[-1])         # 'g'  last character
print(filename[0:4])        # 'walk'  slice: start included, end excluded
print(filename[-3:])        # 'png'   the last 3 characters
print(filename.upper())     # 'WALK_CYCLE_042.PNG'
print(filename.endswith(".png"))    # True
```

Splitting a name into parts:
```python
parts = filename.split("_")       # ['walk', 'cycle', '042.png']
print(parts)
number = parts[2].replace(".png", "")
print(number)                     # '042'
print(int(number) + 1)            # 43
```

Batch renaming (the kind of job scripts are made for):
```python
for i in range(1, 6):
    print(f"walk_cycle_{i:03d}.png")
# walk_cycle_001.png ... walk_cycle_005.png
```

Looping over a string:
```python
count = 0
for ch in "walk_cycle_042":
    if ch.isdigit():
        count += 1
print(count)   # 3
```

> **Important:** strings are **immutable**. You cannot change a character in place (`filename[0] = "W"` is an error). You create a new string instead. This idea comes back in DSA.

### Your Turn
Given `"Hero_Run_v3.mov"`, print the three parts (`Hero`, `Run`, `v3`) and the file extension (`mov`) on separate lines. *Hint: split twice.*

---

## Part 7: Lists

### Concept
A list is an **ordered, changeable** collection, like a timeline. It's Python's version of an array, and the most important structure to master before DSA. A clip is literally a list of frames.

### Code Along
```python
clip = ["pose_A", "pose_B", "pose_C", "pose_D"]

print(clip[0])       # pose_A
print(clip[-1])      # pose_D
print(len(clip))     # 4

clip.append("pose_E")        # add to the end
clip.insert(1, "pose_X")     # insert at index 1
clip.remove("pose_C")        # remove a value
last = clip.pop()            # remove and return the last item
print(clip, last)
```

Looping:
```python
for frame in clip:
    print(frame)

for i in range(len(clip)):
    print(i, clip[i])

for i, frame in enumerate(clip):   # index AND value together
    print(i, frame)
```

Slicing (same rules as strings):
```python
shots = [24, 48, 12, 96, 36, 60]
print(shots[1:4])    # [48, 12, 96]
print(shots[:3])     # [24, 48, 12]
print(shots[3:])     # [96, 36, 60]
```

### Finding the longest shot manually (a real algorithm!)
```python
def find_longest(lengths):
    longest = lengths[0]
    for x in lengths:
        if x > longest:
            longest = x
    return longest

print(find_longest([24, 48, 12, 96, 36, 60]))   # 96
```

**Explanation:** Assume the first item is the biggest. Walk through every item; whenever you find a bigger one, update. That's a complete algorithm in 5 lines. It looks at each item once, so with *n* items it takes about *n* steps. Remember this idea; we'll call it **O(n)** later.

### Playing a clip backwards
```python
def reversed_clip(frames):
    result = []
    for i in range(len(frames) - 1, -1, -1):
        result.append(frames[i])
    return result

print(reversed_clip(["f1", "f2", "f3"]))   # ['f3', 'f2', 'f1']
```

### List comprehension (shortcut, optional for now)
```python
opacities = [frame / 10 for frame in range(11)]    # fade in: 0.0, 0.1, ... 1.0
even_frames = [f for f in range(20) if f % 2 == 0]
```

### Your Turn
1. Write `find_shortest(lengths)` without using `min()`.
2. Write `average_length(lengths)` that returns the average shot length.
3. Write `count_long_shots(lengths, limit)` that counts how many shots are longer than `limit`.

---

## Part 8: Tuples, Sets, and Dictionaries

### Tuple: ordered, **unchangeable**
Perfect for colors and positions, things that belong together and shouldn't change by accident.
```python
red = (255, 0, 0)          # (R, G, B)
position = (320, 180)      # (x, y)

r, g, b = red              # unpacking
print(r, g, b)

x, y = position
print(f"Sprite is at x={x}, y={y}")
```

Brightness of a color:
```python
def brightness(color):
    return color[0] + color[1] + color[2]

print(brightness((255, 0, 0)))       # 255
print(brightness((100, 100, 100)))   # 300  (the gray is brighter!)
```

### Set: **unique** items, no order
```python
palette = ["red", "blue", "red", "green", "blue"]
unique = set(palette)
print(unique)               # {'red', 'blue', 'green'}  (order may vary)
print("red" in unique)      # True (very fast lookup)
```

### Dictionary: key → value pairs
Perfect for properties, like a layer's settings.
```python
sprite = {"name": "Mimi", "x": 120, "y": 80, "opacity": 1.0}

print(sprite["name"])              # Mimi
sprite["x"] = 150                  # update
sprite["rotation"] = 45            # add a new key
print(sprite.get("scale", 1.0))    # safe lookup with a default

for key, value in sprite.items():
    print(key, "->", value)
```

### Counting with a dictionary (extremely common pattern)
```python
tags = ["walk", "run", "walk", "jump", "walk"]

counts = {}
for tag in tags:
    if tag in counts:
        counts[tag] += 1
    else:
        counts[tag] = 1
print(counts)   # {'walk': 3, 'run': 1, 'jump': 1}
```

**Why this matters for DSA:** Dictionaries and sets let you look things up almost instantly, which is how you make slow algorithms fast. Game engines use them to find assets by name. We'll revisit them under hash tables.

### Your Turn
Given a list of layer names, build a dictionary that counts how many times each layer name appears.

---

## Part 9: Recursion (A Function Calling Itself)

### Concept
Recursion solves a problem by solving a smaller version of the same problem. Think of a **folder inside a folder inside a folder**: opening each one is the same action repeated. Every recursive function needs:
1. **Base case**: when to stop
2. **Recursive case**: call itself with a smaller problem

### Code Along: the bouncing ball
Each bounce reaches 60% of the previous height.
```python
def bounce_height(height, bounces):
    if bounces == 0:                                 # base case
        return height
    return bounce_height(height * 0.6, bounces - 1)  # recursive case

print(bounce_height(100, 0))   # 100
print(bounce_height(100, 1))   # 60.0
print(bounce_height(100, 3))   # 21.6
```

**Trace it by hand** (do this on paper!):
```
bounce_height(100, 2)
= bounce_height(60.0, 1)
= bounce_height(36.0, 0)
= 36.0
```

### Code Along: folders inside folders
A timeline has layers (strings) and folders (lists), and folders can hold more folders:
```python
def count_layers(folder):
    total = 0
    for item in folder:
        if isinstance(item, list):       # it's a folder: look inside it
            total += count_layers(item)
        else:                            # it's a layer: count it
            total += 1
    return total

scene = ["background", ["hero", "shadow", ["hat"]], "effects"]
print(count_layers(scene))   # 5
```

Without recursion you couldn't know how deep the folders go. Recursion handles any depth.

> If you forget the base case, Python raises `RecursionError`. Try it and see.

### Your Turn
1. Write a recursive `sum_to(n)` that returns `1 + 2 + ... + n`.
2. Write a recursive `countdown(n)` that prints `n, n-1, ..., 1, "Action!"`.

---

## Part 10: Bridge to Data Structures and Algorithms

You now have the tools. Here's where they lead.

### Linear search
Finding a keyframe by checking every frame, one by one:
```python
def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

print(linear_search([0, 12, 24, 48, 96], 48))   # 3
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

print(binary_search([0, 12, 24, 48, 96], 48))   # 3
```

**Explanation:** Look at the middle. If the target is bigger, throw away the left half; if smaller, throw away the right half. It's like jumping to the middle of a timeline, checking whether you've gone too far, then jumping again. A timeline of 1,000,000 frames needs only about 20 jumps instead of up to 1,000,000.

### Big-O in one table (just the idea for now)

| Notation | Name | Example |
|---|---|---|
| O(1) | constant | `clip[0]` |
| O(log n) | logarithmic | binary search |
| O(n) | linear | linear search, `find_longest` |
| O(n²) | quadratic | loop inside a loop (comparing every frame to every other frame) |

The question we'll keep asking all semester: **"How does the work grow as the input grows?"** It's the same reason a render that takes 1 minute for 10 frames may take hours for a feature film if the algorithm is slow.

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
| `TypeError` | mixing types, like `"24" + 24` |
| `IndexError` | list index out of range (asking for frame 10 in a 5-frame clip) |
| `KeyError` | dictionary key doesn't exist |

---

## Animation Practice Set (Auto-Checked)

Once you've finished the sections above, open the `practice_animation` folder and fill in `practice_anim.py`. Check your work with:
```
python test_practice_anim.py
```

| # | Problem | Skill it trains |
|---|---|---|
| 1 | Frame number → `MM:SS:FF` timecode | `//`, `%`, f-strings |
| 2 | Tween between two colors | functions, tuples, math |
| 3 | Play a clip backwards | lists, loops |
| 4 | Find the brightest pixel | accumulator pattern, tuples |
| 5 | Clean up a color palette | sets, lists |
| 6 | Do two scenes have the same layers? | dictionaries, counting |
| 7 | Find a keyframe fast | binary search |
| 8 | Count animation tags | dictionaries |
| 9 | Bouncing ball | recursion |
| 10 | Challenge: count layers in folders | recursion on nested data |

---

## Self-Check Before Moving On

You're ready for the first DSA topic if you can do all of these without help:

- [ ] Write a function that takes a list and returns something computed from it
- [ ] Loop through a list using both `for item in list` and `for i in range(len(list))`
- [ ] Explain the difference between `print` and `return`
- [ ] Use a dictionary to count things
- [ ] Trace a small recursive function by hand
- [ ] Read an error message and find the line that caused it
