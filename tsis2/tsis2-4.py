cars = ["Ford", "Volvo", "BMW"] #python don't actually have an arrays, so we use lists instead
x = cars[0]
cars[0] = "Toyota"
x = len(cars)
for x in cars:
  print(x)
cars.append("Honda") #we use "append" to add one more element to the array
cars.pop(1) #we use "pop" to delete element from the array
cars.remove("Volvo") #you can also use "remove" to delete elemet from the array