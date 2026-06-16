"""
Selection Sort finds the minimum element from the unsorted portion of the array
and places it at its correct position in each iteration.

Time Complexity:
Best Case: O(n^2)
Average Case: O(n^2)
Worst Case: O(n^2)

Space Complexity: O(1) since it is an in-place sorting algorithm.

Example:
Input: [5, 3, 8, 4]

Iteration 1:
Minimum = 3
[3, 5, 8, 4]

Iteration 2:
Minimum = 4
[3, 4, 8, 5]

Iteration 3:
Minimum = 5
[3, 4, 5, 8]

Output:

[3, 4, 5, 8]
"""

def selection_sort(arr):
    """Sort a list in place using selection sort."""
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


if __name__ == "__main__":
    sample = [64, 25, 12, 22, 11]
    print(selection_sort(sample))