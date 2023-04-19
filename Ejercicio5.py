# 5.- Diseña un programa que reciba dos números a y b y una operación aritmética (representada por un número) entre las cuatro básicas (suma, resta, multiplicación y división). Si no se ingresó una operación válida, indicarlo. Imprimir en consola los resultados.

a = float(input('Ingrese el primer número : '))
b = float(input('Ingrese el segundo número : '))
op = input('Ingrese la operación : \n 1) Suma \n 2) Resta \n 3) Mult \n 4) Div\n')

if op == '1':
    suma = a + b
    print('La suma es: ' + str(suma))
elif op == '2':
    resta = a - b
    print('La resta es: ' + str(resta))
elif op == '3':
    mult = a * b
    print('La multiplicación es: ' + str(mult))
elif op == '4':
    div = a / b
    print('La división es: ' + str(div))
else:
    print('La operación ingresada no es válida ')
print('Adiós!')
