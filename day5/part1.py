#!/usr/bin/env python3


def main() -> int:
    file = open("./input.txt", "r", encoding="UTF-8")
    file_content = file.read()
    rules, updates = file_content.split("\n\n")

    mapped_rules: dict[int, set[int]] = {}
    for rule in rules.splitlines():
        before_val, after_val = tuple(map(int, rule.strip().split("|")))
        mapped_rules.setdefault(after_val, set())
        mapped_rules[after_val].add(before_val)
    res: int = 0
    for update in updates.splitlines():
        is_correct_update: bool = True
        update_pages: tuple[int, ...] = tuple(map(int, update.split(",")))
        for a_idx, a_val in enumerate(update_pages):
            for b_idx, b_val in enumerate(update_pages):
                if a_idx >= b_idx:
                    continue
                if b_val in mapped_rules[a_val]:
                    print(mapped_rules[a_val])
                    is_correct_update = False
        if is_correct_update:
            update_middle_idx: int = len(update_pages) // 2
            update_middle_val: int = update_pages[update_middle_idx]
            res += update_middle_val
    print(res)
    file.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
