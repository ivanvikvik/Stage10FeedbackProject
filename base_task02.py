# before
def check_sequence(num):
    num = abs(num)
    first_digit = num % 10
    second_digit = num // 10 % 10

    if first_digit < second_digit:
        num = reverse(num)

    while num > 0:
        first_digit = num % 10
        second_digit = num // 10 % 10

        if first_digit > second_digit:
            num //= 10
        else:
            break

    return first_digit > second_digit


# after
def check_sequence_asc(num):
    num = abs(num)

    while num > 0:
        first = num % 10
        num //= 10
        second = num % 10

        if first <= second:
            return False

    return True


def check_sequence_desc(num):
    num = abs(num)

    while num > 0:
        first = num % 10
        num //= 10
        second = num % 10

        if first >= second:
            return False

    return True


def check_sequence(num):
    return check_sequence_asc(num) or check_sequence_desc(num)
