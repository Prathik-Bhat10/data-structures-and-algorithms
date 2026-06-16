"""
VALID SUDOKU
-------------
Determine if a 9×9 Sudoku board is valid. Only filled cells need
to be validated according to the following rules:

  1. Each row must contain digits 1–9 with no repetition.
  2. Each column must contain digits 1–9 with no repetition.
  3. Each of the nine 3×3 sub-boxes must contain digits 1–9 with no repetition.

Note: The board does not need to be solvable.

Example:
Input : (standard partially filled 9×9 board)
Output: True or False
"""
from collections import defaultdict

# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (Separate Passes)
# ─────────────────────────────────────────────
"""
Make three separate passes:
  1. Validate all rows.
  2. Validate all columns.
  3. Validate all 3×3 boxes.

Each validation collects digits, skips '.', and checks for duplicates.

Time  : O(1)  — board is always 9×9 (81 cells, constant)
Space : O(1)  — at most 9 digits stored at a time
"""

def is_valid_sudoku_brute(board):
    def has_duplicate(cells):
        digits = [c for c in cells if c != '.']
        return len(digits) != len(set(digits))

    # Rows
    for row in board:
        if has_duplicate(row):
            return False

    # Columns
    for col in range(9):
        if has_duplicate([board[row][col] for row in range(9)]):
            return False

    # 3×3 boxes
    for box_row in range(3):
        for box_col in range(3):
            cells = [
                board[box_row * 3 + r][box_col * 3 + c]
                for r in range(3)
                for c in range(3)
            ]
            if has_duplicate(cells):
                return False

    return True


# ─────────────────────────────────────────────
# APPROACH 2 — OPTIMAL (Single Pass with Hash Sets)
# ─────────────────────────────────────────────
"""
Use three sets of sets — one for rows, one for columns,
one for boxes — and validate everything in a single pass.

Box index: (row // 3, col // 3) → maps each cell to its 3×3 box.

Trace (single filled cell '5' at row=0, col=0):
  rows[0]    → add '5'
  cols[0]    → add '5'
  boxes[0,0] → add '5'
  If '5' appears again in same row/col/box → return False

Time  : O(1)  — 81 cells, constant
Space : O(1)  — at most 9 entries per set, 27 sets total
"""



def is_valid_sudoku_optimal(board):
    rows    = defaultdict(set)
    cols    = defaultdict(set)
    boxes   = defaultdict(set)   # key: (row//3, col//3)

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue

            box_key = (r // 3, c // 3)

            if (val in rows[r] or
                val in cols[c] or
                val in boxes[box_key]):
                return False

            rows[r].add(val)
            cols[c].add(val)
            boxes[box_key].add(val)

    return True


# ─────────────────────────────────────────────
if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]
    print(is_valid_sudoku_brute(board))    # True
    print(is_valid_sudoku_optimal(board))  # True