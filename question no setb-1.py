def is_Palindrome(a):
  a=str(a)
  return a==a[::-1]

a=int(input("Enter a number:"))
if is_Palindrome(a):
  print(f"Yes, {a} is a palindrome")

else:
  print(f"No, {a} is not a palindrome")
