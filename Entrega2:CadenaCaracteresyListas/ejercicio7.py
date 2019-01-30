lista = []
maximo = 0
suma = 0
alumnos_mayores_edad = []

nombre = input("Introduce el nombre del alumno: ")
edad = int(input("Introdce la edad del alumno: "))

while nombre != "*":
	lista.append([nombre,edad])
	nombre = input("Introduce el nombre del alumno: ")
	if nombre != "*":
		edad = int(input("Introdce la edad del alumno: "))

for i in lista:
	if i[1] > maximo:
		maximo = i[1]
		mayores_edad = i[0]
print ("Alumnos con más edad: ",mayores_edad)

for i in lista:
	suma = suma + i[1]
	media = suma / len(lista)
print ("La edad media de la clase: ", media)

nombre_alumno = input("Introduce el nombre del alumno del que desea saber la edad: ")

for i in lista:
	if nombre_alumno == i[0]:
		print ("La edad del alumno introducido es: ",i[1])

for i in lista:
	if i[1] > 18:
		alumnos_mayores_edad.append(i[0])
print ("Los alumnos mayores de edad son: ",alumnos_mayores_edad)
