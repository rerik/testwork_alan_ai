from enum import Enum
from typing import TypedDict
from random import choice, choices


class Smooth(Enum):
    SMOOTH = .35
    ROUGH = .65


class Color(Enum):
    RED = .50
    GREEN = .30
    BLUE = .20


class Ball(TypedDict):
    id: int
    smooth: Smooth
    color: Color


smooths = list(Smooth)
colors = list(Color)

smooth_p = [smooth.value for smooth in Smooth]
color_p = [color.value for color in Color]


def choice_smooth() -> Smooth:
    return choices(population=smooths, weights=smooth_p, k=1)[0]


def choice_color() -> Color:
    return choices(population=colors, weights=color_p, k=1)[0]


def random_ball(id: int = 0) -> Ball:
    return {
        "id": id,
        "smooth": choice(smooths),
        "color": choice(colors)
    }


def create_balls(n: int = 1) -> list[Ball]:
    return [random_ball(i) for i in range(n)]


if __name__ == '__main__':

    b: Ball = {
        "id": 1,
        "smooth": Smooth.SMOOTH,
        "color": Color.RED
    }
    print(b)

    rb = random_ball()
    print(rb)

    rbs = create_balls(5)
    print()
    for ball in rbs:
        print(ball)
