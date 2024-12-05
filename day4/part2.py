#!/usr/bin/env python3


def main() -> int:
    file = open("input.txt", "r", encoding="UTF-8")
    lines: list[str] = file.readlines()
    matrix: list[list[str]] = [list(line.strip()) for line in lines]

    rows_count: int = len(matrix)
    cols_count: int = len(matrix[0])
    res: int = 0

    """
M.S
.A.
M.S
"""

    for row_idx in range(rows_count):
        for col_idx in range(cols_count):
            # Like in the example
            if (
                row_idx + 2 < rows_count
                and col_idx + 2 < cols_count
                and matrix[row_idx][col_idx] == "M"
                and matrix[row_idx][col_idx + 2] == "S"
                and matrix[row_idx + 1][col_idx + 1] == "A"
                and matrix[row_idx + 2][col_idx] == "M"
                and matrix[row_idx + 2][col_idx + 2] == "S"
            ):
                res += 1

            # Left-top to bottom-right reversed.
            if (
                row_idx + 2 < rows_count
                and col_idx + 2 < cols_count
                and matrix[row_idx][col_idx] == "S"
                and matrix[row_idx][col_idx + 2] == "S"
                and matrix[row_idx + 1][col_idx + 1] == "A"
                and matrix[row_idx + 2][col_idx] == "M"
                and matrix[row_idx + 2][col_idx + 2] == "M"
            ):
                res += 1

            # Right-top to left-bottom reversed.
            if (
                row_idx + 2 < rows_count
                and col_idx + 2 < cols_count
                and matrix[row_idx][col_idx] == "M"
                and matrix[row_idx][col_idx + 2] == "M"
                and matrix[row_idx + 1][col_idx + 1] == "A"
                and matrix[row_idx + 2][col_idx] == "S"
                and matrix[row_idx + 2][col_idx + 2] == "S"
            ):
                res += 1

            # Both diagonal reversed.
            if (
                row_idx + 2 < rows_count
                and col_idx + 2 < cols_count
                and matrix[row_idx][col_idx] == "S"
                and matrix[row_idx][col_idx + 2] == "M"
                and matrix[row_idx + 1][col_idx + 1] == "A"
                and matrix[row_idx + 2][col_idx] == "S"
                and matrix[row_idx + 2][col_idx + 2] == "M"
            ):
                res += 1

    print(res)
    file.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
