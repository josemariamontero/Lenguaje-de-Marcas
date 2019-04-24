with open('notas.txt','r') as fichero:
	lineas = fichero.readlines()
	#print (lineas)

alumnos = {}
datos = []
alumnos2 = []

for i in lineas:
	datos.append(i.strip("\n"))
	datos2 = datos[0].split(",")
#print (datos2)

for i in datos:
	datos3 = i.split(",")
	alumnos["nombre"] = datos3[1]
	alumnos["apellidos"] = datos3[0]
	alumnos["curso"] = datos3[2]
	alumnos["notas"] = {}
	#print(datos3)

for i in range(3,len(datos3)):
	alumnos["notas"][datos2[i]] = datos3[i]
	alumnos2.append(alumnos2)
	alumnos = {}

del alumnos2[0]

print ("1º => Nota media")
print ("2º => Curso y asignatura")
print ("3º => Porcentaje aprobados por asignatura")
print ("4º => Crea fichero con alumnos y nota media")
print ("5º => Salir")

opcion = int(input("Elige una opción: "))

if opcion == 1:
	for i in alumnos2:
		asignaturas = i["notas"]
		lista_notas = []
		for i,x in asignaturas.iteritems():
			lista_notas.append(x)
			print(lista_notas)