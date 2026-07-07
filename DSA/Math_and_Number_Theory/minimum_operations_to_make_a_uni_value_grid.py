"""
MINIMUM OPERATIONS TO MAKE A UNI-VALUE GRID
-------------------------------------------
You are given an m x n integer grid and an integer `x`.

In one operation, you can add or subtract `x` from any element.

Return the minimum number of operations required to make all
elements in the grid equal. If it is impossible, return -1.

Example:
Input :
grid = [[2, 4],
        [6, 8]]
x = 2

Output: 4

Input :
grid = [[1, 5],
        [2, 3]]
x = 1

Output: 5
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Flatten the grid and try making every existing value the target.

For each target:
1. Check whether every element can be converted
   ((abs(a - target) % x == 0)).
2. Compute total operations.

Time  : O((mn)²)
Space : O(mn)
"""


def min_operations_brute(grid, x):
    nums = [num for row in grid for num in row]

    minimum = float("inf")

    for target in nums:
        operations = 0
        possible = True

        for num in nums:
            diff = abs(num - target)

            if diff % x != 0:
                possible = False
                break

            operations += diff // x

        if possible:
            minimum = min(minimum, operations)

    return minimum if minimum != float("inf") else -1


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Sorting + Median)
# ─────────────────────────────────────────────
"""
Observation:
The median minimizes the sum of absolute differences.

Steps:
1. Flatten the grid.
2. Verify all numbers have the same remainder modulo x.
3. Sort the array.
4. Choose the median.
5. Count required operations.

Time  : O(mn log(mn))
Space : O(mn)
"""


def min_operations_better(grid, x):
    nums = [num for row in grid for num in row]

    remainder = nums[0] % x
    for num in nums:
        if num % x != remainder:
            return -1

    nums.sort()
    median = nums[len(nums) // 2]

    operations = 0
    for num in nums:
        operations += abs(num - median) // x

    return operations


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL
# ─────────────────────────────────────────────
"""
The optimal solution is identical to the sorting approach.

Reason:
The target value that minimizes the total number of operations
is the median after sorting.

Time  : O(mn log(mn))
Space : O(mn)
"""


def min_operations_optimal(grid, x):
    nums = [num for row in grid for num in row]

    base = nums[0] % x

    for num in nums:
        if num % x != base:
            return -1

    nums.sort()
    median = nums[len(nums) // 2]

    operations = 0

    for num in nums:
        operations += abs(num - median) // x

    return operations


# ─────────────────────────────────────────────
if __name__ == "__main__":
    grid1 = [
        [2, 4],
        [6, 8]
    ]

    grid2 = [
        [1, 5],
        [2, 3]
    ]

    print(min_operations_brute(grid1, 2))      # 4
    print(min_operations_better(grid1, 2))     # 4
    print(min_operations_optimal(grid1, 2))    # 4

    print(min_operations_optimal(grid2, 1))    # 5