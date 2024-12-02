#!/usr/bin/env python3


def main() -> int:
    safe_rows = 0
    with open("./input.txt", "r", encoding="UTF-8") as file:
        for line in file:
            nums_in_line: list[int] = list(map(lambda x: int(x.strip()), line.split()))
            correct_row = False
            for idx in range(len(nums_in_line)):
                sub_window = nums_in_line[:idx] + nums_in_line[idx+1:]
                incremental = sub_window == sorted(sub_window)
                decremental = sub_window == sorted(sub_window, reverse=True)
                correct_order = incremental or decremental

                correct_window = True
                for sub_idx in range(len(sub_window)-1):
                    curr = sub_window[sub_idx]
                    next =  sub_window[sub_idx+1]
                    diff = abs(curr-next)
                    if not 1 <= diff <= 3:
                        correct_window = False
                if correct_order and correct_window:
                    correct_row = True
            if correct_row:
                safe_rows += 1
    print(safe_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
