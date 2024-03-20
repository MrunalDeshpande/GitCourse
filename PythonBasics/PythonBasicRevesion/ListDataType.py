# List is data type that allows multiple values and different data type
#List is mutable data type that is updation is possible
value = [1,2,5.6,'John', "David"]
print(value[0])
print(value[2])
print(value[4])

# To print last index of the list
print(value[-1])
print(value[-2])
print(value[0:4])
value.insert(4,'Dsouza')
print(value)
value.append('End')
print(value)
value[3]='JOHN' #Updating
print(value)
del value[0]
print(value)
