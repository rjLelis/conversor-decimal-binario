def reverse(string):
  ''' Reverses a string '''
  return string[::-1]

def decimal_to_bin(n):
  ''' Convertes a decimal number to binary '''
  res = ""
  while n > 0:
    res+= str(n % 2)
    n //=2
  return reverse(res)

number = int(input("Type a decimal number to convert: "))
print(f"{number} is {decimal_to_bin(number)} in binary")
