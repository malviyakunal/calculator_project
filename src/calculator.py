class Calculator:
    def add(self,a,b):
        return a+b
    
    def subtract(self,a,b):
        return a-b
    
    def multiply(self,a,b):
        return a*b
    
    def divide(self, a, b):        # ✅ lowercase self
        if b == 0:
             raise ValueError("Cannot divide by zero")  # ✅ exact message
        return a / b
    
    def module(self,a,b):
        if b == 0:
            raise ValueError("Cannot mod by zero")
        return a % b