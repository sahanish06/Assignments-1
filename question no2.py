def decimal_to_binary(decimal_number):
  number=str(bin(decimal_number))
  return number[2:]
number=8
print(decimal_to_binary(number))
