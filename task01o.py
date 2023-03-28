# before
def counter_digit(num):
    num_digit = 0
    length = len(str(abs(num)))
    while 0 < length:
        num_digit += 1
        length -= 1

    return num_digit


# after
def count_digits(num):
    return len(str(abs(num)))
