import math

import typer


def load_grid(path: str):
    grid = []
    with open(path, "r") as fh:
        for idx, line in enumerate(fh):
            line = line.strip()
            grid.append([int(i) for i in line])

    assert all([len(row) == len(grid) for row in grid])
    return grid


def count_visible_trees(grid):
    total = 0

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid) - 1):
            current = grid[row][col]
            v_left = all([grid[row][c] < current for c in range(0, col)])
            v_right = all([grid[row][c] < current for c in range(col + 1, len(grid))])
            v_up = all([grid[r][col] < current for r in range(0, row)])
            v_down = all([grid[r][col] < current for r in range(row + 1, len(grid))])
            print(
                f"Tree [{row}, {col}] with height {current}: {v_left, v_right, v_up, v_down}"
            )

            if any([v_left, v_right, v_up, v_down]):
                print("\tTree is visible")
                total += 1

    total += (len(grid) * 2) + ((len(grid) - 2) * 2)
    print(f"Total visible trees is {total}")


def find_visibility(current, heights):
    visibility = 0
    for height in heights:
        # Issue here was that I was incrementing after the check
        visibility += 1
        if height >= current:
            break
    return visibility


def find_scenic_score(grid):
    scores = []
    for row in range(0, len(grid)):
        for col in range(0, len(grid)):
            current = grid[row][col]

            left = [grid[row][c] for c in range(0, col)][::-1]
            right = [grid[row][c] for c in range(col + 1, len(grid))]
            up = [grid[r][col] for r in range(0, row)][::-1]
            down = [grid[r][col] for r in range(row + 1, len(grid))]

            visibilities = [
                find_visibility(current, item) for item in [left, right, up, down]
            ]
            visibility = math.prod(visibilities)
            scores.append(visibility)
            print(
                f"Tree [{row}, {col}] with height {current} has visibility {visibility}"
            )

    print(f"Highest scenic score is {max(scores)}")


def main(path: str):
    grid = load_grid(path)
    # count_visible_trees(grid)
    find_scenic_score(grid)


if __name__ == "__main__":
    typer.run(main)
