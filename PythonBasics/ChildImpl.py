from OopsConcepts import calculator

class ChildImpl(calculator):
    num2 = 200

    def __init__(self):
        calculator.__init__(self,2,10)
        
    def getCompleteData(self):
        return ChildImpl.num2 + self.num + self.summation()

obj = ChildImpl()
print(obj.getCompleteData())