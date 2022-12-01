import typer


def main(path: str, top: int = 1):
    loop = 0
    current = 0
    most = [0] * top

    with open(path, "r") as fh:
        while True:
            loop += 1
            line = fh.readline()

            # Counter reset
            if line.strip() == "":
                if current > min(most):
                    most[most.index(min(most))] = current
                print(f"[{loop}] Current: {current}; Most: {most}")
                current = 0

                # Exit condition
                if line == "":
                    break
                else:
                    continue

            # Increment counter
            if line.strip().isnumeric():
                current += int(line.strip())
            else:
                raise ValueError(f"Unexpected value '{line}' found")

    print(f"\n Sum of top {top} is {sum(most)}")


if __name__ == "__main__":
    typer.run(main)
