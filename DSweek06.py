from collections import deque


class Student:
    def __init__(self):
        self.name = ""
        self.course = ""

    def prompt(self):
        self.name = input("Enter name: ")
        self.course = input("Enter course: ")

    def display(self):
        print("Now helping {} with {}".format(self.name, self.course))


class HelpSystem:
    def __init__(self):
        self.waiting_list = deque()

    def is_student_waiting(self):
        return len(self.waiting_list) > 0

    def add_to_waiting_list(self, student):
        self.waiting_list.append(student)

    def help_next_student(self):
        if self.is_student_waiting():
            student = self.waiting_list.popleft()
            student.display()
            print()
        else:
            print("\nNo one to help\n")


def main():
    # s = Student()
    h = HelpSystem()

    selection = 0

    print("Options: ")
    while selection != 3:
        print("1. Add a new student ")
        print("2. Help next student ")
        print("3. Quit")
        selection = int(input("Enter selection: "))

        if selection == 1:
            s = Student()
            print()
            s.prompt()
            print()
            h.add_to_waiting_list(s)
        elif selection == 2:
            h.help_next_student()

    print("\nGoodbye")


if __name__ == "__main__":
    main()
