class Calculator:
    num = 100 # class variables

# self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# constructor name should be _init_
# new keyword is not required when you create object

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("i am called automaticallz when object is created")

    def getData(self):
        print("Executing method in class")

    def sumThatShit(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3) #syntax to create objects in python
obj.getData()
print(obj.sumThatShit())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.sumThatShit())