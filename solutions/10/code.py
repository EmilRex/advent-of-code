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

    # Render screen
    screen = []
    pos = 0
    for idx in range(240):
        if sum(operations[: idx + 1]) - 1 <= pos <= sum(operations[: idx + 1]) + 1:
            screen.append("#")
        else:
            screen.append(".")
        pos += 1
        if pos == 40:
            pos = 0

    for i in range(0, 240, 40):
        print("".join(screen[i : i + 40]))


if __name__ == "__main__":
    typer.run(main)
