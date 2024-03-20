values = [1, 2, 3, "Mrunal" , 4.5]
print(type(values))
print(values[0])
print(values[3])
print(values[-1])
print(values[-2])
print(values[1:4])

values.insert(3,'Manaswi')
print(values)

values.append(500)
print(values)

values[4] = "MRUNAL"
print(values)

del values[0]
print(values)