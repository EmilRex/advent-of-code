import typer


def main(path: str):
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

            if (s1 >= s2 and e1 <= e2) or (s2 >= s1 and e2 <= e1):
                total += 1
                print(f"[{loop}] Ranges {line} overlap... total: {total}")


if __name__ == "__main__":
    typer.run(main)
