fruits = ["apple", "banana", "cherry"] #with for we can go throgh list 
for x in fruits:
  print(x)

for x in "banana":
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


for x in range(6): #To loop through a set of code a specified number of times, we use range()
  print(x)
#range starts with 0, in range(6) it goes from 0 to 5, so in sum it iterates 6 times


for x in range(2, 6):
  print(x)


for x in range(2, 30, 3): #by adding third value we determine incrementing value for sequence
  print(x)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits: #nested loop-it is the loop within other loop, the inner loop will execute each time outer loop iterates
    print(x, y)

for x in [0, 1, 2]:
  pass # "for" loop can't be empty, so to avoid an error we use "pass"