# Java Refresher for Game Development Students: Code Along Guide

**For:** BS Entertainment and Multimedia Computing (Game Development) students restarting Java before Data Structures and Algorithms

**Why you're learning this:** Every game you've ever played is built from the same few ideas: variables for health and score, loops that run once per frame, arrays for tile maps, lists for inventories, and objects for players and enemies. Engines like **LibGDX, jMonkeyEngine and Minecraft modding** are written in Java, and the same ideas carry straight over to C# in Unity and C++ in Unreal. This guide re-teaches the basics using game examples.

**How to use this guide:** Don't just read it. Open a file, **type every example yourself** (no copy-paste), run it, then change a number and run it again. Breaking code on purpose is how you learn what it does.

Each section has:
- **Concept**: the idea in plain words
- **Code Along**: type and run this
- **Your Turn**: try it yourself before moving on

When you finish, test yourself with the auto-checked **Game Dev Practice Set** (see the end).

> **Reading the code blocks:** a block that contains `public class` is a complete file. A block with only a few lines goes **inside** the `main` method of your practice file, like this:
> ```java
> public class Practice {
>     public static void main(String[] args) {
>         // paste the lines here
>     }
> }
> ```

---

## Part 0: Setting Up Your Computer

You need two things: the **JDK** (Java Development Kit, which compiles and runs your code) and **Visual Studio Code** (the editor, where you write it). Install them in this order. This takes about 15 to 20 minutes.

> **JDK, not JRE.** You need the *Development Kit*. The plain "Java Runtime" can run programs but cannot compile them.

### Step 1: Check if Java is already installed

Open a terminal:
- **Windows:** press the Windows key, type `cmd`, press Enter
- **Mac:** open Spotlight (Cmd + Space), type `Terminal`, press Enter

Type **both** of these:
```
java -version
javac -version
```
- If both show version **17 or higher** (for example `javac 21.0.4`), skip to **Step 3**.
- If `java` works but `javac` says *"not recognized"* or *"command not found"*, you only have the runtime. Continue to Step 2.
- If either shows an older version or an error, continue to Step 2.

### Step 2: Install the JDK

1. Go to **https://adoptium.net/** (Eclipse Temurin, a free and trusted build of Java).
2. Click the download button for **JDK 21 (LTS)** for your operating system.
3. Run the installer.
4. **Windows only:** on the *Custom Setup* screen, click the small drive icon next to each of these and choose **"Will be installed on local hard drive"**:
   - **Add to PATH**
   - **Set JAVA_HOME variable**
   
   These two are the most commonly missed steps. Without them your terminal can't find Java.
5. Finish the install.
6. **Close your terminal and open a new one**, then check again:
   ```
   java -version
   javac -version
   ```
   Both should now show version 21.

**Still not working?**

| Problem | Fix |
|---|---|
| `'javac' is not recognized...` | PATH wasn't set. Re-run the installer, choose **Change**, and enable *Add to PATH*. Then open a **new** terminal. |
| `java` works but `javac` doesn't | You installed the JRE. Install the JDK from Step 2. |
| It still shows an old version | You may have two Javas installed. Ask your instructor. |
| It worked, then stopped after restart | Open a new terminal. Old terminals don't see PATH changes. |

### Step 3: Install Visual Studio Code

1. Go to **https://code.visualstudio.com/**
2. Click **Download** and run the installer.
3. On Windows, during install, tick these options if you see them:
   - *Add "Open with Code" action to Windows Explorer file context menu*
   - *Add to PATH*
4. Open VS Code when it finishes.

### Step 4: Add the Java extension to VS Code

VS Code doesn't know Java by itself. The extension teaches it.

1. Click the **Extensions** icon on the left sidebar (it looks like four squares), or press `Ctrl + Shift + X`.
2. In the search box, type **Extension Pack for Java**.
3. Install the one by **Microsoft**. It bundles everything you need: code suggestions, error highlighting, running, and debugging. It may take a minute to finish setting up. Wait for the spinning icon at the bottom of the window to stop.

### Step 5: Make a folder for your work

Never write code loose on your Desktop. Keep it all in one folder.

