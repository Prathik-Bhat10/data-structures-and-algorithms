"""
SQUARES OF A SORTED ARRAY
-------------------------
Given an integer array `nums` sorted in non-decreasing order,
return an array of the squares of each number, also sorted
in non-decreasing order.

Example:
Input : nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]

Explanation:
Squaring changes the order because negative numbers become positive.

[-4, -1, 0, 3, 10]
 ↓    ↓   ↓  ↓   ↓
16    1   0  9 100

Sorted result:
[0, 1, 9, 16, 100]
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Square every element and then sort the result.

Time  : O(n log n)
Space : O(n)
"""

def sorted_squares_brute(nums):
    result = []

    for num in nums:
        result.append(num * num)

    result.sort()

    return result


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Using Absolute Values)
# ─────────────────────────────────────────────
"""
Idea:
The largest square comes from the element having the largest
absolute value.

Steps:
1. Sort the array based on absolute values.
2. Square every element.

Example:
nums = [-4,-1,0,3,10]

Sorted by abs:
[0,-1,3,-4,10]

Squares:
[0,1,9,16,100]

Time  : O(n log n)
Space : O(n)
"""

def sorted_squares_better(nums):
    nums = sorted(nums, key=abs)

    return [num * num for num in nums]


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Two Pointers)
# ─────────────────────────────────────────────
"""
Observation:
Since the array is already sorted,
the largest square will always come from either:

- Leftmost negative number
- Rightmost positive number

Use two pointers.

Example:
nums = [-4,-1,0,3,10]

           L            R
        [-4,-1,0,3,10]

Compare:
|-4| = 4
|10| =10

100 is larger.

Place 100 at the end.

Repeat until pointers cross.

Time  : O(n)
Space : O(n)

This is the expected interview / LeetCode solution.
"""

def sorted_squares_optimal(nums):
    n = len(nums)
    result = [0] * n

    left = 0
    right = n - 1
    pos = n - 1

    while left <= right:
        left_square = nums[left] * nums[left]
        right_square = nums[right] * nums[right]

        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1

        pos -= 1

    return result


# ─────────────────────────────────────────────
if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]

    print(sorted_squares_brute(nums))
    print(sorted_squares_better(nums))
    print(sorted_squares_optimal(nums))