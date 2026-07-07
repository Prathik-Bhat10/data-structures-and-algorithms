"""
ENCODE AND DECODE STRINGS
-------------------------
Design an algorithm to encode a list of strings into a single
string and decode it back to the original list.

The encoding should work even if the strings contain special
characters like '#', '/', spaces, or numbers.

Example:
Input : ["neet", "code", "love", "you"]
Encoded: "4#neet4#code4#love3#you"
Output : ["neet", "code", "love", "you"]

Input : ["hello", "", "world"]
Encoded: "5#hello0#5#world"
Output : ["hello", "", "world"]
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (Escape Characters)
# ─────────────────────────────────────────────
"""
Escape every occurrence of '/' and '#' before joining
the strings with a delimiter.

During decoding, reverse the escaping process.

Time  : O(total characters)
Space : O(total characters)
"""


def encode_brute(strs):
    encoded = []

    for s in strs:
        temp = ""
        for ch in s:
            if ch == "/" or ch == "#":
                temp += "/"
            temp += ch
        encoded.append(temp)

    return "#".join(encoded)


def decode_brute(s):
    result = []
    current = []
    i = 0

    while i < len(s):
        if s[i] == "/":
            i += 1
            current.append(s[i])
        elif s[i] == "#":
            result.append("".join(current))
            current = []
        else:
            current.append(s[i])
        i += 1

    result.append("".join(current))
    return result


# ─────────────────────────────────────────────
# APPROACH 2 — OPTIMAL (Length Prefix)
# ─────────────────────────────────────────────
"""
Store each string as:

length + '#' + string

Example:
"code" → "4#code"

While decoding:
1. Read the number before '#'
2. Extract exactly that many characters
3. Repeat

Since the length is known, any character can safely
appear inside the string.

Time  : O(total characters)
Space : O(total characters)
"""


def encode_optimal(strs):
    encoded = []

    for s in strs:
        encoded.append(str(len(s)) + "#" + s)

    return "".join(encoded)


def decode_optimal(s):
    result = []
    i = 0

    while i < len(s):
        j = i

        while s[j] != "#":
            j += 1

        length = int(s[i:j])
        result.append(s[j + 1:j + 1 + length])

        i = j + 1 + length

    return result


# ─────────────────────────────────────────────
if __name__ == "__main__":
    strings = ["neet", "code", "love", "you"]

    encoded = encode_brute(strings)
    print(encoded)
    print(decode_brute(encoded))

    encoded = encode_optimal(strings)
    print(encoded)
    print(decode_optimal(encoded))
