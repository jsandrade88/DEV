#print first and last name
print("Julio", "Andrade")

#creating list
cars = ['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']
#printing list
print(cars)

#length of list
print(len(cars))

#adding buick to list
cars.append('Buick')
print(cars)

#printing fourth element
print(cars[4])

#adding Toyota to list
cars.insert(3,'Toyota')
print(cars)

#removing element 5
cars.pop(5)
print(cars)

#sorting ascending 
cars.sort()
print(cars)

#descending sort
cars.sort(reverse=True)
print(cars)

#assigning two variables 
my_array_length = len(cars)
array_string = "The length of my array is"

#concatenating both variables 
print(array_string, my_array_length)