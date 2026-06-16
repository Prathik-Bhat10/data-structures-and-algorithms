"""
Merge Sort uses the Divide and Conquer technique.
It recursively divides the array into two halves, sorts each half,
and merges them back together in sorted order.

Time Complexity:
Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)

Space Complexity: O(n) because extra space is required during merging.

Example:
Input: [38, 27, 43, 3]

Divide:
[38, 27] [43, 3]

Divide:
[38] [27] [43] [3]

Merge:
[27, 38]
[3, 43]

Final Merge:
[3, 27, 38, 43]

Output:

[3, 27, 38, 43]
"""

def merge_sort(arr):
    """Sort a list using merge sort."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(sample))