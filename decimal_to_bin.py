def reverse(s):
  ''' Reverses a string '''
  str = ""
  for i in s:
    str = i + str
  return str

def decimal_to_bin(n):
  ''' Convertes a decimal number to binary '''
  res = ""
  while n > 0:
    res+= str(n % 2)
    n //=2
  return reverse(res)

number = int(input("Type a decimal number to convert: "))
print("{0} is {1} in binary".format(number, decimal_to_bin(number)))