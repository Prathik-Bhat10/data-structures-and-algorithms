"""
CONTAINS DUPLICATE
-------------------
Given an integer array `nums`, return True if any value appears
at least twice, and False if every element is distinct.

Example:
Input : nums = [1, 2, 3, 1]
Output: True

Input : nums = [1, 2, 3, 4]
Output: False
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Compare every pair of elements.

Time  : O(n²)
Space : O(1)
"""

def contains_duplicate_brute(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Sorting)
# ─────────────────────────────────────────────
"""
Sort the array — duplicates will land next to each other.

Time  : O(n log n)
Space : O(1)
"""

def contains_duplicate_sort(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Hash Set)
# ─────────────────────────────────────────────
"""
Use a set to track seen numbers. Return True the moment
a number appears that is already in the set.

Time  : O(n)
Space : O(n)
"""

def contains_duplicate_optimal(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# ─────────────────────────────────────────────
if __name__ == "__main__":
    print(contains_duplicate_brute([1, 2, 3, 1]))     # True
    print(contains_duplicate_sort([1, 2, 3, 4]))      # False
    print(contains_duplicate_optimal([1, 2, 3, 1]))   # True