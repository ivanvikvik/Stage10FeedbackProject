# before
def search_match(num):
    num = abs(num)
    desired_digit = 8
    times_occurs = 0
    while num > 0:
        digit = num % 10
        num //= 10
        if digit == desired_digit:
            times_occurs += 1

    return times_occurs


# after
def search_match(num, digit):
    num = abs(num)
    count = 0

    while num > 0:
        dgt = num % 10
        num //= 10

        if dgt == digit:
            count += 1

    return count
