class Phone:
    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    def prompt_number(self):
        self.area_code = input("Area Code: ")
        self.prefix = input("Prefix: ")
        self.suffix = input("Suffix: ")

    def display(self):
        print("Phone info: ")
        print("({}){}-{}".format(self.area_code,self.prefix,self.suffix))

class SmartPhone(Phone):
    def __init__(self):
        super().__init__()
        self.email = ""

    def prompt(self):
        self.prompt_number()
        self.email = input("Email: ")

    def display(self):
        super().display()
        print("Email: {}".format(self.email))

def main():
    p = Phone()
    s = SmartPhone()

    print("Phone:")
    p.prompt_number()
    print()
    p.display()
    print()

    print("Smart phone")
    s.prompt()
    print()
    s.display()

if __name__ == "__main__":
    main()