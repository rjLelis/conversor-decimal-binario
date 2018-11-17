def reverse(string):
    ''' Reverses a string '''
    return string[::-1]


def decimal_to_bin(decimal_number):
    ''' Convertes a decimal number to binary '''
    res = ""
    while decimal_number > 0:
        res += str(decimal_number % 2)
        decimal_number //= 2
    return reverse(res)

number = int(input("Type a decimal number to convert: "))
print(f"{number} is {decimal_to_bin(number)} in binary")
