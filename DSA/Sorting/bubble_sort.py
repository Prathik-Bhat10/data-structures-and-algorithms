"""
Bubble Sort repeatedly compares adjacent elements and swaps them
if they are in the wrong order.

After every iteration, the largest element moves to its correct
position at the end of the array.

Time Complexity:
Best Case: O(n)
Average Case: O(n^2)
Worst Case: O(n^2)

Space Complexity: O(1) since it is an in-place sorting algorithm.

Example:
Input: [5, 3, 8, 4]

Pass 1:
[3, 5, 8, 4]
[3, 5, 4, 8]

Pass 2:
[3, 4, 5, 8]

Output:

[3, 4, 5, 8]
"""

def bubble_sort(arr):
    """Sort a list in place using bubble sort."""
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(sample))