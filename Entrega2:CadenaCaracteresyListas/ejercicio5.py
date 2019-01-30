lista = []
lista2 = []
palabras_2listas = []
palabras_lista1 = []
palabras_lista2 = []
palabrasen_2listas = []
contador = 1
contador2 = 1

cantidad = int(input("Cuantas palabras tiene la primera lista: "))

for i in range(cantidad):
	palabra = input("Digame la palabra %d: " % (contador))
	lista.append(palabra)
	contador = contador + 1
print ("La primera lista es: ",lista)

cantidad2 = int(input("Cuantas palabras tiene la segunda lista: "))

for i in range(cantidad2):
	palabra2 = input("Digame la palabra %d: " % (contador2))
	lista2.append(palabra2)
	contador2 = contador2 + 1
print ("La segunda lista es: ",lista2)

for i in lista:
	if i in lista2:
		palabras_2listas.append(i)
print ("Palabras que aparecen en las dos listas: ",palabras_2listas)

for i in lista:
	if i not in lista2:
		palabras_lista1.append(i)
print ("Palabras que aparecen en la primera lista: ",palabras_lista1)

for i in lista2:
	if i not in lista:
		palabras_lista2.append(i)
print ("Palabras que aparecen en la segunda lista: ",palabras_lista2)

for i in lista:
	if i in lista2:
		palabrasen_2listas.append(i)
print ("Todas las palabras: ",palabrasen_2listas)
