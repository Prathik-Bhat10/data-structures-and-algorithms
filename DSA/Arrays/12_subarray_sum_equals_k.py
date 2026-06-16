"""
SUBARRAY SUM EQUALS K
----------------------
Given an integer array `nums` and an integer `k`,
return the total number of subarrays whose sum equals k.

Example:
Input : nums = [1, 1, 1], k = 2
Output: 2   # [1,1] at index (0,1) and (1,2)

Input : nums = [1, 2, 3], k = 3
Output: 2   # [3] and [1,2]
"""

from collections import defaultdict

# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Try every subarray [i..j] and compute its sum.

Time  : O(n²)
Space : O(1)
"""

def subarray_sum_brute(nums, k):
    count = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                count += 1
    return count


# ─────────────────────────────────────────────
# APPROACH 2 — OPTIMAL (Prefix Sum + Hash Map)
# ─────────────────────────────────────────────
"""
Key insight:
  If prefix_sum[j] - prefix_sum[i] == k
  then subarray (i+1 .. j) sums to k.

  Rearranged: prefix_sum[i] == prefix_sum[j] - k

Use a hash map to count how many times each prefix sum has
appeared. For each new prefix sum, check if (current - k)
exists in the map — each occurrence is a valid subarray.

Trace (nums = [1, 1, 1], k = 2):
  map = {0: 1}      ← empty prefix sum
  i=0 prefix=1  → (1-2)=-1 not in map → map={0:1, 1:1}
  i=1 prefix=2  → (2-2)= 0 in map (×1) → count=1  map={0:1,1:1,2:1}
  i=2 prefix=3  → (3-2)= 1 in map (×1) → count=2  ✓

Time  : O(n)
Space : O(n)
"""



def subarray_sum_optimal(nums, k):
    prefix_count = defaultdict(int)
    prefix_count[0] = 1        # empty prefix
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num
        count += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] += 1

    return count


# ─────────────────────────────────────────────
if __name__ == "__main__":
    print(subarray_sum_brute([1, 1, 1], 2))    # 2
    print(subarray_sum_optimal([1, 1, 1], 2))  # 2

    print(subarray_sum_brute([1, 2, 3], 3))    # 2
    print(subarray_sum_optimal([1, 2, 3], 3))  # 2