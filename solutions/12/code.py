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
    graph = nx.DiGraph()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            pos = grid[row][col]
            value = MAPPING[pos]
            if pos in ("S", "E"):
                name = pos
            else:
                name = f"{row},{col}"
            for horz, vert in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                try:
                    if (row + horz < 0) or (col + vert < 0):
                        continue
                    neighbor_pos = grid[row + horz][col + vert]
                    neighbor_value = MAPPING[neighbor_pos]
                    if neighbor_pos in ("S", "E"):
                        neighbor_name = neighbor_pos
                        # if neighbor_pos == "E":
                        #     graph.add_edge(name, neighbor_name)
                        #     continue
                    else:
                        neighbor_name = f"{row + horz},{col + vert}"
                    if abs(neighbor_value - value) <= 1:
                        graph.add_edge(name, neighbor_name)
                        graph.add_edge(neighbor_name, name)
                except IndexError:
                    continue
    return graph


def main(path: str):
    grid = load_grid(path)
    graph = populate_graph(grid)
    length = nx.shortest_path_length(graph, "S", "E")
    print(f"Shortest path length is {length}")


if __name__ == "__main__":
    typer.run(main)
