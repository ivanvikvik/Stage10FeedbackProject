def search_same_parity(num):
    num = abs(num)
    length = len(str(num))
    same_parity = 0

    while num > 0:
        digit = num % 10
        num //= 10

        if digit % 2 == 0:
            same_parity += 1
        else:
            same_parity -= 1

    return abs(same_parity) == length


# after
def is_all_digits_even(num):
    num = abs(num)

    while num > 0:
        digit = num % 10

        if digit % 2 == 1:
            return False

        num //= 10

    return True


def is_all_digits_odd(num):
    num = abs(num)

    while num > 0:
        digit = num % 10

        if digit % 2 == 0:
            return False

        num //= 10

    return True


def is_same_parity(num):
    return is_all_digits_even(num) or is_all_digits_odd(num)
