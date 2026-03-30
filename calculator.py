class Calculator:
    def add(self, a, b):
        """Returns the sum of a and b"""
        return a + b
    def subtract(self, a, b):
        """Returns the difference of a and b"""
        return a - b
    def multiply(self, a, b):
        """Returns the product of a and b"""
        return a * b
    def divide(self, a, b):
        """Returns the quotient of a and b. Raises ValueError if b is zero."""
        if b == 0:
          raise ValueError("Cannot divide by zero")
        return a / b
    def power(self, a, b):
        """Returns a raised to the power of b"""
        return a ** b
calc = Calculator()
print(calc.add(250, 50))        
print(calc.subtract(250, 50))   
print(calc.multiply(250, 50))   
print(calc.divide(250, 50))