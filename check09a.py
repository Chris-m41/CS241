done = False

while not done:
    try:
        number = int(input("Enter a number: "))
        done = True
    except ValueError:
        print("The value entered is not valid.")

print("The result is: {}".format(number * 2))

