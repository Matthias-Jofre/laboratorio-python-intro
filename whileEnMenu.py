
# Crea un menú con las opciones de sumar, restar, multiplicar y dividir dos números

while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        print('Soy la opción 1, suma')
    elif opcion == 2:
        print('Soy la opción 2, resta')
    elif opcion == 3:
        print('Soy la opción 3, multiplicación')
    elif opcion == 4:
        print('Soy la opción 4, división')
    elif opcion == 5:
        print("Gracias por usar el programa")
        break
    else:
        print("Opción no válida")
    print()