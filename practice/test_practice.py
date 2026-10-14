"""
Automatic checker for practice.py

Run:  python test_practice.py
"""
import ast
import inspect
import unittest

import practice


def code_tree(func):
    """Parse a function's code, ignoring comments and the docstring."""
    tree = ast.parse(inspect.getsource(func).strip())
    fn = tree.body[0]
    if (fn.body and isinstance(fn.body[0], ast.Expr)
            and isinstance(fn.body[0].value, ast.Constant)
            and isinstance(fn.body[0].value.value, str)):
        fn.body = fn.body[1:] or [ast.Pass()]
    return fn


def calls(func):
    """Names of everything the function calls, e.g. {'len', 'sorted'}."""
    names = set()
    for node in ast.walk(code_tree(func)):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                names.add(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                names.add(node.func.attr)
    return names


def implemented(test, func):
    """Fail with a friendly message if the student hasn't started yet."""
    body = code_tree(func).body
    if len(body) == 1 and isinstance(body[0], ast.Pass):
        test.fail("Not started yet (the function still just says 'pass')")


class Test1_FizzBuzz(unittest.TestCase):
    def test_small(self):
        implemented(self, practice.fizzbuzz)
        self.assertEqual(practice.fizzbuzz(5), ["1", "2", "Fizz", "4", "Buzz"])

    def test_fizzbuzz_case(self):
        result = practice.fizzbuzz(15)
        self.assertEqual(result[14], "FizzBuzz", "15 should be FizzBuzz")
        self.assertEqual(len(result), 15, "Should have exactly n items")

    def test_returns_strings(self):
        self.assertEqual(practice.fizzbuzz(1), ["1"],
                         "Numbers must be strings, e.g. '1' not 1")

    def test_zero(self):
        self.assertEqual(practice.fizzbuzz(0), [])


class Test2_ReverseList(unittest.TestCase):
    def test_basic(self):
        implemented(self, practice.reverse_list)
        self.assertEqual(practice.reverse_list([1, 2, 3]), [3, 2, 1])

    def test_edges(self):
        self.assertEqual(practice.reverse_list([]), [])
        self.assertEqual(practice.reverse_list([7]), [7])

    def test_does_not_change_original(self):
        original = [1, 2, 3, 4]
        practice.reverse_list(original)
        self.assertEqual(original, [1, 2, 3, 4],
                         "You changed the original list. Build a NEW one.")

    def test_returns_new_list(self):
        original = [1, 2]
        self.assertIsNot(practice.reverse_list(original), original)

    def test_no_shortcuts(self):
        banned = {"reverse", "reversed"} & calls(practice.reverse_list)
        self.assertFalse(banned, f"Not allowed: {', '.join(banned)}")
        for node in ast.walk(code_tree(practice.reverse_list)):
            if isinstance(node, ast.Slice) and node.step is not None:
                self.fail("Not allowed: slicing with a step like [::-1]")


class Test3_SecondLargest(unittest.TestCase):
    def test_basic(self):
        implemented(self, practice.second_largest)
        self.assertEqual(practice.second_largest([5, 3, 8, 1]), 5)

    def test_duplicates_of_max(self):
        self.assertEqual(practice.second_largest([5, 3, 8, 8, 1]), 5,
                         "Distinct values only: the second largest of "
                         "[8, 8, 5] is 5, not 8")

    def test_negatives(self):
        self.assertEqual(practice.second_largest([-5, -2, -9]), -5)

    def test_not_enough(self):
        self.assertIsNone(practice.second_largest([4]))
        self.assertIsNone(practice.second_largest([4, 4, 4]))
        self.assertIsNone(practice.second_largest([]))

    def test_no_shortcuts(self):
        banned = {"sorted", "sort"} & calls(practice.second_largest)
        self.assertFalse(banned, f"Not allowed: {', '.join(banned)}")


class Test4_RemoveDuplicates(unittest.TestCase):
    def test_basic(self):
        implemented(self, practice.remove_duplicates)
        self.assertEqual(practice.remove_duplicates([3, 1, 3, 2, 1]), [3, 1, 2])

    def test_keeps_order(self):
        self.assertEqual(practice.remove_duplicates([9, 8, 9, 7]), [9, 8, 7],
                         "Order must stay the same as the original")

    def test_no_duplicates(self):
        self.assertEqual(practice.remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_empty_and_all_same(self):
        self.assertEqual(practice.remove_duplicates([]), [])
        self.assertEqual(practice.remove_duplicates([5, 5, 5]), [5])

    def test_strings(self):
        self.assertEqual(practice.remove_duplicates(["a", "b", "a"]), ["a", "b"])

    def test_returns_list(self):
        self.assertIsInstance(practice.remove_duplicates([1, 1]), list,
                              "Return a list, not a set")


class Test5_Anagram(unittest.TestCase):
    def test_true(self):
        implemented(self, practice.is_anagram)
        self.assertIs(practice.is_anagram("listen", "silent"), True)

    def test_ignores_case(self):
        self.assertIs(practice.is_anagram("Listen", "SILENT"), True)

    def test_false(self):
        self.assertIs(practice.is_anagram("hello", "world"), False)

    def test_different_counts(self):
        self.assertIs(practice.is_anagram("aab", "abb"), False,
                      "Same letters but different counts is NOT an anagram")

    def test_different_lengths(self):
        self.assertIs(practice.is_anagram("abc", "abcd"), False)

    def test_empty(self):
        self.assertIs(practice.is_anagram("", ""), True)


class Test6_TwoSum(unittest.TestCase):
    def check(self, nums, target):
        result = practice.two_sum(nums, target)
        self.assertIsNotNone(result, "A valid pair exists, but you returned None")
        self.assertEqual(len(result), 2)
        i, j = result
        self.assertNotEqual(i, j, "Cannot use the same index twice")
        self.assertLess(i, j, "Return the smaller index first")
        self.assertEqual(nums[i] + nums[j], target,
                         f"nums[{i}] + nums[{j}] = {nums[i] + nums[j]}, "
                         f"not {target}")

    def test_basic(self):
        implemented(self, practice.two_sum)
        self.check([2, 7, 11, 15], 9)

    def test_not_at_start(self):
        self.check([3, 2, 4], 6)

    def test_duplicates(self):
        self.check([3, 3], 6)

    def test_negatives(self):
        self.check([-3, 4, 3, 90], 0)

    def test_cannot_reuse_same_item(self):
        self.assertIsNone(practice.two_sum([5, 1, 2], 10),
                          "5 + 5 doesn't count: there is only one 5")

    def test_no_pair(self):
        self.assertIsNone(practice.two_sum([1, 2, 3], 100))
        self.assertIsNone(practice.two_sum([], 5))


class Test7_CountVowels(unittest.TestCase):
    def test_basic(self):
        implemented(self, practice.count_vowels)
        self.assertEqual(practice.count_vowels("Banana Bread"),
                         {"a": 4, "e": 1})

    def test_ignores_case(self):
        self.assertEqual(practice.count_vowels("AaEe"), {"a": 2, "e": 2})

    def test_no_vowels(self):
        self.assertEqual(practice.count_vowels("rhythm"), {})
        self.assertEqual(practice.count_vowels(""), {})

    def test_only_vowels_present(self):
        result = practice.count_vowels("hello")
        self.assertEqual(result, {"e": 1, "o": 1},
                         "Only include vowels that actually appear")

    def test_ignores_non_letters(self):
        self.assertEqual(practice.count_vowels("a1 b2! a"), {"a": 2})


class Test8_Power(unittest.TestCase):
    def test_basic(self):
        implemented(self, practice.power)
        self.assertEqual(practice.power(2, 5), 32)

    def test_zero_exponent(self):
        self.assertEqual(practice.power(7, 0), 1)
        self.assertEqual(practice.power(0, 0), 1)

    def test_exponent_one(self):
        self.assertEqual(practice.power(9, 1), 9)

    def test_negative_base(self):
        self.assertEqual(practice.power(-2, 3), -8)
        self.assertEqual(practice.power(-2, 4), 16)

    def test_bigger(self):
        self.assertEqual(practice.power(3, 10), 59049)

    def test_must_be_recursive(self):
        self.assertIn("power", calls(practice.power),
                      "Your function must call itself (recursion)")

    def test_no_shortcuts(self):
        self.assertNotIn("pow", calls(practice.power), "Not allowed: pow()")
        for node in ast.walk(code_tree(practice.power)):
            if isinstance(node, ast.Pow):
                self.fail("Not allowed: the ** operator")


PROBLEMS = [
    ("1. FizzBuzz", Test1_FizzBuzz, practice.fizzbuzz),
    ("2. Reverse a list", Test2_ReverseList, practice.reverse_list),
    ("3. Second largest", Test3_SecondLargest, practice.second_largest),
    ("4. Remove duplicates", Test4_RemoveDuplicates, practice.remove_duplicates),
    ("5. Anagram check", Test5_Anagram, practice.is_anagram),
    ("6. Two sum", Test6_TwoSum, practice.two_sum),
    ("7. Count vowels", Test7_CountVowels, practice.count_vowels),
    ("8. Power (recursion)", Test8_Power, practice.power),
]


def run_all():
    loader = unittest.TestLoader()
    solved = 0
    details = []

    print("=" * 56)
    print(" PRACTICE SET RESULTS")
    print("=" * 56)

    for title, case, func in PROBLEMS:
        body = code_tree(func).body
        if len(body) == 1 and isinstance(body[0], ast.Pass):
            print(f" [ -- ] {title}  (not started)")
            continue
        suite = loader.loadTestsFromTestCase(case)
        result = unittest.TestResult()
        suite.run(result)
        total = suite.countTestCases()
        bad = result.failures + result.errors
        passed = total - len(bad)

        if not bad:
            solved += 1
            print(f" [PASS] {title}  ({passed}/{total} tests)")
        else:
            print(f" [FAIL] {title}  ({passed}/{total} tests)")
            details.append((title, bad))

    print("-" * 56)
    print(f" Solved {solved} of {len(PROBLEMS)} problems")
    print("=" * 56)

    for title, bad in details:
        print(f"\n--- {title} ---")
        for test, trace in bad:
            name = test.id().split(".")[-1].replace("test_", "").replace("_", " ")
            last = trace.strip().splitlines()[-1]
            print(f"  x {name}: {last}")

    if solved == len(PROBLEMS):
        print("\nAll done. Great work!")


if __name__ == "__main__":
    run_all()
