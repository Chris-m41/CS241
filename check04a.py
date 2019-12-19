class Person:
    def __init__(self):
        self.name = "Anonymous"
        self.year = "Unknown"

    def display(self):
        print("{} (b. {})".format(self.name, self.year))


class Book:
    def __init__(self):
        self.title = "Untitled"
        self.author = Person()
        self.publisher = "unpublished"

    def display(self):
        print(self.title)
        print("Publisher: ")
        print(self.publisher)
        print("Author: ")
        self.author.display()


def main():
    b = Book()
    b.display()
    print("\n")
    print("Please enter the following: ")
    b.author.name = input("Name: ")
    b.author.year = input("Year: ")
    b.title = input("Title: ")
    b.publisher = input("Publisher: ")
    print("\n")
    b.display()


if __name__ == "__main__":
    main()
