class MathDojo:
    def __init__(self,num=0):
        self.result = num
    
    def add(self,num1, *num2):
        total = 0
        argList = []
        argList.append(num1)
        argList.append(num2)
        total = self.totalHelper(total, argList)
        self.result += total
        return self
    def subtract(self,num1, *num2):
        total = 0
        argList = []
        argList.append(num1)
        argList.append(num2)
        total = self.totalHelper(total, argList)
        self.result -= total
        return self
    def totalHelper(self, total, argList):
        for item in argList:
            try:
                total = self.totalHelper(total, item)
            except TypeError:
                total+=item
        return total
