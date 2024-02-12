def user_input(number):
    return list(range(1, number + 1))

def sum_collection(numbers):
    return sum(numbers)

def remove_element(number, numbers):
    if number in numbers:
        numbers.remove(number)
        return number
    return None


