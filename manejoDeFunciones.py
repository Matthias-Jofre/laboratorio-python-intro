# Para la implementación de funciones se debe tener en cuenta para que será utilizada la función
# Por ejemplo, para poder crear una función que ejecute el ejercicio 'whileEnMenu.py'

# while True:
#     print("1. Suma")
#     print("2. Resta")
#     print("3. Multiplicación")
#     print("4. División")
#     print("5. Salir")
#     opcion = int(input("Ingrese una opción: "))

#     if opcion == 1:
#         print('Soy la opción 1, suma')
#     elif opcion == 2:
#         print('Soy la opción 2, resta')
#     elif opcion == 3:
#         print('Soy la opción 3, multiplicación')
#     elif opcion == 4:
#         print('Soy la opción 4, división')
#     elif opcion == 5:
#         print("Gracias por usar el programa")
#         break
#     else:
#         print("Opción no válida")
#     print()

# Se crea la función menu() que contiene el código del ejercicio whileEnMenu.py

def menu():
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

# Para ejecutar la función menu() se debe llamar a la función menu() de la siguiente manera:

menu()