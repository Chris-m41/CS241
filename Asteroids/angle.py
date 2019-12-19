import arcade
import random


class Angle:

    def __init__(self):
        pass

    def generate_angle(self, start):
        """
        The object will pass  in random start number
        This number will decide which side of the screen the
        astroid will spawn at.

        This function will return an appropriate angle
        that the astroid should start will with.
        """

        # left side
        if start == 1:
            return random.randint(-30, 30)
        # right side
        elif start == 2:
            return random.randint(150, 210)
        # bottom
        elif start == 3:
            return random.randint(60, 120)
        # top
        else:
            return random.randint(240, 300)