def bin_to_decimal(binary):
    ''' Converts a binary number to decimal '''
    binary = str(binary)
    bits = []
    bit = 1
    for _ in range(0, len(binary)):
        bits.append(b)
        bit*=2
    bits.reverse()
    res = 0
    for n in range(0, len(binary)):
        if binary[n] == "1":
            res += bits[n]
    return res

number = input("Type a binary number to convert: ")
print(f"{number} is {bin_to_decimal(number)} in decimal")
