lista = []
contador = 1
posicion = 0
opcion = -1

cantidad = int(input("Cuántas palabras tiene la lista?: "))

for i in range(cantidad):
	cadena = str(input("Dime la palabra %d: " % (contador)))
	contador = contador + 1
	lista.append(cadena)
print ("La lista creada es de:", lista)

while opcion != 0:
	print ("1º. Contar")
	print ("2º. Modificar")
	print ("3º. Eliminar")
	print ("0º. Salir")

	opcion = int(input("Elige opción: "))

	if opcion == 1:
		palabra = str(input("Dime la palabra a buscar: "))
		if palabra in lista:
			print ("La palabra", palabra, "aparece %d veces en la lista" % (lista.count(palabra)))
		else:
			print ("La palabra a buscar no está en la lista")
	elif opcion == 2:
		buscar_palabra = input("Introduce la palabra que desea buscar: ")
		sustituir_palabra = input("Introduce la palabra que desea sustituir: ")
		for i in lista:
			if i == buscar_palabra:
				lista[posicion] = sustituir_palabra
			posicion = posicion + 1 
		print ("La lista es ahora: ",lista)
	elif opcion == 3:
		eliminar_palabra = input("Introduce la palabra que desea eliminar: ")
		for i in lista:
			if i == eliminar_palabra:
				lista.remove(eliminar_palabra)
		print ("La lista es ahora: ",lista)
	elif opcion == 0:
		print ("Adiós!!")