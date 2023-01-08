def fibonacci(number):
    if number <= 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(3))
print(fibonacci(7))
print(fibonacci(12))