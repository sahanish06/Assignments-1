fibonacci =[0,1]
for i in range(2,10):
  number=fibonacci[-1]+fibonacci[-2]
  fibonacci.append(number)
for index, i  in enumerate(fibonacci):
  print(index+1,"=",i)