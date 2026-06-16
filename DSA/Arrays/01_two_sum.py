"""
TWO SUM
-------
Given an array of integers `nums` and a target integer,
return the indices of the two numbers that add up to target.

Constraints:
- Exactly one solution exists.
- Cannot use the same element twice.

Example:
Input : nums = [2, 7, 11, 15], target = 9
Output: [0, 1]   # nums[0] + nums[1] = 2 + 7 = 9
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Check every pair (i, j) where i < j.

Time  : O(n²)
Space : O(1)
"""

def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


# ─────────────────────────────────────────────
# APPROACH 2 — OPTIMAL (Hash Map)
# ─────────────────────────────────────────────
"""
For each number, check if its complement (target - num)
already exists in a hash map. Store each number → index
as you go.

Trace (nums = [2, 7, 11, 15], target = 9):
  i=0  num=2   complement=7   not in map → map={2:0}
  i=1  num=7   complement=2   found at 0 → return [0, 1] ✓

Time  : O(n)
Space : O(n)
"""

def two_sum_optimal(nums, target):
    seen = {}                          # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


# ─────────────────────────────────────────────
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum_brute(nums, target))    # [0, 1]
    print(two_sum_optimal(nums, target))  # [0, 1]