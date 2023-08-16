import random
import time
from random import randint


def main() -> None:
    lb, ub = 10, 70  # borders
    line_count = 5

    random.seed()
    minpos = lb + 1
    maxpos = ub - 1
    stars = []
    for _ in range(line_count):
        stars.append(randint(minpos, maxpos))
    line = [" "] * (ub + 1)
    line[lb] = line[ub] = "│"
    try:
        while True:
            unique_stars = set(stars)
            for i in unique_stars:
                line[i] = "*"
            print("".join(line))
            for i in unique_stars:
                line[i] = " "

            for i, pos in enumerate(stars):
                if pos == minpos:
                    stars[i] += randint(0, 1)
                elif pos == maxpos:
                    stars[i] += randint(-1, 0)
                else:
                    stars[i] += randint(-1, 1)

            time.sleep(0.04)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
