
def EsMultiplo(num1,num2):
    try:
        if num1%num2 == 0:
            return print(num2,"es múltiplo de",num1)
        elif num2%num1 == 0:
            return print(num1,"es múltiplo de",num2)
        else:
            return print("Ninguno es módulo del otro")
    except ZeroDivisionError as error:
        print("Excepción captada:",error)
    except TypeError as error:
        print("Excepción captada:",error)
    except NameError as error:
        print("Excepción captada:",error)

if __name__=="__main__":
    EsMultiplo(6,'0')
