from fractions import Fraction

class Rational:
    def __init__(self):
        self.top = 0
        self.bottom = 1

    def display(self):
        if self.top/self.bottom < 1:
            print("{}/{}".format(self.top, self.bottom))
        else:
            whole = self.top // self.bottom
            new_top = self.top % self.bottom
            print("{} {}/{}".format(int(whole),int(new_top),int(self.bottom)))


    def prompt(self):
        self.top = float(input("Enter a numerator: "))
        self.bottom = float(input("Enter a denominator: "))

    def display_decimal(self):
        decimal = self.top / self.bottom
        print(decimal)

    def reduce(self):
        f = Fraction(int(self.top),int(self.bottom))
        print(f)

    def multiply_by(self):
        n_top = int(input("Enter new numerator"))
        n_bottom = int(input("Enter new denominator"))
        a_top = int(n_top * self.top)
        a_bottom = int(n_bottom * self.bottom)
        f = Fraction(a_top,a_bottom)
        print(f)




def main():
    r = Rational()
    r.display()
    r.prompt()
    r.display()
    r.display_decimal()
    r.reduce()
    r.multiply_by()


if __name__ == "__main__":
    main()
