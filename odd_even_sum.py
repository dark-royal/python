# sum_of_even = 0
# sum_of_odd = 0
# number = int(input("Enter number"))
#
# for i in range(1, number):
#     if i % 2 == 0:
#         sum_of_even += i
#
#     else:
#         sum_of_odd += i
#
# print(sum_of_even)
# print(sum_of_odd)
try:
    number = int(input("Enter number"))
    sum_even = sum(list(range(1, number))[1::2])
    sum_odd = sum(list(range(1, number))[::2])
except ValueError:
    print("invalid input")

# print(sum_even,sum_odd)
''