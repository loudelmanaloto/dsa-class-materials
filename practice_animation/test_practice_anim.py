"""
Automatic checker for practice_anim.py

Run:  python test_practice_anim.py
"""
import ast
import inspect
import unittest

import practice_anim as p


def code_tree(func):
    """Parse a function's code, ignoring comments and the docstring."""
    fn = ast.parse(inspect.getsource(func).strip()).body[0]
    if (fn.body and isinstance(fn.body[0], ast.Expr)
            and isinstance(fn.body[0].value, ast.Constant)
            and isinstance(fn.body[0].value.value, str)):
        fn.body = fn.body[1:] or [ast.Pass()]
    return fn


def is_stub(func):
    body = code_tree(func).body
    return len(body) == 1 and isinstance(body[0], ast.Pass)


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
    if is_stub(func):
        test.fail("Not started yet (the function still just says 'pass')")


def no_calls(test, func, banned_names):
    banned = set(banned_names) & calls(func)
    test.assertFalse(banned, f"Not allowed: {', '.join(sorted(banned))}")


class Test1_Timecode(unittest.TestCase):
    def test_zero(self):
        implemented(self, p.frame_to_timecode)
        self.assertEqual(p.frame_to_timecode(0, 24), "00:00:00")

    def test_basic(self):
        self.assertEqual(p.frame_to_timecode(100, 24), "00:04:04")

    def test_exactly_one_second(self):
        self.assertEqual(p.frame_to_timecode(24, 24), "00:01:00")

    def test_over_a_minute(self):
        self.assertEqual(p.frame_to_timecode(1500, 24), "01:02:12")

    def test_other_fps(self):
        self.assertEqual(p.frame_to_timecode(45, 30), "00:01:15")

    def test_returns_string(self):
        self.assertIsInstance(p.frame_to_timecode(5, 24), str)


class Test2_TweenColor(unittest.TestCase):
    def test_start(self):
        implemented(self, p.tween_color)
        self.assertEqual(p.tween_color((10, 20, 30), (200, 100, 0), 0),
                         (10, 20, 30))

    def test_end(self):
        self.assertEqual(p.tween_color((10, 20, 30), (200, 100, 0), 1),
                         (200, 100, 0))

    def test_quarter(self):
        self.assertEqual(p.tween_color((0, 0, 0), (100, 200, 40), 0.25),
                         (25, 50, 10))

    def test_half(self):
        self.assertEqual(p.tween_color((0, 0, 0), (100, 200, 40), 0.5),
                         (50, 100, 20))

    def test_going_down(self):
        self.assertEqual(p.tween_color((200, 100, 50), (0, 0, 0), 0.5),
                         (100, 50, 25))

    def test_returns_whole_number_tuple(self):
        result = p.tween_color((0, 0, 0), (255, 255, 255), 0.3)
        self.assertIsInstance(result, tuple, "Return a tuple, not a list")
        for channel in result:
            self.assertIsInstance(channel, int,
                                  "Use round() so each channel is a whole number")
        self.assertEqual(result, (76, 76, 76))


class Test3_ReverseClip(unittest.TestCase):
    def test_basic(self):
        implemented(self, p.reverse_clip)
        self.assertEqual(p.reverse_clip(["f1", "f2", "f3"]), ["f3", "f2", "f1"])

    def test_edges(self):
        self.assertEqual(p.reverse_clip([]), [])
        self.assertEqual(p.reverse_clip(["only"]), ["only"])

    def test_does_not_change_original(self):
        original = [1, 2, 3, 4]
        p.reverse_clip(original)
        self.assertEqual(original, [1, 2, 3, 4],
                         "You changed the original list. Build a NEW one.")

    def test_returns_new_list(self):
        original = [1, 2]
        self.assertIsNot(p.reverse_clip(original), original)

    def test_no_shortcuts(self):
        no_calls(self, p.reverse_clip, {"reverse", "reversed"})
        for node in ast.walk(code_tree(p.reverse_clip)):
            if isinstance(node, ast.Slice) and node.step is not None:
                self.fail("Not allowed: slicing with a step like [::-1]")


