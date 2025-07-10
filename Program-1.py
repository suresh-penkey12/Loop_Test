class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()  # Normalize input

    def calculate(self):
        if self.operation == "add" or self.operation == "+":
            return self.a + self.b
        elif self.operation == "subtract" or self.operation == "-":
            return self.a - self.b
        elif self.operation == "multiply" or self.operation == "*":
            return self.a * self.b
        elif self.operation == "divide" or self.operation == "/":
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Error: Invalid operation"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide or +, -, *, /): ")

calc = Calculator(a, b, operation)
result = calc.calculate()
print("Result:", result)
