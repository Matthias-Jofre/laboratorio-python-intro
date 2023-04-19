# 3. Crea un programa que dado un número, determine si es par o no. En concreto, si el número es par, imprime “Es par” y luego imprime el número elevado al cuadrado. Al término del programa, despídete con un “Adiós mundo!” independiente de si el número era par o no.

num = int(input('Ingrese el número : '))

var = num % 2 == 0

if var:
    print('Es par ')
    print(num ** 2)
print('Adiós mundo !')

