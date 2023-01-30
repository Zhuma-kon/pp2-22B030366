#tuple is also used to store different data type in one variable
#tuples are unchangable and ordered, they are written with round brackets
thistuple = ("apple", "banana", "cherry") #items are indexed, index starts with [0]
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry") #tuples can contain duplicates
print(thistuple)

print(len(thistuple)) #len() shows the number of elements in tuple

thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#NOTE don't forget a comma when creating a tuple, even if tuple has 1 element


tuple1 = ("abc", 34, True, 40, "male")
#tuple can store a different data types