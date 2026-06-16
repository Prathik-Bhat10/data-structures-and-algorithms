"""
NEXT PERMUTATION
-----------------
Given an array of integers `nums`, rearrange it into the
lexicographically next greater permutation of its elements.

If no such permutation exists (array is descending), rearrange
into the lowest order (ascending). Must be done in-place with O(1) space.

Example:
Input : [1, 2, 3] → Output: [1, 3, 2]
Input : [3, 2, 1] → Output: [1, 2, 3]  (wrap around)
Input : [1, 1, 5] → Output: [1, 5, 1]
"""
from itertools import permutations

# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Generate all permutations in sorted order and return the one
right after the current. Very slow and impractical for large input.

Time  : O(n! × n)
Space : O(n!)
"""



def next_permutation_brute(nums):
    perms = sorted(set(permutations(nums)))
    current = tuple(nums)
    idx = perms.index(current)
    next_perm = perms[(idx + 1) % len(perms)]
    for i in range(len(nums)):
        nums[i] = next_perm[i]


# ─────────────────────────────────────────────
# APPROACH 2 — OPTIMAL (Single Pass)
# ─────────────────────────────────────────────
"""
Algorithm (finding the next permutation directly):

Step 1 — Find the "pivot":
  Scan from right to left. Find the first index i where
  nums[i] < nums[i+1]. This is the drop point.

Step 2 — Find the swap target:
  Scan from right to left again. Find the first index j where
  nums[j] > nums[i]. Swap nums[i] and nums[j].

Step 3 — Reverse the suffix:
  Reverse everything after index i. This turns the descending
  suffix into the smallest possible ascending order.

If no pivot found (entire array is descending), reverse all → smallest permutation.

Trace (nums = [1, 2, 3]):
  Step 1: i=1  (nums[1]=2 < nums[2]=3)
  Step 2: j=2  (nums[2]=3 > nums[1]=2) → swap → [1, 3, 2]
  Step 3: reverse after i=1 → [1, 3, 2]  ✓

Trace (nums = [1, 3, 2]):
  Step 1: i=0  (nums[0]=1 < nums[1]=3)
  Step 2: j=2  (nums[2]=2 > nums[0]=1) → swap → [2, 3, 1]
  Step 3: reverse after i=0 → [2, 1, 3]  ✓

Time  : O(n)
Space : O(1)
"""

def next_permutation_optimal(nums):
    n = len(nums)
    i = n - 2

    # Step 1: find pivot (first descending element from the right)
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: find rightmost element greater than pivot
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: reverse the suffix after pivot
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# ─────────────────────────────────────────────
if __name__ == "__main__":
    def test(fn, nums):
        arr = nums[:]
        fn(arr)
        return arr

    print(test(next_permutation_brute,   [1, 2, 3]))  # [1, 3, 2]
    print(test(next_permutation_optimal, [1, 2, 3]))  # [1, 3, 2]

    print(test(next_permutation_brute,   [3, 2, 1]))  # [1, 2, 3]
    print(test(next_permutation_optimal, [3, 2, 1]))  # [1, 2, 3]

    print(test(next_permutation_brute,   [1, 1, 5]))  # [1, 5, 1]
    print(test(next_permutation_optimal, [1, 1, 5]))  # [1, 5, 1]