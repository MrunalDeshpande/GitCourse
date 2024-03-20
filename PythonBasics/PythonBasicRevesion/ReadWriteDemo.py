file =open('test.txt')
#read all the contents of file
#read n number of characters by passing parameteres
# print(file.read(10))
#
# read one single at a time
# print(file.readline())
# print(file.readline())

# print line by line using readline() method
# line = file.readline()
# while line != '':
#     print(line)
#     line=file.readline()

for line in file.readlines():
    print(line)
file.close()