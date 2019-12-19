class Time:
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.seconds = 0
        self.simple_hour = 0
        self.period_type = ""
        self.secondsSinceMidnight = 0

    def get_hour(self):
        return self.hour

    def set_hour(self, hour):
        if hour < 0:
            hour = 0
        elif hour > 23:
            hour = 23

        self.hour = hour

    def get_minute(self):
        return self.minute

    def set_minute(self, minute):
        if minute < 0:
            minute = 0
        elif minute > 59:
            minute = 59
        self.minute = minute

    def get_seconds(self):
        return self.seconds

    def set_seconds(self, seconds):
        if seconds < 0:
            seconds = 0
        elif seconds > 59:
            seconds = 59
        self.seconds = seconds

    def get_hours_simple(self):
        return self.simple_hour

    def set_hours_simple(self, simple_hour):
        self.simple_hour = simple_hour

    def get_period(self):
        return self.period_type

    def set_period(self, period):
        self.period_type = period

    h = property(get_hour, set_hour)
    m = property(get_minute, set_minute)
    s = property(get_seconds, set_seconds)

    @property
    def hours_simple(self):
        return self.get_hours_simple()

    @hours_simple.setter
    def hours_simple(self,simple_hour):
        return self.set_hours_simple(simple_hour)

    @property
    def period(self):
        return self.get_period()

    @period.setter
    def period(self, period):
        self.set_period(period)

    # hours_simple = property(get_hours_simple, set_hours_simple)
    # period = property(get_period, set_period)

    @property
    def seconds_since_midnight(self):
        return self.secondsSinceMidnight

    @seconds_since_midnight.setter
    def seconds_since_midnight(self, secondsSinceMidnight):
        self.secondsSinceMidnight = secondsSinceMidnight


def main():
    time = Time()

    # hour = int(input("Enter hour: "))
    # # time.set_hour(hour)
    # time.h = hour
    #
    # minute = int(input("Enter minute: "))
    # # time.set_minute(minute)
    # time.m = minute
    #
    # seconds = int(input("Enter seconds: "))
    # # time.set_seconds(seconds)
    # time.s = seconds
    #
    # hours_simple = int(input("Enter Simple Time: "))
    # time.hours_simple = hours_simple
    #
    # period = input("Enter Period(AM/PM): ")
    # time.period = period

    # h1 = time.get_hour()
    # m2 = time.get_minute()
    # s3 = time.get_seconds()
    # print("{}:{}:{}".format(h1,m2,s3))

    # print("{} {}".format(time.hours_simple, time.period))

    sem = int(input("Enter Seconds Since Midnight: "))
    time.seconds_since_midnight = sem

    hours = int(sem % 60)
    minutes = int(hours % 60)
    seconds = int(minutes % 60)

    print("{}:{}:{}".format(hours,minutes,seconds))

if __name__ == "__main__":
    main()
