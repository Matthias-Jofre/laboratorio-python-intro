# Se pregunta al usuario la cantidad de números que desea ingresar almacenandolos en la variable cantidad
cantidad = int(input("Ingrese la cantidad de números a consultar: "))

# Se recorre la cantidad de números ingresados por el usuario y se pregunta si el número es par o impar iniciando la variable i en 0
i = 0

# Mientras i sea menor a la cantidad de números ingresados por el usuario se pregunta si el número es par o impar
while i < cantidad:
    if (i % 2 == 0):
        print(i, "es par")
    else:
        print(i, "es impar")
    i = i + 1