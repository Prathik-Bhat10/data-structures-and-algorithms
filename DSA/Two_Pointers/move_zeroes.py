"""
MOVE ZEROES
-----------
Given an integer array `nums`, move all 0's to the end while
maintaining the relative order of the non-zero elements.

The operation must be done IN-PLACE.

Example:
Input : nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (Extra Array)
# ─────────────────────────────────────────────
"""
Create a new array.

1. Store all non-zero elements.
2. Append zeros until the size becomes n.
3. Copy back to the original array.

Time  : O(n)
Space : O(n)
"""

def move_zeroes_brute(nums):
    temp = []

    for num in nums:
        if num != 0:
            temp.append(num)

    while len(temp) < len(nums):
        temp.append(0)

    for i in range(len(nums)):
        nums[i] = temp[i]


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Two Pass In-place)
# ─────────────────────────────────────────────
"""
Idea:
1. Copy every non-zero element to the front.
2. Fill the remaining positions with zeros.

Example:
nums = [0,1,0,3,12]

After copying:
[1,3,12,3,12]

Fill remaining with zeros:
[1,3,12,0,0]

Time  : O(n)
Space : O(1)
"""

def move_zeroes_better(nums):
    insert = 0

    for num in nums:
        if num != 0:
            nums[insert] = num
            insert += 1

    while insert < len(nums):
        nums[insert] = 0
        insert += 1


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Two Pointers + Swapping)
# ─────────────────────────────────────────────
"""
Maintain two pointers:

left  -> position where the next non-zero should go.
right -> scans the array.

Whenever nums[right] is non-zero:
    swap(nums[left], nums[right])
    left += 1

Example:
nums = [0,1,0,3,12]

Initial:
left = 0

right = 0 -> 0 (skip)

right = 1 -> 1
swap(0,1)
[1,0,0,3,12]
left = 1

right = 2 -> 0 (skip)

right = 3 -> 3
swap(1,3)
[1,3,0,0,12]
left = 2

right = 4 -> 12
swap(2,4)
[1,3,12,0,0]

Time  : O(n)
Space : O(1)

This is the expected interview / LeetCode solution because:
- Runs in one traversal.
- Performs the operation in-place.
- Maintains the relative order of non-zero elements.
"""

def move_zeroes_optimal(nums):
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1


# ─────────────────────────────────────────────
if __name__ == "__main__":
    nums1 = [0, 1, 0, 3, 12]
    move_zeroes_brute(nums1)
    print(nums1)

    nums2 = [0, 1, 0, 3, 12]
    move_zeroes_better(nums2)
    print(nums2)

    nums3 = [0, 1, 0, 3, 12]
    move_zeroes_optimal(nums3)
    print(nums3)