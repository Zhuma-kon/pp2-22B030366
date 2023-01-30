i = 1
while i <= 6: #we use while when the times of needed action is unknown, while will last as long as condition is true 
  print(i)
  i += 1
i = 1



while i < 6:
  print(i)
  if i == 3:
    break #break will break the loop even if condition is not fullfilled
  i += 1



i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #with the "continue" we can skip ine step of loop.
  print(i)


  i = 1
while i < 6:
  print(i)
  i += 1
else: # else is still else
  print("i is no longer less than 6")