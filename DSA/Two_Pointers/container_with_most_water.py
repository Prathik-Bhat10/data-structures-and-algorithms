"""
CONTAINER WITH MOST WATER
-------------------------
Given an integer array `height` where each element represents
the height of a vertical line, find two lines that together with
the x-axis form a container that holds the maximum amount of water.

The amount of water is determined by:

Area = min(height[left], height[right]) × (right - left)

Example:
Input : height = [1,8,6,2,5,4,8,3,7]
Output: 49

Explanation:

Height
 8 |      |                   |
 7 |      |                 | |
 6 |      | |               | |
 5 |      | |     |         | |
 4 |      | |     | |       | |
 3 |      | |     | |     | | |
 2 |      | | |   | |     | | |
 1 | |    | | | | | | |   | | |
   +-----------------------------
     0 1 2 3 4 5 6 7 8

Choose:
Left  = index 1 (height = 8)
Right = index 8 (height = 7)

Width = 8 - 1 = 7
Height = min(8,7) = 7

Area = 7 × 7 = 49
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Try every possible pair of lines.

For each pair:
Area = min(height[i], height[j]) × (j - i)

Keep track of the maximum area.

Time  : O(n²)
Space : O(1)
"""

def max_area_brute(height):
    n = len(height)
    maximum = 0

    for i in range(n):
        for j in range(i + 1, n):
            area = min(height[i], height[j]) * (j - i)
            maximum = max(maximum, area)

    return maximum


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Skip Smaller Heights)
# ─────────────────────────────────────────────
"""
Idea:
For every left index, expand the right pointer.
Skip calculations when the right height cannot improve
the current minimum height.

Although some unnecessary computations are avoided,
the worst-case complexity is still O(n²).

Time  : O(n²)
Space : O(1)
"""

def max_area_better(height):
    n = len(height)
    maximum = 0

    for left in range(n):

        max_right_height = 0

        for right in range(n - 1, left, -1):

            if height[right] <= max_right_height:
                continue

            max_right_height = height[right]

            area = min(height[left], height[right]) * (right - left)
            maximum = max(maximum, area)

    return maximum


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Two Pointers)
# ─────────────────────────────────────────────
"""
Observation:

Area depends on:

1. Width
2. Smaller height

Initially use the maximum width.

If we move the taller line,
the width decreases but the smaller height
does not improve.

So always move the pointer pointing to
the smaller height.

Example:

height = [1,8,6,2,5,4,8,3,7]

L                              R
1 8 6 2 5 4 8 3 7

Area = min(1,7) × 8 = 8

Move left pointer because 1 < 7.

Continue until pointers meet.

Time  : O(n)
Space : O(1)

This is the expected interview / LeetCode solution.
"""

def max_area_optimal(height):
    left = 0
    right = len(height) - 1
    maximum = 0

    while left < right:

        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height

        maximum = max(maximum, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maximum


# ─────────────────────────────────────────────
if __name__ == "__main__":

    height = [1,8,6,2,5,4,8,3,7]

    print(max_area_brute(height))
    print(max_area_better(height))
    print(max_area_optimal(height))