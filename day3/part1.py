#!/usr/bin/env python3

import re

def main() -> int:
    file = open("./input.txt", "r", encoding="UTF-8")
    res = 0


    pat = re.compile(r'mul\(\d{1,3},\d{1,3}\)')

    for line in file:
        for idx in range(len(line)):

            mul_window = line[idx:idx+4]
            if mul_window != "mul(":
                continue

            extended_window = line[idx:idx+12]

            match_res = pat.match(extended_window)
            if not match_res:
                continue
            filtered_mul_cmd = match_res.group(0)

            try:
                part_a, part_b = filtered_mul_cmd.split(",")
            except Exception:
                continue

            first_num = int("".join(char for char in part_a if char.isdigit()))
            second_num = int("".join(char for char in part_b if char.isdigit()))

            res += first_num * second_num

    print(res)
    file.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
