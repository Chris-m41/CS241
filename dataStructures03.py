def inputNumber():
    odd = []
    even = []
    number = 1
    while number != 0:
        number = int(input("Enter a number (0 to quit): "))
        if number != 0 and number % 2 == 0:
            even.append(number)
        elif number % 2 == 1:
            odd.append(number)
    return odd, even

def displayList(odd, even):
    print("\nEven Numbers: ")
    for i in even:
        print(i)

    print("\nOdd Numbers: ")
    for i in odd:
        print(i)



def main():
    odd, even = inputNumber()
    displayList(odd, even)

if __name__ == "__main__":
    main()