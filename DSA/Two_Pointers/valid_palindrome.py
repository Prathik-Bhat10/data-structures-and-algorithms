"""
VALID PALINDROME
----------------
Given a string `s`, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Return True if it is a palindrome, otherwise False.

Example 1:
Input : s = "A man, a plan, a canal: Panama"
Output: True

Explanation:
After removing non-alphanumeric characters
and converting to lowercase:

"amanaplanacanalpanama"

which reads the same forwards and backwards.

Example 2:
Input : s = "race a car"
Output: False

Processed string:
"raceacar"

Forward :
raceacar

Backward:
racaecar

Not equal.
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Build a cleaned string containing only lowercase
alphanumeric characters.

Reverse the cleaned string and compare.

Time  : O(n)
Space : O(n)
"""

def is_palindrome_brute(s):
    cleaned = ""

    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()

    return cleaned == cleaned[::-1]


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Using Extra List)
# ─────────────────────────────────────────────
"""
Instead of repeated string concatenation,
store characters in a list and join them.

This avoids creating many intermediate strings.

Time  : O(n)
Space : O(n)
"""

def is_palindrome_better(s):
    chars = []

    for ch in s:
        if ch.isalnum():
            chars.append(ch.lower())

    cleaned = "".join(chars)

    return cleaned == cleaned[::-1]


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Two Pointers)
# ─────────────────────────────────────────────
"""
Observation:
A palindrome reads the same from both ends.

Use two pointers:
- Left starts from beginning.
- Right starts from end.

Skip non-alphanumeric characters.

Compare lowercase versions of valid characters.

If any mismatch occurs,
return False.

Otherwise continue until pointers cross.

Example:

s = "A man, a plan, a canal: Panama"

L                                 R
A man, a plan, a canal: Panama

Compare:
A == a ✓

Move inward while skipping spaces,
commas, and colon.

Eventually all characters match.

Return True.

Time  : O(n)
Space : O(1)

This is the expected interview / LeetCode solution.
"""

def is_palindrome_optimal(s):
    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# ─────────────────────────────────────────────
if __name__ == "__main__":
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"

    print(is_palindrome_brute(s1))
    print(is_palindrome_better(s1))
    print(is_palindrome_optimal(s1))

    print(is_palindrome_optimal(s2))