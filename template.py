import typer


def main(path: str):
    total = 0

    with open(path, "r") as fh:
        for idx, line in enumerate(fh):
            line = line.strip()

            # Code goes here
            print(f"[{idx}] '{line}' - total: {total}")


if __name__ == "__main__":
    typer.run(main)