class Test4_BrightestColor(unittest.TestCase):
    def test_basic(self):
        implemented(self, p.brightest_color)
        self.assertEqual(
            p.brightest_color([(10, 10, 10), (200, 0, 0), (50, 50, 50)]),
            (200, 0, 0))

    def test_brightest_is_last(self):
        self.assertEqual(
            p.brightest_color([(0, 0, 0), (10, 10, 10), (255, 255, 255)]),
            (255, 255, 255))

    def test_adds_all_three_channels(self):
        self.assertEqual(p.brightest_color([(200, 0, 0), (100, 100, 100)]),
                         (100, 100, 100),
                         "Brightness is r + g + b (300 beats 200)")

    def test_tie_returns_first(self):
        self.assertEqual(p.brightest_color([(100, 0, 0), (0, 100, 0)]),
                         (100, 0, 0))

    def test_single_and_empty(self):
        self.assertEqual(p.brightest_color([(1, 2, 3)]), (1, 2, 3))
        self.assertIsNone(p.brightest_color([]))

    def test_no_shortcuts(self):
        no_calls(self, p.brightest_color, {"max", "min", "sorted", "sort"})


class Test5_UniqueColors(unittest.TestCase):
    def test_basic(self):
        implemented(self, p.unique_colors)
        self.assertEqual(
            p.unique_colors(["red", "blue", "red", "green", "blue"]),
            ["red", "blue", "green"])

    def test_keeps_order(self):
        self.assertEqual(p.unique_colors(["z", "a", "z", "m"]), ["z", "a", "m"],
                         "Order must stay the same as the original")

    def test_no_duplicates_and_empty(self):
        self.assertEqual(p.unique_colors(["a", "b"]), ["a", "b"])
        self.assertEqual(p.unique_colors([]), [])

    def test_all_same(self):
        self.assertEqual(p.unique_colors(["x", "x", "x"]), ["x"])

    def test_tuples_work_too(self):
        self.assertEqual(p.unique_colors([(1, 2, 3), (4, 5, 6), (1, 2, 3)]),
                         [(1, 2, 3), (4, 5, 6)])

    def test_returns_list(self):
        self.assertIsInstance(p.unique_colors(["a", "a"]), list,
                              "Return a list, not a set")


class Test6_SameLayers(unittest.TestCase):
    def test_true(self):
        implemented(self, p.same_layers)
        self.assertIs(p.same_layers(["Sky", "Hero", "Tree"],
                                    ["tree", "SKY", "hero"]), True)

    def test_false(self):
        self.assertIs(p.same_layers(["Sky", "Hero"], ["Sky", "Villain"]), False)

    def test_different_counts(self):
        self.assertIs(p.same_layers(["a", "a", "b"], ["a", "b", "b"]), False,
                      "Same names but different counts is NOT the same")

    def test_different_lengths(self):
        self.assertIs(p.same_layers(["a"], ["a", "b"]), False)

    def test_empty(self):
        self.assertIs(p.same_layers([], []), True)

    def test_does_not_change_inputs(self):
        a, b = ["B", "A"], ["a", "b"]
        p.same_layers(a, b)
        self.assertEqual((a, b), (["B", "A"], ["a", "b"]),
                         "Don't modify the lists that were passed in")


class CountingSequence:
    """A big sorted list that counts how many items you look at."""

    def __init__(self, n):
        self.n = n
        self.looks = 0

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        if isinstance(i, slice):
            raise TypeError("Don't slice the list. Use index positions "
                            "(low, high, mid) instead.")
        if i < 0 or i >= self.n:
            raise IndexError(i)
        self.looks += 1
        return i * 2  # sorted even numbers: 0, 2, 4, ...


class Test7_FindKeyframe(unittest.TestCase):
    def test_found(self):
        implemented(self, p.find_keyframe)
        self.assertEqual(p.find_keyframe([0, 12, 24, 48, 96], 48), 3)

    def test_first_and_last(self):
        data = [0, 12, 24, 48, 96]
        self.assertEqual(p.find_keyframe(data, 0), 0)
        self.assertEqual(p.find_keyframe(data, 96), 4)

    def test_not_found(self):
        data = [0, 12, 24, 48, 96]
        self.assertEqual(p.find_keyframe(data, 50), -1)
        self.assertEqual(p.find_keyframe(data, -5), -1)
        self.assertEqual(p.find_keyframe(data, 1000), -1)

    def test_empty_and_single(self):
        self.assertEqual(p.find_keyframe([], 5), -1)
        self.assertEqual(p.find_keyframe([7], 7), 0)
        self.assertEqual(p.find_keyframe([7], 8), -1)

    def test_every_item_found(self):
        data = list(range(0, 100, 3))
        for i, value in enumerate(data):
            self.assertEqual(p.find_keyframe(data, value), i)

    def test_is_really_binary_search(self):
        seq = CountingSequence(1_000_000)
        self.assertEqual(p.find_keyframe(seq, 1_234_568), 617_284)
        self.assertLess(seq.looks, 100,
                        f"You looked at {seq.looks} items out of 1,000,000. "
                        "Binary search needs only about 20.")

    def test_missing_in_big_list_is_fast_too(self):
        seq = CountingSequence(1_000_000)
        self.assertEqual(p.find_keyframe(seq, 7), -1)  # odd: not in list
        self.assertLess(seq.looks, 100,
                        f"You looked at {seq.looks} items. Binary search "
                        "needs only about 20.")

    def test_no_shortcuts(self):
        no_calls(self, p.find_keyframe, {"index", "count"})