1. Create a folder somewhere you'll find it again, for example `Documents\DSA-Java`.
2. In VS Code, click **File → Open Folder...** and choose that folder.
3. If VS Code asks *"Do you trust the authors of the files in this folder?"*, click **Yes, I trust the authors** (it's your own folder).

### Step 6: Create and run your first program

Java is strict about one rule: **the file name must match the class name.** A class called `Hello` must live in a file called `Hello.java`, with the same capital letters.

1. In the **Explorer** panel on the left, hover over your folder name and click the **New File** icon. Name it `Hello.java`.
2. Type this exactly:
   ```java
   public class Hello {
       public static void main(String[] args) {
           System.out.println("Game start!");
       }
   }
   ```
3. Press `Ctrl + S` to save. **Always save before running.**
4. Above the line `public static void main`, you'll see a small **Run** link. Click it. (You can also click the ▶ button at the top right of the editor.)
5. A terminal opens at the bottom, and you should see:
   ```
   Game start!
   ```

If you see that, your setup is finished.

### Running your code from the terminal

The ▶ button is convenient, but you'll also need the terminal, because your auto-checker runs from there. Java is a **compiled** language, so there are two steps:

1. In VS Code, open a terminal with **Terminal → New Terminal** (or press ``Ctrl + ` ``, the key above Tab).
2. **Compile** (translate your code into something the computer can run):
   ```
   javac Hello.java
   ```
   If there's a mistake in your code, the errors show up here. If everything is fine, it prints nothing and creates `Hello.class`.
3. **Run** it. Note there is **no `.java` or `.class`** here, just the class name:
   ```
   java Hello
   ```

> **Every time you change your code, compile again.** Running `java Hello` without recompiling runs your *old* code. This is the most common beginner confusion in Java.

Make sure the terminal is **inside the same folder** as your file. Check with `dir` on Windows (or `ls` on Mac) and look for your file in the list. To move into a folder, type `cd foldername`.

### Handy VS Code habits

| Shortcut | What it does |
|---|---|
| `Ctrl + S` | Save the file (do this constantly) |
| `Ctrl + /` | Comment or uncomment the selected lines |
| `Ctrl + Z` | Undo |
| `Shift + Alt + F` | Auto-format your code (fixes indentation) |
| `Ctrl + Space` | Show suggestions |
| ``Ctrl + ` `` | Show or hide the terminal |
| `Ctrl + Shift + P` | Command Palette (search any command) |

> **Mac users:** use `Cmd` in place of `Ctrl`, and `Shift + Option + F` to format.

### Setup checklist

- [ ] `java -version` **and** `javac -version` both show 17 or higher
- [ ] VS Code opens, and the Extension Pack for Java is installed
- [ ] I opened my work **folder** in VS Code (not just a single file)
- [ ] `Hello.java` runs and prints `Game start!`
- [ ] I can open a terminal in VS Code and run `javac Hello.java` then `java Hello`

If all five are checked, you're ready for Part 1.

---

## Part 1: Anatomy of a Java Program

### Code Along
```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Game start!");   // prints and moves to the next line
        System.out.print("Loading");         // prints and stays on the same line
        System.out.println("...");
    }
}
```

**Explanation, line by line:**
- `public class Hello` — every Java program lives inside a **class**. The name matches the file.
- `public static void main(String[] args)` — the **entry point**. Java starts running here. You'll type this line a lot.
- `System.out.println(...)` — prints text to the screen. Whenever you're unsure what your code is doing, print it.
- `;` — every statement ends with a semicolon.
- `{ }` — curly braces mark where a block of code begins and ends. (Python used indentation. Java uses braces. Indentation is just for readability, so use it anyway.)
- `// comment` — a note for humans. Java ignores it.

> **Java is case-sensitive.** `System` works, `system` doesn't. `String` works, `string` doesn't.

### Your Turn
Print a title screen of three lines:
```
=== SPACE RUNNER ===
Press START
```
Then print your name on a third line.

---

## Part 2: Variables and Data Types

### Concept
A **variable** is a named box that holds a value. In Java, **you must declare the type** of the box, and it can't change. This is called *static typing*, and it catches many mistakes before the game even runs.

| Type | Game example | Meaning |
|---|---|---|
| `int` | `100` (health) | whole number |
| `double` | `0.75` (volume) | decimal number |
| `boolean` | `true` (isAlive) | yes or no |
| `char` | `'A'` (grade) | one single character, in single quotes |
| `String` | `"Mimi"` (name) | text, in double quotes. Note the capital **S** |

### Code Along
```java
String playerName = "Mimi";
int health = 100;
double speed = 4.5;
boolean isAlive = true;
char rank = 'S';

System.out.println(playerName + " has " + health + " HP");
System.out.println("Speed: " + speed + ", alive: " + isAlive + ", rank: " + rank);
```

Math:
```java
int a = 17;
int b = 5;

System.out.println(a + b);   // 22
System.out.println(a - b);   // 12
System.out.println(a * b);   // 85
System.out.println(a / b);   // 3    <-- integer division, drops the decimal!
System.out.println(a % b);   // 2    modulo (the remainder)
System.out.println(17.0 / 5);   // 3.4
```

> **Watch out:** when both numbers are `int`, `/` drops the decimal part. `7 / 2` is `3`, not `3.5`. If you want the decimal, one side must be a `double`: `7 / 2.0` gives `3.5`.

**Casting** (converting between types):
```java
double exact = 7.9;
int whole = (int) exact;        // 7  (chops the decimal, doesn't round)
int rounded = (int) Math.round(exact);   // 8

int hits = 3;
int shots = 4;
double accuracy = (double) hits / shots;   // 0.75
System.out.println(accuracy);
```

**Math helpers:**
```java
System.out.println(Math.max(10, 25));     // 25
System.out.println(Math.min(10, 25));     // 10
System.out.println(Math.abs(-7));         // 7
System.out.println(Math.sqrt(16));        // 4.0
System.out.println(Math.pow(2, 5));       // 32.0
```

**Constants** use `final` and are written in CAPITALS:
```java
final int MAX_HEALTH = 100;
// MAX_HEALTH = 200;   <-- error! A final value can't change.
```

### Real use: level and XP
```java
int xp = 1275;
int level = xp / 100 + 1;        // every 100 XP is a level
int xpIntoLevel = xp % 100;      // progress toward the next level
System.out.println("Level " + level + " (" + xpIntoLevel + "/100 XP)");
// Level 13 (75/100 XP)
```

**Why this matters for DSA:** `/` and `%` show up constantly: splitting time into minutes and seconds, finding the middle of an array (`length / 2`), wrapping around a tile map.

### Your Turn
A boss has 5,000 HP and your attack does 175 damage per hit. How many hits to kill it? Remember: a partial hit still takes a full swing, so round **up**. Print the result. *Hint: `Math.ceil` works on doubles.*

---

## Part 3: Input and Output

### Code Along
```java
import java.util.Scanner;

public class Greeting {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter hero name: ");
        String name = input.nextLine();

        System.out.print("Enter level: ");
        int level = input.nextInt();

        System.out.println("Welcome, " + name + " (Lv " + level + ")!");
        System.out.printf("Next level at %d XP%n", (level + 1) * 100);
        input.close();
    }
}
```

**Explanation:**
- `import java.util.Scanner;` goes at the very top. It brings in a tool that is not available by default.
- `new Scanner(System.in)` creates a reader for the keyboard.
- `nextLine()` reads a whole line of text. `nextInt()` reads a whole number. `nextDouble()` reads a decimal.
- `printf` prints with formatting: `%d` for whole numbers, `%.2f` for decimals with 2 places, `%s` for text, `%n` for a new line.

```java
System.out.printf("Accuracy: %.1f%%%n", 87.456);   // Accuracy: 87.5%
System.out.printf("%02d:%02d%n", 5, 7);            // 05:07
```

> **Common trap:** if you call `nextInt()` and then `nextLine()`, the `nextLine()` appears to get skipped. `nextInt()` leaves the Enter key behind. Fix it by adding an extra `input.nextLine();` after `nextInt()` to throw the leftover away.

### Your Turn
Ask for a player's current HP and max HP. Print their health percentage with 1 decimal place.

---

## Part 4: Conditionals (Making Decisions)

### Concept
The program picks a path depending on whether a condition is `true` or `false`. Games do this every frame: *Is the player on the ground? Is health at zero? Did the bullet hit?*

### Code Along
```java
int health = 40;

if (health > 60) {
    System.out.println("Green bar");
} else if (health > 25) {
    System.out.println("Yellow bar");
} else if (health > 0) {
    System.out.println("Red bar, flashing!");
} else {
    System.out.println("Game over");
}
```

**Explanation:**
- The condition goes in `( )` and must be a boolean.
- Java checks top to bottom and runs **only the first** branch that is true.

Comparison operators: `==` `!=` `<` `>` `<=` `>=`
Logical operators: `&&` (and), `||` (or), `!` (not)

```java
boolean hasKey = true;
int level = 5;

if (hasKey && level >= 5) {
    System.out.println("Door opens");
}
```

### `switch`: choosing between many exact values
```java
int choice = 2;

switch (choice) {
    case 1:
        System.out.println("New Game");
        break;
    case 2:
        System.out.println("Load Game");
        break;
    case 3:
        System.out.println("Quit");
        break;
    default:
        System.out.println("Invalid option");
}
```
**Don't forget `break`.** Without it, Java keeps running into the next case.

### The biggest Java trap: comparing Strings
```java
String command = "attack";

if (command.equals("attack")) {       // correct
    System.out.println("You swing your sword!");
}
// if (command == "attack")           // WRONG for Strings!
```
`==` on Strings checks whether they're the *same object in memory*, not whether the text matches. **Always use `.equals()`** for Strings. (`==` is fine for `int`, `double`, `boolean`, and `char`.)

Also useful: `command.equalsIgnoreCase("ATTACK")`.

> **Common mistake:** `=` assigns a value, `==` compares. `if (health = 0)` is an error.

### Your Turn
Write code that takes an `int damage` and prints `"Miss"` if it's 0, `"Hit"` if it's 1 to 49, `"Critical hit!"` if it's 50 to 99, and `"OVERKILL"` if it's 100 or more.

---

## Part 5: Loops (Repeating Things)

### Concept
Loops let you repeat code. A game *is* a loop: the same update code runs once per frame, 60 times per second. Loops are the backbone of almost every algorithm.

### `for` loop: when you know how many times
```java
for (int i = 0; i < 5; i++) {
    System.out.println("Spawning enemy " + i);
}
```
Output: enemies `0 1 2 3 4`. Notice it starts at 0 and **stops before 5**.

The three parts inside `( )`:
1. `int i = 0` — start here
2. `i < 5` — keep going while this is true
3. `i++` — after each round, add 1 to `i`

Variations:
```java
for (int i = 2; i < 6; i++)   { }   // 2, 3, 4, 5
for (int i = 0; i < 10; i += 2) { }   // 0, 2, 4, 6, 8
for (int i = 5; i > 0; i--)   { }   // 5, 4, 3, 2, 1  (counting down)
```

### `while` loop: repeat until something changes
```java
int bossHp = 100;
int round = 1;

while (bossHp > 0) {
    bossHp -= 30;
    System.out.println("Round " + round + ": boss HP is " + Math.max(bossHp, 0));
    round++;     // without something that changes, the loop never ends!
}
```

### Accumulator pattern (you'll use this forever)
```java
int totalScore = 0;
for (int i = 1; i <= 100; i++) {
    totalScore += i;
}
System.out.println(totalScore);   // 5050
```

### `break` and `continue`
```java
for (int wave = 1; wave <= 10; wave++) {
    if (wave == 3) {
        continue;       // skip wave 3
    }
    if (wave == 6) {
        break;          // stop the loop entirely
    }
    System.out.println("Wave " + wave);   // 1 2 4 5
}
```

### Randomness: loot rolls
```java
import java.util.Random;

public class LootRoll {
    public static void main(String[] args) {
        Random rng = new Random();
        for (int i = 0; i < 5; i++) {
            int roll = rng.nextInt(100) + 1;    // 1 to 100
            if (roll > 95) {
                System.out.println("Roll " + roll + ": LEGENDARY!");
            } else {
                System.out.println("Roll " + roll + ": common");
            }
        }
    }
}
```

### Your Turn
1. Print every 5th frame from 0 to 100 (`0, 5, 10, ...`).
2. Print a pyramid of blocks, one more per line:
   ```
   #
   ##
   ###
   ####
   ```
   *Hint: a loop inside a loop, or build the line with a second loop.*

---

## Part 6: Methods

### Concept
A **method** is a named, reusable block of code, like a skill or a power-up. It takes **parameters** (inputs) and can **return** a value (output). Because Java is strictly typed, you must declare the type of everything going in and coming out.

### Code Along
```java
public class Combat {

    static int calculateDamage(int attack, int defense) {
        int damage = attack - defense;
        if (damage < 0) {
            damage = 0;
        }
        return damage;
    }

    public static void main(String[] args) {
        int hit = calculateDamage(50, 20);
        System.out.println("Damage dealt: " + hit);                      // 30
        System.out.println("Weak hit: " + calculateDamage(5, 20));       // 0
    }
}
```

**Anatomy of a method:**
```
static  int  calculateDamage  (int attack, int defense)  { ... }
  |      |         |                  |
  |      |         |                  +-- parameters, with types
  |      |         +-- the method's name
  |      +-- the type it returns (void if it returns nothing)
  +-- needed for now so main can call it directly
```

**`void` vs returning a value:** a `void` method does something but gives nothing back. A method with a return type must `return` a value, which you can then use in other calculations.
```java
static void printHealthBar(int health) {      // prints, returns nothing
    System.out.println("HP: " + health);
}

static int heal(int health, int amount) {     // returns a value
    return Math.min(health + amount, 100);
}
```
A method that only prints can't be used inside other calculations. That's why in the practice set your methods must **return** their answers.

**Overloading** (same name, different parameters):
```java
static int add(int a, int b)             { return a + b; }
static double add(double a, double b)    { return a + b; }
```

### Methods get a *copy* of simple values
```java
static void tryToHeal(int health) {
    health = health + 50;       // changes only the local copy
}

// in main:
int hp = 20;
tryToHeal(hp);
System.out.println(hp);    // still 20!
```
To change the original value, **return** the new one and store it: `hp = heal(hp, 50);`

### Your Turn
Write `static boolean isCritical(int roll)` that returns `true` if the roll is 90 or above. Test it with 95 and 40.

---

## Part 7: Strings

### Concept
A `String` is a sequence of characters. Games deal with strings all day: names, chat messages, dialogue, save files, and commands.

### Code Along
```java
String command = "cast fireball";

System.out.println(command.length());          // 13
System.out.println(command.charAt(0));         // 'c'  first character
System.out.println(command.charAt(command.length() - 1));   // 'l'  last character
System.out.println(command.substring(0, 4));  // "cast"  start included, end excluded
System.out.println(command.substring(5));      // "fireball"  from index 5 to the end
System.out.println(command.toUpperCase());     // "CAST FIREBALL"
System.out.println(command.indexOf("fire"));   // 5   (-1 if not found)
System.out.println(command.contains("ball"));  // true
```

Splitting a command into parts (this is how text games read what you type):
```java
String line = "give sword 3";
String[] parts = line.split(" ");     // {"give", "sword", "3"}

String action = parts[0];
String item = parts[1];
int amount = Integer.parseInt(parts[2]);    // text "3" -> number 3

System.out.println(action + " " + amount + "x " + item);
```

Looping over characters:
```java
int vowels = 0;
for (int i = 0; i < "dragon slayer".length(); i++) {
    char c = "dragon slayer".charAt(i);
    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
        vowels++;
    }
}
System.out.println(vowels);    // 4
```

### Strings are immutable
Strings can't be changed after they're created. Methods like `toUpperCase()` give you a **new** string and leave the original alone:
```java
String name = "mimi";
name.toUpperCase();                // result thrown away!
System.out.println(name);          // still "mimi"

name = name.toUpperCase();         // store the new string
System.out.println(name);          // "MIMI"
```

Building a long string in a loop with `+` creates a new String each time (slow). Use `StringBuilder` instead:
```java
StringBuilder bar = new StringBuilder();
for (int i = 0; i < 10; i++) {
    bar.append("#");
}
System.out.println(bar.toString());    // ##########
```

### Your Turn
Write `static boolean isPalindrome(String text)` that returns `true` for words like `"racecar"` that read the same forwards and backwards. *Hint: compare `charAt(i)` with `charAt(length - 1 - i)`.*

---

## Part 8: Arrays

### Concept
An **array** is a fixed-size row of values of the same type, like the slots of a hotbar. You choose its size once, and it can never grow or shrink. Arrays are the most important structure to master before DSA.

### Code Along
```java
int[] scores = {250, 900, 475, 120, 660};

System.out.println(scores[0]);          // 250  (the first item is index 0)
System.out.println(scores[4]);          // 660  (last item)
System.out.println(scores.length);      // 5    (note: no parentheses, unlike String)

scores[1] = 950;                        // change a value
```

Creating an empty array (all slots start as `0`, `false`, or `null`):
```java
int[] inventory = new int[8];          // 8 slots, all zero
String[] names = new String[3];        // 3 slots, all null
inventory[0] = 15;
```

> **Out of range = crash.** `scores[5]` on a 5-item array throws `ArrayIndexOutOfBoundsException`. Valid indexes go from `0` to `length - 1`.

Looping:
```java
for (int i = 0; i < scores.length; i++) {
    System.out.println("Slot " + i + ": " + scores[i]);
}

for (int s : scores) {                  // "for each" loop: just the values
    System.out.println(s);
}
```

Printing a whole array nicely:
```java
import java.util.Arrays;

public class ArrayDemo {
    public static void main(String[] args) {
        int[] scores = {250, 900, 475};
        System.out.println(Arrays.toString(scores));   // [250, 900, 475]
    }
}
```
(Printing the array directly gives something like `[I@1b6d3586`, which is useless.)

### Finding the highest score manually (a real algorithm!)
```java
static int findHighest(int[] scores) {
    int highest = scores[0];
    for (int i = 1; i < scores.length; i++) {
        if (scores[i] > highest) {
            highest = scores[i];
        }
    }
    return highest;
}
```

**Explanation:** Assume the first item is the biggest. Walk through the rest; whenever you find a bigger one, update. That's a complete algorithm in a few lines. It looks at each item once, so with *n* items it takes about *n* steps. Remember this idea; we'll call it **O(n)** later.

### Rewinding: building a reversed copy
```java
static int[] reversed(int[] arr) {
    int[] result = new int[arr.length];
    for (int i = 0; i < arr.length; i++) {
        result[i] = arr[arr.length - 1 - i];
    }
    return result;
}
```

### Arrays are passed by reference
Unlike a plain `int`, a method that receives an array can change the **original**:
```java
static void zeroOut(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        arr[i] = 0;
    }
}
// after zeroOut(scores), the caller's scores array is all zeros!
```
This is why your practice problems say *"do not change the original array"*.

### 2D arrays: tile maps
A grid is an array of arrays. This is how many 2D games store their levels.
```java
public class TileMap {
    public static void main(String[] args) {
        // 0 = floor, 1 = wall, 2 = coin
        int[][] map = {
            {1, 1, 1, 1, 1},
            {1, 0, 2, 0, 1},
            {1, 0, 1, 2, 1},
            {1, 1, 1, 1, 1}
        };

        int coins = 0;
        for (int row = 0; row < map.length; row++) {
            for (int col = 0; col < map[row].length; col++) {
                if (map[row][col] == 2) {
                    coins++;
                }
            }
        }
        System.out.println("Coins on the map: " + coins);   // 2
        System.out.println("Tile at row 1, col 2: " + map[1][2]);   // 2
    }
}
```
`map[row][col]`: first the row (down), then the column (across). A loop inside a loop visits every tile.

### Your Turn
1. Write `static int findLowest(int[] arr)` without using `Math.min`.
2. Write `static double average(int[] arr)` that returns the average score. *Careful with integer division!*
3. Write `static int countAbove(int[] arr, int limit)` that counts how many scores are above `limit`.

---

## Part 9: ArrayList

### Concept
An array can't grow. An **`ArrayList`** can. It's a resizable list, perfect for inventories, enemy lists, and bullet lists, where the count changes as the game runs.

### Code Along
```java
import java.util.ArrayList;

public class InventoryDemo {
    public static void main(String[] args) {
        ArrayList<String> inventory = new ArrayList<>();

        inventory.add("sword");
        inventory.add("potion");
        inventory.add("key");
        inventory.add(1, "shield");        // insert at index 1

        System.out.println(inventory);              // [sword, shield, potion, key]
        System.out.println(inventory.get(0));       // sword
        System.out.println(inventory.size());       // 4  (a method, so it has parentheses)

        inventory.remove("potion");        // remove by value
        inventory.remove(0);               // remove by index
        System.out.println(inventory);              // [shield, key]

        System.out.println(inventory.contains("key"));   // true
        inventory.set(0, "iron shield");           // replace
    }
}
```

The `<String>` is a **generic**: it says what type the list holds. Lists hold objects, not primitives, so use the wrapper types: `ArrayList<Integer>` (not `int`), `ArrayList<Double>`, `ArrayList<Boolean>`.

Looping:
```java
ArrayList<String> loot = new ArrayList<>();
loot.add("gold");
loot.add("gem");

for (int i = 0; i < loot.size(); i++) {
    System.out.println(i + ": " + loot.get(i));
}

for (String item : loot) {
    System.out.println(item);
}
```

> **Don't remove items while looping over them with `for-each`.** It crashes with `ConcurrentModificationException`. Use a normal `for` loop going backwards, or collect what to remove first.

### Array vs ArrayList

| | Array `int[]` | `ArrayList<Integer>` |
|---|---|---|
| Size | fixed | grows and shrinks |
| Get item | `a[i]` | `list.get(i)` |
| Length | `a.length` | `list.size()` |
| Holds primitives (`int`) | yes | no (use `Integer`) |

### Your Turn
Write `static ArrayList<Integer> evensOnly(ArrayList<Integer> nums)` that returns a new list containing only the even numbers.

---

## Part 10: HashMap and HashSet

### HashSet: **unique** items, no order
```java
import java.util.ArrayList;
import java.util.HashSet;

public class SetDemo {
    public static void main(String[] args) {
        HashSet<String> found = new HashSet<>();
        found.add("gold");
        found.add("gem");
        found.add("gold");              // ignored: already there

        System.out.println(found.size());           // 2
        System.out.println(found.contains("gem"));  // true (very fast lookup)
    }
}
```

### HashMap: key → value pairs
Perfect for looking things up by name.
```java
import java.util.HashMap;

public class MapDemo {
    public static void main(String[] args) {
        HashMap<String, Integer> prices = new HashMap<>();
        prices.put("potion", 25);
        prices.put("sword", 150);
        prices.put("shield", 90);

        System.out.println(prices.get("sword"));                   // 150
        System.out.println(prices.get("bow"));                     // null (not found)
        System.out.println(prices.getOrDefault("bow", 0));         // 0
        System.out.println(prices.containsKey("potion"));          // true

        prices.put("potion", 30);          // same key: replaces the value
        prices.remove("shield");

        for (String item : prices.keySet()) {
            System.out.println(item + " costs " + prices.get(item));
        }
    }
}
```
Key and value types go in `<Key, Value>` and must be objects (`Integer`, not `int`). A HashMap has **no guaranteed order**.

### Counting with a HashMap (extremely common pattern)
```java
import java.util.HashMap;

public class DropCounter {
    public static void main(String[] args) {
        String[] drops = {"gold", "gem", "gold", "potion", "gold"};

        HashMap<String, Integer> counts = new HashMap<>();
        for (String drop : drops) {
            counts.put(drop, counts.getOrDefault(drop, 0) + 1);
        }
        System.out.println(counts);    // {gold=3, gem=1, potion=1} (order may vary)
    }
}
```

**Explanation:** `getOrDefault(drop, 0)` means "how many have I counted so far, or 0 if this is the first one?" Then add 1 and store it back.

**Why this matters for DSA:** HashMaps and HashSets let you look things up almost instantly, which is how you make slow algorithms fast. Game engines use them to find assets and entities by name or ID. We'll revisit them under hash tables.

### Your Turn
Given an array of enemy type names, build a `HashMap<String, Integer>` that counts how many of each type there are.

---

## Part 11: Classes and Objects

### Concept
Until now, a player's data lived in loose variables (`playerName`, `playerHealth`, `playerX`...). A **class** bundles related data and behavior into one unit, a blueprint. An **object** is one thing made from that blueprint. A game is mostly objects: players, enemies, bullets, items.

### Code Along
Make a file `Player.java`:
```java
public class Player {
    // fields: the data each player has
    private String name;
    private int health;
    private int x;
    private int y;

    // constructor: runs when you create a player
    public Player(String name, int health) {
        this.name = name;
        this.health = health;
        this.x = 0;
        this.y = 0;
    }

    // methods: what a player can do
    public void takeDamage(int amount) {
        health -= amount;
        if (health < 0) {
            health = 0;
        }
    }

    public void moveRight(int steps) {
        x += steps;
    }

    public boolean isAlive() {
        return health > 0;
    }

    // getters: let other code read private fields
    public String getName() { return name; }
    public int getHealth() { return health; }

    @Override
    public String toString() {
        return name + " [HP " + health + ", at (" + x + ", " + y + ")]";
    }
}
```

And a second file, `Game.java`, in the same folder:
```java
public class Game {
    public static void main(String[] args) {
        Player hero = new Player("Mimi", 100);
        Player rival = new Player("Kuro", 80);

        hero.moveRight(3);
        hero.takeDamage(30);
        rival.takeDamage(200);

        System.out.println(hero);                  // Mimi [HP 70, at (3, 0)]
        System.out.println(rival.isAlive());       // false
        System.out.println(hero.getName());        // Mimi
    }
}
```

Compile both and run the one with `main`:
```
javac Player.java Game.java
java Game
```

**Explanation:**
- `private` hides the data, so other code can only change `health` through your methods. That way nothing can accidentally set a player's health to -500.
- `this.name = name` means "this object's `name` field gets the parameter called `name`".
- `new Player(...)` creates an object and runs the constructor.
- `hero` and `rival` are two separate objects with their own data.
- `toString()` controls how an object prints.

### Many objects: an ArrayList of enemies
```java
import java.util.ArrayList;

public class Wave {
    public static void main(String[] args) {
        ArrayList<Player> enemies = new ArrayList<>();
        enemies.add(new Player("Goblin", 30));
        enemies.add(new Player("Orc", 80));
        enemies.add(new Player("Slime", 10));

        for (Player e : enemies) {
            e.takeDamage(40);
        }
        for (Player e : enemies) {
            System.out.println(e.getName() + " alive? " + e.isAlive());
        }
    }
}
```
(Run this one in the same folder as `Player.java`.)

### `null`: "no object here"
```java
Player target = null;
// target.takeDamage(5);   <-- NullPointerException! There is no object to use.
if (target != null) {
    target.takeDamage(5);
}
```
`NullPointerException` is the most common Java crash. It means you tried to use an object that doesn't exist yet.

### Your Turn
Create a class `Enemy` with `name`, `health` and `attackPower`. Give it a constructor, an `attack(Player p)` method that damages the player, and a `toString()`. Make three enemies and have them all attack the same player.

---

## Part 12: Recursion (A Method Calling Itself)

### Concept
Recursion solves a problem by solving a smaller version of the same problem. Think of a **chest inside a chest inside a chest**: opening each one is the same action repeated. Every recursive method needs:
1. **Base case**: when to stop
2. **Recursive case**: call itself with a smaller problem

### Code Along: the poison counter
Poison deals `damage` this turn, then 1 less each turn until it fades. What's the total?
```java
public class Poison {

    static int totalPoison(int damage) {
        if (damage <= 0) {                            // base case
            return 0;
        }
        return damage + totalPoison(damage - 1);      // recursive case
    }

    public static void main(String[] args) {
        System.out.println(totalPoison(3));    // 6   (3 + 2 + 1)
        System.out.println(totalPoison(5));    // 15
    }
}
```

**Trace it by hand** (do this on paper!):
```
totalPoison(3)
= 3 + totalPoison(2)
= 3 + (2 + totalPoison(1))
= 3 + (2 + (1 + totalPoison(0)))
= 3 + (2 + (1 + 0))
= 6
```

### Code Along: chests inside chests
A chest holds items (Strings) and other chests (arrays), and chests can nest forever:
```java
public class Chests {

    static int countItems(Object[] chest) {
        int total = 0;
        for (Object thing : chest) {
            if (thing instanceof Object[]) {                 // it's another chest
                total += countItems((Object[]) thing);       // open it and count inside
            } else {                                         // it's an item
                total++;
            }
        }
        return total;
    }

    public static void main(String[] args) {
        Object[] loot = {
            "sword",
            new Object[]{ "potion", "key", new Object[]{ "gem" } },
            "shield"
        };
        System.out.println(countItems(loot));    // 5
    }
}
```
Without recursion, you couldn't know how deep the chests go. Recursion handles any depth.

> **No base case = crash.** Forget it, and Java throws `StackOverflowError`. Every call waits on the "call stack" for the next one to finish, and eventually the stack runs out of room. Try it and see.

### Your Turn
1. Write a recursive `static int power(int base, int exp)` for `exp >= 0`.
2. Write a recursive `static void countdown(int n)` that prints `n, n-1, ..., 1, "GO!"`.

---

## Part 13: Bridge to Data Structures and Algorithms

You now have the tools. Here's where they lead.

### Linear search
Finding a score by checking every item, one by one:
```java
static int linearSearch(int[] items, int target) {
    for (int i = 0; i < items.length; i++) {
        if (items[i] == target) {
            return i;
        }
    }
    return -1;      // not found
}
```

### Binary search (needs a **sorted** array; much faster)
```java
static int binarySearch(int[] items, int target) {
    int low = 0;
    int high = items.length - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (items[mid] == target) {
            return mid;
        } else if (items[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}
```

**Explanation:** Look at the middle. If the target is bigger, throw away the left half; if smaller, throw away the right half. It's the "higher or lower" guessing game, played smartly. A leaderboard of 1,000,000 scores needs only about 20 looks instead of up to 1,000,000.

### Big-O in one table (just the idea for now)

| Notation | Name | Game example |
|---|---|---|
| O(1) | constant | `inventory[0]`, `map.get("sword")` |
| O(log n) | logarithmic | binary search on a leaderboard |
| O(n) | linear | linear search, `findHighest`, updating every enemy once per frame |
| O(n²) | quadratic | checking every bullet against every enemy (collision checks) |

The question we'll keep asking all semester: **"How does the work grow as the input grows?"** With 10 enemies, an O(n²) collision check is 100 tests. With 1,000 enemies it's 1,000,000 tests *every frame*, and the game stutters. Choosing the right algorithm is what keeps a game at 60 FPS.

---

## Debugging Habits

1. **Read the error message from the top.** Java tells you the file, the line number, and what's wrong.
2. **Print values** with `System.out.println` to see what the code is actually doing, not what you think it's doing.
3. **Test small.** Try an empty array, a one-item array, and a normal array.
4. **Change one thing at a time**, and recompile every time.

**Compile errors** (show up when you run `javac`; the program never starts):

| Error message | Usually means |
|---|---|
| `';' expected` | missing semicolon on that line or the line before |
| `cannot find symbol` | misspelled name, wrong capitalization, missing `import`, or variable used outside its `{ }` |
| `incompatible types: possible lossy conversion from double to int` | you're squeezing a decimal into an `int`; cast it: `(int) value` |
| `missing return statement` | some path through your method doesn't `return` |
| `class X is public, should be declared in a file named X.java` | file name and class name don't match |
| `variable might not have been initialized` | you used a variable before giving it a value |

**Runtime errors** (the program starts, then crashes):

| Exception | Usually means |
|---|---|
| `ArrayIndexOutOfBoundsException` | index below 0 or `>= length` |
| `NullPointerException` | using an object that is `null` |
| `NumberFormatException` | `Integer.parseInt("abc")`, text isn't a number |
| `InputMismatchException` | `Scanner.nextInt()` got text instead of a number |
| `StackOverflowError` | recursion that never reaches its base case |
| `ArithmeticException: / by zero` | dividing an `int` by 0 |

---

## Game Dev Practice Set (Auto-Checked)

Once you've finished the sections above, open the `java_gamedev/practice` folder in VS Code and fill in the methods in `Practice.java`. Only edit that one file. Check your work from a terminal inside that folder:

```
javac Practice.java Checker.java SortedScores.java
java Checker
```

Run **both** commands every time you change your code.

| # | Problem | Skill it trains |
|---|---|---|
| 1 | Playtime clock `HH:MM:SS` | `/`, `%`, `String.format` |
| 2 | Take damage (armor, no negative health) | methods, conditionals |
| 3 | Rewind an array | arrays, loops |
| 4 | Find the strongest enemy | arrays, the max-finding pattern |
| 5 | Tidy the loot (remove duplicates) | `ArrayList`, `HashSet` |
| 6 | Do two players carry the same items? | `HashMap`, counting |
| 7 | Find a score fast | binary search |
| 8 | Count the monster drops | `HashMap` |
| 9 | Poison damage | recursion |
| 10 | Challenge: chests inside chests | recursion on nested data |

If your code has a compile error, `javac` will print it and `java Checker` will not run (or will run your old version). Fix the errors first.

---

## Self-Check Before Moving On

You're ready for the first DSA topic if you can do all of these without help:

- [ ] Write a method that takes an array and returns something computed from it
- [ ] Loop through an array using both `for (int i...)` and for-each
- [ ] Explain the difference between a method that prints and a method that returns
- [ ] Explain why you use `.equals()` and not `==` for Strings
- [ ] Use a `HashMap` to count things
- [ ] Create a class with fields, a constructor and a method, and make objects from it
- [ ] Trace a small recursive method by hand
- [ ] Read a compile error and find the line that caused it
