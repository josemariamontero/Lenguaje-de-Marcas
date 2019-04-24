with open("notas.txt","r") as fichero:
	lineas = fichero.readlines()

alumnos = {}
alumnos2 = []
evaluacion = []
lista = []
media = 0

for a in lineas:
	evaluacion.append(a.rstrip("\n"))
	datos = evaluacion[0].split(",")

for b in evaluacion:
	valor = b.split(",")
	alumnos["nombre"] = valor[1]
	alumnos["apellidos"] = valor[0]
	alumnos["curso"] = valor[2]
	alumnos["notas"] = {}

for c in range(3,len(valor)):
	alumnos["notas"][datos[c]] = valor[c]
alumnos2.append(alumnos)
alumnos = {}

del alumnos2[0]

print ("1º => Nota media")
print ("2º => Curso y asignatura")
print ("3º => Porcentaje aprobados por asignatura")
print ("4º => Crea fichero con alumnos y nota media")
print ("5º => Salir")

elegir = input("Elige alguna opción: ")

if elegir == "1":
	for notas2 in alumnos2:
		asignaturas = notas2["notas"]
		lista = []
		for clave, calificacion in asignaturas.iteritems():
			lista.append(calificacion)

def media(nota1,nota2,nota3,nota4,nota5,nota6):
	suma = nota1 + nota2 + nota3 + nota4 + nota5 + nota6
	return suma
total = media(int(lista[0],int(lista[1]),int(lista[2]),int(lista[3]),int(lista[4]),int(lista[5]))
media = total / len(notas2["notas"])
print ("El alumno %s %s tiene una media de %i" % (notas2["nombre"],notas2["apellidos"],media))

if elegir == "2":
	curso = input("Introduce el curso: ")
	asignatura = input("Introduce la asignatura: ")
	for elemento in alumnos2:
		if elemento["curso"] == curso:
			print (elemento["nombre"],elemento["apellidos"])
			print (elemento["notas"][asignatura])

elif elegir == "3":
	curso = input("Introduce el curso: ")
	alumnos3 = 0
	calificaciones = {"FH": 0, "LM": 0, "ISO": 0, "PAR": 0, "SGBD": 0, "FOL": 0}
	for elemento in alumnos2:
		if elemento["curso"] == curso:
			alumnos3 = alumnos3 + 1
			for asigna in elemento["notas"]:
				if elemento["notas"][asigna] >= 5:
					calificaciones[asigna] = calificaciones[asigna] + float(elemento["notas"][asiga])
print ("El porcentaje de aprobados en la asignatura FH: ", (float(calificaciones["FH"])/alumnos3)*10)
print ("El porcentaje de aprobados en la asignatura LM: ", (float(calificaciones["LM"])/alumnos3)*10)
print ("El porcentaje de aprobados en la asignatura ISO: ",(float(calificaciones["ISO"])/alumnos3)*10)
print ("El porcentaje de aprobados en la asignatura FOL: ",(float(calificaciones["FOL"])/alumnos3)*10)
print ("El porcentaje de aprobados en la asignatura PAR: ",(float(calificaciones["PAR"])/alumnos3)*10)
print ("El porcentaje de aprobados en la asignatura SGBD: ",(float(calificaciones["SGBD"])/alumnos3)*10)

if elegir == "4":
	curso = input("Introduce el curso: ")
	for nota in alumnos2:
		media = 0
		nombredelcurso = curso + ".txt"
		if nota["curso"] == curso:
			asignaturas = nota["notas"]
			lista = []
			for clave, calificacion in asignaturas.iteritems():
				lista.append(calificacion)
				media = total / len(nota["notas"])
				escribir_fichero = nota["nombre"],nota["apellidos"],media
				fichero = open(nombredelcurso, "a")
				escrito = fichero.write(str(escribir_fichero))
				fichero.close()

elif elegir == "5":
	print ("Salir")
else:
	print ("Incorrecto, elige una opción entre el 1 y el 5")