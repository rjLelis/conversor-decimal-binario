def bin_to_decimal(binary):
    ''' Converts a binary number to decimal '''
    binary = str(binary)
    bits = []
    b = 1
    res = 0
    for n in range(0, len(binary)):
        bits.append(b)
        b*=2
    bits.reverse()
    for n in range(0, len(binary)):
        if binary[n] == "1":
            res += bits[n]
    return res

number = input("Type a binary number to convert: ")
print("{0} is {1} in decimal".format(number, bin_to_decimal(number)))