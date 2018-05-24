def reverse(string):
  ''' Reverses a string '''
  new_string = ""
  for s in string:
    new_string = s + new_string
  return str

def decimal_to_bin(n):
  ''' Convertes a decimal number to binary '''
  res = ""
  while n > 0:
    res+= str(n % 2)
    n //=2
  return reverse(res)

number = int(input("Type a decimal number to convert: "))
print(f"{number} is {decimal_to_bin(number)} in binary")
