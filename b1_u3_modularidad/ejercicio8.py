#factorial de un número
# from math import factorial

# print(factorial(6))

def factorial(n:int):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(f"El factorial es {factorial(6)}")