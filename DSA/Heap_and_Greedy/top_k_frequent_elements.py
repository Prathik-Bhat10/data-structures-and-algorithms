"""
TOP K FREQUENT ELEMENTS
-----------------------
Given an integer array `nums` and an integer `k`,
return the `k` most frequent elements.

You may return the answer in any order.

Example:
Input : nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input : nums = [1], k = 1
Output: [1]
"""

from collections import Counter
import heapq


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Count frequencies manually, then repeatedly find
the highest-frequency element.

Time  : O(n²)
Space : O(n)
"""

def top_k_frequent_brute(nums, k):
    freq = {}

    # Count frequencies
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    result = []

    for _ in range(k):
        max_key = None
        max_freq = -1

        for key, value in freq.items():
            if value > max_freq:
                max_freq = value
                max_key = key

        result.append(max_key)
        del freq[max_key]

    return result


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Heap)
# ─────────────────────────────────────────────
"""
Count frequencies using a hash map and use a max heap
to extract the k most frequent elements.

Time  : O(n log n)
Space : O(n)
"""

def top_k_frequent_heap(nums, k):
    freq = Counter(nums)

    max_heap = [(-count, num) for num, count in freq.items()]
    heapq.heapify(max_heap)

    result = []

    for _ in range(k):
        _, num = heapq.heappop(max_heap)
        result.append(num)

    return result


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Bucket Sort)
# ─────────────────────────────────────────────
"""
Store numbers in buckets based on their frequency.
Traverse buckets from highest frequency to lowest
until k elements are collected.

Time  : O(n)
Space : O(n)
"""

def top_k_frequent_optimal(nums, k):
    freq = Counter(nums)

    buckets = [[] for _ in range(len(nums) + 1)]

    for num, count in freq.items():
        buckets[count].append(num)

    result = []

    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result


# ─────────────────────────────────────────────
if __name__ == "__main__":
    print(top_k_frequent_brute([1, 1, 1, 2, 2, 3], 2))      # [1, 2]
    print(top_k_frequent_heap([1, 1, 1, 2, 2, 3], 2))       # [1, 2]
    print(top_k_frequent_optimal([1, 1, 1, 2, 2, 3], 2))    # [1, 2]