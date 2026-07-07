"""
TWO SUM II — INPUT ARRAY IS SORTED
----------------------------------
Given a 1-indexed array `numbers` that is already sorted in
non-decreasing order, find two numbers such that they add up
to a given target.

Return the indices (1-indexed) of the two numbers.

Constraints:
- Exactly one valid solution exists.
- You may not use the same element twice.
- Use only constant extra space.

Example:
Input :
numbers = [2, 7, 11, 15]
target = 9

Output:
[1, 2]

Explanation:
numbers[0] + numbers[1] = 2 + 7 = 9
Return their 1-based indices: [1, 2]
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Check every possible pair.

For each element, compare it with every element after it.

Time  : O(n²)
Space : O(1)
"""

def two_sum_brute(numbers, target):
    n = len(numbers)

    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Binary Search)
# ─────────────────────────────────────────────
"""
Idea:
Since the array is sorted,
for every element search for

target - current_element

using Binary Search.

Example:
numbers = [2, 7, 11, 15]
target = 9

Current = 2
Need = 7

Binary Search finds 7.

Answer = [1, 2]

Time  : O(n log n)
Space : O(1)
"""

def two_sum_better(numbers, target):
    n = len(numbers)

    for i in range(n):
        need = target - numbers[i]

        left = i + 1
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if numbers[mid] == need:
                return [i + 1, mid + 1]

            elif numbers[mid] < need:
                left = mid + 1

            else:
                right = mid - 1


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Two Pointers)
# ─────────────────────────────────────────────
"""
Observation:
Since the array is already sorted,

- If the current sum is too small,
  move the left pointer to increase the sum.

- If the current sum is too large,
  move the right pointer to decrease the sum.

Example:
numbers = [2, 7, 11, 15]
target = 9

        L          R
    [2, 7, 11, 15]

2 + 15 = 17 > 9
Move R

        L      R
    [2, 7, 11, 15]

2 + 11 = 13 > 9
Move R

        L  R
    [2, 7, 11, 15]

2 + 7 = 9
Found!

Return:
[1, 2]

Time  : O(n)
Space : O(1)

This is the expected interview / LeetCode solution.
"""

def two_sum_optimal(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]

        elif current_sum < target:
            left += 1

        else:
            right -= 1


# ─────────────────────────────────────────────
if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9

    print(two_sum_brute(numbers, target))
    print(two_sum_better(numbers, target))
    print(two_sum_optimal(numbers, target))