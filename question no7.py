ask=input("Enter three numbers seprated by space:").split()

ask_int=list(map(int,ask))
if ask_int[2]==ask_int[0]+ask_int[1]:
  print("The third number is sum of first two numbers")
else:
  print("NO it is not!!")
  