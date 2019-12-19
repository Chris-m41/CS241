from flyingObject import FlyingObject
import arcade
from globals import *
import math
import arcade
import random
from angle import Angle
from abc import abstractmethod
from abc import ABC


class Asteroid(FlyingObject, ABC):
    """
    This class inherits from FLyingObject.
    This is the base class for all other asteroids.
    """

    def __init__(self):
        super().__init__()
        # this decides which side of the screen to spawn at.
        self.start = random.randint(1, 4)

        # uses the function from point to find the x and y
        self.center.x = self.center.generate_asteroid_x(self.start)
        self.center.y = self.center.generate_asteroid_y(self.start)

        # uses angle object and its methods
        # to find the direction it should go
        angle = Angle()
        self.direction = angle.generate_angle(self.start)

        # uses the direction to get the correct speed
        self.velocity.dx = math.cos(math.radians(self.direction)) * BIG_ROCK_SPEED
        self.velocity.dy = math.sin(math.radians(self.direction)) * BIG_ROCK_SPEED

        self.radius = BIG_ROCK_RADIUS

        # starts at 0, but this will increase as the astroids advance
        self.rotation = 0

        self.dr = 1

        self.texture = arcade.load_texture("images/meteorGrey_big1.png")
        self.width = 50
        self.height = 50

    def spin(self):
        self.rotation += self.dr

    @abstractmethod
    def split(self):
        # this will be implemented in the child classes
        pass

    @abstractmethod
    def hit_ship(self):
        # this will be implemented in the child classes
        pass


class BigAsteroid(Asteroid):

    def __init__(self):
        super().__init__()
        # takes two hits to kill
        self.health = 2
        self.dr = BIG_ROCK_SPIN

    def split(self):
        # takes one away from health
        self.health -= 1

        # checks if the astorid is dead
        if self.health == 0:
            # when the laser hits the astroid, it will split and
            # produce two medium and 1 small astroid.
            # velocity is changed from the orginal astroid
            list = [MediumAsteroid(self.center.x, self.center.y, self.velocity.dx, self.velocity.dy + 2),
                    MediumAsteroid(self.center.x, self.center.y, self.velocity.dx, self.velocity.dy - 2),
                    SmallAsteroid(self.center.x, self.center.y, self.velocity.dx + 5, self.velocity.dy)]
            # kills it
            self.alive = False

        else:
            list = []

        # either returns the new astroids or an empty list
        return list

    def hit_ship(self):
        # does 8 damage to the ship
        return 6


class MediumAsteroid(Asteroid):

    def __init__(self, x, y, dx, dy):
        super().__init__()
        self.center.x = x
        self.center.y = y
        self.velocity.dx = dx
        self.velocity.dy = dy
        self.radius = MEDIUM_ROCK_RADIUS
        self.texture = arcade.load_texture("images/meteorGrey_med1.png")
        self.width = 35
        self.height = 35
        self.dr = MEDIUM_ROCK_SPIN

    def split(self):
        list = [SmallAsteroid(self.center.x, self.center.y, self.velocity.dx + 1.5, self.velocity.dy + 1.5),
                SmallAsteroid(self.center.x, self.center.y, self.velocity.dx - 1.5, self.velocity.dy - 1.5), ]
        # kill it
        self.alive = False

        # returns a list of two small asteroids
        # when it is hit by a laser
        return list

    def hit_ship(self):
        # does 5 damage to the ship
        return 5


class SmallAsteroid(Asteroid):

    def __init__(self, x, y, dx, dy):
        super().__init__()
        self.center.x = x
        self.center.y = y
        self.velocity.dx = dx
        self.velocity.dy = dy
        self.radius = SMALL_ROCK_RADIUS
        self.texture = arcade.load_texture("images/meteorGrey_small1.png")
        self.width = 22
        self.height = 22
        self.dr = SMALL_ROCK_SPIN

    def split(self):
        # asteroid is done splitting
        list = []

        # kill it
        self.alive = False

        # returns an empty list
        return list

    def hit_ship(self):
        # does only damage of 2 to ship
        return 3