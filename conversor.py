def reverse(s):
  ''' Reverses a string '''
  str = ""
  for i in s:
    str = i + str
  return str

def bin_to_decimal(n):
  ''' Convertes a decimal number to binary '''
  res = ""
  while n > 0:
    res+= str(n % 2)
    n //=2
  return reverse(res)

number = int(input("Type a number to convert: "))
print("{0} is {1} in binary".format(number, bin_to_decimal(number)))