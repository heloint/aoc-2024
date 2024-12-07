#!/usr/bin/env python3


def main() -> int:
    file = open("./input.txt", "r", encoding="UTF-8")
    file_content = file.read()
    rules, updates = file_content.split("\n\n")

    mapped_rules_after_before: dict[int, set[int]] = {}

    for rule in rules.splitlines():
        before_val, after_val = tuple(map(int, rule.strip().split("|")))

        mapped_rules_after_before.setdefault(after_val, set())
        mapped_rules_after_before[after_val].add(before_val)

    res: int = 0
    for update in updates.splitlines():
        is_correct_update: bool = True
        update_pages: list[int] = list(map(int, update.split(",")))
        for a_idx, a_val in enumerate(update_pages):
            for b_idx, b_val in enumerate(update_pages):
                if a_idx >= b_idx:
                    continue
                if b_val in mapped_rules_after_before[a_val]:
                    is_correct_update = False
        if not is_correct_update:
            # breakpoint()
            print(update_pages)
            for a_idx in range(len(update_pages) - 1):
                for b_idx in range(a_idx + 1, len(update_pages)):
                    before_val: int = update_pages[a_idx]
                    after_val: int = update_pages[b_idx]
                    if after_val not in mapped_rules_after_before:
                        continue
                    if before_val in mapped_rules_after_before[after_val]:
                        # update_pages[a_idx] = update_pages[b_idx]
                        # update_pages[b_idx] = update_pages[a_idx]
                        update_pages[b_idx], update_pages[a_idx] = update_pages[a_idx], update_pages[b_idx]

            print(update_pages)
            print("**************")
            update_middle_idx: int = len(update_pages) // 2
            update_middle_val: int = update_pages[update_middle_idx]
            res += update_middle_val
    print(res)
    file.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
