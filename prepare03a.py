class Student:
    def __init__(self):
        self.firstName = " "
        self.lastName = " "
        self.id = 0

def studentInfo():
    newStudent = Student()

    newStudent.firstName = input("Enter your first name: ")
    newStudent.lastName = input("Enter your last name: ")
    newStudent.id = input("Enter your id number: ")

    return newStudent

def displayInfo(info):
    print("\nYour information: ")
    print("{} - {} {}".format(info.id, info.firstName, info.lastName))

def main():
    info = studentInfo()
    displayInfo(info)


if __name__ == "__main__":
    main()