def test_odd_and_even_number(num):
    sum_of_even = 0
    sum_of_odd = 0

    for i in range(1, num):
        if i % 2 == 0:
            sum_of_even += i
            return sum_of_even
        else:
            sum_of_odd += i
            return sum_of_odd

