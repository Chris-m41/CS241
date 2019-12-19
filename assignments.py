from date import Date


class Assignments:
    def __init__(self):
        self.name = "Untitled"
        self.start_date = Date()
        self.due_date = Date()
        self.end_date = Date()
        self.long_display = Date

    def prompt(self):
        self.name = input("Enter Name: ")

        print("Start Date: ")
        self.start_date.prompt()

        print("Due date: ")
        self.due_date.prompt()

        print("End date: ")
        self.end_date.prompt()

    def display(self):
        print("Assignment: {}".format(self.name))
        print("Start Date: ")
        self.start_date.display()
        print("Due Date: ")
        self.due_date.display()
        print("End Date: ")
        self.end_date.display()
        self.long_display


