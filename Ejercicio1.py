# 1.- Escribe un programa que pida al usuario el lado de un cuadrado y que entregue el área, el permetro y el valor de su diagonal.

lado = float ( input ('Ingrese el lado del cuadrado : '))

perimetro = lado * 4

area = lado ** 2

diagonal = lado * (2 ** (1/2))

print ('El perimetro es: ' + str ( perimetro ))
print ('El área es: ' + str ( area ))
print ('La diagonal es: ' + str ( diagonal ))