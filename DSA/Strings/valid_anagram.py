"""
VALID ANAGRAM
-------------
Given two strings `s` and `t`, return True if `t` is an
anagram of `s`, and False otherwise.

An Anagram is a word formed by rearranging the letters
of another word using all the original letters exactly once.

Example:
Input : s = "anagram", t = "nagaram"
Output: True

Input : s = "rat", t = "car"
Output: False
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
For every character in `s`, search for a matching unused
character in `t`.

Time  : O(n²)
Space : O(n)
"""

def is_anagram_brute(s, t):
    if len(s) != len(t):
        return False

    used = [False] * len(t)

    for ch in s:
        found = False
        for i in range(len(t)):
            if not used[i] and t[i] == ch:
                used[i] = True
                found = True
                break
        if not found:
            return False

    return True


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Sorting)
# ─────────────────────────────────────────────
"""
Sort both strings and compare them.

Time  : O(n log n)
Space : O(n)
"""

def is_anagram_sort(s, t):
    return sorted(s) == sorted(t)


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Hash Map)
# ─────────────────────────────────────────────
"""
Count the frequency of each character in both strings.
If all frequencies match, the strings are anagrams.

Time  : O(n)
Space : O(n)
"""

def is_anagram_optimal(s, t):
    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    return True


# ─────────────────────────────────────────────
if __name__ == "__main__":
    print(is_anagram_brute("anagram", "nagaram"))     # True
    print(is_anagram_sort("rat", "car"))              # False
    print(is_anagram_optimal("listen", "silent"))     # True