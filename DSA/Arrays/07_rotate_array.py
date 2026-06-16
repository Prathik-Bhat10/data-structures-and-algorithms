"""
ROTATE ARRAY
-------------
Given an integer array `nums`, rotate it to the right by `k` steps.

Example:
Input : nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]

Explanation:
  rotate 1 step  → [7, 1, 2, 3, 4, 5, 6]
  rotate 2 steps → [6, 7, 1, 2, 3, 4, 5]
  rotate 3 steps → [5, 6, 7, 1, 2, 3, 4]
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (Rotate one step at a time)
# ─────────────────────────────────────────────
"""
Rotate the array by 1 step, k times.
Each step: save the last element, shift everyone right, put last at front.

Time  : O(n × k)
Space : O(1)
"""

def rotate_brute(nums, k):
    n = len(nums)
    k = k % n
    for _ in range(k):
        last = nums[-1]
        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]
        nums[0] = last


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Extra Array)
# ─────────────────────────────────────────────
"""
Place each element directly at its final position
(i + k) % n in a new array, then copy back.

Time  : O(n)
Space : O(n)
"""

def rotate_better(nums, k):
    n = len(nums)
    k = k % n
    result = [0] * n
    for i in range(n):
        result[(i + k) % n] = nums[i]
    for i in range(n):
        nums[i] = result[i]


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Three Reversals)
# ─────────────────────────────────────────────
"""
Rotating right by k is equivalent to:
  1. Reverse the entire array.
  2. Reverse the first k elements.
  3. Reverse the remaining n-k elements.

Trace (nums = [1,2,3,4,5,6,7], k=3):
  Reverse all       → [7, 6, 5, 4, 3, 2, 1]
  Reverse first 3   → [5, 6, 7, 4, 3, 2, 1]
  Reverse last 4    → [5, 6, 7, 1, 2, 3, 4] ✓

Time  : O(n)
Space : O(1)
"""

def rotate_optimal(nums, k):
    n = len(nums)
    k = k % n

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, n - 1)      # step 1: reverse all
    reverse(0, k - 1)      # step 2: reverse first k
    reverse(k, n - 1)      # step 3: reverse rest


# ─────────────────────────────────────────────
if __name__ == "__main__":
    def test(fn, nums, k):
        arr = nums[:]
        fn(arr, k)
        return arr

    print(test(rotate_brute,   [1,2,3,4,5,6,7], 3))   # [5,6,7,1,2,3,4]
    print(test(rotate_better,  [1,2,3,4,5,6,7], 3))   # [5,6,7,1,2,3,4]
    print(test(rotate_optimal, [1,2,3,4,5,6,7], 3))   # [5,6,7,1,2,3,4]