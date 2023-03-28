# before
def same_num(num):
    if num <= 9:
        return "Error! Input your number >= 10!"

    while num > 9:
        flag = True
        last_digit = num % 10
        last2_digit = num % 100 // 10
        if last_digit != last2_digit:
            flag = False
            break
        num //= 10
    return "YES" if flag else "NO"


# after
def same_num(num):
    if num <= 9:
        return "Error! Input your number >= 10!"

    flag = True

    while num > 9:
        last_digit = num % 10
        num //= 10
        last2_digit = num % 10

        if last_digit != last2_digit:
            flag = False
            break

    return flag
