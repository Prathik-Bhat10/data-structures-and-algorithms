"""
3SUM
-----
Given an integer array `nums`, return all the unique triplets
[nums[i], nums[j], nums[k]] such that:

nums[i] + nums[j] + nums[k] == 0

The solution set must NOT contain duplicate triplets.

Example:
Input : nums = [-1,0,1,2,-1,-4]
Output:
[
    [-1,-1,2],
    [-1,0,1]
]
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Check every possible triplet.

Use a set to avoid duplicate triplets.

Time  : O(n³)
Space : O(k)
(k = number of unique triplets)
"""

def three_sum_brute(nums):
    n = len(nums)
    result = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)

    return [list(t) for t in result]


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (HashSet)
# ─────────────────────────────────────────────
"""
Fix one element.

For the remaining array, solve Two Sum using a hash set.

Duplicate triplets are removed using a set.

Example:

nums = [-1,0,1,2,-1,-4]

Fix -1

Need target = 1

seen = {}

0 -> seen
1 -> found because 0 + 1 = 1

Triplet = [-1,0,1]

Time  : O(n²)
Space : O(n)
"""

def three_sum_better(nums):
    n = len(nums)
    result = set()

    for i in range(n):
        seen = set()

        for j in range(i + 1, n):
            third = -(nums[i] + nums[j])

            if third in seen:
                triplet = tuple(sorted([nums[i], nums[j], third]))
                result.add(triplet)

            seen.add(nums[j])

    return [list(t) for t in result]


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Sorting + Two Pointers)
# ─────────────────────────────────────────────
"""
Sort the array first.

Fix one number.

Use two pointers to find the remaining two numbers.

Skip duplicates:
- Skip duplicate first elements.
- Skip duplicate left values.
- Skip duplicate right values.

Example:

nums = [-4,-1,-1,0,1,2]

Fix -1

left = -1
right = 2

sum = 0

Triplet found:
[-1,-1,2]

Move both pointers while skipping duplicates.

Time  : O(n²)
Space : O(1) extra
"""

def three_sum_optimal(nums):
    nums.sort()
    n = len(nums)

    result = []

    for i in range(n - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:

            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1

            elif total > 0:
                right -= 1

            else:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result


# ─────────────────────────────────────────────
if __name__ == "__main__":

    nums = [-1, 0, 1, 2, -1, -4]

    print(three_sum_brute(nums))
    print(three_sum_better(nums))
    print(three_sum_optimal(nums))