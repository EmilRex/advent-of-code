import typer


def main(path: str):
    total = 0
    idx = 0

    with open(path, "r") as fh:
        while True:
            idx += 1
            line = fh.readline().strip()

            # Exit condition
            if line == "":
                break

            # Code goes here
            print(f"[{idx}] '{line}' - total: {total}")


if __name__ == "__main__":
    typer.run(main)
