from collections import defaultdict

import typer


def construct_grid(path: str):
    grid = defaultdict(lambda: ".")

    with open(path, "r") as fh:
        for line in fh:
            line = line.strip()

            nodes = line.split(" -> ")
            for idx in range(1, len(nodes)):
                from_x, from_y = (int(v) for v in nodes[idx - 1].split(","))
                to_x, to_y = (int(v) for v in nodes[idx].split(","))

                print(f"Drawing {from_x},{from_y} -> {to_x},{to_y}")
                if from_x == to_x:
                    for y in range(min(from_y, to_y), max(from_y, to_y) + 1):
                        print(f"\tDrawing # at {from_x},{y}")
                        grid[(from_x, y)] = "#"
                if from_y == to_y:
                    for x in range(min(from_x, to_x), max(from_x, to_x) + 1):
                        print(f"\tDrawing # at {x},{from_y}")
                        grid[(x, from_y)] = "#"
    return grid


def visualize_grid(grid):
    x_min = min([k[0] for k in grid])
    x_max = max([k[0] for k in grid])
    y_max = max([k[1] for k in grid])

    for y in range(y_max + 1):
        print(f"[{y:3}]", "".join([grid[(x, y)] for x in range(x_min - 1, x_max + 1)]))


def fill_grid(grid, floor: bool):
    abyss_start = max([k[1] for k in grid])
    total = 0
    x, y = 500, 0

    while True:
        # Exit condition(s)
        if grid[x, y] == "o":
            return total

        if y > abyss_start:
            if floor:
                grid[(x, y)] = "o"
                x, y = 500, 0
                total += 1
                continue
            else:
                return total

        # Current grain path
        if grid[(x, y + 1)] == ".":
            y += 1
            continue
        elif grid[(x - 1, y + 1)] == ".":
            y += 1
            x -= 1
            continue
        elif grid[(x + 1, y + 1)] == ".":
            y += 1
            x += 1
            continue
        else:
            grid[(x, y)] = "o"
            x, y = 500, 0
            total += 1
            continue


def main(path: str, floor: bool):
    # Construct the grid
    grid = construct_grid(path)
    # Visualize grid
    visualize_grid(grid)
    # Fill with sand
    total = fill_grid(grid, floor)
    visualize_grid(grid)
    print(f"Total is {total}")


if __name__ == "__main__":
    typer.run(main)
