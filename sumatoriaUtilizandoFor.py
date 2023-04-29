
# Entrada de datos
n = int(input("Ingrese la cabtidad de numeros a sumar:"))

# Se crea un contador para ir almacenando la sumatoria
sumatoria = 0

# Se itera hasta la cantidad de numeros ingresados almacenados en la variable n
for i in range(n):
    x = int(input("Ingrese el numero a sumar:"))	
    sumatoria = x + sumatoria

# Salida de datos
print("El resultado de los números a sumar es:", sumatoria)