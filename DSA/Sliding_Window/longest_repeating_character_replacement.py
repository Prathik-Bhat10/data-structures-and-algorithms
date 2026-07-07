"""
LONGEST REPEATING CHARACTER REPLACEMENT
---------------------------------------
Given a string `s` and an integer `k`, you can replace at most
`k` characters with any uppercase English letter.

Return the length of the longest substring containing the same
letter after performing at most `k` replacements.

Example:
Input : s = "ABAB", k = 2
Output: 4

Input : s = "AABABBA", k = 1
Output: 4
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Generate every substring and check whether it can be converted
into a substring of identical characters.

A substring is valid if:
(length of substring - highest character frequency) <= k

Time  : O(n² * 26)
Space : O(26)
"""

def character_replacement_brute(s, k):
    n = len(s)
    answer = 0

    for i in range(n):
        freq = {}

        for j in range(i, n):
            freq[s[j]] = freq.get(s[j], 0) + 1
            max_freq = max(freq.values())

            if (j - i + 1) - max_freq <= k:
                answer = max(answer, j - i + 1)

    return answer


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Sliding Window)
# ─────────────────────────────────────────────
"""
Maintain a sliding window.

Keep shrinking the window until it becomes valid.
Recompute the maximum frequency whenever the window shrinks.

Time  : O(26 * n)
Space : O(26)
"""

def character_replacement_better(s, k):
    freq = {}
    left = 0
    answer = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while True:
            max_freq = max(freq.values())
            window_size = right - left + 1

            if window_size - max_freq <= k:
                break

            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        answer = max(answer, right - left + 1)

    return answer


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Sliding Window)
# ─────────────────────────────────────────────
"""
Keep track of the highest frequency seen so far instead of
recomputing it every time.

If:
(window size - max_frequency) > k

shrink the window.

Time  : O(n)
Space : O(26)
"""

def character_replacement_optimal(s, k):
    freq = {}
    left = 0
    max_freq = 0
    answer = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        max_freq = max(max_freq, freq[s[right]])

        while (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            left += 1

        answer = max(answer, right - left + 1)

    return answer


# ─────────────────────────────────────────────
if __name__ == "__main__":
    print(character_replacement_brute("ABAB", 2))          # 4
    print(character_replacement_better("AABABBA", 1))      # 4
    print(character_replacement_optimal("AABABBA", 1))     # 4