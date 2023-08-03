from ball import *

from itertools import product

import numpy as np


class Box:

    balls: dict[Smooth, dict[Color, list[int]] | np.ndarray]

    def __init__(self, balls: list[Ball]):

        self.balls = {
            Smooth.SMOOTH: {
                Color.RED: [],
                Color.GREEN: [],
                Color.BLUE: []
            },
            Smooth.ROUGH: {
                Color.RED: [],
                Color.GREEN: [],
                Color.BLUE: []
            }
        }

        for ball in balls:
            self.balls[ball["smooth"]][ball["color"]].append(ball["id"])

        for smooth, color in product(smooths, colors):
            self.balls[smooth][color] = np.array(self.balls[smooth][color])

    def get_ball(self) -> Ball:
        smooth = choice_smooth()
        color = choice_color()
        return {
            "id": np.random.choice(self.balls[smooth][color]),
            "smooth": smooth,
            "color": color
        }
