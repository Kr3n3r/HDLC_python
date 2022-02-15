# MCD por el método de Euclides

def gcd(number1,number2):
    if number2 <= 0 :
        return
    elif number1 >= number2:
        pass
    else:
        aux = number1
        number1 = number2
        number2 = aux
    
    if number1%number2 == 0 or number1%number2 == 1:
        return number2
    else:
        return gcd(number2,number1%number2)

print(f"El MCD es {gcd(5,27)}")