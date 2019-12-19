import arcade
import math
from globals import *
from flyingObject import FlyingObject

"""
This is the laser class, to be fired from the ship.
Inherited most attibutes and methods from FlyingObject
"""


class Laser(FlyingObject):

    def __init__(self, angle, x, y, dx, dy):
        # angle: same angle as the ship's
        # x, y: same position as the ship's

        super().__init__()
        self.center.x = x
        self.center.y = y
        self.rotation = angle  # receives angle (to be used for speed)
        self.ship_dx = dx
        self.ship_dy = dy
        self.velocity.dx = math.cos(math.radians(self.rotation)) * LASER_SPEED  # + self.ship_dx
        self.velocity.dy = math.sin(math.radians(self.rotation)) * LASER_SPEED  # + self.ship_dx
        # I decided that for my game I did not want to add ship speed to
        # to the velocty of the lasers. I wanted the lasers to always
        # have a constant velocity. However, I have shown above that I
        # know how to implement it. you only need to get rid of the hastag
        # in the top two lines of code to make it work.
        self.texture = arcade.load_texture("images/laserBlue01.png")
        self.width = 25
        self.height = 6
        self.time_alive = 0.0  # used to keep track how long laser has been alive
        self.radius = LASER_RADIUS

    def check_alive(self):
        # this function is called every frame
        # it will add one.
        self.time_alive += 1

        # lasers will only last for the 60 frames.
        if self.time_alive > LASER_LIFE:
            self.alive = False

    def hit_ship(self):
        # does 7 damage to the ship
        return 7