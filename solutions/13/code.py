import typer


def compare(left, right):
    # print(f"\tComparing {left} to {right}")
    # First condition
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
    # Third condition
    if isinstance(left, list) and isinstance(right, int):
        right = [right]
    if isinstance(left, int) and isinstance(right, list):
        left = [left]
    # Second condition
    if isinstance(left, list) and isinstance(right, list):
        for i in range(max(len(left), len(right))):
            if len(left) != len(right):
                if i == len(left):
                    return True
                if i == len(right):
                    return False
            result = compare(left[i], right[i])
            if result is not None:
                return result


def main(path: str):
    idx = 0
    total = 0
    packets = []

    with open(path, "r") as fh:
        while True:
            idx += 1
            left, right, space = (fh.readline().strip() for _ in range(3))

            if left == right == "":
                break

            left, right = eval(left), eval(right)

            packets.extend([left, right])

            correct = compare(left, right)
            if correct:
                total += idx

            print(f"[{idx}] {correct} - {left}, {right}")

    print(f"Total is {total}\n")

    # Sort packets
    ordered = [[[2]], [[6]]]
    for packet in packets:
        for idx, item in enumerate(ordered):
            if compare(packet, item):
                ordered.insert(idx, packet)
                break
        else:
            ordered.append(packet)

    print(f"Index for [[2]] is {ordered.index([[2]]) + 1}")
    print(f"Index for [[6]] is {ordered.index([[6]]) + 1}")


if __name__ == "__main__":
    typer.run(main)
