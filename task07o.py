# before
def search_same_parity(num):
    num = abs(num)
    same_parity = 0

    while num > 0:
        digit = num % 10
        num //= 10

        if digit % 2 == 0:
            same_parity += 1

    return same_parity > 0


# after
def is_one_even(num):
    num = abs(num)

    while num > 0:
        digit = num % 10
        num //= 10

        if digit % 2 == 0:
            return True

    return False


def is_one_odd(num):
    num = abs(num)

    while num > 0:
        digit = num % 10
        num //= 10

        if digit % 2 == 1:
            return True

    return False
