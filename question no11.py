vowel=["a","e","i","o","u"]
ask=input("Enter the word::")
count=0
for i in ask: 
  if i.lower() in vowel:
    count+=1
print(f"There are total {count} vowels in the word {ask}")


    
