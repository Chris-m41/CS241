def prompt_number():
    number = -1
    while number < 0:
        number = int(input("Enter a postive number: "))
        if number < 0:
            print("Invalid entry. The number must be positive.")
    return number

def compute_sum(num1, num2, num3):
    sum = num1 + num2 + num3
    print("The sum is: {}".format(sum))


def main():
    number1 = prompt_number()
    number2 = prompt_number()
    number3 = prompt_number()

    compute_sum(number1, number2, number3)


if __name__ == "__main__":
    main()