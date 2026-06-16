"""
TRAPPING RAIN WATER
--------------------
Given an array `height` where height[i] is the height of a bar,
compute how much water can be trapped between the bars after raining.

Water above position i = min(max_left, max_right) - height[i]

Example:
Input : height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Visualization:
       |
   |   ||  |
_|_|__|_||||_|

trapped water fills the valleys.
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
For each bar i, find the max height to its left and to its right.
Water at i = min(left_max, right_max) - height[i].

Time  : O(n²)
Space : O(1)
"""

def trap_brute(height):
    n = len(height)
    total = 0

    for i in range(n):
        left_max = max(height[:i + 1])
        right_max = max(height[i:])
        total += min(left_max, right_max) - height[i]

    return total


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Prefix/Suffix Max Arrays)
# ─────────────────────────────────────────────
"""
Precompute left_max[i] and right_max[i] arrays,
then compute water in one final pass.

Trace (height = [0,1,0,2,1,0,1,3,2,1,2,1]):
  left_max  = [0,1,1,2,2,2,2,3,3,3,3,3]
  right_max = [3,3,3,3,3,3,3,3,2,2,2,1]
  water[i]  = min(L,R) - h[i]
  sum       = 6 ✓

Time  : O(n)
Space : O(n)
"""

def trap_better(height):
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    total = 0
    for i in range(n):
        total += min(left_max[i], right_max[i]) - height[i]

    return total


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Two Pointers)
# ─────────────────────────────────────────────
"""
Use two pointers (left, right) moving inward.
The side with the smaller max height is the bottleneck —
process that side and move its pointer inward.

Key insight: if left_max < right_max, the water at `left`
is determined by left_max (right side is guaranteed taller).

Time  : O(n)
Space : O(1)
"""

def trap_optimal(height):
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    total = 0

    while left < right:
        if height[left] <= height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total += right_max - height[right]
            right -= 1

    return total


# ─────────────────────────────────────────────
if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap_brute(height))    # 6
    print(trap_better(height))   # 6
    print(trap_optimal(height))  # 6