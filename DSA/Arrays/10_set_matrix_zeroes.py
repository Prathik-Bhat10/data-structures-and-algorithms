"""
SET MATRIX ZEROES
------------------
Given an m×n matrix, if an element is 0, set its entire
row and column to 0. Do it in-place.

Example:
Input:
  [[1, 1, 1],
   [1, 0, 1],
   [1, 1, 1]]

Output:
  [[1, 0, 1],
   [0, 0, 0],
   [1, 0, 1]]
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
For each 0 found, mark its entire row and column with a sentinel
(-inf), then replace all sentinels with 0.
Avoids confusion between original 0s and newly placed ones.

Time  : O((m × n) × (m + n))
Space : O(1)
"""

def set_zeroes_brute(matrix):
    SENTINEL = float('-inf')
    m, n = len(matrix), len(matrix[0])

    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                for col in range(n):
                    if matrix[r][col] != 0:
                        matrix[r][col] = SENTINEL
                for row in range(m):
                    if matrix[row][c] != 0:
                        matrix[row][c] = SENTINEL

    for r in range(m):
        for c in range(n):
            if matrix[r][c] == SENTINEL:
                matrix[r][c] = 0


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Row & Column Sets)
# ─────────────────────────────────────────────
"""
First pass: record which rows and columns contain a zero.
Second pass: zero out those rows and columns.

Time  : O(m × n)
Space : O(m + n)
"""

def set_zeroes_better(matrix):
    m, n = len(matrix), len(matrix[0])
    zero_rows = set()
    zero_cols = set()

    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)

    for r in range(m):
        for c in range(n):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Use First Row & Column as Markers)
# ─────────────────────────────────────────────
"""
Use the first row and first column of the matrix itself as
marker arrays (instead of extra O(m+n) space).

Steps:
  1. Check if row-0 or col-0 originally has any zero (store separately).
  2. For every cell (r, c) where r>0, c>0:
       if matrix[r][c] == 0 → mark matrix[r][0] = 0 and matrix[0][c] = 0
  3. Use markers to zero out the interior cells.
  4. Handle row-0 and col-0 using the flags from step 1.

Time  : O(m × n)
Space : O(1)
"""

def set_zeroes_optimal(matrix):
    m, n = len(matrix), len(matrix[0])

    first_row_zero = any(matrix[0][c] == 0 for c in range(n))
    first_col_zero = any(matrix[r][0] == 0 for r in range(m))

    # Mark zeros on first row/col using interior cells
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    # Zero out interior cells based on markers
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    # Zero out first row and column if needed
    if first_row_zero:
        for c in range(n):
            matrix[0][c] = 0

    if first_col_zero:
        for r in range(m):
            matrix[r][0] = 0


# ─────────────────────────────────────────────
if __name__ == "__main__":
    import copy

    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    m1 = copy.deepcopy(matrix)
    set_zeroes_brute(m1)
    print(m1)   # [[1,0,1],[0,0,0],[1,0,1]]

    m2 = copy.deepcopy(matrix)
    set_zeroes_better(m2)
    print(m2)   # [[1,0,1],[0,0,0],[1,0,1]]

    m3 = copy.deepcopy(matrix)
    set_zeroes_optimal(m3)
    print(m3)   # [[1,0,1],[0,0,0],[1,0,1]]