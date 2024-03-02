def user_input(number):
    return list(range(1, number + 1))


def sum_collection(numbers):
    return sum(numbers)


def remove_element(number, numbers):
    if number in numbers:
        numbers.remove(number)
        return number
    return None


def find_intersection(number1, number2):
    intersection = number1.intersection(number2)
    return intersection


def display_list(number):
    return list(range(1, number))


def element_duplicate(numbers):
    numbers = list(range(1, 16))
    number1 = []
    for i in numbers:
        number1.append(i)

    return number1


def eliminate_duplicate(numbers):  # 1 1 2 3 4 5 6 7 8 9
    new_l = []
    for i in numbers:
        if i not in new_l:
            new_l.append(i)
    return new_l


# def add_element(numbers):
#     for number in range(len(numbers):
#
def add_element(numbers):
    total = 0
    for i in numbers[2::3]:
        total += i
    return total
