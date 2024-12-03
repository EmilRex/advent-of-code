import typer

S1_MAP = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissor
}

S2_MAP = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
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

OUTCOMES_POINTS_MAP = {
    "win": 6,
    "lose": 0,
    "draw": 3,
}


def calculate_score(opp_shape, my_shape, strategy):
    if strategy == 1:
        outcome = OUTCOMES_MAP[my_shape][opp_shape]
        shape_points = S1_MAP[my_shape]
    elif strategy == 2:
        outcome = S2_MAP[my_shape]
        for i, n in OUTCOMES_MAP.items():
            for j, m in n.items():
                if j == opp_shape and m == outcome:
                    expected_shape = i
                    break
        shape_points = S1_MAP[expected_shape]
    else:
        raise ValueError(f"Invalid strategy '{strategy}'")

    outcome_points = OUTCOMES_POINTS_MAP[outcome]
    return shape_points + outcome_points


def main(path: str, strategy: int):
    round = 0
    total_score = 0

    with open(path, "r") as fh:
        while True:
            round += 1
            line = fh.readline()

            if line == "":
                break

            opp_shape, my_shape = line.strip().split(" ")
            round_score = calculate_score(opp_shape, my_shape, strategy)
            total_score += round_score
            print(
                f"[Round {round}] {opp_shape} vs {my_shape} - round:{round_score} total:{total_score}"
            )


if __name__ == "__main__":
    typer.run(main)