class Test8_CountTags(unittest.TestCase):
    def test_basic(self):
        implemented(self, p.count_tags)
        self.assertEqual(p.count_tags(["walk", "run", "walk"]),
                         {"walk": 2, "run": 1})

    def test_empty(self):
        self.assertEqual(p.count_tags([]), {})

    def test_all_same(self):
        self.assertEqual(p.count_tags(["idle"] * 4), {"idle": 4})

    def test_many(self):
        tags = ["walk", "run", "walk", "jump", "walk", "run"]
        self.assertEqual(p.count_tags(tags), {"walk": 3, "run": 2, "jump": 1})

    def test_returns_dict(self):
        self.assertIsInstance(p.count_tags(["a"]), dict)


class Test9_BounceHeight(unittest.TestCase):
    def test_no_bounces(self):
        implemented(self, p.bounce_height)
        self.assertAlmostEqual(p.bounce_height(100, 0), 100)

    def test_one_bounce(self):
        self.assertAlmostEqual(p.bounce_height(100, 1), 60.0)

    def test_two_bounces(self):
        self.assertAlmostEqual(p.bounce_height(100, 2), 36.0)

    def test_many_bounces(self):
        self.assertAlmostEqual(p.bounce_height(100, 3), 21.6)

    def test_custom_ratio(self):
        self.assertAlmostEqual(p.bounce_height(80, 3, 0.5), 10.0)

    def test_must_be_recursive(self):
        self.assertIn("bounce_height", calls(p.bounce_height),
                      "Your function must call itself (recursion)")

    def test_no_loops(self):
        for node in ast.walk(code_tree(p.bounce_height)):
            if isinstance(node, (ast.For, ast.While)):
                self.fail("No loops allowed. Use recursion instead.")


class Test10_CountLayers(unittest.TestCase):
    def test_flat(self):
        implemented(self, p.count_layers)
        self.assertEqual(p.count_layers(["bg", "hero", "fx"]), 3)

    def test_empty(self):
        self.assertEqual(p.count_layers([]), 0)

    def test_one_folder(self):
        self.assertEqual(p.count_layers(["bg", ["hero", "shadow"]]), 3)

    def test_nested(self):
        self.assertEqual(
            p.count_layers(["bg", ["hero", "shadow", ["hat"]], "fx"]), 5)

    def test_deep(self):
        self.assertEqual(p.count_layers([[[["deep"]]]]), 1)

    def test_empty_folders(self):
        self.assertEqual(p.count_layers([[], ["a", []], []]), 1)

    def test_does_not_change_input(self):
        scene = ["bg", ["hero", ["hat"]]]
        p.count_layers(scene)
        self.assertEqual(scene, ["bg", ["hero", ["hat"]]])

    def test_must_be_recursive(self):
        self.assertIn("count_layers", calls(p.count_layers),
                      "Your function must call itself (recursion)")


PROBLEMS = [
    ("1.  Timecode", Test1_Timecode, p.frame_to_timecode),
    ("2.  Color tween", Test2_TweenColor, p.tween_color),
    ("3.  Play it backwards", Test3_ReverseClip, p.reverse_clip),
    ("4.  Brightest pixel", Test4_BrightestColor, p.brightest_color),
    ("5.  Clean up a palette", Test5_UniqueColors, p.unique_colors),
    ("6.  Same layers?", Test6_SameLayers, p.same_layers),
    ("7.  Find a keyframe", Test7_FindKeyframe, p.find_keyframe),
    ("8.  Count the tags", Test8_CountTags, p.count_tags),
    ("9.  Bouncing ball", Test9_BounceHeight, p.bounce_height),
    ("10. CHALLENGE: layers", Test10_CountLayers, p.count_layers),
]


def run_all():
    loader = unittest.TestLoader()
    solved = 0
    details = []

    print("=" * 56)
    print(" ANIMATION PRACTICE SET RESULTS")
    print("=" * 56)

    for title, case, func in PROBLEMS:
        if is_stub(func):
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
