"""
4SUM
-----
Given an integer array `nums` and an integer `target`,
return all unique quadruplets

    [nums[a], nums[b], nums[c], nums[d]]

such that:

- a, b, c, and d are distinct indices.
- nums[a] + nums[b] + nums[c] + nums[d] == target.

The solution set must not contain duplicate quadruplets.

Example:
Input :
nums = [1,0,-1,0,-2,2]
target = 0

Output:
[
    [-2,-1,1,2],
    [-2,0,0,2],
    [-1,0,0,1]
]
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Try every possible combination of four numbers.

For every quadruplet:
1. Check if the sum equals target.
2. Sort the quadruplet before inserting into a set
   to avoid duplicates.

Time  : O(n⁴)
Space : O(number of unique quadruplets)
"""

def four_sum_brute(nums, target):
    n = len(nums)
    result = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for m in range(k + 1, n):

                                if nums[i] + nums[j] + nums[k] + nums[m] == target:
                                    quad = tuple(sorted([
                                        nums[i],
                                        nums[j],
                                        nums[k],
                                        nums[m]
                                    ]))
                                    result.add(quad)

    return [list(x) for x in result]


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Hash Set)
# ─────────────────────────────────────────────
"""
Fix the first two numbers.

For the remaining array:
Use a hash set to find the fourth number.

Need:
target - (nums[i] + nums[j] + nums[k])

Store unique quadruplets in a set.

Time  : O(n³)
Space : O(n)
"""

def four_sum_better(nums, target):
    nums.sort()
    n = len(nums)
    result = set()

    for i in range(n):

        for j in range(i + 1, n):

            seen = set()

            for k in range(j + 1, n):

                need = target - (
                    nums[i] +
                    nums[j] +
                    nums[k]
                )

                if need in seen:
                    result.add((
                        nums[i],
                        nums[j],
                        need,
                        nums[k]
                    ))

                seen.add(nums[k])

    return [list(x) for x in result]


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Sorting + Two Pointers)
# ─────────────────────────────────────────────
"""
Idea:

1. Sort the array.
2. Fix the first number (i).
3. Fix the second number (j).
4. Solve the remaining problem using
   two pointers.

Duplicate values are skipped to avoid
duplicate quadruplets.

Example:

nums =
[1,0,-1,0,-2,2]

Sorted:
[-2,-1,0,0,1,2]

Fix:
i = -2
j = -1

Remaining:
0 0 1 2

Use two pointers to search.

Time  : O(n³)
Space : O(1) extra
(ignoring output list)

This is the expected interview / LeetCode solution.
"""

def four_sum_optimal(nums, target):
    nums.sort()
    n = len(nums)

    result = []

    for i in range(n - 3):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):

            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:

                total = (
                    nums[i] +
                    nums[j] +
                    nums[left] +
                    nums[right]
                )

                if total == target:

                    result.append([
                        nums[i],
                        nums[j],
                        nums[left],
                        nums[right]
                    ])

                    left += 1
                    right -= 1

                    while (
                        left < right and
                        nums[left] == nums[left - 1]
                    ):
                        left += 1

                    while (
                        left < right and
                        nums[right] == nums[right + 1]
                    ):
                        right -= 1

                elif total < target:
                    left += 1

                else:
                    right -= 1

    return result


# ─────────────────────────────────────────────
if __name__ == "__main__":

    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    print(four_sum_brute(nums, target))
    print(four_sum_better(nums, target))
    print(four_sum_optimal(nums, target))