"""
SPIRAL MATRIX
--------------
Given an m×n matrix, return all elements in spiral order
(clockwise from the top-left).

Example:
Input:
  [[1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]]

Spiral:
  → → →
        ↓
  ← ←  ↓
  ↑     ↓
  ↑  ←  ↓ (inward)

Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (Direction Array)
# ─────────────────────────────────────────────
"""
Simulate the spiral using a visited matrix and a direction array
[right, down, left, up]. Turn when hitting a boundary or visited cell.

Time  : O(m × n)
Space : O(m × n)  — for the visited matrix
"""

def spiral_order_brute(matrix):
    if not matrix:
        return []

    m, n = len(matrix), len(matrix[0])
    visited = [[False] * n for _ in range(m)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]   # R, D, L, U
    dr, dc = 0, 1                                       # start going right
    dir_idx = 0

    result = []
    r, c = 0, 0

    for _ in range(m * n):
        result.append(matrix[r][c])
        visited[r][c] = True

        nr, nc = r + dr, c + dc
        if not (0 <= nr < m and 0 <= nc < n) or visited[nr][nc]:
            dir_idx = (dir_idx + 1) % 4
            dr, dc = directions[dir_idx]
            nr, nc = r + dr, c + dc

        r, c = nr, nc

    return result


# ─────────────────────────────────────────────
# APPROACH 2 — OPTIMAL (Shrinking Boundaries)
# ─────────────────────────────────────────────
"""
Maintain four boundaries: top, bottom, left, right.
Peel one layer at a time — traverse the top row, right column,
bottom row, left column, then shrink the boundaries inward.

Trace ([[1,2,3],[4,5,6],[7,8,9]]):
  top=0 bottom=2 left=0 right=2
  → top row    [1,2,3]  → top=1
  → right col  [6,9]    → right=1
  → bottom row [8,7]    → bottom=1
  → left col   [4]      → left=1
  top=1 bottom=1 left=1 right=1
  → top row    [5]      → top=2
  top > bottom → stop
  Result: [1,2,3,6,9,8,7,4,5] ✓

Time  : O(m × n)
Space : O(1)  (output array excluded)
"""

def spiral_order_optimal(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse top row →
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1

        # Traverse right column ↓
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1

        # Traverse bottom row ← (if still valid)
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

        # Traverse left column ↑ (if still valid)
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

    return result


# ─────────────────────────────────────────────
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(spiral_order_brute(matrix))    # [1,2,3,6,9,8,7,4,5]
    print(spiral_order_optimal(matrix))  # [1,2,3,6,9,8,7,4,5]