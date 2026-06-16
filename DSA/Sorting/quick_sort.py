"""
Quick Sort follows the Divide and Conquer approach.
It selects a pivot element and partitions the array into elements
smaller than the pivot and greater than the pivot.

Time Complexity:
Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n^2)

Space Complexity: O(log n) due to recursion stack.

Example:
Input: [8, 3, 1, 7, 0, 10, 2]

Pivot = 8

Left Partition:
[3, 1, 7, 0, 2]

Right Partition:
[10]

Recursively sort left and right partitions.

Output:

[0, 1, 2, 3, 7, 8, 10]
"""

def quick_sort(arr):
    """Sort a list using quick sort."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    sample = [8, 3, 1, 7, 0, 10, 2]
    print(quick_sort(sample))