"""
Insertion Sort builds a sorted array one element at a time by inserting
each element into its correct position in the already sorted portion.

Time Complexity:
Best Case: O(n)
Average Case: O(n^2)
Worst Case: O(n^2)

Space Complexity: O(1) since it is an in-place sorting algorithm.

Example:
Input: [5, 3, 8, 4]

Insert 3:
[3, 5, 8, 4]

Insert 8:
[3, 5, 8, 4]

Insert 4:
[3, 4, 5, 8]

Output:

[3, 4, 5, 8]
"""

def insertion_sort(arr):
    """Sort a list in place using insertion sort."""
    n = len(arr)

    for i in range(1, n):
        current = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current

    return arr


if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print(insertion_sort(sample))