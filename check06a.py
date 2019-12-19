class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 0

    def prompt_book_info(self):
        self.title = input("Enter Title: ")
        self.author = input("Enter Author: ")
        self.publication_year = input("Enter Publication Year: ")

    def display_book_info(self):
        print("{} ({}) by {}".format(self.title,self.publication_year, self.author))

class TextBook(Book):
    def __init__(self):
        self.subject = ""

    def prompt_subject(self):
        self.subject = input("Enter Subject: ")

    def display_subject(self):
        print("Subject: {}".format(self.subject))

class PictureBook(Book):
    def __init__(self):
        self.illustrator = ""

    def prompt_illustrator(self):
        self.illustrator = input("Enter Illustrator: ")

    def display_illustrator(self):
        print("Illustrator {}".format(self.illustrator))


def main():
    b = Book()
    t = TextBook()
    p = PictureBook()

    b.prompt_book_info()
    print()
    b.display_book_info()
    print()

    t.prompt_book_info()
    t.prompt_subject()
    t.display_book_info()
    print()
    t.display_subject()
    print()

    p.prompt_book_info()
    p.prompt_illustrator()
    p.display_book_info()
    print()
    p.display_illustrator()

if __name__ == "__main__":
    main()
