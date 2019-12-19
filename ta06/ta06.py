class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def prompt_for_point(self):
        self.x = input("Enter x: ")
        self.y = input("Enter y: ")

    def display(self):
        print("\nCenter: ")
        print("({},{})".format(self.x,self.y))

class Circle(Point):
    def __init__(self):
        super().__init__()
        self.radius = 0

    def prompt_for_circle(self):
        self.prompt_for_point()
        self.radius = input("Enter radius: ")

    def display(self):
        super().display()
        print("Radius: {}".format(self.radius))

def main():
    p = Point()
    c = Circle()

    c.prompt_for_circle()
    c.display()

if __name__ == "__main__":
    main()