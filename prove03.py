class Robot:
    # Initializing variables
    def __init__(self):
        self.x = 10
        self.y = 10
        self.fuel_amount = 100

    # Moves up
    def move_up(self):
        # Checks if there is enough fuel
        # if no fuel
        if self.fuel_amount < 15:
            print("Insufficient fuel to perform action")
        # If there is sufficient fuel
        else:
            self.y -= 1
            self.fuel_amount -= 5

    # Moves down
    def move_down(self):
        # Checks if there is enough fuel
        # if no fuel
        if self.fuel_amount < 15:
            print("Insufficient fuel to perform action")
        # If there is sufficient fuel
        else:
            self.y += 1
            self.fuel_amount -= 5

    # Moves down
    def move_left(self):
        # Checks if there is enough fuel
        # if no fuel
        if self.fuel_amount < 15:
            print("Insufficient fuel to perform action")
        # If there is sufficient fuel
        else:
            self.x -= 1
            self.fuel_amount -= 5

    # Moves Right
    def move_right(self):
        # Checks if there is enough fuel
        # if no fuel
        if self.fuel_amount < 15:
            print("Insufficient fuel to perform action")
            # If there is sufficient fuel
        else:
            self.x += 1
            self.fuel_amount -= 5

    # Fires laser
    def fire(self):
        # Checks if there is enough fuel
        # if no fuel
        if self.fuel_amount < 15:
            print("Insufficient fuel to perform action")
        # If there is sufficient fuel
        else:
            self.fuel_amount -= 15
            print("Pew! Pew!")

    # Displays current status
    def status(self):
        print("({},{}) - Fuel: {}".format(self.x, self.y, self.fuel_amount))


def main():
    robot = Robot() # Call Robot class
    choice = None
    while choice != "quit":

        choice = input("Enter command: ")
        if choice == "up":
            robot.move_up()
        elif choice == "down":
            robot.move_down()
        elif choice == "left":
            robot.move_left()
        elif choice == "right":
            robot.move_right()
        elif choice == "status":
            robot.status()
        elif choice == "fire":
            robot.fire()
    print("Goodbye.")


if __name__ == "__main__":
    main()
