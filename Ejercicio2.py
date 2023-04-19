# 2.- Imagina que estás en un curso que tiene 3 pruebas que ponderan un 20 % cada una y un examen que pondera el 40 % restante. El curso se aprueba si el promedio no aproximado del curso es mayor o igual que 4.0. Escribe un programa que reciba las 4 notas e imprima True si aprobaste el curso y False en caso contrario.

n1 = float(input('Ingrese la nota de la prueba 1: '))

n2 = float(input('Ingrese la nota de la prueba 2: '))

n3 = float(input('Ingrese la nota de la prueba 3: '))

ex = float(input('Ingrese la nota del examen : '))

promedio = 0.2 * n1 + 0.2 * n2 + 0.2 * n3 + 0.4 * ex

pasaste = promedio >= 4.0

print(pasaste)

if (pasaste == True):
    print('Pasaste la asignatura')
else:
    print('Reprobaste')
