import random


class Point:

    def __init__(self):
        # this will be generating the center for the object.
        self.x = 0
        self.y = 0

    def generate_asteroid_x(self, start):
        """
        The object will pass  in random start number
        This number will decide which side of the screen the
        asteroid will spawn at.
        This function will return the x point.
        """
        # left side
        if start == 1:
            return 0
        # right side
        elif start == 2:
            return 800
        # bottom
        elif start == 3:
            return random.randint(50, 750)
        # top
        else:
            return random.randint(50, 750)

    def generate_asteroid_y(self, start):
        """
        The object will pass  in random start number
        This number will decide which side of the screen the
        asteroid will spawn at.
        This function will return the y point.
        """
        # left side
        if start == 1:
            return random.randint(50, 550)
        # right side
        elif start == 2:
            return random.randint(50, 550)
        # bottom
        elif start == 3:
            return 0
        # top
        else:
            return 600