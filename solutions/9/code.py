from collections import defaultdict

import typer


def one(n: int):
    if n < 0:
        return -1
    return 1


def move_head(head, direction):
    if direction == "R":
        return (head[0] + 1, head[1])
    elif direction == "L":
        return (head[0] - 1, head[1])
    elif direction == "U":
        return (head[0], head[1] + 1)
    elif direction == "D":
        return (head[0], head[1] - 1)
    else:
        raise ValueError(f"Unexpected direction {direction}")


def move_tail(head, tail):
    horizontal = head[0] - tail[0]
    vertical = head[1] - tail[1]

    # Touching
    if abs(horizontal) <= 1 and abs(vertical) <= 1:
        return tail
    # Single direction movement
    elif horizontal in (-2, 2) and vertical == 0:
        return (tail[0] + int(horizontal / 2), tail[1])
    elif horizontal == 0 and vertical in (-2, 2):
        return (tail[0], tail[1] + int(vertical / 2))
    # Diagonal movement
    else:
        return (tail[0] + one(horizontal), tail[1] + one(vertical))


def main(path: str):
    head = (0, 0)
    tail = (0, 0)
    positions = defaultdict(int)
    positions[tail] = 1

    with open(path, "r") as fh:
        for idx, line in enumerate(fh):
            line = line.strip()
            direction, steps = line.split(" ")
            steps = int(steps)

            for _ in range(steps):
                head = move_head(head, direction)
                tail = move_tail(head, tail)

                positions[tail] += 1

            # Code goes here
            print(f"[{idx}] '{line}' - head {head} - tail {tail}")

    print(f"Positions visited: {len(positions)}")


if __name__ == "__main__":
    typer.run(main)
