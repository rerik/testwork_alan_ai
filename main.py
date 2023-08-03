from ball import Ball, create_balls
from box import Box

import pandas as pd

from sys import getsizeof
from time import perf_counter


def stats(balls: list[Ball]):
    df = pd.DataFrame(balls)
    print(df["smooth"].value_counts(normalize=True))
    print(df["color"].value_counts(normalize=True))


BALLS = 1_000_000
GETS = 10_000_000

if __name__ == '__main__':

    all_balls = create_balls(BALLS)
    box = Box(all_balls)

    start = perf_counter()
    got_balls = [box.get_ball() for _ in range(GETS)]
    stop = perf_counter()

    print("All balls:")
    stats(all_balls)

    print()
    print("Got balls:")
    stats(got_balls)

    print()
    print(f"Memory used: {getsizeof(all_balls) + getsizeof(box)} bytes")
    print(f"Time of getting balls: {(stop - start)*1000: .2f} ms")
