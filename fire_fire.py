lists = []
for i in range(10):
    numbers = int(input("Enter number: "))
    lists.append(numbers)
print(lists)


def length_of_number():
    count = 0
    for number in numbers:
        count = count + 1
    return count


print(length_of_number())


def sum_all_even():
    sum_of_even = 0
    for index in range(1, length_of_number(), 2):
        sum_of_even += numbers[index]
    return sum_of_even


print(sum_all_even())


def sum_all_odd():
    sum_of_odd = 0
    for index in range(0, length_of_number(), 2):
        sum_of_odd += numbers[index]
    return sum_of_odd


print("odd", sum_all_odd())


def multiply_odd_element():
    multiply = 1
    for index in range(0, length_of_number(), 2):
        multiply *= numbers[index]
    return multiply


print(multiply_odd_element())


def average_of_elements():
    count = 0
    total = 0
    average = 0
    for index in range(0, length_of_number(), 2):
        average += numbers[index] / length_of_number()
    return average


print(average_of_elements())


def largest():
    largest1 = numbers[0]
    for number in numbers:
        if number > largest1:
            largest1 = number
    return largest1


print(largest())


def smallest():
    smallest1 = numbers[0]
    for number in numbers:
        if number < smallest1:
            smallest1 = number
    return smallest1


print(smallest())
