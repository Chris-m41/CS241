import arcade
import random
from point import Point
from velocity import Velocity
from globals import *


class FlyingObject:
    """
    This is a base class for all flying objects (lasers and ship and astroids)
    """

    def __init__(self):
        self.center = Point()  # initially 0 for x and y
        self.velocity = Velocity()  # initially 0 for dx and dy
        self.alive = True  # always start being alive
        self.height = 0  # figure height
        self.width = 0  # figure width
        self.texture = arcade.load_texture("images/playerShip1_orange.png")  # import the texture
        self.rotation = 0  # how much the figure is rotation
        self.alpha = 1000  # will not be transparent
        self.radius = 0
        # self.color = (0,200,50)    # this was used hit box detection

    def draw(self):
        # display the figure
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture,
                                      self.rotation, self.alpha)

        # used to check hit boxes
        # get rid of hash tags to check it out
        # arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, self.color)

    def check_wrap(self):
        """
        Every flying object will wrap.
        meaning that if goes off the screen it will
        move to another side of the screen
        """

        if self.center.y > SCREEN_HEIGHT:
            # move it to the bottom
            self.center.y = 0

        if self.center.y < 0:
            # move it the top
            self.center.y = SCREEN_HEIGHT

        if self.center.x > SCREEN_WIDTH:
            # move it to the left
            self.center.x = 0

        if self.center.x < 0:
            # move it to the right
            self.center.x = SCREEN_WIDTH

    def advance(self):
        # change the position by adding velocity
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy