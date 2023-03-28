# before
def sum_digit(num):
    num = abs(num)
    summa = 0
    multi_num = 1

    while 0 < num:
        summa += num % 10
        multi_num *= num % 10
        num //= 10

    return summa, multi_num


# after
def sum_digit(num):
    num = abs(num)  # active fool-proof
    summ = 0

    while num > 0:
        summ += num % 10
        num //= 10

    return summ


def prod_digits(num):
    num = abs(num)  # active fool-proof
    prod = 0

    while num > 0:
        prod *= num % 10
        num //= 10

    return prod
