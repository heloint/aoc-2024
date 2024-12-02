#!/usr/bin/env python3


def main() -> int:
    left_side: list[int] = []
    right_side: list[int] = []
    with open("./input.txt", "r", encoding="UTF-8") as file:
        for line in file:
            line_parts: list[str] = line.split()
            curr_left = int(line_parts[0].strip())
            curr_right = int(line_parts[1].strip())

            left_side.append(curr_left)
            right_side.append(curr_right)
    left_side.sort()
    right_side.sort()

    res = 0
    for left, right in zip(left_side, right_side):
        res += abs(right-left)

    print(res)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
