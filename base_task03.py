# before
def palindrome(number):
    temp_number = number
    reverse_number = 0

    while number > 0:
        digit = number % 10
        reverse_number = reverse_number * 10 + digit
        number = number // 10

    if temp_number == reverse_number:
        msg = "Палиндромное число !"
    else:
        msg = "Не палиндромное число !"

    return msg


# after
def check_palindrome(number):
    copy = number
    reverse = 0

    while number > 0:
        reverse = reverse * 10
        reverse += number % 10
        number //= 10

    return copy == reverse
