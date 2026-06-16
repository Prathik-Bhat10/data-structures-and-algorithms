"""
SORT COLORS (Dutch National Flag Problem)
------------------------------------------
Given an array `nums` with values 0, 1, and 2 (representing
red, white, and blue), sort them in-place so all 0s come first,
then 1s, then 2s.

Must solve in one pass using O(1) space.

Example:
Input : nums = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (Built-in Sort)
# ─────────────────────────────────────────────
"""
Use Python's built-in sort. Works but doesn't exploit the fact
that there are only 3 distinct values.

Time  : O(n log n)
Space : O(1)
"""

def sort_colors_brute(nums):
    nums.sort()


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Counting Sort)
# ─────────────────────────────────────────────
"""
Count occurrences of 0, 1, and 2, then overwrite the array.
Two passes but simple to understand.

Time  : O(n)
Space : O(1)
"""

def sort_colors_better(nums):
    count = [0, 0, 0]
    for num in nums:
        count[num] += 1

    idx = 0
    for val in range(3):
        for _ in range(count[val]):
            nums[idx] = val
            idx += 1


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Dutch National Flag / Three Pointers)
# ─────────────────────────────────────────────
"""
Maintain three pointers:
  low  → boundary of 0s (everything left of low is 0)
  mid  → current element being examined
  high → boundary of 2s (everything right of high is 2)

Rules:
  nums[mid] == 0 → swap with low,  move both low and mid forward
  nums[mid] == 1 → mid is in place, just move mid forward
  nums[mid] == 2 → swap with high, move high backward (re-examine mid)

Trace (nums = [2, 0, 2, 1, 1, 0]):
  low=0 mid=0 high=5 → nums[0]=2 → swap(0,5) → [0,0,2,1,1,2] high=4
  low=0 mid=0 high=4 → nums[0]=0 → swap(0,0) → low=1 mid=1
  low=1 mid=1 high=4 → nums[1]=0 → swap(1,1) → low=2 mid=2
  low=2 mid=2 high=4 → nums[2]=2 → swap(2,4) → [0,0,1,1,2,2] high=3
  low=2 mid=2 high=3 → nums[2]=1 → mid=3
  low=2 mid=3 high=3 → nums[3]=1 → mid=4
  mid > high → done → [0, 0, 1, 1, 2, 2] ✓

Time  : O(n)
Space : O(1)
"""

def sort_colors_optimal(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:                                   # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# ─────────────────────────────────────────────
if __name__ == "__main__":
    def test(fn, nums):
        arr = nums[:]
        fn(arr)
        return arr

    print(test(sort_colors_brute,   [2, 0, 2, 1, 1, 0]))  # [0,0,1,1,2,2]
    print(test(sort_colors_better,  [2, 0, 2, 1, 1, 0]))  # [0,0,1,1,2,2]
    print(test(sort_colors_optimal, [2, 0, 2, 1, 1, 0]))  # [0,0,1,1,2,2]