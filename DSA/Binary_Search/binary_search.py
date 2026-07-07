"""
BINARY SEARCH
-------------
Given a sorted integer array `nums` and an integer `target`,
return the index of `target` if it exists. Otherwise, return -1.

Example:
Input : nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4

Input : nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (Linear Search)
# ─────────────────────────────────────────────
"""
Traverse the array from left to right and compare each
element with the target.

Time  : O(n)
Space : O(1)
"""

def binary_search_brute(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


# ─────────────────────────────────────────────
# APPROACH 2 — ITERATIVE BINARY SEARCH (Optimal)
# ─────────────────────────────────────────────
"""
Since the array is sorted, repeatedly divide the search
space into half until the target is found or the search
space becomes empty.

Time  : O(log n)
Space : O(1)
"""

def binary_search_iterative(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ─────────────────────────────────────────────
# APPROACH 3 — RECURSIVE BINARY SEARCH
# ─────────────────────────────────────────────
"""
Recursively search the left or right half depending on
the middle element.

Time  : O(log n)
Space : O(log n)   (Recursion stack)
"""

def binary_search_recursive(nums, target):

    def search(left, right):
        if left > right:
            return -1

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return search(mid + 1, right)
        else:
            return search(left, mid - 1)

    return search(0, len(nums) - 1)


# ─────────────────────────────────────────────
if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]

    print(binary_search_brute(nums, 9))         # 4
    print(binary_search_iterative(nums, 2))     # -1
    print(binary_search_recursive(nums, 5))     # 3