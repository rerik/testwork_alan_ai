from ball import *

from random import choice


class Box:

    balls: dict[Smooth, dict[Color, list[Ball]]]

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
            self.balls[ball["smooth"]][ball["color"]].append(ball)

    def get_ball(self) -> Ball:
        smooth = choice_smooth()
        color = choice_color()
        return choice(self.balls[smooth][color])
