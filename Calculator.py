class Calculator:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            print("Cannot divide by zero!")

    @staticmethod
    def subtract(x, y):
        return x - y


calculator = Calculator()

x = float(input("Give me firt number "))
y = float(input("Give me second number "))

print(f"Result of adding Your numbers is : {calculator.add(x, y)}")
print(f"Result of subtract Your numbers is : {calculator.subtract(x, y)}")
print(f"Result of divide Your numbers is : {calculator.divide(x, y)}")
print(f"Result of multiply Your numbers is : {calculator.multiply(x, y)}")
