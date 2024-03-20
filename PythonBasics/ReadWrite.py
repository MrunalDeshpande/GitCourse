# file = open('test.txt')
# #Read all contents of file
# # print(file.read())
# #read n number of characters by passing parameters
# # print(file.read(5))
# # Read single line at a time - readline()
# print(file.readline())
# print(file.readline())
# file.close()

#Print line by line using readline method
file = open('test.txt')
# line = file.readline()
# while line!= "":
#     print(line)
#     line = file.readline()

# readlines() meth0d allows you to create one list is created and then all the operation such extract,update deletlet are easier.

for line in file.readlines():
    print(line)
file.close()
