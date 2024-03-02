# days_per_month = {'january':31, 'february' : 28, 'march' : 31}
#
# for month, days in days_per_month.items():
#     print(f'{month} has {days}')


# roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}
#
# print(roman_numerals['V'])
#
# roman_numerals['X'] = 10
#
# print(roman_numerals['X'])
#
# roman_numerals['L'] = 50
#
# print(roman_numerals)
#
# del roman_numerals['III']
# print(roman_numerals)
#
# roman_numerals.pop('X')
# print(roman_numerals)
#
# roman_numerals.get('III')
# roman_numerals.get('III', 'III not in dictionary')
# print(roman_numerals['III'])
# roman_numerals.get('V')

# months = {'january': 1, 'february': 2, 'march': 3}
#
# for month_number in months.values():
#     print(month_number, end=' ')
#
# months_view = months.keys()
# for key in months_view:
#     print(key, end=' ')
#
# months['December'] =  12
# print(months)
#
# for key in months_view:
#     print(key, end=' ')


# numbers = list(range(1,16))
# print(numbers)
#
# print(numbers[1:len(numbers):2])
# numbers[5:10] = [0] * len(numbers[5:10])
# print(numbers)
#
# numbers[5:] = []
# print(numbers)

# numbers = list(range(0,10))
# print(numbers)
#
# del numbers[-1]
# print(numbers)
#
# del numbers[0:2]
# print(numbers)

# numbers = list(range(1,16))
# print(numbers)
#
# del numbers[:4]
# print(numbers)
#
# del numbers[::2]
# print(numbers)


# def modify_elements(items):
#     for i in range(len(items)):
#         items[i] *= 2
# numbers = [10, 3, 7, 1, 9]
# modify_elements(numbers)
# print(numbers)

# numbers = [10, 3, 5, 7, 9, 4, 1, 2]
# numbers.sort()
# print(numbers)
#
# numbers.sort(reverse=True)
# print(numbers)


#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# var = numbers[1:len(numbers): 2]
# print(var)
#
# yoo = numbers[5:9] = [0] * len(numbers[5:9])
# print(numbers)
#
# num = numbers[:5]
# print (num)
#
# nums = numbers[:] = []
# print(nums)

# numbers = list(range(1, 16))
filtering = 8
list2 = [item for item in range(1, 11) if item % 2 == 0]
print(list2)

colors = ['red', 'yellow', 'blue', 'green']
colors2 = [item.upper() for item in colors]
print(colors)

multiple = [i for i in range(3, 30, 3)]
print(multiple)

# del numbers[:4]
# print(numbers)
#
# del numbers[::2]
# print(numbers)

# def modifying_element(items):
#     for i in range(len(items)):
#         items[i] *= 2
#
#
# numbers = [10, 2, 5, 6]
#
# modifying_element(numbers)
# print(numbers)
#
#

from decimal import Decimal


class Account:
    def __init__(self, name, balance: Decimal):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < Decimal(0.00):
            raise ValueError("invalid amount for balance")

        self.balance = balance

    def __str__(self):
        return f"Name:{self.name} Balance: {self.balance}"


ai = Account('dayo', Decimal(10))
print(ai)
