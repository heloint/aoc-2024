#!/usr/bin/env python3


def main() -> int:
    file = open("input.txt", "r", encoding="UTF-8")
    lines: list[str] = file.readlines()
    matrix: list[list[str]] = [list(line.strip()) for line in lines]

    rows_count: int = len(matrix)
    cols_count: int = len(matrix[0])
    res = 0
    for row_idx in range(rows_count):
        for col_idx in range(cols_count):
            # vertical
            if row_idx + 3 < rows_count and matrix[row_idx][col_idx] == "X" and matrix[row_idx+1][col_idx] == "M" and matrix[row_idx+2][col_idx] == "A" and matrix[row_idx+3][col_idx] == "S":
                res += 1
            # vertical reversed
            if row_idx + 3 < rows_count and matrix[row_idx+3][col_idx] == "X" and matrix[row_idx+2][col_idx] == "M" and matrix[row_idx+1][col_idx] == "A" and matrix[row_idx][col_idx] == "S":
                res += 1

            # horizontal
            if col_idx + 3 < cols_count and matrix[row_idx][col_idx] == "X" and matrix[row_idx][col_idx+1] == "M" and matrix[row_idx][col_idx+2] == "A" and matrix[row_idx][col_idx+3] == "S":
                res += 1
            # horizontal reversed
            if col_idx + 3 < cols_count and matrix[row_idx][col_idx+3] == "X" and matrix[row_idx][col_idx+2] == "M" and matrix[row_idx][col_idx+1] == "A" and matrix[row_idx][col_idx] == "S":
                res += 1

            # diagonal left-top to right-bottom
            if col_idx + 3 < cols_count and row_idx+3 < rows_count and matrix[row_idx][col_idx] == "X" and matrix[row_idx+1][col_idx+1] == "M" and matrix[row_idx+2][col_idx+2] == "A" and matrix[row_idx+3][col_idx+3] == "S":
                res += 1
            # diagonal left-top to right-bottom reversed
            if col_idx + 3 < cols_count and row_idx+3 < rows_count and matrix[row_idx+3][col_idx+3] == "X" and matrix[row_idx+2][col_idx+2] == "M" and matrix[row_idx+1][col_idx+1] == "A" and matrix[row_idx][col_idx] == "S":
                res += 1

            # diagonal left-bottom to right-top
            if col_idx + 3 < cols_count and row_idx-3 > -1 and matrix[row_idx][col_idx] == "X" and matrix[row_idx-1][col_idx+1] == "M" and matrix[row_idx-2][col_idx+2] == "A" and matrix[row_idx-3][col_idx+3] == "S":
                res += 1
            # diagonal left-bottom to right-top reversed
            if col_idx + 3 < cols_count and row_idx-3 > -1 and matrix[row_idx-3][col_idx+3] == "X" and matrix[row_idx-2][col_idx+2] == "M" and matrix[row_idx-1][col_idx+1] == "A" and matrix[row_idx][col_idx] == "S":
                res += 1

    print(res)
    file.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
