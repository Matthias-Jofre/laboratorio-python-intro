
# Se pregunta al usuario la cantidad de números que desea ingresar almacenandolos en la variable cantidad
cantidad = int(input("Ingrese la cantidad de números a consultar: "))

# Se recorre la cantidad de números ingresados por el usuario y se pregunta si el número es par o impar
for i in range(cantidad):
    if (i % 2 == 0):
        print(i, "es par")
    else:
        print(i, "es impar")
