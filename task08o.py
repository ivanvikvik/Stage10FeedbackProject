from task01o import count_digits


# before
def search_same_parity(num):
    num = abs(num)
    same_parity = 0

    while num > 0:
        digit = num % 10
        num //= 10

        if digit % 2 == 0:
            same_parity += 1
        else:
            same_parity -= 1

    return same_parity


# after
def check_most_even_digits(num):
    num = abs(num)
    count = 0

    while num > 0:
        digit = num % 10
        num //= 10

        if digit % 2 == 0:
            count += 1

    return count_digits(num) - count < count


def check_most_odd_digits(num):
    num = abs(num)
    count = 0

    while num > 0:
        digit = num % 10
        num //= 10

        if digit % 2 == 1:
            count += 1

    return count_digits(num) - count < count
