# before
def equal_digits(num):
    num = abs(num)

    first_digit = num % 10
    second_digit = 0

    while num > 0:
        second_digit = num % 10

        if first_digit == second_digit:
            num //= 10
        else:
            break

    return first_digit == second_digit


# after
def equal_digits(num):
    num = abs(num)

    first_digit = num % 10
    num //= 10

    while num > 0:
        second_digit = num % 10

        if first_digit != second_digit:
            return False

        num //= 10

    return True
