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


def main(path: str, knots: int = 1):
    head = (0, 0)
    tails = [(0, 0)] * knots
    positions = [defaultdict(int) for i in range(knots)]
    for i in range(knots):
        positions[i][tails[i]] = 1

    with open(path, "r") as fh:
        for line in fh:
            line = line.strip()
            direction, steps = line.split(" ")
            steps = int(steps)

            for _ in range(steps):
                head = move_head(head, direction)

                for idx in range(knots):

                    tails[idx] = move_tail([head, *tails][idx], tails[idx])

                print(f"'{line}' - head {head} - tail {tails}")
                for i, tail in enumerate(tails):
                    positions[i][tail] += 1

    print(f"Positions visited: {len(positions[-1])}")


if __name__ == "__main__":
    typer.run(main)
