import typer


def main(path: str):
    operations = [1]
    with open(path, "r") as fh:
        for line in fh:
            line = line.strip()

            if line.startswith("noop"):
                operations.append(0)
            elif line.startswith("addx"):
                operations.extend([0, int(line.split(" ")[1])])

    total = 0
    for idx in [20, 60, 100, 140, 180, 220]:
        print(f"[{idx}] X = {sum(operations[:idx])}")
        total += idx * sum(operations[:idx])
    print(f"Total: {total}")


if __name__ == "__main__":
    typer.run(main)
