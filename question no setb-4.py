array=list(range(1,16))
def find(array,target):
  indices=[]
  reversed=array[::-1]
  for i in array:
    for j in reversed:
      if i+j==target:
        indices.append(array.index(i))
        indices.append(array.index(j))
        return indices
finds=find(array,9)
print(finds)
