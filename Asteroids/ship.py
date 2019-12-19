from flyingObject import FlyingObject
import arcade
import math
from globals import *


class Ship(FlyingObject):

    def __init__(self):
        super().__init__()
        self.center.x = 400
        self.center.y = 300
        self.thrust = SHIP_THRUST_AMOUNT
        self.rotation = 0
        self.texture1 = arcade.load_texture("images/playerShip1_orange.png")
        self.width = 40
        self.height = 35
        self.radius = SHIP_RADIUS
        self._health = SHIP_HEALTH

    def ignite_thrusters(self):
        self.velocity.dx += math.cos(math.radians(self.rotation + 90)) * self.thrust
        self.velocity.dy += math.sin(math.radians(self.rotation + 90)) * self.thrust

    def check_state(self, frame):
        # makes the ship transparent when the ship
        # was recently hit. Helps the player to know
        # when their invincibility runs out
        if frame < 40:
            self.alpha = .3
        else:
            self.alpha = 1

        # if health at 0 then kill it
        if self.health == 0:
            self.alive = False

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        if health < 0:
            self._health = 0
        else:
            self._health = health


class Ship_Thrusters(Ship):

    def __init__(self):
        super().__init__()
        # Exact same ship, but with a different texture that has thrusters
        self.texture = arcade.load_texture("images/playerShip1_Thruster.png")