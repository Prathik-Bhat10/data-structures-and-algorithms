"""
PRODUCT OF ARRAY EXCEPT SELF
------------------------------
Given an array `nums`, return an array `answer` where answer[i]
equals the product of all elements except nums[i].

Constraints:
- Must run in O(n) time.
- Division operator is NOT allowed.

Example:
Input : nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
For each index i, multiply all elements except nums[i].

Time  : O(n²)
Space : O(1) extra  (output array excluded)
"""

def product_except_self_brute(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)
    return result


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Prefix + Suffix Arrays)
# ─────────────────────────────────────────────
"""
answer[i] = (product of all elements LEFT of i)
          × (product of all elements RIGHT of i)

Build two separate arrays for prefix and suffix products.

Time  : O(n)
Space : O(n) extra
"""

def product_except_self_better(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n

    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    return [prefix[i] * suffix[i] for i in range(n)]


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (In-place Prefix × Suffix)
# ─────────────────────────────────────────────
"""
Same idea as above but uses the output array itself for prefix,
then multiplies suffix in a second pass with a running variable.

Trace (nums = [1, 2, 3, 4]):
  After prefix pass : result = [1,  1,  2,  6 ]
  After suffix pass : result = [24, 12, 8,  6 ] ✓

Time  : O(n)
Space : O(1) extra  (output array excluded)
"""

def product_except_self_optimal(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


# ─────────────────────────────────────────────
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(product_except_self_brute(nums))    # [24, 12, 8, 6]
    print(product_except_self_better(nums))   # [24, 12, 8, 6]
    print(product_except_self_optimal(nums))  # [24, 12, 8, 6]