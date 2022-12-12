import string

import networkx as nx
import typer

MAPPING = {
    l: n
    for l, n in zip(string.ascii_lowercase, range(1, len(string.ascii_lowercase) + 1))
}
MAPPING["S"] = 1
MAPPING["E"] = 26


def load_grid(path: str):
    grid = []
    with open(path, "r") as fh:
        for line in fh:
            line = line.strip()
            grid.append([i for i in line])
    return grid


def populate_graph(grid):
    start, end = None, None
    graph = nx.DiGraph()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            pos = grid[row][col]
            value = MAPPING[pos]
            name = f"{row},{col}"
            if pos == "S":
                start = name
            if pos == "E":
                end = name
            for horz, vert in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (
                    (row + horz < 0)
                    or (col + vert < 0)
                    or (row + horz >= len(grid))
                    or (col + vert >= len(grid[0]))
                ):
                    continue
                neighbor_pos = grid[row + horz][col + vert]
                neighbor_value = MAPPING[neighbor_pos]
                neighbor_name = f"{row + horz},{col + vert}"
                if neighbor_value - value <= 1:
                    graph.add_edge(name, neighbor_name)
    return graph, start, end


def main(path: str):
    grid = load_grid(path)
    graph, start, end = populate_graph(grid)
    length = nx.shortest_path_length(graph, start, end)
    print(f"Shortest path from 'S' to 'E' is {length} steps")

    lenghts = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            pos = grid[row][col]
            name = f"{row},{col}"

            if pos == "a":
                try:
                    lenghts.append(nx.shortest_path_length(graph, name, end))
                except Exception:
                    pass
    print(f"Shortest path from any 'a' to 'E' is {min(lenghts)}")


if __name__ == "__main__":
    typer.run(main)
