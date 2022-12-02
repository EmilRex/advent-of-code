import typer

POINTS_MAP = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissor
}

OUTCOMES_MAP = {
    "X": {
        "C": "win",
        "B": "lose",
        "A": "draw",
    },
    "Y": {
        "A": "win",
        "C": "lose",
        "B": "draw",
    },
    "Z": {
        "B": "win",
        "A": "lose",
        "C": "draw",
    },
}


def calculate_score(opp_shape, my_shape):
    shape_points = POINTS_MAP[my_shape]

    outcome = OUTCOMES_MAP[my_shape][opp_shape]
    if outcome == "win":
        return shape_points + 6
    elif outcome == "lose":
        return shape_points + 3
    elif outcome == "draw":
        return shape_points


def main(path: str):
    round = 0
    total_score = 0

    with open(path, "r") as fh:
        while True:
            round += 1
            line = fh.readline()

            if line == "":
                break

            opp_shape, my_shape = line.strip().split(" ")
            round_score = calculate_score(opp_shape, my_shape)
            total_score += round_score
            print(
                f"[Round {round}] {opp_shape} vs {my_shape} - round:{round_score} total:{total_score}"
            )


if __name__ == "__main__":
    typer.run(main)
