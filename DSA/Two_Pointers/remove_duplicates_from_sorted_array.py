"""
REMOVE DUPLICATES FROM SORTED ARRAY
-----------------------------------
Given an integer array `nums` sorted in non-decreasing order,
remove the duplicates in-place such that each unique element
appears only once.

Return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique
elements in their original order.

Example:
Input : nums = [1,1,2]
Output: k = 2
nums = [1,2,_]

Example:
Input : nums = [0,0,1,1,1,2,2,3,3,4]
Output: k = 5
nums = [0,1,2,3,4,_,_,_,_,_]

Explanation:
The array is modified in-place.
Anything beyond the first `k` elements is ignored.
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Store all unique elements in a separate list,
then copy them back into the original array.

Time  : O(n)
Space : O(n)
"""

def remove_duplicates_brute(nums):
    if not nums:
        return 0

    unique = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] != unique[-1]:
            unique.append(nums[i])

    for i in range(len(unique)):
        nums[i] = unique[i]

    return len(unique)


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Using Set)
# ─────────────────────────────────────────────
"""
Store unique elements using a set,
sort them again, then overwrite the array.

Although correct, this approach is NOT suitable
because it uses extra space and sorting.

Time  : O(n log n)
Space : O(n)
"""

def remove_duplicates_better(nums):
    unique = sorted(set(nums))

    for i in range(len(unique)):
        nums[i] = unique[i]

    return len(unique)


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Two Pointers)
# ─────────────────────────────────────────────
"""
Observation:
Since the array is already sorted,
all duplicates are adjacent.

Maintain two pointers:

read  -> scans every element
write -> points to the next unique position

Whenever a new unique element is found,
copy it to the write position.

Example:

nums = [0,0,1,1,2,2,3]

Initial:
W
R
[0,0,1,1,2,2,3]

Duplicate (0):
Move read

New unique (1):
Write at index 1

[0,1,1,1,2,2,3]
    W
      R

Continue...

Final:
[0,1,2,3,...]

Return write index as k.

Time  : O(n)
Space : O(1)

This is the expected interview / LeetCode solution.
"""

def remove_duplicates_optimal(nums):
    if not nums:
        return 0

    write = 1

    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1

    return write


# ─────────────────────────────────────────────
if __name__ == "__main__":
    nums1 = [1,1,2]
    nums2 = [1,1,2]
    nums3 = [1,1,2]

    k = remove_duplicates_brute(nums1)
    print(k, nums1[:k])

    k = remove_duplicates_better(nums2)
    print(k, nums2[:k])

    k = remove_duplicates_optimal(nums3)
    print(k, nums3[:k])