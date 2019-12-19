"""
File: asteroids.py
Original Author: Br. Burton
Implemented and imporved by Jacob Jashinsky
"""
import arcade
import math
import random
from laser import Laser
from ship import *
from asteroid import *
from globals import *


class Game(arcade.Window):
    """
    This class handles all  the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    """

    """
    Extras Added:

    Ship has health and is displayed on screen

    Ship can get hurt by your own laser

    Ship shoots in the direction of the mouse

    Increase ship velocity with space bar in
    the direction ship is facing

    Ship has glowing thrusters when the space bar is pressed

    You move ship direction with mouse location

    Ship has invincibility for a time after it is hit

    Big asteroids take 2 hits to split

    The game can restart the game after the player won or died

    Astroids always spawn at the sides of the screens

    Improved hit box detection

    Added optional graphics to show the hit boxes 

    Added game intro screen

    Game ends when asteroids are all cleared or when player dies

    A different screen appears when player dies or wins.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.held_keys = set()

        # create a ship
        self.ship = Ship()

        # create a ship that has thrusters
        self.ship_thrusters = Ship_Thrusters()

        # this will be used to determine when to draw the ship with thrusters
        self.draw_thrust = 0

        # list for all asteroids
        self.asteroids = []

        # start at with 5 asteroids incoming
        self.create_asteroids()

        # list for all lasers
        self.lasers = []

        # keeps track of frame count
        self.frame = 0

        # keeps track of delta time
        self.remember_time = 0

        # the state of the game
        # starts with the game intro
        self.current_state = GAME_INTRO

    def frame_count(self):
        """
        This function counts the frames
        """
        self.frame += 1

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # if self.draw_thrust has a value of 1 or more then draw the
        # ship with thrusters
        if self.draw_thrust > 0 and self.current_state != GAME_DEATH:
            self.ship_thrusters.draw()

        # draws ship
        # will stop drawing the ship when
        # the player loses the game
        if self.current_state != GAME_DEATH:
            self.ship.draw()

            # draw each laser in laser list
            for laser in self.lasers:
                laser.draw()

        # calls function to draw health on screen
        self.draw_health()

        # draw the intro to the game
        if self.current_state == GAME_INTRO:
            self.draw_warning()

        # move the asteroids when the game is the running state
        # or when the player dies.
        if self.current_state == GAME_RUN or self.current_state == GAME_DEATH:
            # goes through the asteroid list and draws them
            for asteroid in self.asteroids:
                asteroid.draw()

        # if current state of the game is death
        # then display the death screen
        if self.current_state == GAME_DEATH:
            self.draw_end()

        # if the player wins
        # then display the win screen
        if self.current_state == GAME_WIN:
            self.draw_win()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.remember_time += delta_time

        # count the frame
        self.frame_count()

        # calls the check wrap function
        # dont wrap when the game ends.
        # Acts as if the ship "left the screen"
        if self.current_state != GAME_WIN:
            self.check_wrap()

        # advance the lasers
        for laser in self.lasers:
            laser.advance()

        # advance the ship
        self.ship.advance()

        # now advance the ship with thrusters
        self.ship_thrusters.advance()

        if self.draw_thrust > 0:
            # if we should be drawing the thrusters
            # then add 1 each time the update function is called
            self.draw_thrust += 1
            if self.draw_thrust == 10:
                # now if it goes to 10 then set it to zero
                # so it doesn't draw again untill the space is pressed.
                self.draw_thrust = 0

        # switches from intro state to run state after 4 seconds
        if self.remember_time > 4 and self.current_state != GAME_WIN:
            self.current_state = GAME_RUN

        # only advance the asteroids and create asteroids
        # if the state is in run mode
        if self.current_state == GAME_RUN:

            # advance the asteroids
            for asteroid in self.asteroids:
                asteroid.advance()
                asteroid.spin()

            # see if a new asteroid should be added
            self.create_asteroid()

        # check collisions
        self.check_collisions()

        # update the current state of the ship
        self.ship.check_state(self.frame)

        # finally we clean up any dead objects
        self.clean_up_objects()

    def create_asteroids(self):
        """
        Creates 5 asteroids and adds it to the list.
        To be called in the init at the start of the game
        """

        for i in range(1, 6):
            self.asteroids.append(BigAsteroid())

    def create_asteroid(self):
        """
        Creates a new big asteroid and adds it to the list.
        with 1/1200 probability. onkly creates big asteroids
        """
        if random.randint(1, 1200) == 1:
            self.asteroids.append(BigAsteroid())

    def check_wrap(self):
        """
        goes through every object and calls their check wrap function
        """

        for asteroid in self.asteroids:
            asteroid.check_wrap()

        for laser in self.lasers:
            laser.check_wrap()

        self.ship.check_wrap()
        self.ship_thrusters.check_wrap()

    def check_collisions(self):
        """
        Checks to see if lasers have hit asteroids.
        then
        Checks to see if asteroids have hit the ship.
        then
        Checks to see if lasers have hit the ship.
        """

        for laser in self.lasers:
            for asteroid in self.asteroids:

                # Make sure they are both alive before checking for a collision
                if laser.alive and asteroid.alive:
                    too_close = laser.radius + asteroid.radius

                    if ((laser.center.x - asteroid.center.x) ** 2 + (
                            laser.center.y - asteroid.center.y) ** 2) ** .5 < too_close:
                        # its a hit!
                        laser.alive = False
                        list = asteroid.split()
                        self.asteroids += list

        for asteroid in self.asteroids:
            # Make sure they are both alive before checking for a collision
            if self.ship.alive and asteroid.alive:
                too_close = self.ship.radius + asteroid.radius
                if ((self.ship.center.x - asteroid.center.x) ** 2 + (
                        self.ship.center.y - asteroid.center.y) ** 2) ** .5 < too_close:
                    # its a hit!
                    if self.frame > 40:
                        hit_points = asteroid.hit_ship()
                        self.ship.health -= hit_points
                        self.frame = 0

        for laser in self.lasers:
            # Make sure they are both alive before checking for a collision
            if self.ship.alive and laser.alive and laser.time_alive > 30:
                too_close = self.ship.radius + laser.radius
                if ((self.ship.center.x - laser.center.x) ** 2 + (
                        self.ship.center.y - laser.center.y) ** 2) ** .5 < too_close:
                    # its a hit!
                    laser.alive = False

                    # if the ship has not been hit in the
                    # past 30 frames then it can be hit
                    # INVICIBILITY!
                    if self.frame > 30:
                        hit_points = laser.hit_ship()
                        self.ship.health -= hit_points
                        self.frame = 0

    def clean_up_objects(self):
        """
        Goes through every object within the list
        and checks if they are dead and need to be removed
        Also checks to see if the player had died or won.
        """

        for laser in self.lasers:
            # checks to see if the lasers have passed their
            # 60 frames limit
            laser.check_alive()
            if laser.alive == False:
                self.lasers.remove(laser)

        for asteroid in self.asteroids:
            if asteroid.alive == False:
                self.asteroids.remove(asteroid)

        if self.ship.alive == False:
            self.current_state = GAME_DEATH
        elif not self.asteroids:
            self.current_state = GAME_WIN

    def on_key_press(self, key, key_modifiers):
        # ignite thrusters when space is pressed
        if key == arcade.key.SPACE:
            self.ship.ignite_thrusters()
            self.ship_thrusters.ignite_thrusters()

            # set draw_thrust to 1 so that the draw function is
            # given the okay to draw. It will be turned off after 10 frames
            self.draw_thrust = 1

        # if player has died or won the game and the mouse is pressed then call the restart function
        if key == arcade.key.RETURN and (self.current_state == GAME_DEATH or self.current_state == GAME_WIN):
            self.restart()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # tracks mouse motion
        # set the ship and laser angle in degrees
        self.ship.rotation = self.get_angle_degrees(x, y)
        self.ship_thrusters.rotation = self.get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!

        # grabs the current angle between the ship and mouse
        angle = self.get_angle_degrees(x, y) + 90

        # creates a laser object using information from the ship
        laser = Laser(angle, self.ship.center.x, self.ship.center.y, self.ship.velocity.dx, self.ship.velocity.dy)

        # adds it to the list
        self.lasers.append(laser)

    def get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        """
        # get the angle in radians
        angle_radians = math.atan2(y - self.ship.center.y, x - self.ship.center.x)

        # convert to degrees
        # converted to degrees because the ship and laser class needs degrees
        angle_degrees = math.degrees(angle_radians) - 90

        return angle_degrees

    def restart(self):
        """
        This will restart the game when enter is pressed.
        """

        # clear asteroids
        self.asteroids.clear()

        # create a new ship
        self.ship = Ship()

        # create a new ship that has thrusters
        self.ship_thrusters = Ship_Thrusters()

        # reset to 0
        self.draw_thrust = 0

        # start at with 5 asteroids incoming
        self.create_asteroids()

        # clear list
        self.lasers.clear()

        # restart frame count
        self.frame = 0

        # restart time
        self.remember_time = 0

        # goes back to the game intro
        self.current_state = GAME_INTRO

    def draw_health(self):
        arcade.draw_rectangle_filled(400, 590, self.ship.health * 10, 10, arcade.color.FIREBRICK)
        arcade.draw_rectangle_outline(400, 590, 150, 10, arcade.color.WHITE)
        arcade.draw_text("Hull Integrity:", start_x=215, start_y=SCREEN_HEIGHT - 15, font_size=12,
                         color=arcade.color.WHITE)

    def draw_warning(self):
        """
        draws the warning screen
        """
        output2 = "WARNING!"
        output3 = "...Asteroids Incoming..."

        arcade.draw_text(output2, 240, 450, arcade.color.FIREBRICK, 54)
        arcade.draw_text(output3, 160, 350, arcade.color.FIREBRICK, 40)

    def draw_end(self):
        """
        draws the death screen
        """
        output4 = "ERROR!"
        output5 = "SYSTEM FAILURE"
        output6 = "You Died"
        output10 = "Try Again?\nPress Enter"

        arcade.draw_text(output4, 320, 400, arcade.color.FIREBRICK, 40)
        arcade.draw_text(output5, 310, 300, arcade.color.FIREBRICK, 20)
        arcade.draw_text(output6, 350, 200, arcade.color.FIREBRICK, 20)
        arcade.draw_text(output10, 340, 100, arcade.color.WHITE, 20)

    def draw_win(self):
        """
        draws the winning screen
        """
        output7 = "ASTEROIDS CLEARED!"
        output8 = "PROCEED TO YOUR MISSION"
        output9 = "You Win"
        output10 = "Try Again?\nPress Enter"

        arcade.draw_text(output7, 180, 400, arcade.color.FIREBRICK, 40)
        arcade.draw_text(output8, 175, 300, arcade.color.FIREBRICK, 30)
        arcade.draw_text(output9, 355, 200, arcade.color.FIREBRICK, 20)
        arcade.draw_text(output10, 340, 100, arcade.color.WHITE, 20)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()