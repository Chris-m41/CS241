"""
File: SelectionSort.py
Original Author: Br. Burton, designed to be completed by others.

Sorts a list of numbers.
"""

def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    for sort_position in range(len(numbers) - 1, 0, -1):
        max_position = 0

        for swap_position in range(sort_position + 1):
            if numbers[swap_position] > numbers[max_position]:
                max_position = swap_position

        numbers[sort_position], numbers[max_position] = numbers[max_position], numbers[sort_position]

def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers

def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)

def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)

if __name__ == "__main__":
    main()