ask =int(input("Enter the number: "))
if ask<=1:
  print("Enter the number greater than 1")
else: 
  for i in range(2,int(ask**0.5+1)):
    if ask%i==0:
      print("Not a prime number")
      break
  else:
    print(f"{ask} is a prime number")
