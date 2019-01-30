




lista = []
maximo = 0
alumnosconmasedad = []
indice = 0
media = 0
contador = 0
contador2 = 1
mayores_edad = []

nombre = input("Introduce el nombre de un alumno: ")
edad = int(input("Introduce la edad del alumno: "))

while nombre != "*":
	lista.append(nombre)
	lista.append(edad)
	nombre = input("Introduce el nombre de un alumno: ")
	if nombre != "*":
		edad = int(input("Introduce la edad del alumno: "))	

maximo = max(lista[1::2])

print (lista)

for i in lista[1::2]:
	if i == maximo:
		indice = lista.index(i, indice + 1)
		posicion = indice - 1
		alumnosconmasedad.append(lista[posicion])
print ("Alumnos con mas edad: ",alumnosconmasedad)

print ("La edad media de la clase es: ",sum(lista[1::2]) / len(lista[1::2]))

nombre2 = input("Dime el nombre del alumno del que desea saber la edad: ")

longitud = len(lista) // 2

for i in range(longitud):
	if lista[contador] == nombre2:
		print (lista[contador],"con",lista[contador + 1],"años")
		contador = contador + 2
	else:
		contador = contador + 2

for i in range(longitud):
	if lista[contador2] >= 18:
		mayores_edad.append(lista[contador2 - 1])
		mayores_edad.append(lista[contador2])
		contador2 = contador2 + 2
	else:
		contador2 = contador2 + 2
print ("Los alumnos mayores de edad son: ",mayores_edad)