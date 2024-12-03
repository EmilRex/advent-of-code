from collections import deque

import typer


def get_example():
    return {
        1: deque("NZ"),
        2: deque("DCM"),
        3: deque("P"),
    }


def get_input():
    return {
        1: deque("VQWMBNZC"),
        2: deque("BCWRZH"),
        3: deque("JRQF"),
        4: deque("TMNFHWSZ"),
        5: deque("PQNLWFG"),
        6: deque("WPL"),
        7: deque("JQCGRDBV"),
        8: deque("WBNQZ"),
        9: deque("JTGCFLH"),
    }


def main(path: str, strategy: int):
    idx = 0

    # TODO: Parse instead of hardcoding
    if path == "example.txt":
        queues = get_example()
    elif path == "input.txt":
        queues = get_input()
    else:
        raise ValueError(f"Unexpected path {path}")

    with open(path, "r") as fh:
        while True:
            idx += 1
            line = fh.readline().strip()

            # Exit condition
            if line == "":
                break

            if "move" not in line:
                print(f"Skipping line: {line}")
                continue

            parts = line.split(" ")
            (
                n,
                _from,
                _to,
            ) = (
                int(parts[1]),
                int(parts[3]),
                int(parts[5]),
            )

            if strategy == 1:
                for _ in range(n):
                    queues[_to].appendleft(queues[_from].popleft())
            elif strategy == 2:
                items = list(reversed([queues[_from].popleft() for _ in range(n)]))
                for i in items:
                    queues[_to].appendleft(i)
            else:
                raise ValueError(f"Unexpected strategy {strategy}")

    # Get the end result
    result = "".join(q.popleft() for q in queues.values())
    print(f"\nFinal result: {result}")


if __name__ == "__main__":
    typer.run(main)
