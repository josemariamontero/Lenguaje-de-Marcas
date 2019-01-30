with open("notas.txt","r") as fichero:
	lineas = fichero.readlines()
#print (lineas)
alumnos = {}
curso = []
alumnos2 = []
lista = []

for i in lineas:
	curso.append(i.rstrip("\n"))
	datos = curso[0].split(",")
#print (curso)

for i in curso:
	datos2 = i.split(",")
	#print (datos2)
	alumnos["Nombre"] = datos2[1]
	alumnos["Apellidos"] = datos2[0]
	alumnos["Curso"] = datos[2]
	alumnos["Notas"] = {} 

for i in range(3,len(datos2)):
	alumnos["Notas"][datos[i]] = datos2[i]

alumnos2.append(alumnos)

#print (alumnos2)


print ("1º. Nota Media")
print ("2º. Curso y Asignatura")
print ("3º. Porcentaje de aprobados por asignatura")
print ("4º. Crear fichero con alumnos y su nota media")
print ("5º. Salir")

opcion = input("Elige una opcion: ")

if opcion == "1":
	for elemento in alumnos2:
		modulos = elemento["Notas"]
		for a in modulos.values():
			lista.append(a)

def notamedia(nota,nota2,nota3,nota4,nota5,nota6):
	sumamedia = nota + nota2 + nota3 + nota4 + nota5 + nota6
	return sumamedia

resultado = notamedia(int(lista[0]),int(lista[1]),int(lista[2]),int(lista[3]),int(lista[4]),int(lista[5]))
media = resultado / len(elemento["Notas"])
print (media)
#print ("El alumno %s %s tiene una media de %d" % (elemento["Nombre"],elemento["Apellidos"],media))