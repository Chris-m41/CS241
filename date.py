class Date:
    def __init__(self):
        self.isMonthTrue = True
        self.day = "1"
        self.month = "1"
        self.year = "2000"
        self.long_month = "Undefined"

    def prompt(self):
        self.isMonthTrue = False
        self.day = input("Enter day: ")
        if int(self.day) > 10:
            self.day = self.day
        else:
            self.day = str("0" + self.day)

        while self.isMonthTrue == False:
            if 13 > int(self.month) > 0:
                self.month = input("Enter month: ")
                if self.month == 12 or self.month == 11:
                    self.month = self.month
                else:
                    self.month = str("0"+self.month)

                self.isMonthTrue = True
            else:
                self.month = input("Enter valid month. 1 - 12")
                self.isMonthTrue = False

        self.year = input("Enter year: ")
        print("\n")

    def display_long(self):
        if int(self.month) == 1:
            self.long_month = "January"
        if int(self.month) == 2:
            self.long_month = "February"
        if int(self.month) == 3:
            self.long_month = "March"
        if int(self.month) == 4:
            self.long_month = "April"
        if int(self.month) == 5:
            self.long_month = "May"
        if int(self.month) == 6:
            self.long_month = "June"
        if int(self.month) == 7:
            self.long_month = "July"
        if int(self.month) == 8:
            self.long_month = "August"
        if int(self.month) == 9:
            self.long_month = "September"
        if int(self.month) == 10:
            self.long_month = "October"
        if int(self.month) == 11:
            self.long_month = "November"
        if int(self.month) == 12:
            self.long_month = "December"

        print("{} {}, {}".format(self.long_month, self.day, self.year))

    def display(self):
        print("{}/{}/{}".format(self.month,self.day,self.year))