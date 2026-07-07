"""
FIND THE DUPLICATE NUMBER
--------------------------
Given an array `nums` of n+1 integers where each integer is in [1, n],
there is exactly one repeated number. Find and return it.

Constraints:
- Must not modify the array.
- Must use only O(1) extra space.
- Only one duplicate, but it may appear more than twice.

Example:
Input : nums = [1, 3, 4, 2, 2]
Output: 2

Input : nums = [3, 1, 3, 4, 2]
Output: 3
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Compare every pair (i, j).

Time  : O(n²)
Space : O(1)
"""

def find_duplicate_brute(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return nums[i]


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Hash Set)
# ─────────────────────────────────────────────
"""
Track seen numbers. Return the first one seen twice.

Time  : O(n)
Space : O(n)
"""

def find_duplicate_better(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Floyd's Cycle Detection)
# ─────────────────────────────────────────────
"""
Treat the array as a linked list where index i points to nums[i].
A duplicate value means two indices point to the same node → cycle.

Phase 1 — Find intersection inside the cycle:
  Move slow by 1 step, fast by 2 steps until they meet.

Phase 2 — Find cycle entrance (= duplicate number):
  Reset one pointer to start. Move both by 1 step.
  They meet at the duplicate.

Trace (nums = [1, 3, 4, 2, 2]):
  Index:  0 → 1 → 3 → 2 → 4 → 2 (cycle at 2)
  Phase 1: slow=1,3,2,4,2  fast=3,2,2
           meet at 2
  Phase 2: p1=0 p2=2 → p1=1,p2=4 → p1=3,p2=2 → p1=2,p2=2 → meet at 2 ✓

Time  : O(n)
Space : O(1)
"""

def find_duplicate_optimal(nums):
    # Phase 1: find intersection
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: find entrance to cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


# ─────────────────────────────────────────────
if __name__ == "__main__":
    print(find_duplicate_brute([1, 3, 4, 2, 2]))    # 2
    print(find_duplicate_better([3, 1, 3, 4, 2]))   # 3
    print(find_duplicate_optimal([1, 3, 4, 2, 2]))  # 2