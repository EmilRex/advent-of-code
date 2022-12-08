import typer


def load_grid(path: str):
    grid = []
    with open(path, "r") as fh:
        for idx, line in enumerate(fh):
            line = line.strip()
            grid.append([int(i) for i in line])

    assert all([len(row) == len(grid) for row in grid])
    return grid


def main(path: str):
    total = 0

    grid = load_grid(path)

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
                print(f"\tTree is visible")
                total += 1

    total += (len(grid) * 2) + ((len(grid) - 2) * 2)

    print(f"Total visible trees is {total}")

    # print(f"[{idx}] '{line}' - total: {total}")


if __name__ == "__main__":
    typer.run(main)
