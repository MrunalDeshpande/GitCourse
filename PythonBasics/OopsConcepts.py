# Self keyword is mandatory for calling variables names into method.
# Instance and class variables have whole different purpose
# Constructor name should be __init__
# new keyword is not required for creating object

class calculator:
    num = 100 #Class Variable which are constant to all.
    x = 10

    def __init__(self,a,b): #Default Constructor
        self.firstNumber = a #Instance Variable
        self.secondNumber = b #Instance Variable
        print("I am called automatically when object is created.")

    def getData(self):
        print("I am now executing as method in class.")

    def summation(self):
        return self.firstNumber + self.secondNumber + calculator.num + calculator.x

obj = calculator(5,6) #Creating class object obj
# print(obj.num)
print(obj.summation()) #Calling variable using class object obj
obj.getData() # Calling methods using class object obj

obj1 = calculator(4,5)
# print(obj.x)
print(obj1.summation())
obj1.getData()