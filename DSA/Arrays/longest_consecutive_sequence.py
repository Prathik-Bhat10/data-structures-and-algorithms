"""
LONGEST CONSECUTIVE SEQUENCE
------------------------------
Given an unsorted integer array `nums`, return the length of the
longest sequence of consecutive integers.

Must run in O(n) time.

Example:
Input : nums = [100, 4, 200, 1, 3, 2]
Output: 4   # sequence [1, 2, 3, 4]
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
For each number, keep incrementing by 1 and check if next
exists in the array (using a set for O(1) lookup per check).

Time  : O(n²) in the worst case
Space : O(n)
"""

def longest_consecutive_brute(nums):
    num_set = set(nums)
    best = 0

    for num in nums:
        length = 1
        while num + length in num_set:
            length += 1
        best = max(best, length)

    return best


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Sorting)
# ─────────────────────────────────────────────
"""
Sort the array, then count consecutive runs.
Skip duplicates.

Time  : O(n log n)
Space : O(1)
"""

def longest_consecutive_sort(nums):
    if not nums:
        return 0
    nums.sort()
    best = 1
    current = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue                         # skip duplicate
        if nums[i] == nums[i - 1] + 1:
            current += 1
            best = max(best, current)
        else:
            current = 1

    return best


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Hash Set + Sequence Start)
# ─────────────────────────────────────────────
"""
Only start counting a sequence from its true beginning —
a number n where (n-1) is NOT in the set.
This ensures each number is visited at most twice overall.

Trace (nums = [100, 4, 200, 1, 3, 2]):
  set = {1, 2, 3, 4, 100, 200}
  100 → 99 not in set → count: 100 → length 1
    1 → 0  not in set → count: 1,2,3,4 → length 4  ← best
  200 → 199 not in set → count: 200 → length 1

Time  : O(n)
Space : O(n)
"""

def longest_consecutive_optimal(nums):
    num_set = set(nums)
    best = 0

    for num in num_set:
        if num - 1 not in num_set:           # sequence start
            length = 1
            while num + length in num_set:
                length += 1
            best = max(best, length)

    return best


# ─────────────────────────────────────────────
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive_brute(nums))    # 4
    print(longest_consecutive_sort(nums))     # 4
    print(longest_consecutive_optimal(nums))  # 4