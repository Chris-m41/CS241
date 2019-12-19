def fibonnaci(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    elif number == 2:
        return 2

    return fibonnaci(number - 1) + fibonnaci(number - 2)

for i in range(0,20):
    print("Fibonacci({}) = {}".format(i,fibonnaci(i)))