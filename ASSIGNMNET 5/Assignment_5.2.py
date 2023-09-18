class Calculator:
    def __init__(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num2 - self.num1
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num1 == 0:
            return "Cannot divide by zero"
        return self.num2 / self.num1

obj = Calculator()
print(obj.add())      
print(obj.subtract()) 
print(obj.multiply()) 
print(obj.divide())   
