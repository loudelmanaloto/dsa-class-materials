"""
ANIMATION PRACTICE SET - fill in each function below.

How to check your work:
    python test_practice_anim.py

Rules:
  * Edit ONLY this file (practice_anim.py).
  * Functions should RETURN their answer, not print it.
  * Some problems ban certain shortcuts. The checker will tell you.
  * Work on one problem at a time. "not started" is normal for the
    ones you haven't reached yet.

Quick vocabulary:
  frame      one still image in an animation
  fps        frames per second (24 is the film standard)
  keyframe   a frame where you set an important pose
  tween      the in-between frames the computer fills in
  layer      one piece of a scene (background, character, shadow...)
  RGB color  a tuple (red, green, blue), each from 0 to 255
"""


# 1. Timecode
# Editing software shows time as "MM:SS:FF" (minutes:seconds:frames).
# Given a frame number and the fps, return that timecode as a string.
# Each part has exactly 2 digits (pad with a leading zero).
# Frame 0 is "00:00:00".
# Hint: // and % are your friends. f"{x:02d}" pads a number to 2 digits.
# Example: frame_to_timecode(100, 24) -> "00:04:04"
#          frame_to_timecode(1500, 24) -> "01:02:12"
def frame_to_timecode(frame, fps):
    pass


# 2. Color tween
# Blend between two colors. t=0 gives the first color, t=1 gives the
# second, t=0.5 is halfway. Do each of the R, G, B channels separately:
#     start + (end - start) * t
# Return a TUPLE of three whole numbers (use round()).
# Example: tween_color((0, 0, 0), (100, 200, 40), 0.25) -> (25, 50, 10)
def tween_color(c1, c2, t):
    pass


# 3. Play it backwards
# Return a NEW list with the frames in reverse order.
# Do not change the original list.
# Not allowed: .reverse(), reversed(), or slicing with a step like [::-1]
# Example: reverse_clip(["f1", "f2", "f3"]) -> ["f3", "f2", "f1"]
def reverse_clip(frames):
    pass


# 4. Brightest pixel
# pixels is a list of (r, g, b) tuples. A pixel's brightness is r + g + b.
# Return the brightest pixel. If there is a tie, return the first one.
# If the list is empty, return None.
# Not allowed: max(), min(), sorted(), .sort()
# Example: brightest_color([(10, 10, 10), (200, 0, 0), (50, 50, 50)])
#          -> (200, 0, 0)
def brightest_color(pixels):
    pass


# 5. Clean up a palette
# Return a new list with duplicate colors removed, keeping the original
# order (the first time each color appears).
# Example: unique_colors(["red", "blue", "red", "green", "blue"])
#          -> ["red", "blue", "green"]
def unique_colors(palette):
    pass


# 6. Same layers?
# Two scene files list their layers. Return True if they contain exactly
# the same layers, in any order, ignoring upper/lower case. A layer that
# appears twice must appear twice in both. Otherwise return False.
# Example: same_layers(["Sky", "Hero", "Tree"], ["tree", "SKY", "hero"])
#          -> True
def same_layers(a, b):
    pass


# 7. Find a keyframe (binary search)
# keyframes is a list of frame numbers, ALREADY SORTED from smallest to
# largest. Return the index where target is found, or -1 if it isn't there.
# Use BINARY SEARCH: look at the middle, then throw away half each time.
# (The checker counts how many items you look at. Looping through
# everything will fail on the big test.)
# Not allowed: .index(), .count()
# Example: find_keyframe([0, 12, 24, 48, 96], 48) -> 3
#          find_keyframe([0, 12, 24, 48, 96], 50) -> -1
def find_keyframe(keyframes, target):
    pass


# 8. Count the tags
# Animators tag their clips: ["walk", "run", "walk", "jump", "walk"].
# Return a dictionary of how many times each tag appears.
# Example: count_tags(["walk", "run", "walk"]) -> {"walk": 2, "run": 1}
def count_tags(tags):
    pass


# 9. Bouncing ball (recursion)
# A ball is dropped from start_height. Every bounce, it only reaches
# `ratio` of its previous height (0.6 means 60%).
# Return how high it gets after the given number of bounces.
# You MUST solve it recursively (the function calls itself, no loops).
# Example: bounce_height(100, 0) -> 100
#          bounce_height(100, 1) -> 60.0
#          bounce_height(100, 2) -> 36.0
def bounce_height(start_height, bounces, ratio=0.6):
    pass


# 10. CHALLENGE: Count layers in folders (recursion)
# A timeline can have folders inside folders. Layers are strings.
# Folders are lists, and can contain layers and other folders.
# Return the total number of layers (strings) anywhere inside.
# You MUST solve it recursively.
# Example: count_layers(["bg", ["hero", "shadow", ["hat"]], "fx"]) -> 5
#          count_layers([]) -> 0
# Hint: for each item, is it a string or a list?
#       isinstance(item, list) tells you.
def count_layers(folder):
    pass
