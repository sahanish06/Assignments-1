
ask=int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))

if ask==1:
  a=int(input("Enter the first number: "))
  b=int(input("Enter the second number: "))
  print(f"The additon of {a} and {b} is {a+b}")
elif ask==2:
  a=int(input("Enter the first number: "))
  b=int(input("Enter the second number: "))
  print(f"The suvtraction of {a} and {b} is  {a-b}")
elif ask==3:
  a=int(input("Enter the first number: "))
  b=int(input("Enter the second number: "))
  print(f"The multiplication of {a} and {b} is {a*b}")
elif ask==4:
  a=int(input("Enter the first number: "))
  b=int(input("Enter the second number: "))
  print(f"The division of {a} and {b} is {a/b}")

else:
  print("please enter a valid number!!!")
  
