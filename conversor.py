def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

def bin_to_decimal(n):
  res = ""
  while n > 0:
    res+= str(n % 2)
    n //=2
  return reverse(res)

number = int(input("type a number"))
print(bin_to_decimal(number))