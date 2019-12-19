numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]
print(numbers)

numbers.insert(0, 5)
print(numbers)

numbers.remove(2348)
print(numbers)

newNumbers = [6,20,50,1, 51]
numbers += newNumbers
print(numbers)

numbers.sort()
print(numbers)

print(numbers.count(12))

print(numbers.index(96))

middle = len(numbers) // 2
left = numbers[:middle]
right = numbers[middle:]
print(left)
print(right)

skiped_list = numbers[::2]
print(skiped_list)

last_five_numbers = numbers[-5:]
print(last_five_numbers)
