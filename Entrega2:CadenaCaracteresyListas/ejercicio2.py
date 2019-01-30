cadena = str(input("Introduce una cadena de caracteres: "))
repetido = False
for i in cadena:
	if cadena.count(i) >= 2:
		repetido = True

if repetido:
	print ("La cadena de caracteres %s tiene caracteres repetidos" % (cadena))
else:
	print ("La cadena de caracteres %s no tiene caracteres repetidos" % (cadena))