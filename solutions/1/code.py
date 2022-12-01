import typer


def main(path: str):
    loop = 0
    current = 0
    most = 0

    with open(path, "r") as fh:
        while True:
            loop += 1
            line = fh.readline()

            # Exit condition
            if line == '':
                break

            # Counter reset
            if line.strip() == '':
                if current > most:
                    most = current
                print(f"[{loop}] Current: {current}; Most: {most}")
                current = 0
                continue

            # Increment counter
            if line.strip().isnumeric():
                current += int(line.strip())
            else:
                raise ValueError(f"Unexpected value '{line}' found")

    print(f"\nResult is '{most}'")
    return most


if __name__ == "__main__":
    typer.run(main)
