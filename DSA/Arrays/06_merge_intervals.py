"""
MERGE INTERVALS
----------------
Given an array of intervals where intervals[i] = [start, end],
merge all overlapping intervals and return the result.

Two intervals [a, b] and [c, d] overlap if c <= b.

Example:
Input : [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
  → [1,3] and [2,6] overlap → merged to [1,6]
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Repeatedly scan all pairs and merge any overlapping two
until no more merges are possible.

Time  : O(n²)
Space : O(n)
"""

def merge_intervals_brute(intervals):
    changed = True
    while changed:
        changed = False
        result = []
        used = [False] * len(intervals)
        for i in range(len(intervals)):
            if used[i]:
                continue
            curr = list(intervals[i])
            for j in range(i + 1, len(intervals)):
                if not used[j]:
                    a, b = curr
                    c, d = intervals[j]
                    if c <= b:                          # overlap
                        curr = [min(a, c), max(b, d)]
                        used[j] = True
                        changed = True
            result.append(curr)
        intervals = result
    return intervals


# ─────────────────────────────────────────────
# APPROACH 2 — OPTIMAL (Sort + Linear Scan)
# ─────────────────────────────────────────────
"""
1. Sort intervals by start time.
2. Walk through them. If current interval overlaps the last
   merged one (start <= last end), extend it. Otherwise append.

Trace ([[1,3],[2,6],[8,10],[15,18]]):
  sort   → [[1,3],[2,6],[8,10],[15,18]]
  [1,3]  → merged = [[1,3]]
  [2,6]  → 2 <= 3 → extend → merged = [[1,6]]
  [8,10] → 8 > 6  → append → merged = [[1,6],[8,10]]
  [15,18]→ 15 > 10 → append → merged = [[1,6],[8,10],[15,18]] ✓

Time  : O(n log n)
Space : O(n)
"""

def merge_intervals_optimal(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)   # extend
        else:
            merged.append([start, end])           # new interval

    return merged


# ─────────────────────────────────────────────
if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge_intervals_brute(intervals))    # [[1,6],[8,10],[15,18]]
    print(merge_intervals_optimal(intervals))  # [[1,6],[8,10],[15,18]]