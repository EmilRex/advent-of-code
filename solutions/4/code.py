import typer


def contains(s1: int, e1: int, s2: int, e2: int):
    if (s1 >= s2 and e1 <= e2) or (s2 >= s1 and e2 <= e1):
        return 1
    return 0


def intersects(s1: int, e1: int, s2: int, e2: int):
    intersection = set(range(s1, e1 + 1)).intersection(set(range(s2, e2 + 1)))
    if len(intersection) > 0:
        return 1
    return 0


def main(path: str, strategy: str):
    total = 0
    loop = 0

    with open(path, "r") as fh:
        while True:
            loop += 1
            line = fh.readline().strip()

            if line == "":
                break

            r1, r2 = line.split(",")
            s1, e1 = (int(i) for i in r1.split("-"))
            s2, e2 = (int(i) for i in r2.split("-"))

            if strategy == "contains":
                total += contains(s1, e1, s2, e2)
            elif strategy == "intersects":
                total += intersects(s1, e1, s2, e2)
            else:
                raise ValueError(f"Invalid strategy {strategy}")

            print(f"[{loop}] Ranges {line} {strategy}... total: {total}")


if __name__ == "__main__":
    typer.run(main)
