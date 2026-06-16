"""
MAXIMUM SUBARRAY (Kadane's Algorithm)
--------------------------------------
Given an integer array `nums`, find the contiguous subarray
with the largest sum and return that sum.

Example:
Input : nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6   # subarray [4, -1, 2, 1]
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Try every possible subarray [i..j] and track maximum sum.

Time  : O(n²)
Space : O(1)
"""

def max_subarray_brute(nums):
    max_sum = float('-inf')
    n = len(nums)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
    return max_sum


# ─────────────────────────────────────────────
# APPROACH 2 — OPTIMAL (Kadane's Algorithm)
# ─────────────────────────────────────────────
"""
At each element decide: extend the current subarray or start fresh.
A negative running sum only hurts future subarrays — reset it.

Trace (nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]):
  num=-2 → cur=-2  max=-2
  num= 1 → cur= 1  max= 1   (restart: 1 > -2+1)
  num=-3 → cur=-2  max= 1
  num= 4 → cur= 4  max= 4   (restart: 4 > -2+4)
  num=-1 → cur= 3  max= 4
  num= 2 → cur= 5  max= 5
  num= 1 → cur= 6  max= 6   ← answer
  num=-5 → cur= 1  max= 6
  num= 4 → cur= 5  max= 6

Time  : O(n)
Space : O(1)
"""

def max_subarray_kadane(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# ─────────────────────────────────────────────
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray_brute(nums))   # 6
    print(max_subarray_kadane(nums))  # 6