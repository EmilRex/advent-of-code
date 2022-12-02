import typer


def calculate_score(opp_shape, my_shape):
    points_map = {
        "A": 1, # Rock
        "B": 2, # Paper
        "C": 3, # Scissor
        "X": 1, # Rock
        "Y": 2, # Paper
        "Z": 3, # Scissor
    }
    my_points = points_map[my_shape]
    opp_points = points_map[opp_shape]

    # Draw
    if my_points == opp_points:
        return my_points + 3

    # Rock
    if my_shape == "X":
        # Beats scissor
        if opp_shape == "C":
            return my_points + 6
        # Loses to Paper
        return my_points

    # Paper
    if my_shape == "Y":
        # Beats rock
        if opp_shape == "A":
            return my_points + 6
        # Loses to scissor
        return my_points

    # Scissor
    if my_shape == "Z":
        # Beats paper
        if opp_shape == "B":
            return my_points + 6
        # Loses to rock
        return my_points


def main(path: str):
    round = 0
    total_score = 0

    with open(path, "r") as fh:
        while True:
            round += 1
            line = fh.readline()

            if line == '':
                break

            opp_shape, my_shape = line.strip().split(" ")
            round_score = calculate_score(opp_shape, my_shape)
            total_score += round_score
            print(f"[Round {round}] {opp_shape} vs {my_shape} - round:{round_score} total:{total_score}")


if __name__ == "__main__":
    typer.run(main)
