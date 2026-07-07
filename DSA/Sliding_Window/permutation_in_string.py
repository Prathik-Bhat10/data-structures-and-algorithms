"""
PERMUTATION IN STRING
---------------------
Given two strings `s1` and `s2`, return True if `s2`
contains a permutation of `s1`, otherwise return False.

A permutation is a rearrangement of all the characters.

Example:
Input : s1 = "ab", s2 = "eidbaooo"
Output: True

Input : s1 = "ab", s2 = "eidboaoo"
Output: False
"""

from collections import Counter


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Generate every substring of length len(s1),
sort it, and compare with the sorted s1.

Time  : O((n - m + 1) * m log m)
Space : O(m)

where:
m = len(s1)
n = len(s2)
"""

def check_inclusion_brute(s1, s2):
    m, n = len(s1), len(s2)

    if m > n:
        return False

    target = sorted(s1)

    for i in range(n - m + 1):
        if sorted(s2[i:i + m]) == target:
            return True

    return False


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Sliding Window + Counter)
# ─────────────────────────────────────────────
"""
Maintain a sliding window of size len(s1).
Compare the frequency Counter of the window
with the Counter of s1.

Time  : O(26 × n) ≈ O(n)
Space : O(26) ≈ O(1)
"""

def check_inclusion_better(s1, s2):
    m, n = len(s1), len(s2)

    if m > n:
        return False

    target = Counter(s1)
    window = Counter(s2[:m])

    if window == target:
        return True

    for i in range(m, n):
        window[s2[i]] += 1
        window[s2[i - m]] -= 1

        if window[s2[i - m]] == 0:
            del window[s2[i - m]]

        if window == target:
            return True

    return False


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Sliding Window + Frequency Array)
# ─────────────────────────────────────────────
"""
Use two frequency arrays of size 26.
Slide the window while updating counts.
If both frequency arrays match, a permutation exists.

Time  : O(n)
Space : O(1)
"""

def check_inclusion_optimal(s1, s2):
    m, n = len(s1), len(s2)

    if m > n:
        return False

    freq1 = [0] * 26
    freq2 = [0] * 26

    for i in range(m):
        freq1[ord(s1[i]) - ord('a')] += 1
        freq2[ord(s2[i]) - ord('a')] += 1

    if freq1 == freq2:
        return True

    for i in range(m, n):
        freq2[ord(s2[i]) - ord('a')] += 1
        freq2[ord(s2[i - m]) - ord('a')] -= 1

        if freq1 == freq2:
            return True

    return False


# ─────────────────────────────────────────────
if __name__ == "__main__":
    print(check_inclusion_brute("ab", "eidbaooo"))      # True
    print(check_inclusion_better("ab", "eidboaoo"))     # False
    print(check_inclusion_optimal("ab", "eidbaooo"))    # True