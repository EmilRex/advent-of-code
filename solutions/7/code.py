from collections import defaultdict

import typer


def calculate_totals(path: str):
    cwd = [""]
    totals = defaultdict(int)
    seen = set()

    with open(path, "r") as fh:
        for line in fh:
            line = line.strip()

            # Track directory changes
            if line.startswith("$ cd"):
                dir = line.split(" ")[2]
                if dir == "/":
                    cwd = [""]
                elif dir == "..":
                    cwd.pop()
                else:
                    cwd.append(dir)
                continue

            # Skip ls and dir
            if line.startswith("$ ls"):
                continue
            if line.startswith("dir"):
                continue

            size, name = line.split(" ")
            current_file = "/".join([*cwd, name])

            if current_file not in seen:
                for idx in range(len(cwd)):
                    path = "/".join(cwd[: idx + 1])
                    totals[path] += int(size)
                seen.add(current_file)

    return totals


def main(path: str):
    totals = calculate_totals(path)

    part_one = sum([s for s in totals.values() if s <= 100000])
    print(f"Sum of files <= 100000 is {part_one}")

    used = totals[""]
    free = 70000000 - used
    needed = 30000000 - free

    smallest = min({s: p for p, s in totals.items() if s >= needed})
    print(f"Smallest deletable file has size {smallest}")


if __name__ == "__main__":
    typer.run(main)
