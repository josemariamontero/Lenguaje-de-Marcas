with open("notas.txt","r") as fichero:
	lineas = fichero.readlines()

#print (lineas)

alumnos = {}
alumnos2 = []
evaluacion = []
lista = []

for dato in lineas:
	evaluacion.append(dato.strip("\n"))
	datos = evaluacion[0].split(",")

#print (evaluacion)
#print (datos)

for dato in evaluacion:
	valor = dato.split(",")
	print (valor)
	alumnos["nombre"] = valor[1]
	alumnos["apellidos"] = valor[0]
	alumnos["curso"] = valor[2]
	alumnos["notas"] = {}

for dato in range(3,len(valor)):
	print(alumnos["notas"])
	alumnos["notas"][datos[dato]] = valor[dato]
alumnos2.append(alumnos)
alumnos = {}

del alumnos2[0]
