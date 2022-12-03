import string

import typer

PRIORITY_MAP = {
    l: n for l, n in zip(string.ascii_letters, range(1, len(string.ascii_letters) + 1))
}


def split_compartments(s: str):
    # Check assumtions
    assert len(s) >= 2
    assert len(s) % 2 == 0

    half = int(len(s) / 2)

    return s[:half], s[half:]


def find_common_item(c1: str, c2: str):
    items = set(c1).intersection(set(c2))

    assert len(items) == 1

    return items.pop()


def calculate_priority(item: str):
    return PRIORITY_MAP[item]


def main(path: str):
    loop = 0
    total = 0

    with open(path, "r") as fh:
        while True:
            loop += 1
            line = fh.readline().strip()

            if line == "":
                break

            c1, c2 = split_compartments(line)
            item = find_common_item(c1, c2)
            priority = calculate_priority(item)

            total += priority
            print(f"[{loop}] Item {item} with {priority} total:{total}")


if __name__ == "__main__":
    typer.run(main)
