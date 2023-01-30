#dictionaries are used to contain a data values in key:value pairs
#dictionaries are changable, ordered and don't allow duplicates
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 #new value will rewrite ald value
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"] #dictionaries can even contain list
}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway") #dict() function can make a dict.
print(thisdict)