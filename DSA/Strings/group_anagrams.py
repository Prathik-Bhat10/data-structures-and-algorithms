"""
GROUP ANAGRAMS
--------------
Given an array of strings `strs`, group the anagrams together.
You may return the answer in any order.

Example:
Input : strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Input : strs = [""]
Output: [[""]]
"""

from collections import defaultdict


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
For each word, compare it with every other unused word by
sorting both strings. If they match, they belong to the same group.

Time  : O(n² × k log k)
Space : O(n)

where:
n = number of strings
k = average length of each string
"""

def group_anagrams_brute(strs):
    visited = [False] * len(strs)
    result = []

    for i in range(len(strs)):
        if visited[i]:
            continue

        group = [strs[i]]
        visited[i] = True

        for j in range(i + 1, len(strs)):
            if not visited[j] and sorted(strs[i]) == sorted(strs[j]):
                group.append(strs[j])
                visited[j] = True

        result.append(group)

    return result


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Sorted String as Key)
# ─────────────────────────────────────────────
"""
Sort each string and use the sorted string as the dictionary key.

Time  : O(n × k log k)
Space : O(n × k)
"""

def group_anagrams_sort(strs):
    groups = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Character Count)
# ─────────────────────────────────────────────
"""
Count the frequency of each character (26 lowercase letters)
and use the frequency tuple as the dictionary key.

Avoids sorting every string.

Time  : O(n × k)
Space : O(n × k)
"""

def group_anagrams_optimal(strs):
    groups = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1

        groups[tuple(count)].append(word)

    return list(groups.values())


# ─────────────────────────────────────────────
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(group_anagrams_brute(strs))
    print(group_anagrams_sort(strs))
    print(group_anagrams_optimal(strs))